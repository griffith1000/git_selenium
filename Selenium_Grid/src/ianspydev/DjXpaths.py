#!/usr/bin/env python
# -*- coding: utf-8 -*-


class DjXpaths(object):
    
    # header dj homepage link      
        dj_main_homepage_button ="//div[@id='header']/div/div/a"
        
        #Top Navigation

        dj_main_nav_music ="//div[@id='site-nav']/nav/ul/li[1]/a"
        dj_main_nav_sounds ="//div[@id='site-nav']/nav/ul/li[2]/a"
        dj_main_nav_mixes ="//div[@id='site-nav']/nav/ul/li[3]/a"
        dj_main_nav_djs ="//div[@id='site-nav']/nav/ul/li[4]/a"
        #in production the events tab isn't active, so we would only go to li[6]
        dj_main_nav_events ="//div[@id='site-nav']/nav/ul/li[5]/a"
        dj_main_nav_play ="//div[@id='site-nav']/nav/ul/li[6]/a"
        dj_main_nav_news ="//div[@id='site-nav']/nav/ul/li[7]/a"
    
#Profiles button
        dj_main_profile_button = "//div[@class='navigation']//li[1]/a"
        
#Profile List of Users starting with row 1 and 2
        dj_profiles_first_user = "//div[@id='theme']/div/div/div[2]/div/div/ul/li[1]/a/span"
        dj_profiles_second_user ="//div[@id='theme']/div/div/div[2]/div/div/ul/li[2]/a/span"        
        
#Genres starting with first and second ending with li[23]

        dj_profile_first_genre_filter = "//div[@id='theme']/div/div/div[2]/div/div/ul/li[1]/a/span[2]"     
        dj_profile_second_genre_filter = "//div[@id='theme']/div/div/div[2]/div/div/ul/li[2]/a/span[2]"
#Events Button
        dj_main_events_button = "//div[@class='navigation']//li[2]/a"
        
#   Event #Genres starting with first and second ending with li[23]  (Same as profile genrs)
  
        dj_events_first_genre_filter = "//div[@id='theme']/div/div/div[2]/div/div[2]/ul/li[1]/a/span"   
        dj_events_second_genre_filter = "//div[@id='theme']/div/div/div[2]/div/div[2]/ul/li[2]/a/span"   
#       Upcoming/Past events
        dj_events_upcoming_filter = "//div[@id='theme']/div/div/div[2]/div/div[4]/ul/li[1]/a/span"
        dj_events_past_filter = "//div[@id='theme']/div/div/div[2]/div/div[4]/ul/li[2]/a/span"

#Create Profile Button
        dj_main_create_profile_button =  "//div[@class='navigation']//li[3]/a"
        dj_main_create_profile_button2 = "//*[@id=\"header\"]/div/div[2]/ul/li[3]/a"
        
    
#9 featured djs

        dj_main_first_featured_profile = "//div[@id='theme']/div/div/div/div/a[2]/img"
        dj_main_second_featured_profile ="//div[@id='theme']/div/div/div/div/a[3]/img"
        dj_main_third_featured_profile ="//div[@id='theme']/div/div/div/div/a[4]/img"
        dj_main_fourth_featured_profile ="//div[@id='theme']/div/div/div/div/a[5]/img"
        dj_main_fifth_featured_profile ="//div[@id='theme']/div/div/div/div/a[6]/img"
        dj_main_sixth_featured_profile ="//div[@id='theme']/div/div/div/div/a[7]/img"
        dj_main_seventh_featured_profile ="//div[@id='theme']/div/div/div/div/a[8]/img"
        dj_main_eighth_featured_profile ="//div[@id='theme']/div/div/div/div/a[9]/img"
        dj_main_ninth_featured_profile ="//div[@id='theme']/div/div/div/div/a[9]/img"
    
# newest djs

         
        dj_main_first_new_profile = "//div[@id='theme']/div/div/div[2]/a/img"
        dj_main_second_new_profile ="//div[@id='theme']/div/div/div[2]/a[2]/img"
        dj_main_third_new_profile ="//div[@id='theme']/div/div/div[2]/a[3]/img"
        dj_main_fourth_new_profile ="//div[@id='theme']/div/div/div[2]/a[4]/img"
        dj_main_fifth_new_profile ="//div[@id='theme']/div/div/div[2]/a[5]/img"
        dj_main_sixth_new_profile ="//div[@id='theme']/div/div/div[2]/a[6]/img"
        dj_main_seventh_new_profile ="//div[@id='theme']/div/div/div[2]/a[7]/img"
        dj_main_eighth_new_profile ="//div[@id='theme']/div/div/div[2]/a[8]/img"
        dj_main_ninth_new_profile ="//div[@id='theme']/div/div/div[2]/a[9]/img"
        dj_main_tenth_new_profile ="//div[@id='theme']/div/div/div[2]/a[10]/img"
        

#Search input field 
        dj_main_search_field = "//input[@class='text']"
        
#Search submission button
        dj_main_search_button = "//input[@class='submit']"
    
    
    
