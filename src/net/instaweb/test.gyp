# Copyright 2010-2011 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

{
  'variables': {
    # chromium_code indicates that the code is not
    # third-party code and should be subjected to strict compiler
    # warnings/errors in order to catch programming mistakes.
    'chromium_code': 1,
  },

  'targets': [
    {
      'variables': {
        # OpenCV has compile warnings in gcc 4.1 in a header file so turn off
        # strict checking.
        #
        # TODO(jmarantz): disable the specific warning rather than
        # turning off all warnings, and also scope this down to a
        # minimal wrapper around the offending header file.
        #
        # TODO(jmarantz): figure out how to test for this failure in
        # checkin tests, as it passes in gcc 4.2 and fails in gcc 4.1.
        'chromium_code': 0,
      },
      'target_name': 'pagespeed_automatic_test',
      'type': 'executable',
      'dependencies': [
        'test_util',
        'instaweb.gyp:instaweb_automatic',
        'instaweb.gyp:instaweb_javascript',
        'instaweb.gyp:instaweb_spriter_test',
        'instaweb.gyp:instaweb_system',
        '<(DEPTH)/pagespeed/kernel.gyp:pagespeed_cache',
        '<(DEPTH)/pagespeed/kernel.gyp:pagespeed_image_test_util',
        '<(DEPTH)/pagespeed/kernel.gyp:pthread_system',
        '<(DEPTH)/testing/gmock.gyp:gmock',
        '<(DEPTH)/testing/gtest.gyp:gtest_main',
        '<(DEPTH)/third_party/apr/apr.gyp:apr',
        '<(DEPTH)/third_party/aprutil/aprutil.gyp:aprutil',
        '<(DEPTH)/third_party/css_parser/css_parser.gyp:css_parser',
        '<(DEPTH)/third_party/libpng/libpng.gyp:libpng',
        '<(DEPTH)/third_party/re2/re2.gyp:re2',
        'instaweb_core.gyp:instaweb_util_core',
      ],
      'include_dirs': [
        '<(DEPTH)/third_party/protobuf/src',
        '<(SHARED_INTERMEDIATE_DIR)/protoc_out/instaweb',
        '<(DEPTH)',
        '<(DEPTH)/third_party/css_parser/src',
      ],
      'sources': [
        'automatic/cache_html_flow_test.cc',
        'automatic/flush_early_flow_test.cc',
        'automatic/html_detector_test.cc',
        'automatic/proxy_fetch_test.cc',
        'automatic/proxy_interface_test.cc',
        'automatic/proxy_interface_test_base.cc',
        'http/async_fetch_test.cc',
        'http/bot_checker_test.cc',
        'http/cache_url_async_fetcher_test.cc',
        'http/fetcher_test.cc',
        'http/headers_cookie_util_test.cc',
        'http/http_cache_test.cc',
        'http/http_dump_url_async_writer_test.cc',
        'http/http_dump_url_fetcher_test.cc',
        'http/http_dump_url_writer_test.cc',
        'http/http_response_parser_test.cc',
        'http/http_value_test.cc',
        'http/inflating_fetch_test.cc',
        'http/log_record_test.cc',
        'http/mock_url_fetcher_test.cc',
        'http/rate_controlling_url_async_fetcher_test.cc',
        'http/reflecting_test_fetcher_test.cc',
        'http/request_context_test.cc',
        'http/request_headers_test.cc',
        'http/response_headers_test.cc',
        'http/semantic_type_test.cc',
        'http/sync_fetcher_adapter_test.cc',
        'http/url_async_fetcher_stats_test.cc',
        'http/user_agent_matcher_test.cc',
        'http/user_agent_matcher_test_base.cc',
        'http/wait_url_async_fetcher_test.cc',
        'http/write_through_http_cache_test.cc',
        'js/js_lexer_test.cc',
        'rewriter/add_instrumentation_filter_test.cc',
        'rewriter/association_transformer_test.cc',
        'rewriter/base_tag_filter_test.cc',
        'rewriter/blink_util_test.cc',
        'rewriter/cache_extender_test.cc',
        'rewriter/cache_html_filter_test.cc',
        'rewriter/collapse_whitespace_filter_test.cc',
        'rewriter/collect_flush_early_content_filter_test.cc',
        'rewriter/common_filter_test.cc',
        'rewriter/compute_visible_text_filter_test.cc',
        'rewriter/console_suggestions_test.cc',
        'rewriter/critical_css_beacon_filter_test.cc',
        'rewriter/critical_css_filter_test.cc',
        'rewriter/critical_css_finder_test.cc',
        'rewriter/critical_images_beacon_filter_test.cc',
        'rewriter/critical_images_finder_test.cc',
        'rewriter/critical_images_finder_test_base.cc',
        'rewriter/critical_selector_finder_test.cc',
        'rewriter/critical_selector_filter_test.cc',
        'rewriter/css_combine_filter_test.cc',
        'rewriter/css_embedded_config_test.cc',
        'rewriter/css_filter_test.cc',
        'rewriter/css_hierarchy_test.cc',
        'rewriter/css_flatten_imports_test.cc',
        'rewriter/css_image_rewriter_test.cc',
        'rewriter/css_inline_filter_test.cc',
        'rewriter/css_inline_import_to_link_filter_test.cc',
        'rewriter/css_move_to_head_filter_test.cc',
        'rewriter/css_outline_filter_test.cc',
        'rewriter/css_rewrite_test_base.cc',
        'rewriter/css_summarizer_base_test.cc',
        'rewriter/css_tag_scanner_test.cc',
        'rewriter/css_util_test.cc',
        'rewriter/debug_filter_test.cc',
        'rewriter/decode_rewritten_urls_filter_test.cc',
        'rewriter/dedup_inlined_images_filter_test.cc',
        'rewriter/defer_iframe_filter_test.cc',
        'rewriter/delay_images_filter_test.cc',
        'rewriter/distributed_rewrite_context_test.cc',
        'rewriter/dom_stats_filter_test.cc',
        'rewriter/domain_lawyer_test.cc',
        'rewriter/domain_rewrite_filter_test.cc',
        'rewriter/elide_attributes_filter_test.cc',
        'rewriter/experiment_matcher_test.cc',
        'rewriter/experiment_util_test.cc',
        'rewriter/file_load_policy_test.cc',
        'rewriter/flush_early_content_writer_filter_test.cc',
        'rewriter/flush_html_filter_test.cc',
        'rewriter/google_analytics_filter_test.cc',
        'rewriter/handle_noscript_redirect_filter_test.cc',
        'rewriter/html_attribute_quote_removal_test.cc',
        'rewriter/image_combine_filter_test.cc',
        'rewriter/image_endian_test.cc',
        'rewriter/image_oom_test.cc',
        'rewriter/image_rewrite_filter_test.cc',
        'rewriter/image_test.cc',
        'rewriter/image_test_base.cc',
        'rewriter/image_url_encoder_test.cc',
        'rewriter/in_place_rewrite_context_test.cc',
        'rewriter/insert_dns_prefetch_filter_test.cc',
        'rewriter/insert_ga_filter_test.cc',
        'rewriter/javascript_code_block_test.cc',
        'rewriter/javascript_filter_test.cc',
        'rewriter/js_combine_filter_test.cc',
        'rewriter/js_defer_disabled_filter_test.cc',
        'rewriter/js_disable_filter_test.cc',
        'rewriter/js_inline_filter_test.cc',
        'rewriter/js_outline_filter_test.cc',
        'rewriter/lazyload_images_filter_test.cc',
        'rewriter/local_storage_cache_filter_test.cc',
        'rewriter/meta_tag_filter_test.cc',
        'rewriter/mock_critical_css_finder.cc',
        'rewriter/mock_critical_images_finder.cc',
        'rewriter/mock_resource_callback.cc',
        'rewriter/pedantic_filter_test.cc',
        'rewriter/property_cache_util_test.cc',
        'rewriter/redirect_on_size_limit_filter_test.cc',
        'rewriter/remove_comments_filter_test.cc',
        'rewriter/resource_combiner_test.cc',
        'rewriter/resource_fetch_test.cc',
        'rewriter/resource_namer_test.cc',
        'rewriter/resource_slot_test.cc',
        'rewriter/resource_tag_scanner_test.cc',
        'rewriter/resource_update_test.cc',
        'rewriter/rewrite_context_test.cc',
        'rewriter/rewrite_context_test_base.cc',
        'rewriter/rewrite_driver_test.cc',
        'rewriter/rewrite_options_test.cc',
        'rewriter/rewrite_query_test.cc',
        'rewriter/rewrite_single_resource_filter_test.cc',
        'rewriter/rewrite_test_base.cc',
        'rewriter/rewriter_test.cc',
        'rewriter/rewritten_content_scanning_filter_test.cc',
        'rewriter/scan_filter_test.cc',
        'rewriter/script_tag_scanner_test.cc',
        'rewriter/server_context_test.cc',
        'rewriter/shared_cache_test.cc',
        'rewriter/split_html_filter_test.cc',
        'rewriter/static_asserts_test.cc',
        'rewriter/static_asset_manager_test.cc',
        'rewriter/strip_non_cacheable_filter_test.cc',
        'rewriter/strip_scripts_filter_test.cc',
        'rewriter/support_noscript_filter_test.cc',
        'rewriter/suppress_prehead_filter_test.cc',
        'rewriter/two_level_cache_test.cc',
        'rewriter/url_left_trim_filter_test.cc',
        'rewriter/url_namer_test.cc',
        'rewriter/url_partnership_test.cc',
        'spriter/libpng_image_library_test.cc',
        'spriter/image_spriter_test.cc',
        'system/apr_mem_cache_test.cc',
        'system/system_caches_test.cc',
        'util/async_cache_test.cc',
        'util/base64_test.cc',
        'util/cache_batcher_test.cc',
        'util/cache_stats_test.cc',
        'util/charset_util_test.cc',
        'util/chunking_writer_test.cc',
        'util/compressed_cache_test.cc',
        'util/countdown_timer_test.cc',
        'util/data_url_test.cc',
        'util/delay_cache_test.cc',
        'util/escaping_test.cc',
        'util/fallback_cache_test.cc',
        'util/fallback_property_page_test.cc',
        'util/file_cache_test.cc',
        'util/filename_encoder_test.cc',
        'util/gzip_inflater_test.cc',
        'util/hostname_util_test.cc',
        'util/key_value_codec_test.cc',
        'util/mem_debug.cc',
        'util/mock_time_cache_test.cc',
        'util/null_statistics_test.cc',
        'util/property_cache_test.cc',
        'util/pool_test.cc',
        'util/queued_alarm_test.cc',
        'util/split_statistics_test.cc',
        'util/statistics_work_bound_test.cc',
        'util/threadsafe_cache_test.cc',
        'util/url_escaper_test.cc',
        'util/url_multipart_encoder_test.cc',
        'util/url_to_filename_encoder_test.cc',
        'util/vector_deque_test.cc',
        'util/write_through_cache_test.cc',
        '<(DEPTH)/pagespeed/kernel/base/arena_test.cc',
        '<(DEPTH)/pagespeed/kernel/base/callback_test.cc',
        '<(DEPTH)/pagespeed/kernel/base/circular_buffer_test.cc',
        '<(DEPTH)/pagespeed/kernel/base/function_test.cc',
        '<(DEPTH)/pagespeed/kernel/base/hasher_test.cc',
        '<(DEPTH)/pagespeed/kernel/base/inline_slist_test.cc',
        '<(DEPTH)/pagespeed/kernel/base/md5_hasher_test.cc',
        '<(DEPTH)/pagespeed/kernel/base/mem_file_system_test.cc',
        '<(DEPTH)/pagespeed/kernel/base/message_handler_test.cc',
        '<(DEPTH)/pagespeed/kernel/base/mock_message_handler_test.cc',
        '<(DEPTH)/pagespeed/kernel/base/mock_timer_test.cc',
        '<(DEPTH)/pagespeed/kernel/base/ref_counted_ptr_test.cc',
        '<(DEPTH)/pagespeed/kernel/base/shared_string_test.cc',
        '<(DEPTH)/pagespeed/kernel/base/simple_stats_test.cc',
        '<(DEPTH)/pagespeed/kernel/base/statistics_logger_test.cc',
        '<(DEPTH)/pagespeed/kernel/base/stdio_file_system_test.cc',
        '<(DEPTH)/pagespeed/kernel/base/string_multi_map_test.cc',
        '<(DEPTH)/pagespeed/kernel/base/string_util_test.cc',
        '<(DEPTH)/pagespeed/kernel/base/symbol_table_test.cc',
        '<(DEPTH)/pagespeed/kernel/base/time_util_test.cc',
        '<(DEPTH)/pagespeed/kernel/base/waveform_test.cc',
        '<(DEPTH)/pagespeed/kernel/cache/lru_cache_test.cc',
        '<(DEPTH)/pagespeed/kernel/cache/purge_context_test.cc',
        '<(DEPTH)/pagespeed/kernel/cache/purge_set_test.cc',
        '<(DEPTH)/pagespeed/kernel/html/canonical_attributes_test.cc',
        '<(DEPTH)/pagespeed/kernel/html/doctype_test.cc',
        '<(DEPTH)/pagespeed/kernel/html/html_keywords_test.cc',
        '<(DEPTH)/pagespeed/kernel/html/html_name_test.cc',
        '<(DEPTH)/pagespeed/kernel/html/html_parse_test.cc',
        '<(DEPTH)/pagespeed/kernel/http/content_type_test.cc',
        '<(DEPTH)/pagespeed/kernel/http/google_url_test.cc',
        '<(DEPTH)/pagespeed/kernel/http/query_params_test.cc',
        '<(DEPTH)/pagespeed/kernel/image/gif_reader_test.cc',
        '<(DEPTH)/pagespeed/kernel/image/image_converter_test.cc',
        '<(DEPTH)/pagespeed/kernel/image/jpeg_optimizer_test.cc',
        '<(DEPTH)/pagespeed/kernel/image/jpeg_reader_test.cc',
        '<(DEPTH)/pagespeed/kernel/image/jpeg_utils_test.cc',
        '<(DEPTH)/pagespeed/kernel/image/png_optimizer_test.cc',
        '<(DEPTH)/pagespeed/kernel/image/webp_optimizer_test.cc',
        '<(DEPTH)/pagespeed/kernel/js/js_minify_test.cc',
        '<(DEPTH)/pagespeed/kernel/sharedmem/inprocess_shared_mem_test.cc',
        '<(DEPTH)/pagespeed/kernel/thread/mock_scheduler_test.cc',
        '<(DEPTH)/pagespeed/kernel/thread/pthread_condvar_test.cc',
        '<(DEPTH)/pagespeed/kernel/thread/pthread_thread_system_test.cc',
        '<(DEPTH)/pagespeed/kernel/thread/queued_worker_test.cc',
        '<(DEPTH)/pagespeed/kernel/thread/queued_worker_pool_test.cc',
        '<(DEPTH)/pagespeed/kernel/thread/scheduler_based_abstract_lock_test.cc',
        '<(DEPTH)/pagespeed/kernel/thread/scheduler_test.cc',
        '<(DEPTH)/pagespeed/kernel/thread/scheduler_thread_test.cc',
        '<(DEPTH)/pagespeed/kernel/thread/slow_worker_test.cc',
        '<(DEPTH)/pagespeed/kernel/thread/thread_synchronizer_test.cc',
        '<(DEPTH)/pagespeed/kernel/util/copy_on_write_test.cc',
        '<(DEPTH)/pagespeed/kernel/util/fast_wildcard_group_speed_test.cc',
        '<(DEPTH)/pagespeed/kernel/util/fast_wildcard_group_test.cc',
        '<(DEPTH)/pagespeed/kernel/util/file_system_lock_manager_test.cc',
        '<(DEPTH)/pagespeed/kernel/util/re2_test.cc',
        '<(DEPTH)/pagespeed/kernel/util/wildcard_group.cc',
        '<(DEPTH)/pagespeed/kernel/util/wildcard_group_test.cc',
        '<(DEPTH)/pagespeed/kernel/util/wildcard_test.cc',
# Rolling hash test fails to build in 32-bit g++ 4.1
# [google] See b/9203004
#        '<(DEPTH)/pagespeed/kernel/base/rolling_hash_test.cc',
#        'util/split_writer_test.cc',               # not currently needed
      ],
      'conditions': [
        ['support_posix_shared_mem != 1', {
          'sources!' : [
            '<(DEPTH)/pagespeed/kernel/sharedmem/pthread_shared_mem_test.cc',
          ],
        }]
      ],
    },
    {
      'variables': {
        # OpenCV has compile warnings in gcc 4.1 in a header file so turn off
        # strict checking.
        #
        # TODO(jmarantz): disable the specific warning rather than
        # turning off all warnings, and also scope this down to a
        # minimal wrapper around the offending header file.
        #
        # TODO(jmarantz): figure out how to test for this failure in
        # checkin tests, as it passes in gcc 4.2 and fails in gcc 4.1.
        'chromium_code': 0,
      },
      'target_name': 'mod_pagespeed_test',
      'type': 'executable',
      'dependencies': [
        'test_util',
        'instaweb_apr.gyp:instaweb_apr',
        '<(DEPTH)/testing/gmock.gyp:gmock',
        '<(DEPTH)/testing/gtest.gyp:gtest_main',
        '<(DEPTH)/third_party/apr/apr.gyp:apr',
        '<(DEPTH)/third_party/aprutil/aprutil.gyp:aprutil',
        '<(DEPTH)/third_party/httpd/httpd.gyp:include',
      ],
      'include_dirs': [
        '<(DEPTH)/third_party/protobuf/src',
        '<(SHARED_INTERMEDIATE_DIR)/protoc_out/instaweb',
        '<(DEPTH)',
      ],
      'sources': [
        'apache/apr_file_system_test.cc',
        'apache/speed_test.cc',
        'system/add_headers_fetcher_test.cc',
        'system/loopback_route_fetcher_test.cc',
        'system/serf_url_async_fetcher_test.cc',
        'util/mem_debug.cc',
      ],
    },
    {
      'target_name': 'test_infrastructure',
      'type': '<(library)',
      'dependencies': [
        'instaweb.gyp:instaweb_rewriter',
        'instaweb.gyp:instaweb_http_test',
        'instaweb.gyp:process_context',
        '<(DEPTH)/base/base.gyp:base',
        '<(DEPTH)/build/build_util.gyp:mod_pagespeed_version_header',
        '<(DEPTH)/pagespeed/kernel.gyp:pagespeed_base_test_infrastructure',
        '<(DEPTH)/third_party/gflags/gflags.gyp:gflags',
      ],
      'include_dirs': [
        '<(DEPTH)/third_party/protobuf/src',
        '<(SHARED_INTERMEDIATE_DIR)/protoc_out/instaweb',
        '<(DEPTH)',
      ],
      'sources': [
        'rewriter/css_url_extractor.cc',
        'util/delay_cache.cc',
        'util/mock_time_cache.cc',
      ],
    },
    {
      'target_name': 'test_util',
      'type': '<(library)',
      'dependencies': [
        'test_infrastructure',
        '<(DEPTH)/pagespeed/kernel.gyp:base_test_util',
      ],
      'include_dirs': [
        '<(DEPTH)/third_party/protobuf/src',
        '<(DEPTH)',
      ],
      'sources': [
        '<(DEPTH)/pagespeed/kernel/html/html_parse_test_base.cc',
        'http/mock_url_fetcher.cc',
        'rewriter/fake_filter.cc',
        'rewriter/rewrite_test_base.cc',
        'rewriter/test_distributed_fetcher.cc',
        'rewriter/test_rewrite_driver_factory.cc',
        'rewriter/test_url_namer.cc',
      ],
    },
    {
      'target_name': 'mod_pagespeed_speed_test',
      'type': 'executable',
      'dependencies': [
        'instaweb_core.gyp:instaweb_util_core',
        'test_util',
        '<(DEPTH)/pagespeed/kernel.gyp:pthread_system',
        '<(DEPTH)/third_party/css_parser/css_parser.gyp:css_parser',
        '<(DEPTH)/third_party/protobuf/protobuf.gyp:protobuf_lite',
        '<(DEPTH)/third_party/re2/re2.gyp:re2_bench_util',
      ],
      'include_dirs': [
        '<(DEPTH)',
        '<(DEPTH)/third_party/css_parser/src',
      ],
      'sources': [
        '<(DEPTH)/pagespeed/kernel/html/html_parse_speed_test.cc',
        'rewriter/css_minify_speed_test.cc',
        'rewriter/domain_lawyer_speed_test.cc',
        'rewriter/rewrite_driver_speed_test.cc',
        'util/compressed_cache_speed_test.cc',
        'util/deque_speed_test.cc',
        'util/url_escaper_speed_test.cc',
        '<(DEPTH)/pagespeed/kernel/cache/lru_cache_speed_test.cc',
        '<(DEPTH)/pagespeed/kernel/util/fast_wildcard_group_speed_test.cc',
        '<(DEPTH)/pagespeed/kernel/util/wildcard_group.cc',
      ],
    },
    {
      'target_name': 'css_minify_main',
      'type': 'executable',
      'sources': [
        'rewriter/css_minify_main.cc',
      ],
      'dependencies': [
        'instaweb.gyp:automatic_util',
        'instaweb.gyp:instaweb_rewriter',
        'instaweb.gyp:instaweb_rewriter_css',
        'instaweb.gyp:instaweb_util',
        '<(DEPTH)/base/base.gyp:base',
        '<(DEPTH)/pagespeed/kernel.gyp:pthread_system',
        '<(DEPTH)/third_party/css_parser/css_parser.gyp:css_parser',
        '<(DEPTH)/third_party/gflags/gflags.gyp:gflags',
      ],
      'include_dirs': [
        '<(DEPTH)',
        '<(DEPTH)/third_party/css_parser/src',
      ],
    },
  ],
}
