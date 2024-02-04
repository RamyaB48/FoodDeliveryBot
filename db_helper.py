{"payload":{"allShortcutsEnabled":true,"fileTree":{"backend":{"items":[{"name":"__pycache__","path":"backend/__pycache__","contentType":"directory"},{"name":"extra","path":"backend/extra","contentType":"directory"},{"name":"db_helper.py","path":"backend/db_helper.py","contentType":"file"},{"name":"generic_helper.py","path":"backend/generic_helper.py","contentType":"file"},{"name":"main.py","path":"backend/main.py","contentType":"file"},{"name":"requirements.txt","path":"backend/requirements.txt","contentType":"file"}],"totalCount":6},"":{"items":[{"name":"backend","path":"backend","contentType":"directory"},{"name":"db","path":"db","contentType":"directory"},{"name":"dialogflow_assets","path":"dialogflow_assets","contentType":"directory"},{"name":"fchatt","path":"fchatt","contentType":"directory"},{"name":"frontend","path":"frontend","contentType":"directory"},{"name":"README.md","path":"README.md","contentType":"file"}],"totalCount":6}},"fileTreeProcessingTime":8.067114,"foldersToFetch":[],"reducedMotionEnabled":"system","repo":{"id":752501179,"defaultBranch":"master","name":"foodDeliveryBot","ownerLogin":"souravverma12","currentUserCanPush":true,"isFork":false,"isEmpty":false,"createdAt":"2024-02-04T08:15:42.000+05:30","ownerAvatar":"https://avatars.githubusercontent.com/u/144450457?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"master","listCacheKey":"v0:1707017740.0","canEdit":true,"refType":"branch","currentOid":"52de1a5380a6b27c09c870fb30719ae736e9b723"},"path":"backend/db_helper.py","currentUser":{"id":110909321,"login":"RamyaB48","userEmail":"ramyab4803@gmail.com"},"blob":{"rawLines":["# Author: Dhaval Patel. Codebasics YouTube Channel","","import mysql.connector","global cnx","","cnx = mysql.connector.connect(","    host=\"localhost\",","    user=\"root\",","    password=\"root\",","    database=\"pandeyji_eatery\"",")","","# Function to call the MySQL stored procedure and insert an order item","def insert_order_item(food_item, quantity, order_id):","    try:","        cursor = cnx.cursor()","","        # Calling the stored procedure","        cursor.callproc('insert_order_item', (food_item, quantity, order_id))","","        # Committing the changes","        cnx.commit()","","        # Closing the cursor","        cursor.close()","","        print(\"Order item inserted successfully!\")","","        return 1","","    except mysql.connector.Error as err:","        print(f\"Error inserting order item: {err}\")","","        # Rollback changes if necessary","        cnx.rollback()","","        return -1","","    except Exception as e:","        print(f\"An error occurred: {e}\")","        # Rollback changes if necessary","        cnx.rollback()","","        return -1","","# Function to insert a record into the order_tracking table","def insert_order_tracking(order_id, status):","    cursor = cnx.cursor()","","    # Inserting the record into the order_tracking table","    insert_query = \"INSERT INTO order_tracking (order_id, status) VALUES (%s, %s)\"","    cursor.execute(insert_query, (order_id, status))","","    # Committing the changes","    cnx.commit()","","    # Closing the cursor","    cursor.close()","","def get_total_order_price(order_id):","    cursor = cnx.cursor()","","    # Executing the SQL query to get the total order price","    query = f\"SELECT get_total_order_price({order_id})\"","    cursor.execute(query)","","    # Fetching the result","    result = cursor.fetchone()[0]","","    # Closing the cursor","    cursor.close()","","    return result","","# Function to get the next available order_id","def get_next_order_id():","    cursor = cnx.cursor()","","    # Executing the SQL query to get the next available order_id","    query = \"SELECT MAX(order_id) FROM orders\"","    cursor.execute(query)","","    # Fetching the result","    result = cursor.fetchone()[0]","","    # Closing the cursor","    cursor.close()","","    # Returning the next available order_id","    if result is None:","        return 1","    else:","        return result + 1","","# Function to fetch the order status from the order_tracking table","def get_order_status(order_id):","    cursor = cnx.cursor()","","    # Executing the SQL query to fetch the order status","    query = f\"SELECT status FROM order_tracking WHERE order_id = {order_id}\"","    cursor.execute(query)","","    # Fetching the result","    result = cursor.fetchone()","","    # Closing the cursor","    cursor.close()","","    # Returning the order status","    if result:","        return result[0]","    else:","        return None","","","if __name__ == \"__main__\":","    # print(get_total_order_price(56))","    # insert_order_item('Samosa', 3, 99)","    # insert_order_item('Pav Bhaji', 1, 99)","    # insert_order_tracking(99, \"in progress\")","    print(get_next_order_id())"],"stylingDirectives":[[{"start":0,"end":50,"cssClass":"pl-c"}],[],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":12,"cssClass":"pl-s1"},{"start":13,"end":22,"cssClass":"pl-s1"}],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":10,"cssClass":"pl-s1"}],[],[{"start":0,"end":3,"cssClass":"pl-s1"},{"start":4,"end":5,"cssClass":"pl-c1"},{"start":6,"end":11,"cssClass":"pl-s1"},{"start":12,"end":21,"cssClass":"pl-s1"},{"start":22,"end":29,"cssClass":"pl-en"}],[{"start":4,"end":8,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":9,"end":20,"cssClass":"pl-s"}],[{"start":4,"end":8,"cssClass":"pl-s1"},{"start":8,"end":9,"cssClass":"pl-c1"},{"start":9,"end":15,"cssClass":"pl-s"}],[{"start":4,"end":12,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":13,"end":19,"cssClass":"pl-s"}],[{"start":4,"end":12,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":13,"end":30,"cssClass":"pl-s"}],[],[],[{"start":0,"end":70,"cssClass":"pl-c"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":21,"cssClass":"pl-en"},{"start":22,"end":31,"cssClass":"pl-s1"},{"start":33,"end":41,"cssClass":"pl-s1"},{"start":43,"end":51,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"}],[{"start":8,"end":14,"cssClass":"pl-s1"},{"start":15,"end":16,"cssClass":"pl-c1"},{"start":17,"end":20,"cssClass":"pl-s1"},{"start":21,"end":27,"cssClass":"pl-en"}],[],[{"start":8,"end":38,"cssClass":"pl-c"}],[{"start":8,"end":14,"cssClass":"pl-s1"},{"start":15,"end":23,"cssClass":"pl-en"},{"start":24,"end":43,"cssClass":"pl-s"},{"start":46,"end":55,"cssClass":"pl-s1"},{"start":57,"end":65,"cssClass":"pl-s1"},{"start":67,"end":75,"cssClass":"pl-s1"}],[],[{"start":8,"end":32,"cssClass":"pl-c"}],[{"start":8,"end":11,"cssClass":"pl-s1"},{"start":12,"end":18,"cssClass":"pl-en"}],[],[{"start":8,"end":28,"cssClass":"pl-c"}],[{"start":8,"end":14,"cssClass":"pl-s1"},{"start":15,"end":20,"cssClass":"pl-en"}],[],[{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":49,"cssClass":"pl-s"}],[],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":16,"cssClass":"pl-c1"}],[],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":16,"cssClass":"pl-s1"},{"start":17,"end":26,"cssClass":"pl-s1"},{"start":27,"end":32,"cssClass":"pl-v"},{"start":33,"end":35,"cssClass":"pl-k"},{"start":36,"end":39,"cssClass":"pl-s1"}],[{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":50,"cssClass":"pl-s"},{"start":44,"end":49,"cssClass":"pl-s1"},{"start":44,"end":45,"cssClass":"pl-kos"},{"start":45,"end":48,"cssClass":"pl-s1"},{"start":48,"end":49,"cssClass":"pl-kos"}],[],[{"start":8,"end":39,"cssClass":"pl-c"}],[{"start":8,"end":11,"cssClass":"pl-s1"},{"start":12,"end":20,"cssClass":"pl-en"}],[],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":16,"cssClass":"pl-c1"},{"start":16,"end":17,"cssClass":"pl-c1"}],[],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":20,"cssClass":"pl-v"},{"start":21,"end":23,"cssClass":"pl-k"},{"start":24,"end":25,"cssClass":"pl-s1"}],[{"start":8,"end":13,"cssClass":"pl-en"},{"start":14,"end":39,"cssClass":"pl-s"},{"start":35,"end":38,"cssClass":"pl-s1"},{"start":35,"end":36,"cssClass":"pl-kos"},{"start":36,"end":37,"cssClass":"pl-s1"},{"start":37,"end":38,"cssClass":"pl-kos"}],[{"start":8,"end":39,"cssClass":"pl-c"}],[{"start":8,"end":11,"cssClass":"pl-s1"},{"start":12,"end":20,"cssClass":"pl-en"}],[],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":16,"cssClass":"pl-c1"},{"start":16,"end":17,"cssClass":"pl-c1"}],[],[{"start":0,"end":59,"cssClass":"pl-c"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":25,"cssClass":"pl-en"},{"start":26,"end":34,"cssClass":"pl-s1"},{"start":36,"end":42,"cssClass":"pl-s1"}],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":16,"cssClass":"pl-s1"},{"start":17,"end":23,"cssClass":"pl-en"}],[],[{"start":4,"end":56,"cssClass":"pl-c"}],[{"start":4,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":82,"cssClass":"pl-s"}],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":18,"cssClass":"pl-en"},{"start":19,"end":31,"cssClass":"pl-s1"},{"start":34,"end":42,"cssClass":"pl-s1"},{"start":44,"end":50,"cssClass":"pl-s1"}],[],[{"start":4,"end":28,"cssClass":"pl-c"}],[{"start":4,"end":7,"cssClass":"pl-s1"},{"start":8,"end":14,"cssClass":"pl-en"}],[],[{"start":4,"end":24,"cssClass":"pl-c"}],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":16,"cssClass":"pl-en"}],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":25,"cssClass":"pl-en"},{"start":26,"end":34,"cssClass":"pl-s1"}],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":16,"cssClass":"pl-s1"},{"start":17,"end":23,"cssClass":"pl-en"}],[],[{"start":4,"end":58,"cssClass":"pl-c"}],[{"start":4,"end":9,"cssClass":"pl-s1"},{"start":10,"end":11,"cssClass":"pl-c1"},{"start":12,"end":55,"cssClass":"pl-s"},{"start":43,"end":53,"cssClass":"pl-s1"},{"start":43,"end":44,"cssClass":"pl-kos"},{"start":44,"end":52,"cssClass":"pl-s1"},{"start":52,"end":53,"cssClass":"pl-kos"}],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":18,"cssClass":"pl-en"},{"start":19,"end":24,"cssClass":"pl-s1"}],[],[{"start":4,"end":25,"cssClass":"pl-c"}],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":19,"cssClass":"pl-s1"},{"start":20,"end":28,"cssClass":"pl-en"},{"start":31,"end":32,"cssClass":"pl-c1"}],[],[{"start":4,"end":24,"cssClass":"pl-c"}],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":16,"cssClass":"pl-en"}],[],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":17,"cssClass":"pl-s1"}],[],[{"start":0,"end":45,"cssClass":"pl-c"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":21,"cssClass":"pl-en"}],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":16,"cssClass":"pl-s1"},{"start":17,"end":23,"cssClass":"pl-en"}],[],[{"start":4,"end":64,"cssClass":"pl-c"}],[{"start":4,"end":9,"cssClass":"pl-s1"},{"start":10,"end":11,"cssClass":"pl-c1"},{"start":12,"end":46,"cssClass":"pl-s"}],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":18,"cssClass":"pl-en"},{"start":19,"end":24,"cssClass":"pl-s1"}],[],[{"start":4,"end":25,"cssClass":"pl-c"}],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":19,"cssClass":"pl-s1"},{"start":20,"end":28,"cssClass":"pl-en"},{"start":31,"end":32,"cssClass":"pl-c1"}],[],[{"start":4,"end":24,"cssClass":"pl-c"}],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":16,"cssClass":"pl-en"}],[],[{"start":4,"end":43,"cssClass":"pl-c"}],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":7,"end":13,"cssClass":"pl-s1"},{"start":14,"end":16,"cssClass":"pl-c1"},{"start":17,"end":21,"cssClass":"pl-c1"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":16,"cssClass":"pl-c1"}],[{"start":4,"end":8,"cssClass":"pl-k"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":21,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-c1"},{"start":24,"end":25,"cssClass":"pl-c1"}],[],[{"start":0,"end":66,"cssClass":"pl-c"}],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":20,"cssClass":"pl-en"},{"start":21,"end":29,"cssClass":"pl-s1"}],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":16,"cssClass":"pl-s1"},{"start":17,"end":23,"cssClass":"pl-en"}],[],[{"start":4,"end":55,"cssClass":"pl-c"}],[{"start":4,"end":9,"cssClass":"pl-s1"},{"start":10,"end":11,"cssClass":"pl-c1"},{"start":12,"end":76,"cssClass":"pl-s"},{"start":65,"end":75,"cssClass":"pl-s1"},{"start":65,"end":66,"cssClass":"pl-kos"},{"start":66,"end":74,"cssClass":"pl-s1"},{"start":74,"end":75,"cssClass":"pl-kos"}],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":18,"cssClass":"pl-en"},{"start":19,"end":24,"cssClass":"pl-s1"}],[],[{"start":4,"end":25,"cssClass":"pl-c"}],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":19,"cssClass":"pl-s1"},{"start":20,"end":28,"cssClass":"pl-en"}],[],[{"start":4,"end":24,"cssClass":"pl-c"}],[{"start":4,"end":10,"cssClass":"pl-s1"},{"start":11,"end":16,"cssClass":"pl-en"}],[],[{"start":4,"end":32,"cssClass":"pl-c"}],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":7,"end":13,"cssClass":"pl-s1"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":21,"cssClass":"pl-s1"},{"start":22,"end":23,"cssClass":"pl-c1"}],[{"start":4,"end":8,"cssClass":"pl-k"}],[{"start":8,"end":14,"cssClass":"pl-k"},{"start":15,"end":19,"cssClass":"pl-c1"}],[],[],[{"start":0,"end":2,"cssClass":"pl-k"},{"start":3,"end":11,"cssClass":"pl-s1"},{"start":12,"end":14,"cssClass":"pl-c1"},{"start":15,"end":25,"cssClass":"pl-s"}],[{"start":4,"end":38,"cssClass":"pl-c"}],[{"start":4,"end":40,"cssClass":"pl-c"}],[{"start":4,"end":43,"cssClass":"pl-c"}],[{"start":4,"end":46,"cssClass":"pl-c"}],[{"start":4,"end":9,"cssClass":"pl-en"},{"start":10,"end":27,"cssClass":"pl-en"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":null,"configFilePath":null,"networkDependabotPath":"/souravverma12/foodDeliveryBot/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":false,"repoAlertsPath":"/souravverma12/foodDeliveryBot/security/dependabot","repoSecurityAndAnalysisPath":"/souravverma12/foodDeliveryBot/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":false},"displayName":"db_helper.py","displayUrl":"https://github.com/souravverma12/foodDeliveryBot/blob/master/backend/db_helper.py?raw=true","headerInfo":{"blobSize":"2.87 KB","deleteInfo":{"deleteTooltip":"Delete this file"},"editInfo":{"editTooltip":"Edit this file"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"98ec3b3","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Fsouravverma12%2FfoodDeliveryBot%2Fblob%2Fmaster%2Fbackend%2Fdb_helper.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"121","truncatedSloc":"87"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":true,"newDiscussionPath":"/souravverma12/foodDeliveryBot/discussions/new","newIssuePath":"/souravverma12/foodDeliveryBot/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/souravverma12/foodDeliveryBot/blob/master/backend/db_helper.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","dismissStackNoticePath":"/settings/dismiss-notice/publish_stack_from_file","releasePath":"/souravverma12/foodDeliveryBot/releases/new?marketplace=true","showPublishActionBanner":false,"showPublishStackBanner":false},"rawBlobUrl":"https://github.com/souravverma12/foodDeliveryBot/raw/master/backend/db_helper.py","renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"symbolsEnabled":true,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"souravverma12","repoName":"foodDeliveryBot","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":null,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timed_out":false,"not_analyzed":false,"symbols":[{"name":"cnx","kind":"constant","ident_start":87,"ident_end":90,"extent_start":87,"extent_end":210,"fully_qualified_name":"cnx","ident_utf16":{"start":{"line_number":5,"utf16_col":0},"end":{"line_number":5,"utf16_col":3}},"extent_utf16":{"start":{"line_number":5,"utf16_col":0},"end":{"line_number":10,"utf16_col":1}}},{"name":"insert_order_item","kind":"function","ident_start":287,"ident_end":304,"extent_start":283,"extent_end":999,"fully_qualified_name":"insert_order_item","ident_utf16":{"start":{"line_number":13,"utf16_col":4},"end":{"line_number":13,"utf16_col":21}},"extent_utf16":{"start":{"line_number":13,"utf16_col":0},"end":{"line_number":43,"utf16_col":17}}},{"name":"insert_order_tracking","kind":"function","ident_start":1065,"ident_end":1086,"extent_start":1061,"extent_end":1417,"fully_qualified_name":"insert_order_tracking","ident_utf16":{"start":{"line_number":46,"utf16_col":4},"end":{"line_number":46,"utf16_col":25}},"extent_utf16":{"start":{"line_number":46,"utf16_col":0},"end":{"line_number":57,"utf16_col":18}}},{"name":"get_total_order_price","kind":"function","ident_start":1423,"ident_end":1444,"extent_start":1419,"extent_end":1748,"fully_qualified_name":"get_total_order_price","ident_utf16":{"start":{"line_number":59,"utf16_col":4},"end":{"line_number":59,"utf16_col":25}},"extent_utf16":{"start":{"line_number":59,"utf16_col":0},"end":{"line_number":72,"utf16_col":17}}},{"name":"get_next_order_id","kind":"function","ident_start":1800,"ident_end":1817,"extent_start":1796,"extent_end":2212,"fully_qualified_name":"get_next_order_id","ident_utf16":{"start":{"line_number":75,"utf16_col":4},"end":{"line_number":75,"utf16_col":21}},"extent_utf16":{"start":{"line_number":75,"utf16_col":0},"end":{"line_number":92,"utf16_col":25}}},{"name":"get_order_status","kind":"function","ident_start":2285,"ident_end":2301,"extent_start":2281,"extent_end":2705,"fully_qualified_name":"get_order_status","ident_utf16":{"start":{"line_number":95,"utf16_col":4},"end":{"line_number":95,"utf16_col":20}},"extent_utf16":{"start":{"line_number":95,"utf16_col":0},"end":{"line_number":112,"utf16_col":19}}}]}},"copilotInfo":{"documentationUrl":"https://docs.github.com/copilot/overview-of-github-copilot/about-github-copilot-for-individuals","notices":{"codeViewPopover":{"dismissed":false,"dismissPath":"/settings/dismiss-notice/code_view_copilot_popover"}},"userAccess":{"accessAllowed":false,"hasSubscriptionEnded":false,"orgHasCFBAccess":false,"userHasCFIAccess":false,"userHasOrgs":false,"userIsOrgAdmin":false,"userIsOrgMember":false,"business":null,"featureRequestInfo":null}},"copilotAccessAllowed":false,"csrf_tokens":{"/souravverma12/foodDeliveryBot/branches":{"post":"CRsgGXoljG5m0BE_ts3b4-acbebbOQm50eewUl-FE60tItTCUZ9tExDGLMqIyX3TZMUWTeVQZTuRt53uczCHVQ"},"/repos/preferences":{"post":"s-xqtwbQD0_kvc88Bp9LL7aKxmpcK2vTwym0oSm96ylqGHZW4WF-BHqstH0SfAZAliPcwmVi4Nvv07OopK4L-Q"}}},"title":"foodDeliveryBot/backend/db_helper.py at master · souravverma12/foodDeliveryBot"}