#New from your followed dj's
        dj_main_first_followed_content ="//div[@id='theme']/div/div/div/div/a/span[2]/span/img"
        dj_main_second_followed_content ="//div[@id='theme']/div/div/div/div/a[2]/span[2]/span/img"
        dj_main_third_followed_content ="dj_main_first_followed_content =//div[@id='theme']/div/div/div/div/a[3]/span[2]/span/img"
        dj_main_fourth_followed_content ="//div[@id='theme']/div/div/div/div/a[4]/span[2]/span/img"
        dj_main_fifth_followed_content ="//div[@id='theme']/div/div/div/div/a[5]/span[2]/span/img"
        

    
# _________________________________My Profile Page
#follow button/ unfollow button
        dj_profile_follow_button = "//form[@id='profile-follow']/a/span"   
        dj_profile_unfollow_button ="//form[@id='profile-unfollow']/a/span"

#Personal followers and following respectively
        dj_profile_followers_button ="//div[@id='profile-card-full']/div/div[2]/div/div/span[2]/span/div/a[1]/span[2]"
        dj_profile_following_button ="//div[@id='profile-card-full']/div/div[2]/div/div/span[2]/span/div/a[2]/span[2]"
#___________________________

    
    
    
    
        account_page_account_overview_page = "//div[@class=\"accountOverviewSummary\"]";
        account_page_billing_info_link = "//a[contains(@href,\"billing\")]"  
        account_page_audio_format_link = "//a[contains(@href,\"format\")]"
        account_available_for_download_page=  "//h2[contains(text(),\"My Downloads\")]"
        account_available_for_download_page_first_track = "//tr[contains(@class,\"track-grid-content\")][1]/td/a[contains(@href,\"TOKEN\")]"
        account_page_change_password_link = "//a[contains(@href,\"credentials\")]"  
        
        account_password_change_page = "//form[@id=\"form-change-password\"]"  
        account_forgotten_password_link = "//a[contains(@href,\"forgot\")]"  
        account_forgotten_password_page= "//form[@id=\"forgot-password-form\"]"  
        account_forgotten_password_email_textfield = "//form[@id=\"forgot-password-form\"]//input[@id=\"email\"]"  
        account_forgotten_password_email_submit_button = "//button[@type=\"submit\"]"  
        account_email_sent_success_message ="//*[contains(text(),\"have been sent\")]"  
      
      
        add_to_cart_error = "//p[@class=\"error-message\"]"  
        add_to_cart_success = "//div[@id=\"statusMessages\"]//h1[contains(text(),\"successfully added\")]"  
      
        #all_tracks_text = "//span[@data-collection-name=\"All Tracks\"]"  
        already_purchased_dialog ="//div[@id=\"iFrameWrapper\"]//div[contains(text(),\"previously purchased\")]"
        already_purchased_message = "You have previously purchased the item you are adding to your cart."
    
        artist_detail_page = "//div[contains(@*,\"artist-detail\")]"
        artist_detail_latest_releases = "//div[contains(@*,\"artist-detail\")]//div[@name=\"featured\"]"  
        artist_detail_top_downloads = "//div[contains(@class,\"artist-detail\")]//div[contains(@data-collection-name,\"Top 10 Tracks\")]"  
        #artist_label_chart_section   = "//div[contains(@class,\"chart-result\")]"  
       
        artist_label_filter_bar_featured_tab  = "//ul[@class=\"horizontal\"]//li[1]/a"  
        artist_label_filter_bar_release_tab = "//ul[@class=\"horizontal\"]//li[3]/a"  
        artist_label_filter_bar_tracks_tab = "//ul[@class=\"horizontal\"]//li[2]/a"    
        artist_label_release_section = "//table[contains(@class,\"tile-list\")]"  
        artist_label_track_section   = "//table[contains(@class,\"track-grid\")]"  
      
        audio_format_page = "//form[@id = \"format_form\"]"
        #audio_format_dropdown = "//select[@id=\"format\"]"
        audio_format_dropdown_mp3 = "//input[@id=\"format_1\"]"
        audio_format_dropdown_wav = "//select[@id=\"format_3\"]"
        audio_format_dropdown_aiff = "//select[@id=\"format_14\"]"
        audio_format_save_button = "//form[@id=\"format_form\"]//button[@type=\"submit\"]"
      
      
        billing_info_cc_city_textfield="//input[@id=\"billTo_city\"]"  
        billing_info_cc_country_dropdown = "//select[@id=\"billTo_country\"]"  
        billing_info_cc_exp_month_textfield = "//input[@id=\"card_expirationMonth\"]"  
        billing_info_cc_exp_year_textfield = "//input[@id=\"card_expirationYear\"]"  
        billing_info_cc_first_name_textfield = "//input[@id=\"billTo_firstName\"]"  
        billing_info_cc_last_name_textfield = "//input[@id=\"billTo_lastName\"]"  
        billing_info_cc_number_textfield = "//input[@id=\"card_accountNumber\"]"  
        billing_info_cc_postal_code_textfield = "//input[@id=\"billTo_postalCode\"]"  
        billing_info_cc_sec_code = "//input[@id=\"card_cvNumber\"]"  
        billing_info_cc_state_dropdown = "//select[@id=\"billTo_state\"]"  
        billing_info_cc_street1_textfield = "//input[@id=\"billTo_street1\"]"  
        billing_info_cc_submit_button = "//form[@id=\"billing_form\"]//button[@name=\"submit\"]"  
        billing_info_page = "//form[@id = \"billing_form\"]"  
        billing_info_update_success_message = "//*[contains(text(),\"was successfully updated\")]"  
      
        buy_button = "//a[@name=\"buy_button_link\"]"  
        
        cart_move_dropdown = "//select[@id=\"moveToCart\"]"  
        cart_move_hold_bin_move_button ="//div[@id=\"dialogBox\"]//a[@data-move-source-cart=\"cart\"]"  
        cart_move_hold_bin_name_textfield ="//input[@id=\"newCartName\"]"  
        cart_move_open_window_button = "//a[@data-move-cart=\"cart\"]"  
        cart_move_window = "//div[@id=\"dialogBox\"]"  
      
      
        change_password_new_password_confirm_textfiled = "//form[@id=\"form-change-password\"]//input[@id=\"newPasswordConfirm\"]"  
        change_password_new_password_textfiled = "//form[@id=\"form-change-password\"]//input[@id=\"newPassword\"]"  
        change_password_old_password_textfiled = "//form[@id=\"form-change-password\"]//input[@id=\"password\"]"  
        change_password_submit_button = "//button[@type=\"submit\"]"  
        change_password_success_message ="//h1[contains(text(),\"updated successfully\")]"  
      
        chart_detail_meta_data = "//div[@id=\"chart_detail_meta_line\"]"  
        chart_detail_page = "//div[contains(@class,\"chart-detail\")]"  
        chart_detail_page_chart_price = "//div[contains(@class,\"chart-detail\")]//a[contains(@data-buy,\"chart\")]/span[1]/text()"
        chart_detail_page_chart_buy_button = "//div[contains(@class,\"chart-detail\")]//a[contains(@data-buy,\"chart\")]"
        chart_detail_tracks ="//div[contains(@class,\"track-grid-chart\")]//tr[contains(@class,\"track-grid-content\")]"    
        chart_detail_related_charts = "//div[@name=\"featured\"][1]"
        chart_add_track_button = "//a[@data-add=\"track:TOKEN\"]"  
        chart_add_dropdown = "//select[@id=\"addToChart\"]"
        chart_add_dropdown_create_new_chart_option = "Create New Chart"
        chart_add_to_chart_textfield = "//input[@id=\"newChartName\"]"
        chart_add_to_chart_add_button = "//a[contains(@class,\"AddToChart\")][1]"
        chart_add_to_chart_cancel_button = "//a[contains(@class,\"AddToChart\")][2]"
        chart_detail_play_release_row = "//div[@class=\"play-queue-row\"]"
      
      
      
        check_out_page = "//*[contains(@name,\"checkout-header\")]"
        check_out_cvv2_textfield = "//input[@id=\"cvv2\"]"
        check_out_submit_button = "//button[@type=\"submit\"]" 
      
        #for relases, charts, tracks
        detail_meta_data_first_artist = "//a[contains(@href,\"artist\")][1]"  
        detail_meta_data_genre_first ="//a[contains(@href,\"genre\")][1]"  
        detail_meta_data_label = "//a[contains(@href,\"label\")][1]"  
        detail_meta_data_price = "//span[@class=\"currency\"]"  
        detail_meta_data_title = "//div[@class=\"module-title\"]/h2"  
        detail_page_common = "//div[contains(@class,\"detail\")]"  
       
        #for artists nad labels
        
        detail_context_nav_tracks_link = "//div[@name=\"context-nav-bar\"]//a[contains(@href,\"tracks\")]"
        detail_context_nav_releases_link = "//div[@name=\"context-nav-bar\"]//a[contains(@href,\"releases\")]"
        detail_context_nav_featured_link = "//div[@name=\"context-nav-bar\"]//li[1]/a"
       
        dialog_window_ok_button = "//div[contains(@class,\"ui-widget\")]//div[contains(@class,\"buttonset\")]//button[2]"
        dialog_window_cancel_button = "//div[contains(@class,\"ui-widget\")]//div[contains(@class,\"buttonset\")]//button[1]"
       
        downloads_page = "//h2[text()=\"My Downloads\"]"
      
        error_message_element = "//label[@class=\"error\"]"  
        
        filter_bar_featured = "//nav[@class=\"filter-bar\"]//li[1]/a"
        filter_bar_tracks = "//nav[@class=\"filter-bar\"]//li[2]/a"
        filter_bar_relases = "//nav[@class=\"filter-bar\"]//li[3]/a"
        
        follow_artist_link_href = "//div[contains(@class,\"detail-header\")]//a[contains(@href,\"/my-beatport/add/\")]/@href"
        follow_artist_link = "//div[contains(@class,\"detail-header\")]//a[contains(@href,\"/my-beatport/add/\")]"
        follow_artist_link_selected="//div[contains(@class,\"detail-header\")]//a[contains(@href,\"/my-beatport/add/\")][contains(@class,\"selected\")]"
        
        follow_label_link_href = "//div[contains(@class,\"detail-nav\")]//a[contains(@href,\"/my-beatport/add/\")]/@href"
        follow_label_link = "//div[contains(@class,\"detail-nav\")]//a[contains(@href,\"/my-beatport/add/\")]"
        follow_label_link_selected="//div[contains(@class,\"detail-nav\")]//a[contains(@href,\"/my-beatport/add/\")][contains(@class,\"selected\")]"
        
        footer_english = "//a[@id=\"lang-en_US\"]"
        footer_german = "//a[@id=\"lang-de_DE\"]"
        footer_french =  "//a[@id=\"lang-fr_FR\"]"
        footer_spanish =  "//a[@id=\"lang-es_ES\"]"
        footer_italian =  "//a[@id=\"lang-it_IT\"]"
        footer_portugal = "//a[@id=\"lang-pt_BR\"]"
        footer_japan = "//a[@id=\"lang-ja_JP\"]"
        
        
        genre_list_genres = "//ul[@class=\"headerNav\"]//a"
        genre_page_slides = "//div[@id=\"genre-slides\"]"
        genre_position_in_the_list ="//div[@id=\"main_sub_nav_item_TOKEN\"]"  
        genre_link_by_genre_name = "//ul[@class=\"headerNav\"]//a[contains(@href,\"TOKEN\")]"
        genre_new_charts = "//div[@name=\"featured\"][1]"  
        genre_new_release = "//div[@name=\"featured\"][2]"  
        genre_most_popular_tracks = "//div[contains(@data-collection-name,\"TOKEN\")]"  
        genre_name_link ="//a[contains(text(), \"TOKEN\")]"   
        #genre_number = "//a[contains(@id,\"genreName\")]"  
        genre_page_title = "//h2/a[contains(text(),\"TOKEN\")]"   
        genre_staff_picks = "//div[@name=\"featured\"][3]"  

      
        header_account_link = "//li[@class=\"potato-menu-item\"]/a[contains(@href,\"account\")]"  
        header_browse_genre_link = "//a[@class=\"giant-green-button down-arrow\"]"
        header_cart_items_count = "//a[@id=\"cart-icon-count\"]/span"  
        header_cart_total_amount = "//span[@id=\"cart-total\"]"
        header_cart_items_count_element_with_parameter = "//a[@id=\"cart-icon-count\"]/span[text()=TOKEN]"
        header_cart_link = "//a[@id=\"cart-icon-count\"]"  
        header_dj_charts_link = "//div[@id=\"page-header\"]//a[contains(@href,\"charts\")]"  
        #header_login_link = "//a[@id=\"loginLink\"]"  
        header_login_link = "//a[contains(@href,\"login\")]" 
        header_logout_link = "//a[@id=\"logoutLink\"]"  
        header_my_beatport_latest_tracks_link = "//a[@id=\"myBeatportLatestTracksLink\"]"  
        header_my_beatport_link = "//div[contains(@class,\"header\")]//a[contains(@href,\"my-beatport\")]"  
        header_my_beatport_my_artists_link = "//a[@id=\"myBeatportMyArtistsLink\"]"  
        header_my_beatport_my_labels_link = "//a[@id=\"myBeatportMyLabelsLink\"]"  
        header_registration_link = "//a[@id=\"registrationLink\"]"  
        header_search_form_go_button ="//form[@id=\"search\"]/input[2]"  
        header_search_form_textfiled ="//form[@id=\"search\"]/input[1]"  
        
        hold_bin_page = "//div[@class=\"cartHeader\"]//h2[contains(text(),\"Hold Bin\")]"
        hold_bin_beatbot = "//div[contains(@data-collection-name,\"BeatBot Recommendations Based On Your Hold Bin\")]"
        hold_bin_tracks_link = ""
        hold_bin_releases_link = ""
        hold_bin_go_to_cart_button = ""
        hold_bin_empty_hold_bin_button =""

      
        home_based_on_orders_track=  "//div[@class=\"featuredItems\"][1]//tr[@name=\"tracks-grid-feature_track_TOKEN\"]"      
        home_featured_chart ="//div[@*=\"featured\"][2]//tr[1]//td[contains(@name,\"group1\")]"  
        home_featured_chart_unit_title = "//td[contains(@name,\"tiles-grid_chart_group1-row2\")][TOKEN]//a[@name=\"unit_title\"]"
        home_featured_chart_album_art_link = "//td[contains(@name,\"tiles-grid_chart_group1-row1\")][TOKEN]//div[contains(@class,\"image\")]//a[contains(@href,\"chart\")]"
        home_featured_charts_title ="//div[@id=\"featuredCharts\"]//h3"  
        home_featured_chart_section= "//div[@*=\"featured\"][2]"
       
        home_featured_release_section = "//div[@*=\"featured\"][1]"
        home_featured_release ="//div[@*=\"featured\"][1]//tr[1]//td[contains(@name,\"group1\")]"  
        home_featured_release_unit_title = "//td[contains(@name,\"tiles-grid_release_group1-row1\")][TOKEN]//a[@name=\"unit_title\"]"
        home_featured_release_album_art_link = "//td[contains(@name,\"tiles-grid_release_group1-row1\")][TOKEN]//div[contains(@class,\"image\")]//a[contains(@href,\"release\")]"
        home_featured_releases_title ="//div[@name=\"featured\"][1]//h3" 
        
        home_top_ten_title = "//div[contains(@class,\"the-beatport-top-10\")]"
        home_top_downloads_view_all_link = "//a[contains(@href,\"top-100\")]"
        home_top_releases_view_all_link = "//a[contains(@href,\"top-100-releases\")]"
        home_most_popular_title = "//div[@data-collection-name=\"Most Popular Tracks\"]//div[@class=\"module-header-top-10\"]"  
        home_most_popular_track = "//div[@data-collection-name=\"Most Popular Tracks\"]//li[TOKEN]"  
        home_most_popular_tracks_count = "//div[@data-collection-name=\"Most Popular Tracks\"]//li"
        home_most_popular_release = "//div[@data-collection-name=\"Most Popular Releases\"]//li[TOKEN]"  
       
        home_my_beatport = "//div[@id=\"latestMyBeatport\"]//ul[@class=\"currentSlide\"]//li"  
        home_page_main_slides = "//div[@id=\"homepage-slides\"]"                                          #done 
        home_tracks_based_on_latest_orders_section = "//div[contains(@data-modname,\"Last_Order\")]"
        home_tracks_latest_on_my_beatport_section = "//div[@class=\"asyncMod\"][1]"
        home_tracks_based_on_latest_orders_tracks =  "//div[contains(@data-modname,\"Last_Order\")]//div[@class=\"featuredItems\"][1]//tr[@name=\"tracks-grid-feature_track_TOKEN\"]"
      
        label_detail_page = "//div[contains(@class, \"label-detail\")]"
        label_detail_latest_releases = "//div[@data-modname=\"Label-Latest_Releases\"]"  
        label_detail_most_popular_releases = "//div[@data-modname=\"Label-Most_Popular_Releases\"]"
        label_detail_top_downloads = "//div[contains(@class,\"label-detail\")]//div[contains(@data-collection-name,\"Top 10 Tracks\")]"  
      
        login_window = "//div[contains(@class,\"login-box\")]"
        login_window_sign_up_link = "//div[contains(@class,\"login-box\")]//a[contains(@href,\"registration\")]"
        login_page = "//for=m[@id=\"login_form\"]"  
        login_page2 = "//p[@class=\"register-msg\"]"
        #login_button = "//form[@id=\"checkout-login-form\"]//*[@type=\"submit\"]"   
        #login_userid_textfiled = "//form[@id=\"checkout-login-form\"]//input[@id=\"username\"]"  
        #login_userpassword_textfield = "//form[@id=\"checkout-login-form\"]//input[@id=\"password\"]"  
        login_button = "//button[@type=\"submit\"]"   
        login_userid_textfiled = "//input[@id=\"username\"]"  
        login_userpassword_textfield = "//input[@id=\"password\"]"  
        login_invalid_credential_error = "//span[@class=\"error re-auth\"]"
        login_user_locked_out = "//span[@class=\"error locked\"]"
      
        my_beatport_page = "//*[contains(text(),\"MY BEATPORT\")]"
        my_beatport_no_results = "//div[contains(@class,\"noMyBeatportResults\")]"
        my_beatport_latest_tracks_link = "//nav[@class=\"filter-bar\"]//li[1]/a"  
        my_beatport_my_artists_link = "//a[contains(@href,\"/my-beatport/artist\")]"  
        my_beatport_my_labels_link = "//a[contains(@href,\"/my-beatport/label\")]"  
        my_beatport_my_atists_page = "//a[contains(@class,\"selected\")][contains(@href,\"/artist\")]"
        my_artists_artistId = "//div[@class=\"unit\"]//a[contains(@href,\"TOKEN\")]"
        my_labels_labelId = "//div[@class=\"unit\"]//a[contains(@href,\"TOKEN\")]"
        my_beatport_my_labels_page = "//a[contains(@class,\"selected\")][contains(@href,\"/label\")]"
        my_beatport_has_artists = "//div[contains(@class,\"myentities\")]//a[contains(@href,\"performerName\")]"
        my_beatport_has_labels = "//div[contains(@class,\"myentities\")]//a[contains(@href,\"labelName\")]"
        my_beatport_my_units = "//li[@class=\"unit-renderer-row \"]"
        my_beatport_my_units_remove_link = "//li[@class=\"unit-renderer-row \"][1]//a[contains(@href,\"remove\")]"
     
        player_area_buy = "//div[contains(@class,\"now-playing-buy\")][TOKEN]"
        player_area_now_playing ="//td[@id=\"now-playing\"]"
        player_actions_follow_first_artist_link = "//div[@id=\"player_track_actions_container\"]//a[contains(@href,\"/my-beatport/add/artist\")][1]"
        player_actions_follow_first_artist_link_selected = "//div[@id=\"player_track_actions_container\"]//a[contains(@href,\"/my-beatport/add/artist\")][1][contains(@class,\"selected\")]"
        
        player_actions_follow_first_artist_link_href = "//div[@id=\"player_track_actions_container\"]//a[contains(@href,\"/my-beatport/add/artist\")][1]/@href"
        player_actions_follow_artist_link_selected = "//div[@id=\"player_track_actions_container\"]//a[contains(@href,\"/my-beatport/add/artist\")][1][contains(@class,\"selected\")]"
        player_actions_follow_label_link = "//div[@id=\"player_track_actions_container\"]//a[contains(@href,\"/my-beatport/add/label\")]"
        player_actions_follow_label_link_selected = "//div[@id=\"player_track_actions_container\"]//a[contains(@href,\"/my-beatport/add/label\")][contains(@class,\"selected\")]"
        player_actions_follow_label_link_href = "//div[@id=\"player_track_actions_container\"]//a[contains(@href,\"/my-beatport/add/label\")]/@href"
        player_actions_beatpot = "//div[@id=\"player_track_actions_container\"]//a[3]"
        player_genre_link = "//div[@class=\"detail-metadata\"]//span[@class=\"genre\"]/a"
        player_track_in_the_player = "//td[@id=\"now-playing\"]//a[contains(@class,\"trackName\")][contains(@href,\"TOKEN\")]"
        #player_track_meta_data = "//td[@id=\"now-playing\"]//li[@class=\"primary\"][TOKEN]"
        playlist_track = "//ul[@id=\"playlist\"]//li"
        playlist_toggle = "//a[contains(@class,\"TogglePlaylist\")]"
        
        play_button = "//a[contains(@class,\"btn-play\")]"
        play_list_button = "//a[contains(@class,\"btn-queue\")]"
      
        paypal_password_textfield ="//*[@id=\"login_password\"]"
        paypal_submit_login_button = "//*[@id=\"submitLogin\"]"
        paypal_continue_button = "//*[@id=\"continue\"]"
      
        registration_page = "//form[@id=\"registration_form\"]"  
        registration_submit_button = "//button[@value=\"submit\"]"  
        registration_success_message = "//*[contains(text(),\"Congratulations\"]"  
        registrtion_user_email_confirm_textfield= "//input[@id=\"confirmEmailAddress\"]"  
        registration_user_email_confirm_valid = "//label[@for=\"confirmEmailAddress\"]//parent::p[@class=\"valid\"]"  
        registrtion_user_email_textfield= "//input[@id=\"emailAddress\"]"  
        registration_user_email_valid = "//label[@for=\"emailAddress\"]//parent::p[@class=\"valid\"]"  
        registrtion_user_firstname_textfield = "//input[@id=\"firstName\"]"  
        registration_first_name_valid = "//label[@for=\"firstName\"]//parent::p[@class=\"valid\"]"  
        registrtion_user_lastname_textfield= "//input[@id=\"lastName\"]"  
        registration_last_name_valid = "//label[@for=\"lastName\"]//parent::p[@class=\"valid\"]"  
        registrtion_user_password_confirm_textfield= "//input[@id=\"confirmPassword\"]"  
        registration_user_password_confirm_valid = "//label[@for=\"confirmPassword\"]//parent::p[@class=\"valid\"]"  
        registrtion_user_password_textfield= "//input[@id=\"password\"]"  
        registration_user_password_valid = "//label[@for=\"password\"]//parent::p[@class=\"valid\"]"  
        registrtion_user_username_textfield= "//input[@id=\"username\"]"  
        registration_user_username_valid = "//label[@for=\"username\"]//parent::p[@class=\"valid\"]"  
      
      
        release_detail_meta_data="//table[@class=\"meta-data\"]"  
        release_detail_meta_data_label = "//table[@class=\"meta-data\"]//tr[2]"
        release_detail_page = "//div[contains(@class,\"line release-detail\")]"  
        release_detail_tracks="//div[contains(@class,\"line release-detail\")]//table[contains(@*,\"track-grid\")]"  
        release_detail_more_from_this_label = "//h3[text()=\"More Releases From This Label\"]/parent::div/parent::div"
        release_detail_people_also_bought = "//h3[text()=\"People Also Bought\"]/parent::div/parent::div"
        release_detail_play_release_row = "//div[contains(@class,\"item-actions-playcart\")]"
      
        search_results_page = "//*[contains(text(),\"SEARCH FOR\")]"
        search_results_page_nav_label = "//a[contains(@href,\"fieldType:label\")]"
        search_results_page_nav_artist = "//a[contains(@href,\"fieldType:performer\")]"
        search_results_page_nav_track = "//a[contains(@href,\"fieldType:track\")]"
        search_results_page_nav_release = "//a[contains(@href,\"fieldType:release\")]"
        search_results_page_nav_chart = "//a[contains(@href,\"fieldType:chart\")]"
        
        search_results_page_artist_section = "//div[@data-modname=\"Search-artist\"]"
        search_results_page_label_section = "//div[@data-modname=\"Search-label\"]"
        search_results_page_release_section = "//div[@data-modname=\"Search-release\"]"
        search_results_page_chart_section = "//div[@data-modname=\"Search-chart\"]"
        search_results_page_track_section = "//div[@data-modname=\"Search-track\"]"
        
        search_results_label_page = "//div//h3[contains(text(),\"LABEL\")]"
        search_results_label_page_first_label_link = "//li[@name=\"tiles-list_label_1\"]//div[@class=\"unit\"]//a[contains(@href,\"label\")]"
      
        search_results_artist_page = "//div//h3[contains(text(),\"ARTIST\")]"
        search_results_artist_page_first_artist_link = "//li[@name=\"tiles-list_artist_1\"]//div[@class=\"unit\"]//a[contains(@href,\"artist\")]"
      
        search_results_release_page = "//div//h3[contains(text(),\"RELEASE\")]"
        search_results_release_page_first_release_link = "//li[@name=\"tiles-list_release_1\"]//a[@name=\"unit_title\"]"
        
        
        search_button_english = "//input[@class=\"giant-green-button right-arrow\"][@value=\"SEARCH\"]"
        search_button_german = "//input[@class=\"giant-green-button right-arrow\"][@value=\"SUCHEN\"]"
        search_button_french = "//input[@class=\"giant-green-button right-arrow\"][@value=\"RECHERCHER\"]"
        search_button_spanish = "//input[@class=\"giant-green-button right-arrow\"][@value=\"BUSCAR\"]"
        search_button_portugal = "//input[@class=\"giant-green-button right-arrow\"][@value=\"PROCURAR\"]"
        search_button_italian = "//input[@class=\"giant-green-button right-arrow\"][@value=\"CERCA\"]"
                
        shopping_cart_counter_zero = "//span[@id=\"cart-count\"][text()=0]"
        shopping_card_empty_message ="any tracks in your cart."  
        shopping_cart_current_cart_title ="//span[contains(@class,\"cartName\")]" 
        shopping_cart_coupon_textfield = "//input[@id=\"coupon-code-input\"]" 
        shopping_cart_coupon_apply_button = "//button[@id=\"coupon-submit-btn\"]"
        shopping_cart_empty_button = "//a[@id=\"empty-cart-button\"]"  
        shopping_cart_item = "//table[@class =\"track-grid track-grid-cart \"]//tr[contains(@class,\"track-grid-content\")][TOKEN]"      
        shopping_cart_item_move_link = "//a[@data-move=\"track:"  
        shopping_cart_item_audio_format = "//select/option[@selected=\"\"]"
        shopping_cart_item_remove_button= "//a[contains(@href,\"remove\")]"  
        shopping_cart_item_title = "//*[contains(@class,\"artistNames\")]//following-sibling::a[contains(@href,\"track\")]"  
        shopping_cart_item_undo_button = "//a[contains(text(),\"Undo\")]"  
        shopping_cart_page = "//div[@id=\"shopping-cart\"]"  
        shopping_cart_release_currency = "//parent::div//span[@class=\"currency\"]"  
        shopping_cart_unit_price = "//*[contains(@*,\"price\")]/span"
        shopping_cart_release_id = "//tr[@data-play=\"release:TOKEN\"]"
        shopping_cart_release="//table[@class =\"track-grid track-grid-cart releases-grid-cart \"]//tr[contains(@class,\"track-grid-content\")]"      
        shopping_cart_track_id = "//a[@data-play=\"track:TOKEN\"][1]"
        shopping_cart_track_move_to_hold_bin = "//a[contains(@href,\"hold-bin\")][@data-buy=\"track:TOKEN\"]"
        shopping_cart_checkout_button = "//a[contains(@href,\"checkout\")]"
        shopping_cart_checkout_window = "//div[@id=\"checkout-wrap\"]"
        shopping_card_cvv_code_textfield = "//input[@id=\"cvv2\"]"
        shopping_cart_complete_checkout_button ="//form[@id=\"checkout-cvv2-form\"]//button[@value=\"submit\"]"
        shopping_cart_paypal_checkout_button= "//a[@class=\"paypalCheckoutButton\"]"
        shopping_cart_change_all_to_mp3_link = "//div[contains(@class,\"setAll\")]//a[2]"
        shopping_cart_change_all_to_wav_link = "//div[contains(@class,\"setAll\")]//a[1]"
        shopping_cart_beatbot = "//div[contains(@class,\"cart-recommendation\")]"
        shopping_cart_nav_to_hold_bin_button = "//div[@class=\"cartHeader\"]//a[contains(@href,\"/hold-bin\")]"
        shopping_cart_change_change_all_audio= "//select[@id=\"setAll\"]"
        shopping_cart_summary_coupon_discount_amount = "//tr/td[contains(text(),\"Discount\")]//following-sibling::td"
        shopping_cart_summary_grand_total = "//td[@id=\"grand-total\"]"
        shopping_cart_susbcriptions_window_continue_to_downloads_button = "//span[contains(text(),\"Continue to Downloads\")]//parent::a"
        shopping_cart_susbcriptions_window_select_all_artists_link = "//div[contains(@class,\"list-group\")]//h3[contains(text(),\"Artists\")]//parent::div//a"
        shopping_cart_susbcriptions_window_select_all_labels_link = "//div[contains(@class,\"list-group\")]//h3[contains(text(),\"Labels\")]//parent::div//a"
        #shopping_cart_login_button = "//div[@class=\"cart\"]//a[contains(@href,\"login\")]"  
        #shopping_cart_register_button = "//div[@class=\"cart\"]//a[contains(@href,\"registration\")]"  

      
        sushi_logo = "//a[@id=\"home\"]"  
      
        track_detail_appear_in_charts = "//li[@name=\"track-detail-charted-on\"]"  
        track_detail_appear_in_release = "//li[@name=\"track-detail-appears-on-release\"]"  
        track_detail_beatbot = "//div[contains(@data-collection-name,\"BeatBot\")]"  
        track_detail_meta_data= "//span[@class=\"detail-metadata\"]"  
        track_detail_page = "//div[@name=\"track-detail-view\"]"  
        track_detail_users_also_bought = "//h3[text()=\"People Also Bought\"]/parent::div/parent::div"
        track_detail_page_artist = "//span[contains(@class,\"detail-metadata\")][1]//a[contains(@href,\"artist\")]"
        track_detail_page_label = "//span[contains(@class,\"meta-value\")]//a[contains(@href,\"label\")]"
        track_detail_page_genre = "//span[contains(@class,\"meta-value\")]//a[contains(@href,\"genre\")]"
        
        
        
        tracks_view_page = "//div[@class=\"playGroup\"][contains(@data-collection-name,\"Tracks\")]"
        # TOKEN can be trackName, label, genre, publishDate
        tracks_view_sort_link = "//td[contains(@class,\"sort-header\")]//a[contains(@href,\"TOKEN\")]"
        tracks_view_sorting_applied = "//td[contains(@class,\"sort-header-applied\")]"
        tracks_view_trackName = "//tr[TOKEN]//td[3]/a"
        tracks_view_label = "//tr[TOKEN]//td[6]/a"
        tracks_view_genre = "//tr[TOKEN]//td[7]/a"
        tracks_view_release_date = "//tr[TOKEN]//td[8]"
        tracks_view_tracks_number = "//table[contains(@class,\"track-grid\")]//tr"
        
        
        transaction_successful_message = "//*[contains(text(),\"Thanks for Your Order\")]" 
        
        top_downloads_view_all_page = "//div[@class=\"top-100 playGroup\"]"
        
        unit_cover_art_link = "//a[contains(@class,\"cover-art\")]"  
        unit_first_artist = "//*[contains(@href,\"artist\")][1]"  
        unit_first_artist_href = "//*[contains(@href,\"artist\")][1]/@href"  
        unit_genre = "//a[contains(@href,\"genre\")]"  
        unit_id ="//a[@name=\"buy_button_link\"]/@data-buy"  
        unit_label = "//a[contains(@href,\"label\")]" 
        unit_label_href = "//a[contains(@href,\"label\")]/@href"   
        unit_price = "//a[contains(@name,\"buy\")]//span[1]"  
        unit_title = "//a[@name=\"unit_title\"]"  
        unit_track = "//a[contains(@href,\"track\")]"
      
      
        welcome_user_text = "//*[contains(text(),\"Welcome\")]"
