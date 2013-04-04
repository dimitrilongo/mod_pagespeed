/*
 * Copyright 2013 Google Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// Author: pulkitg@google.com (Pulkit Goyal)

#include "net/instaweb/util/public/fallback_property_page.h"

#include "base/logging.h"

namespace net_instaweb {

FallbackPropertyPage::FallbackPropertyPage(
    PropertyPage* actual_property_page,
    PropertyPage* fallback_property_page)
    :  actual_property_page_(actual_property_page),
       fallback_property_page_(fallback_property_page) {
  CHECK(actual_property_page != NULL);
}

FallbackPropertyPage::~FallbackPropertyPage() {
}

PropertyValue* FallbackPropertyPage::GetProperty(
      const PropertyCache::Cohort* cohort,
      const StringPiece& property_name) const {
  PropertyValue* value = actual_property_page_->GetProperty(
      cohort, property_name);
  if (value->has_value() || fallback_property_page_ == NULL) {
    return value;
  }
  return fallback_property_page_->GetProperty(cohort, property_name);
}

void FallbackPropertyPage::UpdateValue(
    const PropertyCache::Cohort* cohort, const StringPiece& property_name,
    const StringPiece& value) {
  actual_property_page_->UpdateValue(cohort, property_name, value);
  if (fallback_property_page_ != NULL) {
    fallback_property_page_->UpdateValue(cohort, property_name, value);
  }
}

void FallbackPropertyPage::WriteCohort(
    const PropertyCache::Cohort* cohort) {
  actual_property_page_->WriteCohort(cohort);
  if (fallback_property_page_ != NULL) {
    fallback_property_page_->WriteCohort(cohort);
  }
}

CacheInterface::KeyState FallbackPropertyPage::GetCacheState(
    const PropertyCache::Cohort* cohort) {
  return actual_property_page_->GetCacheState(cohort);
}

void FallbackPropertyPage::DeleteProperty(const PropertyCache::Cohort* cohort,
                                          const StringPiece& property_name) {
  actual_property_page_->DeleteProperty(cohort, property_name);
  if (fallback_property_page_ != NULL) {
    fallback_property_page_->DeleteProperty(cohort, property_name);
  }
}

const GoogleString& FallbackPropertyPage::key() const {
  return actual_property_page_->key();
}

}  // namespace net_instaweb