#------------ constants---------------
        cc_city_update = ""  
        cc_city= "Denver"  
        cc_country = "United States"  
        cc_country_update = "United States"  
        cc_exp_month = "12"  
        cc_exp_month_update = "12"  
        cc_exp_year = "2020"  
        cc_exp_year_update = "2020"  
        cc_first_name = "Sushi"  
        cc_last_name = "SushiLast"  
        cc_name_update = "Sushi Test Update"  
        #cc_number = "5216308891017267"  
        cc_number=   "4444333322221111"
        cc_number_update = "4539529977152636"  
        cc_postal_code = "80205"  
        cc_postal_code_update = "08205"  
        cc_sec_code = "123"  
        cc_sec_code_update = "345"  
        cc_state = "Colorado"  
        cc_street1 = "2933 Blake Street"  
        cc_street1_update = "2933 Blake Street Update"  
        cc_cvv2 = "123"
        
        coupon_code = "141414"
        
        genres_beatport = ["breaks", "chill-out", "deep-house", "dj-tools", "drum-and-bass","dubstep","electro-house","electronica", "funk-r-and-b/40","glitch-hop","hard-dance", "hardcore-hard-techno", "hip-hop", "house","indie-dance-nu-disco","minimal", "pop-rock", "progressive-house","psy-trance","reggae-dub","tech-house","techno","trance"]
        
        login_userid = "sushi3"  
        login_user_password = "password1"  
        login_user_bad_password ="fgjbgbggfmn"
        login_change_password_userid = "sushitest"
        login_change_password_user_password = "password1!"
        
        login_password_nosubwithord = "password1!"  
        login_password_subsnoorders  = "password1!"  
        login_user_changed_password = "password1?"  
        login_user_email = "tester@beatport.com"  
        login_user_password_wrong = "newtest22"  
        login_userid_nosubwithord = "sushiordersnosub"  
        login_userid_subsnoorders = "sushisubsnoorders"  
      
        test_artist = "Roland Clark"  
        test_label = "mau5trap"  
        test_genre = "Breaks"
        test_email = "diana.tzinov@beatport.com"  
        test_email_invalid = "lkfjer,mnf"  
        test_email_nonexisting = "dt1234@rb.com"  
        test_search_all = "love"  
      
        user_email = "@mailinator.com"  
        user_firstname = "dtSushi"  
        user_lastname = "dtSushi"  
        user_password = "password1!"  
        user_username = "testSushi"  
        user_double_quotes_username = "doublequote1"
        user_double_quotes_password = "\"password1"
        user_single_quotes_username = "singlequote1"
        user_single_quotes_password = "\'password1"
        
        
        def __init__(self):
            pass

