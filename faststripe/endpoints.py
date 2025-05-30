eps = [
    {
        "path": "/v1/account",
        "verb": "get",
        "op_id": "GetAccount",
        "summary": "Retrieve account",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/account_links",
        "verb": "post",
        "op_id": "PostAccountLinks",
        "summary": "Create an account link",
        "params": [
            {
                "name": "account",
                "description": "The identifier of the account to create an account link for."
            },
            {
                "name": "collect",
                "description": "The collect parameter is deprecated. Use `collection_options` instead."
            },
            {
                "name": "collection_options",
                "description": "Specifies the requirements that Stripe collects from connected accounts in the Connect Onboarding flow."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "refresh_url",
                "description": "The URL the user will be redirected to if the account link is expired, has been previously-visited, or is otherwise invalid. The URL you specify should attempt to generate a new account link with the same parameters used to create the original account link, then redirect the user to the new account link's URL so they can continue with Connect Onboarding. If a new account link cannot be generated or the redirect fails you should display a useful error to the user."
            },
            {
                "name": "return_url",
                "description": "The URL that the user will be redirected to upon leaving or completing the linked flow."
            },
            {
                "name": "type",
                "description": "The type of account link the user is requesting. Possible values are `account_onboarding` or `account_update`."
            }
        ]
    },
    {
        "path": "/v1/account_sessions",
        "verb": "post",
        "op_id": "PostAccountSessions",
        "summary": "Create an Account Session",
        "params": [
            {
                "name": "account",
                "description": "The identifier of the account to create an Account Session for."
            },
            {
                "name": "components",
                "description": "Each key of the dictionary represents an embedded component, and each embedded component maps to its configuration (e.g. whether it has been enabled or not)."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/accounts",
        "verb": "get",
        "op_id": "GetAccounts",
        "summary": "List all connected accounts",
        "params": [
            {
                "name": "created",
                "description": "Only return connected accounts that were created during the given date interval."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/accounts",
        "verb": "post",
        "op_id": "PostAccounts",
        "summary": "",
        "params": [
            {
                "name": "account_token",
                "description": "An [account token](https://stripe.com/docs/api#create_account_token), used to securely provide details to the account."
            },
            {
                "name": "bank_account",
                "description": "Either a token, like the ones returned by [Stripe.js](https://stripe.com/docs/js), or a dictionary containing a user's bank account details."
            },
            {
                "name": "business_profile",
                "description": "Business information about the account."
            },
            {
                "name": "business_type",
                "description": "The business type. Once you create an [Account Link](/api/account_links) or [Account Session](/api/account_sessions), this property can only be updated for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts."
            },
            {
                "name": "capabilities",
                "description": "Each key of the dictionary represents a capability, and each capability\nmaps to its settings (for example, whether it has been requested or not). Each\ncapability is inactive until you have provided its specific\nrequirements and Stripe has verified them. An account might have some\nof its requested capabilities be active and some be inactive.\n\nRequired when [account.controller.stripe_dashboard.type](/api/accounts/create#create_account-controller-dashboard-type)\nis `none`, which includes Custom accounts."
            },
            {
                "name": "company",
                "description": "Information about the company or business. This field is available for any `business_type`. Once you create an [Account Link](/api/account_links) or [Account Session](/api/account_sessions), this property can only be updated for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts."
            },
            {
                "name": "controller",
                "description": "A hash of configuration describing the account controller's attributes."
            },
            {
                "name": "country",
                "description": "The country in which the account holder resides, or in which the business is legally established. This should be an ISO 3166-1 alpha-2 country code. For example, if you are in the United States and the business for which you're creating an account is legally represented in Canada, you would use `CA` as the country for the account being created. Available countries include [Stripe's global markets](https://stripe.com/global) as well as countries where [cross-border payouts](https://stripe.com/docs/connect/cross-border-payouts) are supported."
            },
            {
                "name": "default_currency",
                "description": "Three-letter ISO currency code representing the default currency for the account. This must be a currency that [Stripe supports in the account's country](https://docs.stripe.com/payouts)."
            },
            {
                "name": "documents",
                "description": "Documents that may be submitted to satisfy various informational requests."
            },
            {
                "name": "email",
                "description": "The email address of the account holder. This is only to make the account easier to identify to you. If [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts, Stripe doesn't email the account without your consent."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "external_account",
                "description": "A card or bank account to attach to the account for receiving [payouts](/connect/bank-debit-card-payouts) (you won\u2019t be able to use it for top-ups). You can provide either a token, like the ones returned by [Stripe.js](/js), or a dictionary, as documented in the `external_account` parameter for [bank account](/api#account_create_bank_account) creation. <br><br>By default, providing an external account sets it as the new default external account for its currency, and deletes the old default if one exists. To add additional external accounts without replacing the existing default for the currency, use the [bank account](/api#account_create_bank_account) or [card creation](/api#account_create_card) APIs. After you create an [Account Link](/api/account_links) or [Account Session](/api/account_sessions), this property can only be updated for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts."
            },
            {
                "name": "groups",
                "description": "A hash of account group type to tokens. These are account groups this account should be added to."
            },
            {
                "name": "individual",
                "description": "Information about the person represented by the account. This field is null unless `business_type` is set to `individual`. Once you create an [Account Link](/api/account_links) or [Account Session](/api/account_sessions), this property can only be updated for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "settings",
                "description": "Options for customizing how the account functions within Stripe."
            },
            {
                "name": "tos_acceptance",
                "description": "Details on the account's acceptance of the [Stripe Services Agreement](/connect/updating-accounts#tos-acceptance). This property can only be updated for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts. This property defaults to a `full` service agreement when empty."
            },
            {
                "name": "type",
                "description": "The type of Stripe account to create. May be one of `custom`, `express` or `standard`."
            }
        ]
    },
    {
        "path": "/v1/accounts/{account}",
        "verb": "delete",
        "op_id": "DeleteAccountsAccount",
        "summary": "Delete an account",
        "params": []
    },
    {
        "path": "/v1/accounts/{account}",
        "verb": "get",
        "op_id": "GetAccountsAccount",
        "summary": "Retrieve account",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/accounts/{account}",
        "verb": "post",
        "op_id": "PostAccountsAccount",
        "summary": "Update an account",
        "params": [
            {
                "name": "account_token",
                "description": "An [account token](https://stripe.com/docs/api#create_account_token), used to securely provide details to the account."
            },
            {
                "name": "business_profile",
                "description": "Business information about the account."
            },
            {
                "name": "business_type",
                "description": "The business type. Once you create an [Account Link](/api/account_links) or [Account Session](/api/account_sessions), this property can only be updated for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts."
            },
            {
                "name": "capabilities",
                "description": "Each key of the dictionary represents a capability, and each capability\nmaps to its settings (for example, whether it has been requested or not). Each\ncapability is inactive until you have provided its specific\nrequirements and Stripe has verified them. An account might have some\nof its requested capabilities be active and some be inactive.\n\nRequired when [account.controller.stripe_dashboard.type](/api/accounts/create#create_account-controller-dashboard-type)\nis `none`, which includes Custom accounts."
            },
            {
                "name": "company",
                "description": "Information about the company or business. This field is available for any `business_type`. Once you create an [Account Link](/api/account_links) or [Account Session](/api/account_sessions), this property can only be updated for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts."
            },
            {
                "name": "default_currency",
                "description": "Three-letter ISO currency code representing the default currency for the account. This must be a currency that [Stripe supports in the account's country](https://docs.stripe.com/payouts)."
            },
            {
                "name": "documents",
                "description": "Documents that may be submitted to satisfy various informational requests."
            },
            {
                "name": "email",
                "description": "The email address of the account holder. This is only to make the account easier to identify to you. If [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts, Stripe doesn't email the account without your consent."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "external_account",
                "description": "A card or bank account to attach to the account for receiving [payouts](/connect/bank-debit-card-payouts) (you won\u2019t be able to use it for top-ups). You can provide either a token, like the ones returned by [Stripe.js](/js), or a dictionary, as documented in the `external_account` parameter for [bank account](/api#account_create_bank_account) creation. <br><br>By default, providing an external account sets it as the new default external account for its currency, and deletes the old default if one exists. To add additional external accounts without replacing the existing default for the currency, use the [bank account](/api#account_create_bank_account) or [card creation](/api#account_create_card) APIs. After you create an [Account Link](/api/account_links) or [Account Session](/api/account_sessions), this property can only be updated for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts."
            },
            {
                "name": "groups",
                "description": "A hash of account group type to tokens. These are account groups this account should be added to."
            },
            {
                "name": "individual",
                "description": "Information about the person represented by the account. This field is null unless `business_type` is set to `individual`. Once you create an [Account Link](/api/account_links) or [Account Session](/api/account_sessions), this property can only be updated for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "settings",
                "description": "Options for customizing how the account functions within Stripe."
            },
            {
                "name": "tos_acceptance",
                "description": "Details on the account's acceptance of the [Stripe Services Agreement](/connect/updating-accounts#tos-acceptance). This property can only be updated for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts. This property defaults to a `full` service agreement when empty."
            }
        ]
    },
    {
        "path": "/v1/accounts/{account}/bank_accounts",
        "verb": "post",
        "op_id": "PostAccountsAccountBankAccounts",
        "summary": "Create an external account",
        "params": [
            {
                "name": "bank_account",
                "description": "Either a token, like the ones returned by [Stripe.js](https://stripe.com/docs/js), or a dictionary containing a user's bank account details."
            },
            {
                "name": "default_for_currency",
                "description": "When set to true, or if this is the first external account added in this currency, this account becomes the default external account for its currency."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "external_account",
                "description": "A token, like the ones returned by [Stripe.js](https://stripe.com/docs/js) or a dictionary containing a user's external account details (with the options shown below). Please refer to full [documentation](https://stripe.com/docs/api/external_accounts) instead."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            }
        ]
    },
    {
        "path": "/v1/accounts/{account}/bank_accounts/{id}",
        "verb": "delete",
        "op_id": "DeleteAccountsAccountBankAccountsId",
        "summary": "Delete an external account",
        "params": []
    },
    {
        "path": "/v1/accounts/{account}/bank_accounts/{id}",
        "verb": "get",
        "op_id": "GetAccountsAccountBankAccountsId",
        "summary": "Retrieve an external account",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/accounts/{account}/bank_accounts/{id}",
        "verb": "post",
        "op_id": "PostAccountsAccountBankAccountsId",
        "summary": "",
        "params": [
            {
                "name": "account_holder_name",
                "description": "The name of the person or business that owns the bank account."
            },
            {
                "name": "account_holder_type",
                "description": "The type of entity that holds the account. This can be either `individual` or `company`."
            },
            {
                "name": "account_type",
                "description": "The bank account type. This can only be `checking` or `savings` in most countries. In Japan, this can only be `futsu` or `toza`."
            },
            {
                "name": "address_city",
                "description": "City/District/Suburb/Town/Village."
            },
            {
                "name": "address_country",
                "description": "Billing address country, if provided when creating card."
            },
            {
                "name": "address_line1",
                "description": "Address line 1 (Street address/PO Box/Company name)."
            },
            {
                "name": "address_line2",
                "description": "Address line 2 (Apartment/Suite/Unit/Building)."
            },
            {
                "name": "address_state",
                "description": "State/County/Province/Region."
            },
            {
                "name": "address_zip",
                "description": "ZIP or postal code."
            },
            {
                "name": "default_for_currency",
                "description": "When set to true, this becomes the default external account for its currency."
            },
            {
                "name": "documents",
                "description": "Documents that may be submitted to satisfy various informational requests."
            },
            {
                "name": "exp_month",
                "description": "Two digit number representing the card\u2019s expiration month."
            },
            {
                "name": "exp_year",
                "description": "Four digit number representing the card\u2019s expiration year."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "name",
                "description": "Cardholder name."
            }
        ]
    },
    {
        "path": "/v1/accounts/{account}/capabilities",
        "verb": "get",
        "op_id": "GetAccountsAccountCapabilities",
        "summary": "List all account capabilities",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/accounts/{account}/capabilities/{capability}",
        "verb": "get",
        "op_id": "GetAccountsAccountCapabilitiesCapability",
        "summary": "Retrieve an Account Capability",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/accounts/{account}/capabilities/{capability}",
        "verb": "post",
        "op_id": "PostAccountsAccountCapabilitiesCapability",
        "summary": "Update an Account Capability",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "requested",
                "description": "To request a new capability for an account, pass true. There can be a delay before the requested capability becomes active. If the capability has any activation requirements, the response includes them in the `requirements` arrays.\n\nIf a capability isn't permanent, you can remove it from the account by passing false. Some capabilities are permanent after they've been requested. Attempting to remove a permanent capability returns an error."
            }
        ]
    },
    {
        "path": "/v1/accounts/{account}/external_accounts",
        "verb": "get",
        "op_id": "GetAccountsAccountExternalAccounts",
        "summary": "List all external accounts",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "object",
                "description": "Filter external accounts according to a particular object type."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/accounts/{account}/external_accounts",
        "verb": "post",
        "op_id": "PostAccountsAccountExternalAccounts",
        "summary": "Create an external account",
        "params": [
            {
                "name": "bank_account",
                "description": "Either a token, like the ones returned by [Stripe.js](https://stripe.com/docs/js), or a dictionary containing a user's bank account details."
            },
            {
                "name": "default_for_currency",
                "description": "When set to true, or if this is the first external account added in this currency, this account becomes the default external account for its currency."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "external_account",
                "description": "A token, like the ones returned by [Stripe.js](https://stripe.com/docs/js) or a dictionary containing a user's external account details (with the options shown below). Please refer to full [documentation](https://stripe.com/docs/api/external_accounts) instead."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            }
        ]
    },
    {
        "path": "/v1/accounts/{account}/external_accounts/{id}",
        "verb": "delete",
        "op_id": "DeleteAccountsAccountExternalAccountsId",
        "summary": "Delete an external account",
        "params": []
    },
    {
        "path": "/v1/accounts/{account}/external_accounts/{id}",
        "verb": "get",
        "op_id": "GetAccountsAccountExternalAccountsId",
        "summary": "Retrieve an external account",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/accounts/{account}/external_accounts/{id}",
        "verb": "post",
        "op_id": "PostAccountsAccountExternalAccountsId",
        "summary": "",
        "params": [
            {
                "name": "account_holder_name",
                "description": "The name of the person or business that owns the bank account."
            },
            {
                "name": "account_holder_type",
                "description": "The type of entity that holds the account. This can be either `individual` or `company`."
            },
            {
                "name": "account_type",
                "description": "The bank account type. This can only be `checking` or `savings` in most countries. In Japan, this can only be `futsu` or `toza`."
            },
            {
                "name": "address_city",
                "description": "City/District/Suburb/Town/Village."
            },
            {
                "name": "address_country",
                "description": "Billing address country, if provided when creating card."
            },
            {
                "name": "address_line1",
                "description": "Address line 1 (Street address/PO Box/Company name)."
            },
            {
                "name": "address_line2",
                "description": "Address line 2 (Apartment/Suite/Unit/Building)."
            },
            {
                "name": "address_state",
                "description": "State/County/Province/Region."
            },
            {
                "name": "address_zip",
                "description": "ZIP or postal code."
            },
            {
                "name": "default_for_currency",
                "description": "When set to true, this becomes the default external account for its currency."
            },
            {
                "name": "documents",
                "description": "Documents that may be submitted to satisfy various informational requests."
            },
            {
                "name": "exp_month",
                "description": "Two digit number representing the card\u2019s expiration month."
            },
            {
                "name": "exp_year",
                "description": "Four digit number representing the card\u2019s expiration year."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "name",
                "description": "Cardholder name."
            }
        ]
    },
    {
        "path": "/v1/accounts/{account}/login_links",
        "verb": "post",
        "op_id": "PostAccountsAccountLoginLinks",
        "summary": "Create a login link",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/accounts/{account}/people",
        "verb": "get",
        "op_id": "GetAccountsAccountPeople",
        "summary": "List all persons",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "relationship",
                "description": "Filters on the list of people returned based on the person's relationship to the account's company."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/accounts/{account}/people",
        "verb": "post",
        "op_id": "PostAccountsAccountPeople",
        "summary": "Create a person",
        "params": [
            {
                "name": "additional_tos_acceptances",
                "description": "Details on the legal guardian's or authorizer's acceptance of the required Stripe agreements."
            },
            {
                "name": "address",
                "description": "The person's address."
            },
            {
                "name": "address_kana",
                "description": "The Kana variation of the person's address (Japan only)."
            },
            {
                "name": "address_kanji",
                "description": "The Kanji variation of the person's address (Japan only)."
            },
            {
                "name": "dob",
                "description": "The person's date of birth."
            },
            {
                "name": "documents",
                "description": "Documents that may be submitted to satisfy various informational requests."
            },
            {
                "name": "email",
                "description": "The person's email address."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "first_name",
                "description": "The person's first name."
            },
            {
                "name": "first_name_kana",
                "description": "The Kana variation of the person's first name (Japan only)."
            },
            {
                "name": "first_name_kanji",
                "description": "The Kanji variation of the person's first name (Japan only)."
            },
            {
                "name": "full_name_aliases",
                "description": "A list of alternate names or aliases that the person is known by."
            },
            {
                "name": "gender",
                "description": "The person's gender (International regulations require either \"male\" or \"female\")."
            },
            {
                "name": "id_number",
                "description": "The person's ID number, as appropriate for their country. For example, a social security number in the U.S., social insurance number in Canada, etc. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii)."
            },
            {
                "name": "id_number_secondary",
                "description": "The person's secondary ID number, as appropriate for their country, will be used for enhanced verification checks. In Thailand, this would be the laser code found on the back of an ID card. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii)."
            },
            {
                "name": "last_name",
                "description": "The person's last name."
            },
            {
                "name": "last_name_kana",
                "description": "The Kana variation of the person's last name (Japan only)."
            },
            {
                "name": "last_name_kanji",
                "description": "The Kanji variation of the person's last name (Japan only)."
            },
            {
                "name": "maiden_name",
                "description": "The person's maiden name."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "nationality",
                "description": "The country where the person is a national. Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)), or \"XX\" if unavailable."
            },
            {
                "name": "person_token",
                "description": "A [person token](https://docs.stripe.com/connect/account-tokens), used to securely provide details to the person."
            },
            {
                "name": "phone",
                "description": "The person's phone number."
            },
            {
                "name": "political_exposure",
                "description": "Indicates if the person or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction."
            },
            {
                "name": "registered_address",
                "description": "The person's registered address."
            },
            {
                "name": "relationship",
                "description": "The relationship that this person has with the account's legal entity."
            },
            {
                "name": "ssn_last_4",
                "description": "The last four digits of the person's Social Security number (U.S. only)."
            },
            {
                "name": "us_cfpb_data",
                "description": "Demographic data related to the person."
            },
            {
                "name": "verification",
                "description": "The person's verification status."
            }
        ]
    },
    {
        "path": "/v1/accounts/{account}/people/{person}",
        "verb": "delete",
        "op_id": "DeleteAccountsAccountPeoplePerson",
        "summary": "Delete a person",
        "params": []
    },
    {
        "path": "/v1/accounts/{account}/people/{person}",
        "verb": "get",
        "op_id": "GetAccountsAccountPeoplePerson",
        "summary": "Retrieve a person",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/accounts/{account}/people/{person}",
        "verb": "post",
        "op_id": "PostAccountsAccountPeoplePerson",
        "summary": "Update a person",
        "params": [
            {
                "name": "additional_tos_acceptances",
                "description": "Details on the legal guardian's or authorizer's acceptance of the required Stripe agreements."
            },
            {
                "name": "address",
                "description": "The person's address."
            },
            {
                "name": "address_kana",
                "description": "The Kana variation of the person's address (Japan only)."
            },
            {
                "name": "address_kanji",
                "description": "The Kanji variation of the person's address (Japan only)."
            },
            {
                "name": "dob",
                "description": "The person's date of birth."
            },
            {
                "name": "documents",
                "description": "Documents that may be submitted to satisfy various informational requests."
            },
            {
                "name": "email",
                "description": "The person's email address."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "first_name",
                "description": "The person's first name."
            },
            {
                "name": "first_name_kana",
                "description": "The Kana variation of the person's first name (Japan only)."
            },
            {
                "name": "first_name_kanji",
                "description": "The Kanji variation of the person's first name (Japan only)."
            },
            {
                "name": "full_name_aliases",
                "description": "A list of alternate names or aliases that the person is known by."
            },
            {
                "name": "gender",
                "description": "The person's gender (International regulations require either \"male\" or \"female\")."
            },
            {
                "name": "id_number",
                "description": "The person's ID number, as appropriate for their country. For example, a social security number in the U.S., social insurance number in Canada, etc. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii)."
            },
            {
                "name": "id_number_secondary",
                "description": "The person's secondary ID number, as appropriate for their country, will be used for enhanced verification checks. In Thailand, this would be the laser code found on the back of an ID card. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii)."
            },
            {
                "name": "last_name",
                "description": "The person's last name."
            },
            {
                "name": "last_name_kana",
                "description": "The Kana variation of the person's last name (Japan only)."
            },
            {
                "name": "last_name_kanji",
                "description": "The Kanji variation of the person's last name (Japan only)."
            },
            {
                "name": "maiden_name",
                "description": "The person's maiden name."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "nationality",
                "description": "The country where the person is a national. Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)), or \"XX\" if unavailable."
            },
            {
                "name": "person_token",
                "description": "A [person token](https://docs.stripe.com/connect/account-tokens), used to securely provide details to the person."
            },
            {
                "name": "phone",
                "description": "The person's phone number."
            },
            {
                "name": "political_exposure",
                "description": "Indicates if the person or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction."
            },
            {
                "name": "registered_address",
                "description": "The person's registered address."
            },
            {
                "name": "relationship",
                "description": "The relationship that this person has with the account's legal entity."
            },
            {
                "name": "ssn_last_4",
                "description": "The last four digits of the person's Social Security number (U.S. only)."
            },
            {
                "name": "us_cfpb_data",
                "description": "Demographic data related to the person."
            },
            {
                "name": "verification",
                "description": "The person's verification status."
            }
        ]
    },
    {
        "path": "/v1/accounts/{account}/persons",
        "verb": "get",
        "op_id": "GetAccountsAccountPersons",
        "summary": "List all persons",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "relationship",
                "description": "Filters on the list of people returned based on the person's relationship to the account's company."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/accounts/{account}/persons",
        "verb": "post",
        "op_id": "PostAccountsAccountPersons",
        "summary": "Create a person",
        "params": [
            {
                "name": "additional_tos_acceptances",
                "description": "Details on the legal guardian's or authorizer's acceptance of the required Stripe agreements."
            },
            {
                "name": "address",
                "description": "The person's address."
            },
            {
                "name": "address_kana",
                "description": "The Kana variation of the person's address (Japan only)."
            },
            {
                "name": "address_kanji",
                "description": "The Kanji variation of the person's address (Japan only)."
            },
            {
                "name": "dob",
                "description": "The person's date of birth."
            },
            {
                "name": "documents",
                "description": "Documents that may be submitted to satisfy various informational requests."
            },
            {
                "name": "email",
                "description": "The person's email address."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "first_name",
                "description": "The person's first name."
            },
            {
                "name": "first_name_kana",
                "description": "The Kana variation of the person's first name (Japan only)."
            },
            {
                "name": "first_name_kanji",
                "description": "The Kanji variation of the person's first name (Japan only)."
            },
            {
                "name": "full_name_aliases",
                "description": "A list of alternate names or aliases that the person is known by."
            },
            {
                "name": "gender",
                "description": "The person's gender (International regulations require either \"male\" or \"female\")."
            },
            {
                "name": "id_number",
                "description": "The person's ID number, as appropriate for their country. For example, a social security number in the U.S., social insurance number in Canada, etc. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii)."
            },
            {
                "name": "id_number_secondary",
                "description": "The person's secondary ID number, as appropriate for their country, will be used for enhanced verification checks. In Thailand, this would be the laser code found on the back of an ID card. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii)."
            },
            {
                "name": "last_name",
                "description": "The person's last name."
            },
            {
                "name": "last_name_kana",
                "description": "The Kana variation of the person's last name (Japan only)."
            },
            {
                "name": "last_name_kanji",
                "description": "The Kanji variation of the person's last name (Japan only)."
            },
            {
                "name": "maiden_name",
                "description": "The person's maiden name."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "nationality",
                "description": "The country where the person is a national. Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)), or \"XX\" if unavailable."
            },
            {
                "name": "person_token",
                "description": "A [person token](https://docs.stripe.com/connect/account-tokens), used to securely provide details to the person."
            },
            {
                "name": "phone",
                "description": "The person's phone number."
            },
            {
                "name": "political_exposure",
                "description": "Indicates if the person or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction."
            },
            {
                "name": "registered_address",
                "description": "The person's registered address."
            },
            {
                "name": "relationship",
                "description": "The relationship that this person has with the account's legal entity."
            },
            {
                "name": "ssn_last_4",
                "description": "The last four digits of the person's Social Security number (U.S. only)."
            },
            {
                "name": "us_cfpb_data",
                "description": "Demographic data related to the person."
            },
            {
                "name": "verification",
                "description": "The person's verification status."
            }
        ]
    },
    {
        "path": "/v1/accounts/{account}/persons/{person}",
        "verb": "delete",
        "op_id": "DeleteAccountsAccountPersonsPerson",
        "summary": "Delete a person",
        "params": []
    },
    {
        "path": "/v1/accounts/{account}/persons/{person}",
        "verb": "get",
        "op_id": "GetAccountsAccountPersonsPerson",
        "summary": "Retrieve a person",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/accounts/{account}/persons/{person}",
        "verb": "post",
        "op_id": "PostAccountsAccountPersonsPerson",
        "summary": "Update a person",
        "params": [
            {
                "name": "additional_tos_acceptances",
                "description": "Details on the legal guardian's or authorizer's acceptance of the required Stripe agreements."
            },
            {
                "name": "address",
                "description": "The person's address."
            },
            {
                "name": "address_kana",
                "description": "The Kana variation of the person's address (Japan only)."
            },
            {
                "name": "address_kanji",
                "description": "The Kanji variation of the person's address (Japan only)."
            },
            {
                "name": "dob",
                "description": "The person's date of birth."
            },
            {
                "name": "documents",
                "description": "Documents that may be submitted to satisfy various informational requests."
            },
            {
                "name": "email",
                "description": "The person's email address."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "first_name",
                "description": "The person's first name."
            },
            {
                "name": "first_name_kana",
                "description": "The Kana variation of the person's first name (Japan only)."
            },
            {
                "name": "first_name_kanji",
                "description": "The Kanji variation of the person's first name (Japan only)."
            },
            {
                "name": "full_name_aliases",
                "description": "A list of alternate names or aliases that the person is known by."
            },
            {
                "name": "gender",
                "description": "The person's gender (International regulations require either \"male\" or \"female\")."
            },
            {
                "name": "id_number",
                "description": "The person's ID number, as appropriate for their country. For example, a social security number in the U.S., social insurance number in Canada, etc. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii)."
            },
            {
                "name": "id_number_secondary",
                "description": "The person's secondary ID number, as appropriate for their country, will be used for enhanced verification checks. In Thailand, this would be the laser code found on the back of an ID card. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii)."
            },
            {
                "name": "last_name",
                "description": "The person's last name."
            },
            {
                "name": "last_name_kana",
                "description": "The Kana variation of the person's last name (Japan only)."
            },
            {
                "name": "last_name_kanji",
                "description": "The Kanji variation of the person's last name (Japan only)."
            },
            {
                "name": "maiden_name",
                "description": "The person's maiden name."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "nationality",
                "description": "The country where the person is a national. Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)), or \"XX\" if unavailable."
            },
            {
                "name": "person_token",
                "description": "A [person token](https://docs.stripe.com/connect/account-tokens), used to securely provide details to the person."
            },
            {
                "name": "phone",
                "description": "The person's phone number."
            },
            {
                "name": "political_exposure",
                "description": "Indicates if the person or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction."
            },
            {
                "name": "registered_address",
                "description": "The person's registered address."
            },
            {
                "name": "relationship",
                "description": "The relationship that this person has with the account's legal entity."
            },
            {
                "name": "ssn_last_4",
                "description": "The last four digits of the person's Social Security number (U.S. only)."
            },
            {
                "name": "us_cfpb_data",
                "description": "Demographic data related to the person."
            },
            {
                "name": "verification",
                "description": "The person's verification status."
            }
        ]
    },
    {
        "path": "/v1/accounts/{account}/reject",
        "verb": "post",
        "op_id": "PostAccountsAccountReject",
        "summary": "Reject an account",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "reason",
                "description": "The reason for rejecting the account. Can be `fraud`, `terms_of_service`, or `other`."
            }
        ]
    },
    {
        "path": "/v1/apple_pay/domains",
        "verb": "get",
        "op_id": "GetApplePayDomains",
        "summary": "",
        "params": [
            {
                "name": "domain_name",
                "description": ""
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/apple_pay/domains",
        "verb": "post",
        "op_id": "PostApplePayDomains",
        "summary": "",
        "params": [
            {
                "name": "domain_name",
                "description": ""
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/apple_pay/domains/{domain}",
        "verb": "delete",
        "op_id": "DeleteApplePayDomainsDomain",
        "summary": "",
        "params": []
    },
    {
        "path": "/v1/apple_pay/domains/{domain}",
        "verb": "get",
        "op_id": "GetApplePayDomainsDomain",
        "summary": "",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/application_fees",
        "verb": "get",
        "op_id": "GetApplicationFees",
        "summary": "List all application fees",
        "params": [
            {
                "name": "charge",
                "description": "Only return application fees for the charge specified by this charge ID."
            },
            {
                "name": "created",
                "description": "Only return applications fees that were created during the given date interval."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/application_fees/{fee}/refunds/{id}",
        "verb": "get",
        "op_id": "GetApplicationFeesFeeRefundsId",
        "summary": "Retrieve an application fee refund",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/application_fees/{fee}/refunds/{id}",
        "verb": "post",
        "op_id": "PostApplicationFeesFeeRefundsId",
        "summary": "Update an application fee refund",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            }
        ]
    },
    {
        "path": "/v1/application_fees/{id}",
        "verb": "get",
        "op_id": "GetApplicationFeesId",
        "summary": "Retrieve an application fee",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/application_fees/{id}/refund",
        "verb": "post",
        "op_id": "PostApplicationFeesIdRefund",
        "summary": "",
        "params": [
            {
                "name": "amount",
                "description": ""
            },
            {
                "name": "directive",
                "description": ""
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/application_fees/{id}/refunds",
        "verb": "get",
        "op_id": "GetApplicationFeesIdRefunds",
        "summary": "List all application fee refunds",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/application_fees/{id}/refunds",
        "verb": "post",
        "op_id": "PostApplicationFeesIdRefunds",
        "summary": "Create an application fee refund",
        "params": [
            {
                "name": "amount",
                "description": "A positive integer, in _cents (or local equivalent)_, representing how much of this fee to refund. Can refund only up to the remaining unrefunded amount of the fee."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            }
        ]
    },
    {
        "path": "/v1/apps/secrets",
        "verb": "get",
        "op_id": "GetAppsSecrets",
        "summary": "List secrets",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "scope",
                "description": "Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/apps/secrets",
        "verb": "post",
        "op_id": "PostAppsSecrets",
        "summary": "Set a Secret",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "expires_at",
                "description": "The Unix timestamp for the expiry time of the secret, after which the secret deletes."
            },
            {
                "name": "name",
                "description": "A name for the secret that's unique within the scope."
            },
            {
                "name": "payload",
                "description": "The plaintext secret value to be stored."
            },
            {
                "name": "scope",
                "description": "Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user."
            }
        ]
    },
    {
        "path": "/v1/apps/secrets/delete",
        "verb": "post",
        "op_id": "PostAppsSecretsDelete",
        "summary": "Delete a Secret",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "name",
                "description": "A name for the secret that's unique within the scope."
            },
            {
                "name": "scope",
                "description": "Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user."
            }
        ]
    },
    {
        "path": "/v1/apps/secrets/find",
        "verb": "get",
        "op_id": "GetAppsSecretsFind",
        "summary": "Find a Secret",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "name",
                "description": "A name for the secret that's unique within the scope."
            },
            {
                "name": "scope",
                "description": "Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user."
            }
        ]
    },
    {
        "path": "/v1/balance",
        "verb": "get",
        "op_id": "GetBalance",
        "summary": "Retrieve balance",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/balance/history",
        "verb": "get",
        "op_id": "GetBalanceHistory",
        "summary": "List all balance transactions",
        "params": [
            {
                "name": "created",
                "description": "Only return transactions that were created during the given date interval."
            },
            {
                "name": "currency",
                "description": "Only return transactions in a certain currency. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "payout",
                "description": "For automatic Stripe payouts only, only returns transactions that were paid out on the specified payout ID."
            },
            {
                "name": "source",
                "description": "Only returns the original transaction."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "type",
                "description": "Only returns transactions of the given type. One of: `adjustment`, `advance`, `advance_funding`, `anticipation_repayment`, `application_fee`, `application_fee_refund`, `charge`, `climate_order_purchase`, `climate_order_refund`, `connect_collection_transfer`, `contribution`, `issuing_authorization_hold`, `issuing_authorization_release`, `issuing_dispute`, `issuing_transaction`, `obligation_outbound`, `obligation_reversal_inbound`, `payment`, `payment_failure_refund`, `payment_network_reserve_hold`, `payment_network_reserve_release`, `payment_refund`, `payment_reversal`, `payment_unreconciled`, `payout`, `payout_cancel`, `payout_failure`, `payout_minimum_balance_hold`, `payout_minimum_balance_release`, `refund`, `refund_failure`, `reserve_transaction`, `reserved_funds`, `stripe_fee`, `stripe_fx_fee`, `stripe_balance_payment_debit`, `stripe_balance_payment_debit_reversal`, `tax_fee`, `topup`, `topup_reversal`, `transfer`, `transfer_cancel`, `transfer_failure`, or `transfer_refund`."
            }
        ]
    },
    {
        "path": "/v1/balance/history/{id}",
        "verb": "get",
        "op_id": "GetBalanceHistoryId",
        "summary": "Retrieve a balance transaction",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/balance_transactions",
        "verb": "get",
        "op_id": "GetBalanceTransactions",
        "summary": "List all balance transactions",
        "params": [
            {
                "name": "created",
                "description": "Only return transactions that were created during the given date interval."
            },
            {
                "name": "currency",
                "description": "Only return transactions in a certain currency. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "payout",
                "description": "For automatic Stripe payouts only, only returns transactions that were paid out on the specified payout ID."
            },
            {
                "name": "source",
                "description": "Only returns the original transaction."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "type",
                "description": "Only returns transactions of the given type. One of: `adjustment`, `advance`, `advance_funding`, `anticipation_repayment`, `application_fee`, `application_fee_refund`, `charge`, `climate_order_purchase`, `climate_order_refund`, `connect_collection_transfer`, `contribution`, `issuing_authorization_hold`, `issuing_authorization_release`, `issuing_dispute`, `issuing_transaction`, `obligation_outbound`, `obligation_reversal_inbound`, `payment`, `payment_failure_refund`, `payment_network_reserve_hold`, `payment_network_reserve_release`, `payment_refund`, `payment_reversal`, `payment_unreconciled`, `payout`, `payout_cancel`, `payout_failure`, `payout_minimum_balance_hold`, `payout_minimum_balance_release`, `refund`, `refund_failure`, `reserve_transaction`, `reserved_funds`, `stripe_fee`, `stripe_fx_fee`, `stripe_balance_payment_debit`, `stripe_balance_payment_debit_reversal`, `tax_fee`, `topup`, `topup_reversal`, `transfer`, `transfer_cancel`, `transfer_failure`, or `transfer_refund`."
            }
        ]
    },
    {
        "path": "/v1/balance_transactions/{id}",
        "verb": "get",
        "op_id": "GetBalanceTransactionsId",
        "summary": "Retrieve a balance transaction",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/billing/alerts",
        "verb": "get",
        "op_id": "GetBillingAlerts",
        "summary": "List billing alerts",
        "params": [
            {
                "name": "alert_type",
                "description": "Filter results to only include this type of alert."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "meter",
                "description": "Filter results to only include alerts with the given meter."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/billing/alerts",
        "verb": "post",
        "op_id": "PostBillingAlerts",
        "summary": "Create a billing alert",
        "params": [
            {
                "name": "alert_type",
                "description": "The type of alert to create."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "title",
                "description": "The title of the alert."
            },
            {
                "name": "usage_threshold",
                "description": "The configuration of the usage threshold."
            }
        ]
    },
    {
        "path": "/v1/billing/alerts/{id}",
        "verb": "get",
        "op_id": "GetBillingAlertsId",
        "summary": "Retrieve a billing alert",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/billing/alerts/{id}/activate",
        "verb": "post",
        "op_id": "PostBillingAlertsIdActivate",
        "summary": "Activate a billing alert",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/billing/alerts/{id}/archive",
        "verb": "post",
        "op_id": "PostBillingAlertsIdArchive",
        "summary": "Archive a billing alert",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/billing/alerts/{id}/deactivate",
        "verb": "post",
        "op_id": "PostBillingAlertsIdDeactivate",
        "summary": "Deactivate a billing alert",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/billing/credit_balance_summary",
        "verb": "get",
        "op_id": "GetBillingCreditBalanceSummary",
        "summary": "Retrieve the credit balance summary for a customer",
        "params": [
            {
                "name": "customer",
                "description": "The customer for which to fetch credit balance summary."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "filter",
                "description": "The filter criteria for the credit balance summary."
            }
        ]
    },
    {
        "path": "/v1/billing/credit_balance_transactions",
        "verb": "get",
        "op_id": "GetBillingCreditBalanceTransactions",
        "summary": "List credit balance transactions",
        "params": [
            {
                "name": "credit_grant",
                "description": "The credit grant for which to fetch credit balance transactions."
            },
            {
                "name": "customer",
                "description": "The customer for which to fetch credit balance transactions."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/billing/credit_balance_transactions/{id}",
        "verb": "get",
        "op_id": "GetBillingCreditBalanceTransactionsId",
        "summary": "Retrieve a credit balance transaction",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/billing/credit_grants",
        "verb": "get",
        "op_id": "GetBillingCreditGrants",
        "summary": "List credit grants",
        "params": [
            {
                "name": "customer",
                "description": "Only return credit grants for this customer."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/billing/credit_grants",
        "verb": "post",
        "op_id": "PostBillingCreditGrants",
        "summary": "Create a credit grant",
        "params": [
            {
                "name": "amount",
                "description": "Amount of this credit grant."
            },
            {
                "name": "applicability_config",
                "description": "Configuration specifying what this credit grant applies to. We currently only support `metered` prices that have a [Billing Meter](https://docs.stripe.com/api/billing/meter) attached to them."
            },
            {
                "name": "category",
                "description": "The category of this credit grant."
            },
            {
                "name": "customer",
                "description": "ID of the customer to receive the billing credits."
            },
            {
                "name": "effective_at",
                "description": "The time when the billing credits become effective-when they're eligible for use. It defaults to the current timestamp if not specified."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "expires_at",
                "description": "The time when the billing credits expire. If not specified, the billing credits don't expire."
            },
            {
                "name": "metadata",
                "description": "Set of key-value pairs that you can attach to an object. You can use this to store additional information about the object (for example, cost basis) in a structured format."
            },
            {
                "name": "name",
                "description": "A descriptive name shown in the Dashboard."
            },
            {
                "name": "priority",
                "description": "The desired priority for applying this credit grant. If not specified, it will be set to the default value of 50. The highest priority is 0 and the lowest is 100."
            }
        ]
    },
    {
        "path": "/v1/billing/credit_grants/{id}",
        "verb": "get",
        "op_id": "GetBillingCreditGrantsId",
        "summary": "Retrieve a credit grant",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/billing/credit_grants/{id}",
        "verb": "post",
        "op_id": "PostBillingCreditGrantsId",
        "summary": "Update a credit grant",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "expires_at",
                "description": "The time when the billing credits created by this credit grant expire. If set to empty, the billing credits never expire."
            },
            {
                "name": "metadata",
                "description": "Set of key-value pairs you can attach to an object. You can use this to store additional information about the object (for example, cost basis) in a structured format."
            }
        ]
    },
    {
        "path": "/v1/billing/credit_grants/{id}/expire",
        "verb": "post",
        "op_id": "PostBillingCreditGrantsIdExpire",
        "summary": "Expire a credit grant",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/billing/credit_grants/{id}/void",
        "verb": "post",
        "op_id": "PostBillingCreditGrantsIdVoid",
        "summary": "Void a credit grant",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/billing/meter_event_adjustments",
        "verb": "post",
        "op_id": "PostBillingMeterEventAdjustments",
        "summary": "Create a billing meter event adjustment",
        "params": [
            {
                "name": "cancel",
                "description": "Specifies which event to cancel."
            },
            {
                "name": "event_name",
                "description": "The name of the meter event. Corresponds with the `event_name` field on a meter."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "type",
                "description": "Specifies whether to cancel a single event or a range of events for a time period. Time period cancellation is not supported yet."
            }
        ]
    },
    {
        "path": "/v1/billing/meter_events",
        "verb": "post",
        "op_id": "PostBillingMeterEvents",
        "summary": "Create a billing meter event",
        "params": [
            {
                "name": "event_name",
                "description": "The name of the meter event. Corresponds with the `event_name` field on a meter."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "identifier",
                "description": "A unique identifier for the event. If not provided, one is generated. We recommend using UUID-like identifiers. We will enforce uniqueness within a rolling period of at least 24 hours. The enforcement of uniqueness primarily addresses issues arising from accidental retries or other problems occurring within extremely brief time intervals. This approach helps prevent duplicate entries and ensures data integrity in high-frequency operations."
            },
            {
                "name": "payload",
                "description": "The payload of the event. This must contain the fields corresponding to a meter's `customer_mapping.event_payload_key` (default is `stripe_customer_id`) and `value_settings.event_payload_key` (default is `value`). Read more about the [payload](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage#payload-key-overrides)."
            },
            {
                "name": "timestamp",
                "description": "The time of the event. Measured in seconds since the Unix epoch. Must be within the past 35 calendar days or up to 5 minutes in the future. Defaults to current timestamp if not specified."
            }
        ]
    },
    {
        "path": "/v1/billing/meters",
        "verb": "get",
        "op_id": "GetBillingMeters",
        "summary": "List billing meters",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "status",
                "description": "Filter results to only include meters with the given status."
            }
        ]
    },
    {
        "path": "/v1/billing/meters",
        "verb": "post",
        "op_id": "PostBillingMeters",
        "summary": "Create a billing meter",
        "params": [
            {
                "name": "customer_mapping",
                "description": "Fields that specify how to map a meter event to a customer."
            },
            {
                "name": "default_aggregation",
                "description": "The default settings to aggregate a meter's events with."
            },
            {
                "name": "display_name",
                "description": "The meter\u2019s name. Not visible to the customer."
            },
            {
                "name": "event_name",
                "description": "The name of the meter event to record usage for. Corresponds with the `event_name` field on meter events."
            },
            {
                "name": "event_time_window",
                "description": "The time window to pre-aggregate meter events for, if any."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "value_settings",
                "description": "Fields that specify how to calculate a meter event's value."
            }
        ]
    },
    {
        "path": "/v1/billing/meters/{id}",
        "verb": "get",
        "op_id": "GetBillingMetersId",
        "summary": "Retrieve a billing meter",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/billing/meters/{id}",
        "verb": "post",
        "op_id": "PostBillingMetersId",
        "summary": "Update a billing meter",
        "params": [
            {
                "name": "display_name",
                "description": "The meter\u2019s name. Not visible to the customer."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/billing/meters/{id}/deactivate",
        "verb": "post",
        "op_id": "PostBillingMetersIdDeactivate",
        "summary": "Deactivate a billing meter",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/billing/meters/{id}/event_summaries",
        "verb": "get",
        "op_id": "GetBillingMetersIdEventSummaries",
        "summary": "List billing meter event summaries",
        "params": [
            {
                "name": "customer",
                "description": "The customer for which to fetch event summaries."
            },
            {
                "name": "end_time",
                "description": "The timestamp from when to stop aggregating meter events (exclusive). Must be aligned with minute boundaries."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "start_time",
                "description": "The timestamp from when to start aggregating meter events (inclusive). Must be aligned with minute boundaries."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "value_grouping_window",
                "description": "Specifies what granularity to use when generating event summaries. If not specified, a single event summary would be returned for the specified time range. For hourly granularity, start and end times must align with hour boundaries (e.g., 00:00, 01:00, ..., 23:00). For daily granularity, start and end times must align with UTC day boundaries (00:00 UTC)."
            }
        ]
    },
    {
        "path": "/v1/billing/meters/{id}/reactivate",
        "verb": "post",
        "op_id": "PostBillingMetersIdReactivate",
        "summary": "Reactivate a billing meter",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/billing_portal/configurations",
        "verb": "get",
        "op_id": "GetBillingPortalConfigurations",
        "summary": "List portal configurations",
        "params": [
            {
                "name": "active",
                "description": "Only return configurations that are active or inactive (e.g., pass `true` to only list active configurations)."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "is_default",
                "description": "Only return the default or non-default configurations (e.g., pass `true` to only list the default configuration)."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/billing_portal/configurations",
        "verb": "post",
        "op_id": "PostBillingPortalConfigurations",
        "summary": "Create a portal configuration",
        "params": [
            {
                "name": "business_profile",
                "description": "The business information shown to customers in the portal."
            },
            {
                "name": "default_return_url",
                "description": "The default URL to redirect customers to when they click on the portal's link to return to your website. This can be [overriden](https://stripe.com/docs/api/customer_portal/sessions/create#create_portal_session-return_url) when creating the session."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "features",
                "description": "Information about the features available in the portal."
            },
            {
                "name": "login_page",
                "description": "The hosted login page for this configuration. Learn more about the portal login page in our [integration docs](https://stripe.com/docs/billing/subscriptions/integrating-customer-portal#share)."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            }
        ]
    },
    {
        "path": "/v1/billing_portal/configurations/{configuration}",
        "verb": "get",
        "op_id": "GetBillingPortalConfigurationsConfiguration",
        "summary": "Retrieve a portal configuration",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/billing_portal/configurations/{configuration}",
        "verb": "post",
        "op_id": "PostBillingPortalConfigurationsConfiguration",
        "summary": "Update a portal configuration",
        "params": [
            {
                "name": "active",
                "description": "Whether the configuration is active and can be used to create portal sessions."
            },
            {
                "name": "business_profile",
                "description": "The business information shown to customers in the portal."
            },
            {
                "name": "default_return_url",
                "description": "The default URL to redirect customers to when they click on the portal's link to return to your website. This can be [overriden](https://stripe.com/docs/api/customer_portal/sessions/create#create_portal_session-return_url) when creating the session."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "features",
                "description": "Information about the features available in the portal."
            },
            {
                "name": "login_page",
                "description": "The hosted login page for this configuration. Learn more about the portal login page in our [integration docs](https://stripe.com/docs/billing/subscriptions/integrating-customer-portal#share)."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            }
        ]
    },
    {
        "path": "/v1/billing_portal/sessions",
        "verb": "post",
        "op_id": "PostBillingPortalSessions",
        "summary": "Create a portal session",
        "params": [
            {
                "name": "configuration",
                "description": "The ID of an existing [configuration](https://stripe.com/docs/api/customer_portal/configuration) to use for this session, describing its functionality and features. If not specified, the session uses the default configuration."
            },
            {
                "name": "customer",
                "description": "The ID of an existing customer."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "flow_data",
                "description": "Information about a specific flow for the customer to go through. See the [docs](https://stripe.com/docs/customer-management/portal-deep-links) to learn more about using customer portal deep links and flows."
            },
            {
                "name": "locale",
                "description": "The IETF language tag of the locale customer portal is displayed in. If blank or auto, the customer\u2019s `preferred_locales` or browser\u2019s locale is used."
            },
            {
                "name": "on_behalf_of",
                "description": "The `on_behalf_of` account to use for this session. When specified, only subscriptions and invoices with this `on_behalf_of` account appear in the portal. For more information, see the [docs](https://stripe.com/docs/connect/separate-charges-and-transfers#settlement-merchant). Use the [Accounts API](https://stripe.com/docs/api/accounts/object#account_object-settings-branding) to modify the `on_behalf_of` account's branding settings, which the portal displays."
            },
            {
                "name": "return_url",
                "description": "The default URL to redirect customers to when they click on the portal's link to return to your website."
            }
        ]
    },
    {
        "path": "/v1/charges",
        "verb": "get",
        "op_id": "GetCharges",
        "summary": "List all charges",
        "params": [
            {
                "name": "created",
                "description": "Only return charges that were created during the given date interval."
            },
            {
                "name": "customer",
                "description": "Only return charges for the customer specified by this customer ID."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "payment_intent",
                "description": "Only return charges that were created by the PaymentIntent specified by this PaymentIntent ID."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "transfer_group",
                "description": "Only return charges for this transfer group, limited to 100."
            }
        ]
    },
    {
        "path": "/v1/charges",
        "verb": "post",
        "op_id": "PostCharges",
        "summary": "",
        "params": [
            {
                "name": "amount",
                "description": "Amount intended to be collected by this payment. A positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge \u00a5100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99)."
            },
            {
                "name": "application_fee",
                "description": ""
            },
            {
                "name": "application_fee_amount",
                "description": "A fee in cents (or local equivalent) that will be applied to the charge and transferred to the application owner's Stripe account. The request must be made with an OAuth key or the `Stripe-Account` header in order to take an application fee. For more information, see the application fees [documentation](https://stripe.com/docs/connect/direct-charges#collect-fees)."
            },
            {
                "name": "capture",
                "description": "Whether to immediately capture the charge. Defaults to `true`. When `false`, the charge issues an authorization (or pre-authorization), and will need to be [captured](https://stripe.com/docs/api#capture_charge) later. Uncaptured charges expire after a set number of days (7 by default). For more information, see the [authorizing charges and settling later](https://stripe.com/docs/charges/placing-a-hold) documentation."
            },
            {
                "name": "card",
                "description": "A token, like the ones returned by [Stripe.js](https://stripe.com/docs/js)."
            },
            {
                "name": "currency",
                "description": "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "customer",
                "description": "The ID of an existing customer that will be charged in this request."
            },
            {
                "name": "description",
                "description": "An arbitrary string which you can attach to a `Charge` object. It is displayed when in the web interface alongside the charge. Note that if you use Stripe to send automatic email receipts to your customers, your receipt emails will include the `description` of the charge(s) that they are describing."
            },
            {
                "name": "destination",
                "description": ""
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "on_behalf_of",
                "description": "The Stripe account ID for which these funds are intended. Automatically set if you use the `destination` parameter. For details, see [Creating Separate Charges and Transfers](https://stripe.com/docs/connect/separate-charges-and-transfers#settlement-merchant)."
            },
            {
                "name": "radar_options",
                "description": "Options to configure Radar. See [Radar Session](https://stripe.com/docs/radar/radar-session) for more information."
            },
            {
                "name": "receipt_email",
                "description": "The email address to which this charge's [receipt](https://stripe.com/docs/dashboard/receipts) will be sent. The receipt will not be sent until the charge is paid, and no receipts will be sent for test mode charges. If this charge is for a [Customer](https://stripe.com/docs/api/customers/object), the email address specified here will override the customer's email address. If `receipt_email` is specified for a charge in live mode, a receipt will be sent regardless of your [email settings](https://dashboard.stripe.com/account/emails)."
            },
            {
                "name": "shipping",
                "description": "Shipping information for the charge. Helps prevent fraud on charges for physical goods."
            },
            {
                "name": "source",
                "description": "A payment source to be charged. This can be the ID of a [card](https://stripe.com/docs/api#cards) (i.e., credit or debit card), a [bank account](https://stripe.com/docs/api#bank_accounts), a [source](https://stripe.com/docs/api#sources), a [token](https://stripe.com/docs/api#tokens), or a [connected account](https://stripe.com/docs/connect/account-debits#charging-a-connected-account). For certain sources---namely, [cards](https://stripe.com/docs/api#cards), [bank accounts](https://stripe.com/docs/api#bank_accounts), and attached [sources](https://stripe.com/docs/api#sources)---you must also pass the ID of the associated customer."
            },
            {
                "name": "statement_descriptor",
                "description": "For a non-card charge, text that appears on the customer's statement as the statement descriptor. This value overrides the account's default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).\n\nFor a card charge, this value is ignored unless you don't specify a `statement_descriptor_suffix`, in which case this value is used as the suffix."
            },
            {
                "name": "statement_descriptor_suffix",
                "description": "Provides information about a card charge. Concatenated to the account's [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors#static) to form the complete statement descriptor that appears on the customer's statement. If the account has no prefix value, the suffix is concatenated to the account's statement descriptor."
            },
            {
                "name": "transfer_data",
                "description": "An optional dictionary including the account to automatically transfer to as part of a destination charge. [See the Connect documentation](https://stripe.com/docs/connect/destination-charges) for details."
            },
            {
                "name": "transfer_group",
                "description": "A string that identifies this transaction as part of a group. For details, see [Grouping transactions](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options)."
            }
        ]
    },
    {
        "path": "/v1/charges/search",
        "verb": "get",
        "op_id": "GetChargesSearch",
        "summary": "Search charges",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "page",
                "description": "A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results."
            },
            {
                "name": "query",
                "description": "The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for charges](https://stripe.com/docs/search#query-fields-for-charges)."
            }
        ]
    },
    {
        "path": "/v1/charges/{charge}",
        "verb": "get",
        "op_id": "GetChargesCharge",
        "summary": "Retrieve a charge",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/charges/{charge}",
        "verb": "post",
        "op_id": "PostChargesCharge",
        "summary": "Update a charge",
        "params": [
            {
                "name": "customer",
                "description": "The ID of an existing customer that will be associated with this request. This field may only be updated if there is no existing associated customer with this charge."
            },
            {
                "name": "description",
                "description": "An arbitrary string which you can attach to a charge object. It is displayed when in the web interface alongside the charge. Note that if you use Stripe to send automatic email receipts to your customers, your receipt emails will include the `description` of the charge(s) that they are describing."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "fraud_details",
                "description": "A set of key-value pairs you can attach to a charge giving information about its riskiness. If you believe a charge is fraudulent, include a `user_report` key with a value of `fraudulent`. If you believe a charge is safe, include a `user_report` key with a value of `safe`. Stripe will use the information you send to improve our fraud detection algorithms."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "receipt_email",
                "description": "This is the email address that the receipt for this charge will be sent to. If this field is updated, then a new email receipt will be sent to the updated address."
            },
            {
                "name": "shipping",
                "description": "Shipping information for the charge. Helps prevent fraud on charges for physical goods."
            },
            {
                "name": "transfer_group",
                "description": "A string that identifies this transaction as part of a group. `transfer_group` may only be provided if it has not been set. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options) for details."
            }
        ]
    },
    {
        "path": "/v1/charges/{charge}/capture",
        "verb": "post",
        "op_id": "PostChargesChargeCapture",
        "summary": "Capture a payment",
        "params": [
            {
                "name": "amount",
                "description": "The amount to capture, which must be less than or equal to the original amount."
            },
            {
                "name": "application_fee",
                "description": "An application fee to add on to this charge."
            },
            {
                "name": "application_fee_amount",
                "description": "An application fee amount to add on to this charge, which must be less than or equal to the original amount."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "receipt_email",
                "description": "The email address to send this charge's receipt to. This will override the previously-specified email address for this charge, if one was set. Receipts will not be sent in test mode."
            },
            {
                "name": "statement_descriptor",
                "description": "For a non-card charge, text that appears on the customer's statement as the statement descriptor. This value overrides the account's default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).\n\nFor a card charge, this value is ignored unless you don't specify a `statement_descriptor_suffix`, in which case this value is used as the suffix."
            },
            {
                "name": "statement_descriptor_suffix",
                "description": "Provides information about a card charge. Concatenated to the account's [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors#static) to form the complete statement descriptor that appears on the customer's statement. If the account has no prefix value, the suffix is concatenated to the account's statement descriptor."
            },
            {
                "name": "transfer_data",
                "description": "An optional dictionary including the account to automatically transfer to as part of a destination charge. [See the Connect documentation](https://stripe.com/docs/connect/destination-charges) for details."
            },
            {
                "name": "transfer_group",
                "description": "A string that identifies this transaction as part of a group. `transfer_group` may only be provided if it has not been set. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options) for details."
            }
        ]
    },
    {
        "path": "/v1/charges/{charge}/dispute",
        "verb": "get",
        "op_id": "GetChargesChargeDispute",
        "summary": "",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/charges/{charge}/dispute",
        "verb": "post",
        "op_id": "PostChargesChargeDispute",
        "summary": "",
        "params": [
            {
                "name": "evidence",
                "description": "Evidence to upload, to respond to a dispute. Updating any field in the hash will submit all fields in the hash for review. The combined character count of all fields is limited to 150,000."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "submit",
                "description": "Whether to immediately submit evidence to the bank. If `false`, evidence is staged on the dispute. Staged evidence is visible in the API and Dashboard, and can be submitted to the bank by making another request with this attribute set to `true` (the default)."
            }
        ]
    },
    {
        "path": "/v1/charges/{charge}/dispute/close",
        "verb": "post",
        "op_id": "PostChargesChargeDisputeClose",
        "summary": "",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/charges/{charge}/refund",
        "verb": "post",
        "op_id": "PostChargesChargeRefund",
        "summary": "Create a refund",
        "params": [
            {
                "name": "amount",
                "description": "A positive integer in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) representing how much of this charge to refund. Can refund only up to the remaining, unrefunded amount of the charge."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "instructions_email",
                "description": "For payment methods without native refund support (e.g., Konbini, PromptPay), use this email from the customer to receive refund instructions."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "payment_intent",
                "description": "The identifier of the PaymentIntent to refund."
            },
            {
                "name": "reason",
                "description": "String indicating the reason for the refund. If set, possible values are `duplicate`, `fraudulent`, and `requested_by_customer`. If you believe the charge to be fraudulent, specifying `fraudulent` as the reason will add the associated card and email to your [block lists](https://stripe.com/docs/radar/lists), and will also help us improve our fraud detection algorithms."
            },
            {
                "name": "refund_application_fee",
                "description": "Boolean indicating whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded. An application fee can be refunded only by the application that created the charge."
            },
            {
                "name": "reverse_transfer",
                "description": "Boolean indicating whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount).<br><br>A transfer can be reversed only by the application that created the charge."
            }
        ]
    },
    {
        "path": "/v1/charges/{charge}/refunds",
        "verb": "get",
        "op_id": "GetChargesChargeRefunds",
        "summary": "List all refunds",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/charges/{charge}/refunds",
        "verb": "post",
        "op_id": "PostChargesChargeRefunds",
        "summary": "Create customer balance refund",
        "params": [
            {
                "name": "amount",
                "description": ""
            },
            {
                "name": "currency",
                "description": "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "customer",
                "description": "Customer whose customer balance to refund from."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "instructions_email",
                "description": "For payment methods without native refund support (e.g., Konbini, PromptPay), use this email from the customer to receive refund instructions."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "origin",
                "description": "Origin of the refund"
            },
            {
                "name": "payment_intent",
                "description": "The identifier of the PaymentIntent to refund."
            },
            {
                "name": "reason",
                "description": "String indicating the reason for the refund. If set, possible values are `duplicate`, `fraudulent`, and `requested_by_customer`. If you believe the charge to be fraudulent, specifying `fraudulent` as the reason will add the associated card and email to your [block lists](https://stripe.com/docs/radar/lists), and will also help us improve our fraud detection algorithms."
            },
            {
                "name": "refund_application_fee",
                "description": "Boolean indicating whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded. An application fee can be refunded only by the application that created the charge."
            },
            {
                "name": "reverse_transfer",
                "description": "Boolean indicating whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount).<br><br>A transfer can be reversed only by the application that created the charge."
            }
        ]
    },
    {
        "path": "/v1/charges/{charge}/refunds/{refund}",
        "verb": "get",
        "op_id": "GetChargesChargeRefundsRefund",
        "summary": "",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/charges/{charge}/refunds/{refund}",
        "verb": "post",
        "op_id": "PostChargesChargeRefundsRefund",
        "summary": "",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": ""
            }
        ]
    },
    {
        "path": "/v1/checkout/sessions",
        "verb": "get",
        "op_id": "GetCheckoutSessions",
        "summary": "List all Checkout Sessions",
        "params": [
            {
                "name": "created",
                "description": "Only return Checkout Sessions that were created during the given date interval."
            },
            {
                "name": "customer",
                "description": "Only return the Checkout Sessions for the Customer specified."
            },
            {
                "name": "customer_details",
                "description": "Only return the Checkout Sessions for the Customer details specified."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "payment_intent",
                "description": "Only return the Checkout Session for the PaymentIntent specified."
            },
            {
                "name": "payment_link",
                "description": "Only return the Checkout Sessions for the Payment Link specified."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "status",
                "description": "Only return the Checkout Sessions matching the given status."
            },
            {
                "name": "subscription",
                "description": "Only return the Checkout Session for the subscription specified."
            }
        ]
    },
    {
        "path": "/v1/checkout/sessions",
        "verb": "post",
        "op_id": "PostCheckoutSessions",
        "summary": "Create a Checkout Session",
        "params": [
            {
                "name": "adaptive_pricing",
                "description": "Settings for price localization with [Adaptive Pricing](https://docs.stripe.com/payments/checkout/adaptive-pricing)."
            },
            {
                "name": "after_expiration",
                "description": "Configure actions after a Checkout Session has expired."
            },
            {
                "name": "allow_promotion_codes",
                "description": "Enables user redeemable promotion codes."
            },
            {
                "name": "automatic_tax",
                "description": "Settings for automatic tax lookup for this session and resulting payments, invoices, and subscriptions."
            },
            {
                "name": "billing_address_collection",
                "description": "Specify whether Checkout should collect the customer's billing address. Defaults to `auto`."
            },
            {
                "name": "cancel_url",
                "description": "If set, Checkout displays a back button and customers will be directed to this URL if they decide to cancel payment and return to your website. This parameter is not allowed if ui_mode is `embedded` or `custom`."
            },
            {
                "name": "client_reference_id",
                "description": "A unique string to reference the Checkout Session. This can be a\ncustomer ID, a cart ID, or similar, and can be used to reconcile the\nsession with your internal systems."
            },
            {
                "name": "consent_collection",
                "description": "Configure fields for the Checkout Session to gather active consent from customers."
            },
            {
                "name": "currency",
                "description": "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). Required in `setup` mode when `payment_method_types` is not set."
            },
            {
                "name": "custom_fields",
                "description": "Collect additional information from your customer using custom fields. Up to 3 fields are supported."
            },
            {
                "name": "custom_text",
                "description": "Display additional text for your customers using custom text."
            },
            {
                "name": "customer",
                "description": "ID of an existing Customer, if one exists. In `payment` mode, the customer\u2019s most recently saved card\npayment method will be used to prefill the email, name, card details, and billing address\non the Checkout page. In `subscription` mode, the customer\u2019s [default payment method](https://stripe.com/docs/api/customers/update#update_customer-invoice_settings-default_payment_method)\nwill be used if it\u2019s a card, otherwise the most recently saved card will be used. A valid billing address, billing name and billing email are required on the payment method for Checkout to prefill the customer's card details.\n\nIf the Customer already has a valid [email](https://stripe.com/docs/api/customers/object#customer_object-email) set, the email will be prefilled and not editable in Checkout.\nIf the Customer does not have a valid `email`, Checkout will set the email entered during the session on the Customer.\n\nIf blank for Checkout Sessions in `subscription` mode or with `customer_creation` set as `always` in `payment` mode, Checkout will create a new Customer object based on information provided during the payment flow.\n\nYou can set [`payment_intent_data.setup_future_usage`](https://stripe.com/docs/api/checkout/sessions/create#create_checkout_session-payment_intent_data-setup_future_usage) to have Checkout automatically attach the payment method to the Customer you pass in for future reuse."
            },
            {
                "name": "customer_creation",
                "description": "Configure whether a Checkout Session creates a [Customer](https://stripe.com/docs/api/customers) during Session confirmation.\n\nWhen a Customer is not created, you can still retrieve email, address, and other customer data entered in Checkout\nwith [customer_details](https://stripe.com/docs/api/checkout/sessions/object#checkout_session_object-customer_details).\n\nSessions that don't create Customers instead are grouped by [guest customers](https://stripe.com/docs/payments/checkout/guest-customers)\nin the Dashboard. Promotion codes limited to first time customers will return invalid for these Sessions.\n\nCan only be set in `payment` and `setup` mode."
            },
            {
                "name": "customer_email",
                "description": "If provided, this value will be used when the Customer object is created.\nIf not provided, customers will be asked to enter their email address.\nUse this parameter to prefill customer data if you already have an email\non file. To access information about the customer once a session is\ncomplete, use the `customer` field."
            },
            {
                "name": "customer_update",
                "description": "Controls what fields on Customer can be updated by the Checkout Session. Can only be provided when `customer` is provided."
            },
            {
                "name": "discounts",
                "description": "The coupon or promotion code to apply to this Session. Currently, only up to one may be specified."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "expires_at",
                "description": "The Epoch time in seconds at which the Checkout Session will expire. It can be anywhere from 30 minutes to 24 hours after Checkout Session creation. By default, this value is 24 hours from creation."
            },
            {
                "name": "invoice_creation",
                "description": "Generate a post-purchase Invoice for one-time payments."
            },
            {
                "name": "line_items",
                "description": "A list of items the customer is purchasing. Use this parameter to pass one-time or recurring [Prices](https://stripe.com/docs/api/prices).\n\nFor `payment` mode, there is a maximum of 100 line items, however it is recommended to consolidate line items if there are more than a few dozen.\n\nFor `subscription` mode, there is a maximum of 20 line items with recurring Prices and 20 line items with one-time Prices. Line items with one-time Prices will be on the initial invoice only."
            },
            {
                "name": "locale",
                "description": "The IETF language tag of the locale Checkout is displayed in. If blank or `auto`, the browser's locale is used."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "mode",
                "description": "The mode of the Checkout Session. Pass `subscription` if the Checkout Session includes at least one recurring item."
            },
            {
                "name": "optional_items",
                "description": "A list of optional items the customer can add to their order at checkout. Use this parameter to pass one-time or recurring [Prices](https://stripe.com/docs/api/prices).\n\nThere is a maximum of 10 optional items allowed on a Checkout Session, and the existing limits on the number of line items allowed on a Checkout Session apply to the combined number of line items and optional items.\n\nFor `payment` mode, there is a maximum of 100 combined line items and optional items, however it is recommended to consolidate items if there are more than a few dozen.\n\nFor `subscription` mode, there is a maximum of 20 line items and optional items with recurring Prices and 20 line items and optional items with one-time Prices."
            },
            {
                "name": "payment_intent_data",
                "description": "A subset of parameters to be passed to PaymentIntent creation for Checkout Sessions in `payment` mode."
            },
            {
                "name": "payment_method_collection",
                "description": "Specify whether Checkout should collect a payment method. When set to `if_required`, Checkout will not collect a payment method when the total due for the session is 0.\nThis may occur if the Checkout Session includes a free trial or a discount.\n\nCan only be set in `subscription` mode. Defaults to `always`.\n\nIf you'd like information on how to collect a payment method outside of Checkout, read the guide on configuring [subscriptions with a free trial](https://stripe.com/docs/payments/checkout/free-trials)."
            },
            {
                "name": "payment_method_configuration",
                "description": "The ID of the payment method configuration to use with this Checkout session."
            },
            {
                "name": "payment_method_data",
                "description": "This parameter allows you to set some attributes on the payment method created during a Checkout session."
            },
            {
                "name": "payment_method_options",
                "description": "Payment-method-specific configuration."
            },
            {
                "name": "payment_method_types",
                "description": "A list of the types of payment methods (e.g., `card`) this Checkout Session can accept.\n\nYou can omit this attribute to manage your payment methods from the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods).\nSee [Dynamic Payment Methods](https://stripe.com/docs/payments/payment-methods/integration-options#using-dynamic-payment-methods) for more details.\n\nRead more about the supported payment methods and their requirements in our [payment\nmethod details guide](/docs/payments/checkout/payment-methods).\n\nIf multiple payment methods are passed, Checkout will dynamically reorder them to\nprioritize the most relevant payment methods based on the customer's location and\nother characteristics."
            },
            {
                "name": "permissions",
                "description": "This property is used to set up permissions for various actions (e.g., update) on the CheckoutSession object. Can only be set when creating `embedded` or `custom` sessions.\n\nFor specific permissions, please refer to their dedicated subsections, such as `permissions.update_shipping_details`."
            },
            {
                "name": "phone_number_collection",
                "description": "Controls phone number collection settings for the session.\n\nWe recommend that you review your privacy policy and check with your legal contacts\nbefore using this feature. Learn more about [collecting phone numbers with Checkout](https://stripe.com/docs/payments/checkout/phone-numbers)."
            },
            {
                "name": "redirect_on_completion",
                "description": "This parameter applies to `ui_mode: embedded`. Learn more about the [redirect behavior](https://stripe.com/docs/payments/checkout/custom-success-page?payment-ui=embedded-form) of embedded sessions. Defaults to `always`."
            },
            {
                "name": "return_url",
                "description": "The URL to redirect your customer back to after they authenticate or cancel their payment on the\npayment method's app or site. This parameter is required if `ui_mode` is `embedded` or `custom`\nand redirect-based payment methods are enabled on the session."
            },
            {
                "name": "saved_payment_method_options",
                "description": "Controls saved payment method settings for the session. Only available in `payment` and `subscription` mode."
            },
            {
                "name": "setup_intent_data",
                "description": "A subset of parameters to be passed to SetupIntent creation for Checkout Sessions in `setup` mode."
            },
            {
                "name": "shipping_address_collection",
                "description": "When set, provides configuration for Checkout to collect a shipping address from a customer."
            },
            {
                "name": "shipping_options",
                "description": "The shipping rate options to apply to this Session. Up to a maximum of 5."
            },
            {
                "name": "submit_type",
                "description": "Describes the type of transaction being performed by Checkout in order\nto customize relevant text on the page, such as the submit button.\n `submit_type` can only be specified on Checkout Sessions in\n`payment` or `subscription` mode. If blank or `auto`, `pay` is used."
            },
            {
                "name": "subscription_data",
                "description": "A subset of parameters to be passed to subscription creation for Checkout Sessions in `subscription` mode."
            },
            {
                "name": "success_url",
                "description": "The URL to which Stripe should send customers when payment or setup\nis complete.\nThis parameter is not allowed if ui_mode is `embedded` or `custom`. If you'd like to use\ninformation from the successful Checkout Session on your page, read the\nguide on [customizing your success page](https://stripe.com/docs/payments/checkout/custom-success-page)."
            },
            {
                "name": "tax_id_collection",
                "description": "Controls tax ID collection during checkout."
            },
            {
                "name": "ui_mode",
                "description": "The UI mode of the Session. Defaults to `hosted`."
            },
            {
                "name": "wallet_options",
                "description": "Wallet-specific configuration."
            }
        ]
    },
    {
        "path": "/v1/checkout/sessions/{session}",
        "verb": "get",
        "op_id": "GetCheckoutSessionsSession",
        "summary": "Retrieve a Checkout Session",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/checkout/sessions/{session}",
        "verb": "post",
        "op_id": "PostCheckoutSessionsSession",
        "summary": "Update a Checkout Session",
        "params": [
            {
                "name": "collected_information",
                "description": "Information about the customer collected within the Checkout Session. Can only be set when updating `embedded` or `custom` sessions."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "shipping_options",
                "description": "The shipping rate options to apply to this Session. Up to a maximum of 5."
            }
        ]
    },
    {
        "path": "/v1/checkout/sessions/{session}/expire",
        "verb": "post",
        "op_id": "PostCheckoutSessionsSessionExpire",
        "summary": "Expire a Checkout Session",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/checkout/sessions/{session}/line_items",
        "verb": "get",
        "op_id": "GetCheckoutSessionsSessionLineItems",
        "summary": "Retrieve a Checkout Session's line items",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/climate/orders",
        "verb": "get",
        "op_id": "GetClimateOrders",
        "summary": "List orders",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/climate/orders",
        "verb": "post",
        "op_id": "PostClimateOrders",
        "summary": "Create an order",
        "params": [
            {
                "name": "amount",
                "description": "Requested amount of carbon removal units. Either this or `metric_tons` must be specified."
            },
            {
                "name": "beneficiary",
                "description": "Publicly sharable reference for the end beneficiary of carbon removal. Assumed to be the Stripe account if not set."
            },
            {
                "name": "currency",
                "description": "Request currency for the order as a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a supported [settlement currency for your account](https://stripe.com/docs/currencies). If omitted, the account's default currency will be used."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "metric_tons",
                "description": "Requested number of tons for the order. Either this or `amount` must be specified."
            },
            {
                "name": "product",
                "description": "Unique identifier of the Climate product."
            }
        ]
    },
    {
        "path": "/v1/climate/orders/{order}",
        "verb": "get",
        "op_id": "GetClimateOrdersOrder",
        "summary": "Retrieve an order",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/climate/orders/{order}",
        "verb": "post",
        "op_id": "PostClimateOrdersOrder",
        "summary": "Update an order",
        "params": [
            {
                "name": "beneficiary",
                "description": "Publicly sharable reference for the end beneficiary of carbon removal. Assumed to be the Stripe account if not set."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            }
        ]
    },
    {
        "path": "/v1/climate/orders/{order}/cancel",
        "verb": "post",
        "op_id": "PostClimateOrdersOrderCancel",
        "summary": "Cancel an order",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/climate/products",
        "verb": "get",
        "op_id": "GetClimateProducts",
        "summary": "List products",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/climate/products/{product}",
        "verb": "get",
        "op_id": "GetClimateProductsProduct",
        "summary": "Retrieve a product",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/climate/suppliers",
        "verb": "get",
        "op_id": "GetClimateSuppliers",
        "summary": "List suppliers",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/climate/suppliers/{supplier}",
        "verb": "get",
        "op_id": "GetClimateSuppliersSupplier",
        "summary": "Retrieve a supplier",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/confirmation_tokens/{confirmation_token}",
        "verb": "get",
        "op_id": "GetConfirmationTokensConfirmationToken",
        "summary": "Retrieve a ConfirmationToken",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/country_specs",
        "verb": "get",
        "op_id": "GetCountrySpecs",
        "summary": "List Country Specs",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/country_specs/{country}",
        "verb": "get",
        "op_id": "GetCountrySpecsCountry",
        "summary": "Retrieve a Country Spec",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/coupons",
        "verb": "get",
        "op_id": "GetCoupons",
        "summary": "List all coupons",
        "params": [
            {
                "name": "created",
                "description": "A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/coupons",
        "verb": "post",
        "op_id": "PostCoupons",
        "summary": "Create a coupon",
        "params": [
            {
                "name": "amount_off",
                "description": "A positive integer representing the amount to subtract from an invoice total (required if `percent_off` is not passed)."
            },
            {
                "name": "applies_to",
                "description": "A hash containing directions for what this Coupon will apply discounts to."
            },
            {
                "name": "currency",
                "description": "Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) of the `amount_off` parameter (required if `amount_off` is passed)."
            },
            {
                "name": "currency_options",
                "description": "Coupons defined in each available currency option (only supported if `amount_off` is passed). Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "duration",
                "description": "Specifies how long the discount will be in effect if used on a subscription. Defaults to `once`."
            },
            {
                "name": "duration_in_months",
                "description": "Required only if `duration` is `repeating`, in which case it must be a positive integer that specifies the number of months the discount will be in effect."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "id",
                "description": "Unique string of your choice that will be used to identify this coupon when applying it to a customer. If you don't want to specify a particular code, you can leave the ID blank and we'll generate a random code for you."
            },
            {
                "name": "max_redemptions",
                "description": "A positive integer specifying the number of times the coupon can be redeemed before it's no longer valid. For example, you might have a 50% off coupon that the first 20 readers of your blog can use."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "name",
                "description": "Name of the coupon displayed to customers on, for instance invoices, or receipts. By default the `id` is shown if `name` is not set."
            },
            {
                "name": "percent_off",
                "description": "A positive float larger than 0, and smaller or equal to 100, that represents the discount the coupon will apply (required if `amount_off` is not passed)."
            },
            {
                "name": "redeem_by",
                "description": "Unix timestamp specifying the last time at which the coupon can be redeemed. After the redeem_by date, the coupon can no longer be applied to new customers."
            }
        ]
    },
    {
        "path": "/v1/coupons/{coupon}",
        "verb": "delete",
        "op_id": "DeleteCouponsCoupon",
        "summary": "Delete a coupon",
        "params": []
    },
    {
        "path": "/v1/coupons/{coupon}",
        "verb": "get",
        "op_id": "GetCouponsCoupon",
        "summary": "Retrieve a coupon",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/coupons/{coupon}",
        "verb": "post",
        "op_id": "PostCouponsCoupon",
        "summary": "Update a coupon",
        "params": [
            {
                "name": "currency_options",
                "description": "Coupons defined in each available currency option (only supported if the coupon is amount-based). Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "name",
                "description": "Name of the coupon displayed to customers on, for instance invoices, or receipts. By default the `id` is shown if `name` is not set."
            }
        ]
    },
    {
        "path": "/v1/credit_notes",
        "verb": "get",
        "op_id": "GetCreditNotes",
        "summary": "List all credit notes",
        "params": [
            {
                "name": "created",
                "description": "Only return credit notes that were created during the given date interval."
            },
            {
                "name": "customer",
                "description": "Only return credit notes for the customer specified by this customer ID."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "invoice",
                "description": "Only return credit notes for the invoice specified by this invoice ID."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/credit_notes",
        "verb": "post",
        "op_id": "PostCreditNotes",
        "summary": "Create a credit note",
        "params": [
            {
                "name": "amount",
                "description": "The integer amount in cents (or local equivalent) representing the total amount of the credit note."
            },
            {
                "name": "credit_amount",
                "description": "The integer amount in cents (or local equivalent) representing the amount to credit the customer's balance, which will be automatically applied to their next invoice."
            },
            {
                "name": "effective_at",
                "description": "The date when this credit note is in effect. Same as `created` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the credit note PDF."
            },
            {
                "name": "email_type",
                "description": "Type of email to send to the customer, one of `credit_note` or `none` and the default is `credit_note`."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "invoice",
                "description": "ID of the invoice."
            },
            {
                "name": "lines",
                "description": "Line items that make up the credit note."
            },
            {
                "name": "memo",
                "description": "The credit note's memo appears on the credit note PDF."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "out_of_band_amount",
                "description": "The integer amount in cents (or local equivalent) representing the amount that is credited outside of Stripe."
            },
            {
                "name": "reason",
                "description": "Reason for issuing this credit note, one of `duplicate`, `fraudulent`, `order_change`, or `product_unsatisfactory`"
            },
            {
                "name": "refund_amount",
                "description": "The integer amount in cents (or local equivalent) representing the amount to refund. If set, a refund will be created for the charge associated with the invoice."
            },
            {
                "name": "refunds",
                "description": "Refunds to link to this credit note."
            },
            {
                "name": "shipping_cost",
                "description": "When shipping_cost contains the shipping_rate from the invoice, the shipping_cost is included in the credit note."
            }
        ]
    },
    {
        "path": "/v1/credit_notes/preview",
        "verb": "get",
        "op_id": "GetCreditNotesPreview",
        "summary": "Preview a credit note",
        "params": [
            {
                "name": "amount",
                "description": "The integer amount in cents (or local equivalent) representing the total amount of the credit note."
            },
            {
                "name": "credit_amount",
                "description": "The integer amount in cents (or local equivalent) representing the amount to credit the customer's balance, which will be automatically applied to their next invoice."
            },
            {
                "name": "effective_at",
                "description": "The date when this credit note is in effect. Same as `created` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the credit note PDF."
            },
            {
                "name": "email_type",
                "description": "Type of email to send to the customer, one of `credit_note` or `none` and the default is `credit_note`."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "invoice",
                "description": "ID of the invoice."
            },
            {
                "name": "lines",
                "description": "Line items that make up the credit note."
            },
            {
                "name": "memo",
                "description": "The credit note's memo appears on the credit note PDF."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "out_of_band_amount",
                "description": "The integer amount in cents (or local equivalent) representing the amount that is credited outside of Stripe."
            },
            {
                "name": "reason",
                "description": "Reason for issuing this credit note, one of `duplicate`, `fraudulent`, `order_change`, or `product_unsatisfactory`"
            },
            {
                "name": "refund_amount",
                "description": "The integer amount in cents (or local equivalent) representing the amount to refund. If set, a refund will be created for the charge associated with the invoice."
            },
            {
                "name": "refunds",
                "description": "Refunds to link to this credit note."
            },
            {
                "name": "shipping_cost",
                "description": "When shipping_cost contains the shipping_rate from the invoice, the shipping_cost is included in the credit note."
            }
        ]
    },
    {
        "path": "/v1/credit_notes/preview/lines",
        "verb": "get",
        "op_id": "GetCreditNotesPreviewLines",
        "summary": "Retrieve a credit note preview's line items",
        "params": [
            {
                "name": "amount",
                "description": "The integer amount in cents (or local equivalent) representing the total amount of the credit note."
            },
            {
                "name": "credit_amount",
                "description": "The integer amount in cents (or local equivalent) representing the amount to credit the customer's balance, which will be automatically applied to their next invoice."
            },
            {
                "name": "effective_at",
                "description": "The date when this credit note is in effect. Same as `created` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the credit note PDF."
            },
            {
                "name": "email_type",
                "description": "Type of email to send to the customer, one of `credit_note` or `none` and the default is `credit_note`."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "invoice",
                "description": "ID of the invoice."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "lines",
                "description": "Line items that make up the credit note."
            },
            {
                "name": "memo",
                "description": "The credit note's memo appears on the credit note PDF."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "out_of_band_amount",
                "description": "The integer amount in cents (or local equivalent) representing the amount that is credited outside of Stripe."
            },
            {
                "name": "reason",
                "description": "Reason for issuing this credit note, one of `duplicate`, `fraudulent`, `order_change`, or `product_unsatisfactory`"
            },
            {
                "name": "refund_amount",
                "description": "The integer amount in cents (or local equivalent) representing the amount to refund. If set, a refund will be created for the charge associated with the invoice."
            },
            {
                "name": "refunds",
                "description": "Refunds to link to this credit note."
            },
            {
                "name": "shipping_cost",
                "description": "When shipping_cost contains the shipping_rate from the invoice, the shipping_cost is included in the credit note."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/credit_notes/{credit_note}/lines",
        "verb": "get",
        "op_id": "GetCreditNotesCreditNoteLines",
        "summary": "Retrieve a credit note's line items",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/credit_notes/{id}",
        "verb": "get",
        "op_id": "GetCreditNotesId",
        "summary": "Retrieve a credit note",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/credit_notes/{id}",
        "verb": "post",
        "op_id": "PostCreditNotesId",
        "summary": "Update a credit note",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "memo",
                "description": "Credit note memo."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            }
        ]
    },
    {
        "path": "/v1/credit_notes/{id}/void",
        "verb": "post",
        "op_id": "PostCreditNotesIdVoid",
        "summary": "Void a credit note",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/customer_sessions",
        "verb": "post",
        "op_id": "PostCustomerSessions",
        "summary": "Create a Customer Session",
        "params": [
            {
                "name": "components",
                "description": "Configuration for each component. Exactly 1 component must be enabled."
            },
            {
                "name": "customer",
                "description": "The ID of an existing customer for which to create the Customer Session."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/customers",
        "verb": "get",
        "op_id": "GetCustomers",
        "summary": "List all customers",
        "params": [
            {
                "name": "created",
                "description": "Only return customers that were created during the given date interval."
            },
            {
                "name": "email",
                "description": "A case-sensitive filter on the list based on the customer's `email` field. The value must be a string."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "test_clock",
                "description": "Provides a list of customers that are associated with the specified test clock. The response will not include customers with test clocks if this parameter is not set."
            }
        ]
    },
    {
        "path": "/v1/customers",
        "verb": "post",
        "op_id": "PostCustomers",
        "summary": "Create a customer",
        "params": [
            {
                "name": "address",
                "description": "The customer's address."
            },
            {
                "name": "balance",
                "description": "An integer amount in cents (or local equivalent) that represents the customer's current balance, which affect the customer's future invoices. A negative amount represents a credit that decreases the amount due on an invoice; a positive amount increases the amount due on an invoice."
            },
            {
                "name": "cash_balance",
                "description": "Balance information and default balance settings for this customer."
            },
            {
                "name": "description",
                "description": "An arbitrary string that you can attach to a customer object. It is displayed alongside the customer in the dashboard."
            },
            {
                "name": "email",
                "description": "Customer's email address. It's displayed alongside the customer in your dashboard and can be useful for searching and tracking. This may be up to *512 characters*."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "invoice_prefix",
                "description": "The prefix for the customer used to generate unique invoice numbers. Must be 3\u201312 uppercase letters or numbers."
            },
            {
                "name": "invoice_settings",
                "description": "Default invoice settings for this customer."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "name",
                "description": "The customer's full name or business name."
            },
            {
                "name": "next_invoice_sequence",
                "description": "The sequence to be used on the customer's next invoice. Defaults to 1."
            },
            {
                "name": "payment_method",
                "description": ""
            },
            {
                "name": "phone",
                "description": "The customer's phone number."
            },
            {
                "name": "preferred_locales",
                "description": "Customer's preferred languages, ordered by preference."
            },
            {
                "name": "shipping",
                "description": "The customer's shipping information. Appears on invoices emailed to this customer."
            },
            {
                "name": "source",
                "description": ""
            },
            {
                "name": "tax",
                "description": "Tax details about the customer."
            },
            {
                "name": "tax_exempt",
                "description": "The customer's tax exemption. One of `none`, `exempt`, or `reverse`."
            },
            {
                "name": "tax_id_data",
                "description": "The customer's tax IDs."
            },
            {
                "name": "test_clock",
                "description": "ID of the test clock to attach to the customer."
            }
        ]
    },
    {
        "path": "/v1/customers/search",
        "verb": "get",
        "op_id": "GetCustomersSearch",
        "summary": "Search customers",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "page",
                "description": "A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results."
            },
            {
                "name": "query",
                "description": "The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for customers](https://stripe.com/docs/search#query-fields-for-customers)."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}",
        "verb": "delete",
        "op_id": "DeleteCustomersCustomer",
        "summary": "Delete a customer",
        "params": []
    },
    {
        "path": "/v1/customers/{customer}",
        "verb": "get",
        "op_id": "GetCustomersCustomer",
        "summary": "Retrieve a customer",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}",
        "verb": "post",
        "op_id": "PostCustomersCustomer",
        "summary": "Update a customer",
        "params": [
            {
                "name": "address",
                "description": "The customer's address."
            },
            {
                "name": "balance",
                "description": "An integer amount in cents (or local equivalent) that represents the customer's current balance, which affect the customer's future invoices. A negative amount represents a credit that decreases the amount due on an invoice; a positive amount increases the amount due on an invoice."
            },
            {
                "name": "bank_account",
                "description": "Either a token, like the ones returned by [Stripe.js](https://stripe.com/docs/js), or a dictionary containing a user's bank account details."
            },
            {
                "name": "card",
                "description": "A token, like the ones returned by [Stripe.js](https://stripe.com/docs/js)."
            },
            {
                "name": "cash_balance",
                "description": "Balance information and default balance settings for this customer."
            },
            {
                "name": "default_alipay_account",
                "description": "ID of Alipay account to make the customer's new default for invoice payments."
            },
            {
                "name": "default_bank_account",
                "description": "ID of bank account to make the customer's new default for invoice payments."
            },
            {
                "name": "default_card",
                "description": "ID of card to make the customer's new default for invoice payments."
            },
            {
                "name": "default_source",
                "description": "If you are using payment methods created via the PaymentMethods API, see the [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/update#update_customer-invoice_settings-default_payment_method) parameter.\n\nProvide the ID of a payment source already attached to this customer to make it this customer's default payment source.\n\nIf you want to add a new payment source and make it the default, see the [source](https://stripe.com/docs/api/customers/update#update_customer-source) property."
            },
            {
                "name": "description",
                "description": "An arbitrary string that you can attach to a customer object. It is displayed alongside the customer in the dashboard."
            },
            {
                "name": "email",
                "description": "Customer's email address. It's displayed alongside the customer in your dashboard and can be useful for searching and tracking. This may be up to *512 characters*."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "invoice_prefix",
                "description": "The prefix for the customer used to generate unique invoice numbers. Must be 3\u201312 uppercase letters or numbers."
            },
            {
                "name": "invoice_settings",
                "description": "Default invoice settings for this customer."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "name",
                "description": "The customer's full name or business name."
            },
            {
                "name": "next_invoice_sequence",
                "description": "The sequence to be used on the customer's next invoice. Defaults to 1."
            },
            {
                "name": "phone",
                "description": "The customer's phone number."
            },
            {
                "name": "preferred_locales",
                "description": "Customer's preferred languages, ordered by preference."
            },
            {
                "name": "shipping",
                "description": "The customer's shipping information. Appears on invoices emailed to this customer."
            },
            {
                "name": "source",
                "description": ""
            },
            {
                "name": "tax",
                "description": "Tax details about the customer."
            },
            {
                "name": "tax_exempt",
                "description": "The customer's tax exemption. One of `none`, `exempt`, or `reverse`."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/balance_transactions",
        "verb": "get",
        "op_id": "GetCustomersCustomerBalanceTransactions",
        "summary": "List customer balance transactions",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/balance_transactions",
        "verb": "post",
        "op_id": "PostCustomersCustomerBalanceTransactions",
        "summary": "Create a customer balance transaction",
        "params": [
            {
                "name": "amount",
                "description": "The integer amount in **cents (or local equivalent)** to apply to the customer's credit balance."
            },
            {
                "name": "currency",
                "description": "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). Specifies the [`invoice_credit_balance`](https://stripe.com/docs/api/customers/object#customer_object-invoice_credit_balance) that this transaction will apply to. If the customer's `currency` is not set, it will be updated to this value."
            },
            {
                "name": "description",
                "description": "An arbitrary string attached to the object. Often useful for displaying to users."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/balance_transactions/{transaction}",
        "verb": "get",
        "op_id": "GetCustomersCustomerBalanceTransactionsTransaction",
        "summary": "Retrieve a customer balance transaction",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/balance_transactions/{transaction}",
        "verb": "post",
        "op_id": "PostCustomersCustomerBalanceTransactionsTransaction",
        "summary": "Update a customer credit balance transaction",
        "params": [
            {
                "name": "description",
                "description": "An arbitrary string attached to the object. Often useful for displaying to users."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/bank_accounts",
        "verb": "get",
        "op_id": "GetCustomersCustomerBankAccounts",
        "summary": "List all bank accounts",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/bank_accounts",
        "verb": "post",
        "op_id": "PostCustomersCustomerBankAccounts",
        "summary": "Create a card",
        "params": [
            {
                "name": "alipay_account",
                "description": "A token returned by [Stripe.js](https://stripe.com/docs/js) representing the user\u2019s Alipay account details."
            },
            {
                "name": "bank_account",
                "description": "Either a token, like the ones returned by [Stripe.js](https://stripe.com/docs/js), or a dictionary containing a user's bank account details."
            },
            {
                "name": "card",
                "description": "A token, like the ones returned by [Stripe.js](https://stripe.com/docs/js)."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "source",
                "description": "Please refer to full [documentation](https://stripe.com/docs/api) instead."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/bank_accounts/{id}",
        "verb": "delete",
        "op_id": "DeleteCustomersCustomerBankAccountsId",
        "summary": "Delete a customer source",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/bank_accounts/{id}",
        "verb": "get",
        "op_id": "GetCustomersCustomerBankAccountsId",
        "summary": "Retrieve a bank account",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/bank_accounts/{id}",
        "verb": "post",
        "op_id": "PostCustomersCustomerBankAccountsId",
        "summary": "",
        "params": [
            {
                "name": "account_holder_name",
                "description": "The name of the person or business that owns the bank account."
            },
            {
                "name": "account_holder_type",
                "description": "The type of entity that holds the account. This can be either `individual` or `company`."
            },
            {
                "name": "address_city",
                "description": "City/District/Suburb/Town/Village."
            },
            {
                "name": "address_country",
                "description": "Billing address country, if provided when creating card."
            },
            {
                "name": "address_line1",
                "description": "Address line 1 (Street address/PO Box/Company name)."
            },
            {
                "name": "address_line2",
                "description": "Address line 2 (Apartment/Suite/Unit/Building)."
            },
            {
                "name": "address_state",
                "description": "State/County/Province/Region."
            },
            {
                "name": "address_zip",
                "description": "ZIP or postal code."
            },
            {
                "name": "exp_month",
                "description": "Two digit number representing the card\u2019s expiration month."
            },
            {
                "name": "exp_year",
                "description": "Four digit number representing the card\u2019s expiration year."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "name",
                "description": "Cardholder name."
            },
            {
                "name": "owner",
                "description": ""
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/bank_accounts/{id}/verify",
        "verb": "post",
        "op_id": "PostCustomersCustomerBankAccountsIdVerify",
        "summary": "Verify a bank account",
        "params": [
            {
                "name": "amounts",
                "description": "Two positive integers, in *cents*, equal to the values of the microdeposits sent to the bank account."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/cards",
        "verb": "get",
        "op_id": "GetCustomersCustomerCards",
        "summary": "List all cards",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/cards",
        "verb": "post",
        "op_id": "PostCustomersCustomerCards",
        "summary": "Create a card",
        "params": [
            {
                "name": "alipay_account",
                "description": "A token returned by [Stripe.js](https://stripe.com/docs/js) representing the user\u2019s Alipay account details."
            },
            {
                "name": "bank_account",
                "description": "Either a token, like the ones returned by [Stripe.js](https://stripe.com/docs/js), or a dictionary containing a user's bank account details."
            },
            {
                "name": "card",
                "description": "A token, like the ones returned by [Stripe.js](https://stripe.com/docs/js)."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "source",
                "description": "Please refer to full [documentation](https://stripe.com/docs/api) instead."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/cards/{id}",
        "verb": "delete",
        "op_id": "DeleteCustomersCustomerCardsId",
        "summary": "Delete a customer source",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/cards/{id}",
        "verb": "get",
        "op_id": "GetCustomersCustomerCardsId",
        "summary": "Retrieve a card",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/cards/{id}",
        "verb": "post",
        "op_id": "PostCustomersCustomerCardsId",
        "summary": "",
        "params": [
            {
                "name": "account_holder_name",
                "description": "The name of the person or business that owns the bank account."
            },
            {
                "name": "account_holder_type",
                "description": "The type of entity that holds the account. This can be either `individual` or `company`."
            },
            {
                "name": "address_city",
                "description": "City/District/Suburb/Town/Village."
            },
            {
                "name": "address_country",
                "description": "Billing address country, if provided when creating card."
            },
            {
                "name": "address_line1",
                "description": "Address line 1 (Street address/PO Box/Company name)."
            },
            {
                "name": "address_line2",
                "description": "Address line 2 (Apartment/Suite/Unit/Building)."
            },
            {
                "name": "address_state",
                "description": "State/County/Province/Region."
            },
            {
                "name": "address_zip",
                "description": "ZIP or postal code."
            },
            {
                "name": "exp_month",
                "description": "Two digit number representing the card\u2019s expiration month."
            },
            {
                "name": "exp_year",
                "description": "Four digit number representing the card\u2019s expiration year."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "name",
                "description": "Cardholder name."
            },
            {
                "name": "owner",
                "description": ""
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/cash_balance",
        "verb": "get",
        "op_id": "GetCustomersCustomerCashBalance",
        "summary": "Retrieve a cash balance",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/cash_balance",
        "verb": "post",
        "op_id": "PostCustomersCustomerCashBalance",
        "summary": "Update a cash balance's settings",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "settings",
                "description": "A hash of settings for this cash balance."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/cash_balance_transactions",
        "verb": "get",
        "op_id": "GetCustomersCustomerCashBalanceTransactions",
        "summary": "List cash balance transactions",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/cash_balance_transactions/{transaction}",
        "verb": "get",
        "op_id": "GetCustomersCustomerCashBalanceTransactionsTransaction",
        "summary": "Retrieve a cash balance transaction",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/discount",
        "verb": "delete",
        "op_id": "DeleteCustomersCustomerDiscount",
        "summary": "Delete a customer discount",
        "params": []
    },
    {
        "path": "/v1/customers/{customer}/discount",
        "verb": "get",
        "op_id": "GetCustomersCustomerDiscount",
        "summary": "",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/funding_instructions",
        "verb": "post",
        "op_id": "PostCustomersCustomerFundingInstructions",
        "summary": "Create or retrieve funding instructions for a customer cash balance",
        "params": [
            {
                "name": "bank_transfer",
                "description": "Additional parameters for `bank_transfer` funding types"
            },
            {
                "name": "currency",
                "description": "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "funding_type",
                "description": "The `funding_type` to get the instructions for."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/payment_methods",
        "verb": "get",
        "op_id": "GetCustomersCustomerPaymentMethods",
        "summary": "List a Customer's PaymentMethods",
        "params": [
            {
                "name": "allow_redisplay",
                "description": "This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "type",
                "description": "An optional filter on the list, based on the object `type` field. Without the filter, the list includes all current and future payment method types. If your integration expects only one type of payment method in the response, make sure to provide a type value in the request."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/payment_methods/{payment_method}",
        "verb": "get",
        "op_id": "GetCustomersCustomerPaymentMethodsPaymentMethod",
        "summary": "Retrieve a Customer's PaymentMethod",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/sources",
        "verb": "get",
        "op_id": "GetCustomersCustomerSources",
        "summary": "",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "object",
                "description": "Filter sources according to a particular object type."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/sources",
        "verb": "post",
        "op_id": "PostCustomersCustomerSources",
        "summary": "Create a card",
        "params": [
            {
                "name": "alipay_account",
                "description": "A token returned by [Stripe.js](https://stripe.com/docs/js) representing the user\u2019s Alipay account details."
            },
            {
                "name": "bank_account",
                "description": "Either a token, like the ones returned by [Stripe.js](https://stripe.com/docs/js), or a dictionary containing a user's bank account details."
            },
            {
                "name": "card",
                "description": "A token, like the ones returned by [Stripe.js](https://stripe.com/docs/js)."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "source",
                "description": "Please refer to full [documentation](https://stripe.com/docs/api) instead."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/sources/{id}",
        "verb": "delete",
        "op_id": "DeleteCustomersCustomerSourcesId",
        "summary": "Delete a customer source",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/sources/{id}",
        "verb": "get",
        "op_id": "GetCustomersCustomerSourcesId",
        "summary": "",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/sources/{id}",
        "verb": "post",
        "op_id": "PostCustomersCustomerSourcesId",
        "summary": "",
        "params": [
            {
                "name": "account_holder_name",
                "description": "The name of the person or business that owns the bank account."
            },
            {
                "name": "account_holder_type",
                "description": "The type of entity that holds the account. This can be either `individual` or `company`."
            },
            {
                "name": "address_city",
                "description": "City/District/Suburb/Town/Village."
            },
            {
                "name": "address_country",
                "description": "Billing address country, if provided when creating card."
            },
            {
                "name": "address_line1",
                "description": "Address line 1 (Street address/PO Box/Company name)."
            },
            {
                "name": "address_line2",
                "description": "Address line 2 (Apartment/Suite/Unit/Building)."
            },
            {
                "name": "address_state",
                "description": "State/County/Province/Region."
            },
            {
                "name": "address_zip",
                "description": "ZIP or postal code."
            },
            {
                "name": "exp_month",
                "description": "Two digit number representing the card\u2019s expiration month."
            },
            {
                "name": "exp_year",
                "description": "Four digit number representing the card\u2019s expiration year."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "name",
                "description": "Cardholder name."
            },
            {
                "name": "owner",
                "description": ""
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/sources/{id}/verify",
        "verb": "post",
        "op_id": "PostCustomersCustomerSourcesIdVerify",
        "summary": "Verify a bank account",
        "params": [
            {
                "name": "amounts",
                "description": "Two positive integers, in *cents*, equal to the values of the microdeposits sent to the bank account."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/subscriptions",
        "verb": "get",
        "op_id": "GetCustomersCustomerSubscriptions",
        "summary": "List active subscriptions",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/subscriptions",
        "verb": "post",
        "op_id": "PostCustomersCustomerSubscriptions",
        "summary": "Create a subscription",
        "params": [
            {
                "name": "add_invoice_items",
                "description": "A list of prices and quantities that will generate invoice items appended to the next invoice for this subscription. You may pass up to 20 items."
            },
            {
                "name": "application_fee_percent",
                "description": "A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions)."
            },
            {
                "name": "automatic_tax",
                "description": "Automatic tax settings for this subscription. We recommend you only include this parameter when the existing value is being changed."
            },
            {
                "name": "backdate_start_date",
                "description": "For new subscriptions, a past timestamp to backdate the subscription's start date to. If set, the first invoice will contain a proration for the timespan between the start date and the current time. Can be combined with trials and the billing cycle anchor."
            },
            {
                "name": "billing_cycle_anchor",
                "description": "A future timestamp in UTC format to anchor the subscription's [billing cycle](https://stripe.com/docs/subscriptions/billing-cycle). The anchor is the reference point that aligns future billing cycle dates. It sets the day of week for `week` intervals, the day of month for `month` and `year` intervals, and the month of year for `year` intervals."
            },
            {
                "name": "billing_thresholds",
                "description": "Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. When updating, pass an empty string to remove previously-defined thresholds."
            },
            {
                "name": "cancel_at",
                "description": "A timestamp at which the subscription should cancel. If set to a date before the current period ends, this will cause a proration if prorations have been enabled using `proration_behavior`. If set during a future period, this will always cause a proration for that period."
            },
            {
                "name": "cancel_at_period_end",
                "description": "Indicate whether this subscription should cancel at the end of the current period (`current_period_end`). Defaults to `false`. This param will be removed in a future API version. Please use `cancel_at` instead."
            },
            {
                "name": "collection_method",
                "description": "Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`."
            },
            {
                "name": "currency",
                "description": "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "days_until_due",
                "description": "Number of days a customer has to pay invoices generated by this subscription. Valid only for subscriptions where `collection_method` is set to `send_invoice`."
            },
            {
                "name": "default_payment_method",
                "description": "ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over `default_source`. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source)."
            },
            {
                "name": "default_source",
                "description": "ID of the default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If `default_payment_method` is also set, `default_payment_method` will take precedence. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source)."
            },
            {
                "name": "default_tax_rates",
                "description": "The tax rates that will apply to any subscription item that does not have `tax_rates` set. Invoices created will have their `default_tax_rates` populated from the subscription."
            },
            {
                "name": "discounts",
                "description": "The coupons to redeem into discounts for the subscription. If not specified or empty, inherits the discount from the subscription's customer."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "invoice_settings",
                "description": "All invoices will be billed using the specified settings."
            },
            {
                "name": "items",
                "description": "A list of up to 20 subscription items, each with an attached price."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "off_session",
                "description": "Indicates if a customer is on or off-session while an invoice payment is attempted. Defaults to `false` (on-session)."
            },
            {
                "name": "payment_behavior",
                "description": "Only applies to subscriptions with `collection_method=charge_automatically`.\n\nUse `allow_incomplete` to create Subscriptions with `status=incomplete` if the first invoice can't be paid. Creating Subscriptions with this status allows you to manage scenarios where additional customer actions are needed to pay a subscription's invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication) for Billing to learn more. This is the default behavior.\n\nUse `default_incomplete` to create Subscriptions with `status=incomplete` when the first invoice requires payment, otherwise start as active. Subscriptions transition to `status=active` when successfully confirming the PaymentIntent on the first invoice. This allows simpler management of scenarios where additional customer actions are needed to pay a subscription\u2019s invoice, such as failed payments, [SCA regulation](https://stripe.com/docs/billing/migration/strong-customer-authentication), or collecting a mandate for a bank debit payment method. If the PaymentIntent is not confirmed within 23 hours Subscriptions transition to `status=incomplete_expired`, which is a terminal state.\n\nUse `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription's first invoice can't be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further customer action is needed, this parameter doesn't create a Subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://stripe.com/docs/upgrades#2019-03-14) to learn more.\n\n`pending_if_incomplete` is only used with updates and cannot be passed when creating a Subscription.\n\nSubscriptions with `collection_method=send_invoice` are automatically activated regardless of the first Invoice status."
            },
            {
                "name": "payment_settings",
                "description": "Payment settings to pass to invoices created by the subscription."
            },
            {
                "name": "pending_invoice_item_interval",
                "description": "Specifies an interval for how often to bill for any pending invoice items. It is analogous to calling [Create an invoice](https://stripe.com/docs/api#create_invoice) for the given subscription at the specified interval."
            },
            {
                "name": "proration_behavior",
                "description": "Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) resulting from the `billing_cycle_anchor`. If no value is passed, the default is `create_prorations`."
            },
            {
                "name": "transfer_data",
                "description": "If specified, the funds from the subscription's invoices will be transferred to the destination and the ID of the resulting transfers will be found on the resulting charges."
            },
            {
                "name": "trial_end",
                "description": "Unix timestamp representing the end of the trial period the customer will get before being charged for the first time. If set, trial_end will override the default trial period of the plan the customer is being subscribed to. The special value `now` can be provided to end the customer's trial immediately. Can be at most two years from `billing_cycle_anchor`. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more."
            },
            {
                "name": "trial_from_plan",
                "description": "Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more."
            },
            {
                "name": "trial_period_days",
                "description": "Integer representing the number of trial period days before the customer is charged for the first time. This will always overwrite any trials that might apply via a subscribed plan. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more."
            },
            {
                "name": "trial_settings",
                "description": "Settings related to subscription trials."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/subscriptions/{subscription_exposed_id}",
        "verb": "delete",
        "op_id": "DeleteCustomersCustomerSubscriptionsSubscriptionExposedId",
        "summary": "Cancel a subscription",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "invoice_now",
                "description": "Can be set to `true` if `at_period_end` is not set to `true`. Will generate a final invoice that invoices for any un-invoiced metered usage and new/pending proration invoice items."
            },
            {
                "name": "prorate",
                "description": "Can be set to `true` if `at_period_end` is not set to `true`. Will generate a proration invoice item that credits remaining unused time until the subscription period end."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/subscriptions/{subscription_exposed_id}",
        "verb": "get",
        "op_id": "GetCustomersCustomerSubscriptionsSubscriptionExposedId",
        "summary": "Retrieve a subscription",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/subscriptions/{subscription_exposed_id}",
        "verb": "post",
        "op_id": "PostCustomersCustomerSubscriptionsSubscriptionExposedId",
        "summary": "Update a subscription on a customer",
        "params": [
            {
                "name": "add_invoice_items",
                "description": "A list of prices and quantities that will generate invoice items appended to the next invoice for this subscription. You may pass up to 20 items."
            },
            {
                "name": "application_fee_percent",
                "description": "A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions)."
            },
            {
                "name": "automatic_tax",
                "description": "Automatic tax settings for this subscription. We recommend you only include this parameter when the existing value is being changed."
            },
            {
                "name": "billing_cycle_anchor",
                "description": "Either `now` or `unchanged`. Setting the value to `now` resets the subscription's billing cycle anchor to the current time. For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle)."
            },
            {
                "name": "billing_thresholds",
                "description": "Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. When updating, pass an empty string to remove previously-defined thresholds."
            },
            {
                "name": "cancel_at",
                "description": "A timestamp at which the subscription should cancel. If set to a date before the current period ends, this will cause a proration if prorations have been enabled using `proration_behavior`. If set during a future period, this will always cause a proration for that period."
            },
            {
                "name": "cancel_at_period_end",
                "description": "Indicate whether this subscription should cancel at the end of the current period (`current_period_end`). Defaults to `false`. This param will be removed in a future API version. Please use `cancel_at` instead."
            },
            {
                "name": "cancellation_details",
                "description": "Details about why this subscription was cancelled"
            },
            {
                "name": "collection_method",
                "description": "Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`."
            },
            {
                "name": "days_until_due",
                "description": "Number of days a customer has to pay invoices generated by this subscription. Valid only for subscriptions where `collection_method` is set to `send_invoice`."
            },
            {
                "name": "default_payment_method",
                "description": "ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over `default_source`. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source)."
            },
            {
                "name": "default_source",
                "description": "ID of the default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If `default_payment_method` is also set, `default_payment_method` will take precedence. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source)."
            },
            {
                "name": "default_tax_rates",
                "description": "The tax rates that will apply to any subscription item that does not have `tax_rates` set. Invoices created will have their `default_tax_rates` populated from the subscription. Pass an empty string to remove previously-defined tax rates."
            },
            {
                "name": "discounts",
                "description": "The coupons to redeem into discounts for the subscription. If not specified or empty, inherits the discount from the subscription's customer."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "invoice_settings",
                "description": "All invoices will be billed using the specified settings."
            },
            {
                "name": "items",
                "description": "A list of up to 20 subscription items, each with an attached price."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "off_session",
                "description": "Indicates if a customer is on or off-session while an invoice payment is attempted. Defaults to `false` (on-session)."
            },
            {
                "name": "pause_collection",
                "description": "If specified, payment collection for this subscription will be paused. Note that the subscription status will be unchanged and will not be updated to `paused`. Learn more about [pausing collection](https://stripe.com/docs/billing/subscriptions/pause-payment)."
            },
            {
                "name": "payment_behavior",
                "description": "Use `allow_incomplete` to transition the subscription to `status=past_due` if a payment is required but cannot be paid. This allows you to manage scenarios where additional user actions are needed to pay a subscription's invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication) for Billing to learn more. This is the default behavior.\n\nUse `default_incomplete` to transition the subscription to `status=past_due` when payment is required and await explicit confirmation of the invoice's payment intent. This allows simpler management of scenarios where additional user actions are needed to pay a subscription\u2019s invoice. Such as failed payments, [SCA regulation](https://stripe.com/docs/billing/migration/strong-customer-authentication), or collecting a mandate for a bank debit payment method.\n\nUse `pending_if_incomplete` to update the subscription using [pending updates](https://stripe.com/docs/billing/subscriptions/pending-updates). When you use `pending_if_incomplete` you can only pass the parameters [supported by pending updates](https://stripe.com/docs/billing/pending-updates-reference#supported-attributes).\n\nUse `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription's invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not update the subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://stripe.com/docs/upgrades#2019-03-14) to learn more."
            },
            {
                "name": "payment_settings",
                "description": "Payment settings to pass to invoices created by the subscription."
            },
            {
                "name": "pending_invoice_item_interval",
                "description": "Specifies an interval for how often to bill for any pending invoice items. It is analogous to calling [Create an invoice](https://stripe.com/docs/api#create_invoice) for the given subscription at the specified interval."
            },
            {
                "name": "proration_behavior",
                "description": "Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`."
            },
            {
                "name": "proration_date",
                "description": "If set, prorations will be calculated as though the subscription was updated at the given time. This can be used to apply exactly the same prorations that were previewed with the [create preview](https://stripe.com/docs/api/invoices/create_preview) endpoint. `proration_date` can also be used to implement custom proration logic, such as prorating by day instead of by second, by providing the time that you wish to use for proration calculations."
            },
            {
                "name": "transfer_data",
                "description": "If specified, the funds from the subscription's invoices will be transferred to the destination and the ID of the resulting transfers will be found on the resulting charges. This will be unset if you POST an empty value."
            },
            {
                "name": "trial_end",
                "description": "Unix timestamp representing the end of the trial period the customer will get before being charged for the first time. This will always overwrite any trials that might apply via a subscribed plan. If set, trial_end will override the default trial period of the plan the customer is being subscribed to. The special value `now` can be provided to end the customer's trial immediately. Can be at most two years from `billing_cycle_anchor`."
            },
            {
                "name": "trial_from_plan",
                "description": "Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more."
            },
            {
                "name": "trial_settings",
                "description": "Settings related to subscription trials."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/subscriptions/{subscription_exposed_id}/discount",
        "verb": "delete",
        "op_id": "DeleteCustomersCustomerSubscriptionsSubscriptionExposedIdDiscount",
        "summary": "Delete a customer discount",
        "params": []
    },
    {
        "path": "/v1/customers/{customer}/subscriptions/{subscription_exposed_id}/discount",
        "verb": "get",
        "op_id": "GetCustomersCustomerSubscriptionsSubscriptionExposedIdDiscount",
        "summary": "",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/tax_ids",
        "verb": "get",
        "op_id": "GetCustomersCustomerTaxIds",
        "summary": "List all Customer tax IDs",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/tax_ids",
        "verb": "post",
        "op_id": "PostCustomersCustomerTaxIds",
        "summary": "Create a Customer tax ID",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "type",
                "description": "Type of the tax ID, one of `ad_nrt`, `ae_trn`, `al_tin`, `am_tin`, `ao_tin`, `ar_cuit`, `au_abn`, `au_arn`, `aw_tin`, `az_tin`, `ba_tin`, `bb_tin`, `bd_bin`, `bf_ifu`, `bg_uic`, `bh_vat`, `bj_ifu`, `bo_tin`, `br_cnpj`, `br_cpf`, `bs_tin`, `by_tin`, `ca_bn`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `ca_qst`, `cd_nif`, `ch_uid`, `ch_vat`, `cl_tin`, `cm_niu`, `cn_tin`, `co_nit`, `cr_tin`, `cv_nif`, `de_stn`, `do_rcn`, `ec_ruc`, `eg_tin`, `es_cif`, `et_tin`, `eu_oss_vat`, `eu_vat`, `gb_vat`, `ge_vat`, `gn_nif`, `hk_br`, `hr_oib`, `hu_tin`, `id_npwp`, `il_vat`, `in_gst`, `is_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `ke_pin`, `kg_tin`, `kh_tin`, `kr_brn`, `kz_bin`, `la_tin`, `li_uid`, `li_vat`, `ma_vat`, `md_vat`, `me_pib`, `mk_vat`, `mr_nif`, `mx_rfc`, `my_frp`, `my_itn`, `my_sst`, `ng_tin`, `no_vat`, `no_voec`, `np_pan`, `nz_gst`, `om_vat`, `pe_ruc`, `ph_tin`, `ro_tin`, `rs_pib`, `ru_inn`, `ru_kpp`, `sa_vat`, `sg_gst`, `sg_uen`, `si_tin`, `sn_ninea`, `sr_fin`, `sv_nit`, `th_vat`, `tj_tin`, `tr_tin`, `tw_vat`, `tz_vat`, `ua_vat`, `ug_tin`, `us_ein`, `uy_ruc`, `uz_tin`, `uz_vat`, `ve_rif`, `vn_tin`, `za_vat`, `zm_tin`, or `zw_tin`"
            },
            {
                "name": "value",
                "description": "Value of the tax ID."
            }
        ]
    },
    {
        "path": "/v1/customers/{customer}/tax_ids/{id}",
        "verb": "delete",
        "op_id": "DeleteCustomersCustomerTaxIdsId",
        "summary": "Delete a Customer tax ID",
        "params": []
    },
    {
        "path": "/v1/customers/{customer}/tax_ids/{id}",
        "verb": "get",
        "op_id": "GetCustomersCustomerTaxIdsId",
        "summary": "Retrieve a Customer tax ID",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/disputes",
        "verb": "get",
        "op_id": "GetDisputes",
        "summary": "List all disputes",
        "params": [
            {
                "name": "charge",
                "description": "Only return disputes associated to the charge specified by this charge ID."
            },
            {
                "name": "created",
                "description": "Only return disputes that were created during the given date interval."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "payment_intent",
                "description": "Only return disputes associated to the PaymentIntent specified by this PaymentIntent ID."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/disputes/{dispute}",
        "verb": "get",
        "op_id": "GetDisputesDispute",
        "summary": "Retrieve a dispute",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/disputes/{dispute}",
        "verb": "post",
        "op_id": "PostDisputesDispute",
        "summary": "Update a dispute",
        "params": [
            {
                "name": "evidence",
                "description": "Evidence to upload, to respond to a dispute. Updating any field in the hash will submit all fields in the hash for review. The combined character count of all fields is limited to 150,000."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "submit",
                "description": "Whether to immediately submit evidence to the bank. If `false`, evidence is staged on the dispute. Staged evidence is visible in the API and Dashboard, and can be submitted to the bank by making another request with this attribute set to `true` (the default)."
            }
        ]
    },
    {
        "path": "/v1/disputes/{dispute}/close",
        "verb": "post",
        "op_id": "PostDisputesDisputeClose",
        "summary": "Close a dispute",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/entitlements/active_entitlements",
        "verb": "get",
        "op_id": "GetEntitlementsActiveEntitlements",
        "summary": "List all active entitlements",
        "params": [
            {
                "name": "customer",
                "description": "The ID of the customer."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/entitlements/active_entitlements/{id}",
        "verb": "get",
        "op_id": "GetEntitlementsActiveEntitlementsId",
        "summary": "Retrieve an active entitlement",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/entitlements/features",
        "verb": "get",
        "op_id": "GetEntitlementsFeatures",
        "summary": "List all features",
        "params": [
            {
                "name": "archived",
                "description": "If set, filter results to only include features with the given archive status."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "lookup_key",
                "description": "If set, filter results to only include features with the given lookup_key."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/entitlements/features",
        "verb": "post",
        "op_id": "PostEntitlementsFeatures",
        "summary": "Create a feature",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "lookup_key",
                "description": "A unique key you provide as your own system identifier. This may be up to 80 characters."
            },
            {
                "name": "metadata",
                "description": "Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format."
            },
            {
                "name": "name",
                "description": "The feature's name, for your own purpose, not meant to be displayable to the customer."
            }
        ]
    },
    {
        "path": "/v1/entitlements/features/{id}",
        "verb": "get",
        "op_id": "GetEntitlementsFeaturesId",
        "summary": "Retrieve a feature",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/entitlements/features/{id}",
        "verb": "post",
        "op_id": "PostEntitlementsFeaturesId",
        "summary": "Updates a feature",
        "params": [
            {
                "name": "active",
                "description": "Inactive features cannot be attached to new products and will not be returned from the features list endpoint."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format."
            },
            {
                "name": "name",
                "description": "The feature's name, for your own purpose, not meant to be displayable to the customer."
            }
        ]
    },
    {
        "path": "/v1/ephemeral_keys",
        "verb": "post",
        "op_id": "PostEphemeralKeys",
        "summary": "Create an ephemeral key",
        "params": [
            {
                "name": "customer",
                "description": "The ID of the Customer you'd like to modify using the resulting ephemeral key."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "issuing_card",
                "description": "The ID of the Issuing Card you'd like to access using the resulting ephemeral key."
            },
            {
                "name": "nonce",
                "description": "A single-use token, created by Stripe.js, used for creating ephemeral keys for Issuing Cards without exchanging sensitive information."
            },
            {
                "name": "verification_session",
                "description": "The ID of the Identity VerificationSession you'd like to access using the resulting ephemeral key"
            }
        ]
    },
    {
        "path": "/v1/ephemeral_keys/{key}",
        "verb": "delete",
        "op_id": "DeleteEphemeralKeysKey",
        "summary": "Immediately invalidate an ephemeral key",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/events",
        "verb": "get",
        "op_id": "GetEvents",
        "summary": "List all events",
        "params": [
            {
                "name": "created",
                "description": "Only return events that were created during the given date interval."
            },
            {
                "name": "delivery_success",
                "description": "Filter events by whether all webhooks were successfully delivered. If false, events which are still pending or have failed all delivery attempts to a webhook endpoint will be returned."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "type",
                "description": "A string containing a specific event name, or group of events using * as a wildcard. The list will be filtered to include only events with a matching event property."
            },
            {
                "name": "types",
                "description": "An array of up to 20 strings containing specific event names. The list will be filtered to include only events with a matching event property. You may pass either `type` or `types`, but not both."
            }
        ]
    },
    {
        "path": "/v1/events/{id}",
        "verb": "get",
        "op_id": "GetEventsId",
        "summary": "Retrieve an event",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/exchange_rates",
        "verb": "get",
        "op_id": "GetExchangeRates",
        "summary": "List all exchange rates",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is the currency that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with the exchange rate for currency X your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and total number of supported payout currencies, and the default is the max."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is the currency that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with the exchange rate for currency X, your subsequent call can include `starting_after=X` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/exchange_rates/{rate_id}",
        "verb": "get",
        "op_id": "GetExchangeRatesRateId",
        "summary": "Retrieve an exchange rate",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/external_accounts/{id}",
        "verb": "post",
        "op_id": "PostExternalAccountsId",
        "summary": "",
        "params": [
            {
                "name": "account_holder_name",
                "description": "The name of the person or business that owns the bank account."
            },
            {
                "name": "account_holder_type",
                "description": "The type of entity that holds the account. This can be either `individual` or `company`."
            },
            {
                "name": "account_type",
                "description": "The bank account type. This can only be `checking` or `savings` in most countries. In Japan, this can only be `futsu` or `toza`."
            },
            {
                "name": "address_city",
                "description": "City/District/Suburb/Town/Village."
            },
            {
                "name": "address_country",
                "description": "Billing address country, if provided when creating card."
            },
            {
                "name": "address_line1",
                "description": "Address line 1 (Street address/PO Box/Company name)."
            },
            {
                "name": "address_line2",
                "description": "Address line 2 (Apartment/Suite/Unit/Building)."
            },
            {
                "name": "address_state",
                "description": "State/County/Province/Region."
            },
            {
                "name": "address_zip",
                "description": "ZIP or postal code."
            },
            {
                "name": "default_for_currency",
                "description": "When set to true, this becomes the default external account for its currency."
            },
            {
                "name": "documents",
                "description": "Documents that may be submitted to satisfy various informational requests."
            },
            {
                "name": "exp_month",
                "description": "Two digit number representing the card\u2019s expiration month."
            },
            {
                "name": "exp_year",
                "description": "Four digit number representing the card\u2019s expiration year."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "name",
                "description": "Cardholder name."
            }
        ]
    },
    {
        "path": "/v1/file_links",
        "verb": "get",
        "op_id": "GetFileLinks",
        "summary": "List all file links",
        "params": [
            {
                "name": "created",
                "description": "Only return links that were created during the given date interval."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "expired",
                "description": "Filter links by their expiration status. By default, Stripe returns all links."
            },
            {
                "name": "file",
                "description": "Only return links for the given file."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/file_links",
        "verb": "post",
        "op_id": "PostFileLinks",
        "summary": "Create a file link",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "expires_at",
                "description": "The link isn't usable after this future timestamp."
            },
            {
                "name": "file",
                "description": "The ID of the file. The file's `purpose` must be one of the following: `business_icon`, `business_logo`, `customer_signature`, `dispute_evidence`, `finance_report_run`, `financial_account_statement`, `identity_document_downloadable`, `issuing_regulatory_reporting`, `pci_document`, `selfie`, `sigma_scheduled_query`, `tax_document_user_upload`, or `terminal_reader_splashscreen`."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            }
        ]
    },
    {
        "path": "/v1/file_links/{link}",
        "verb": "get",
        "op_id": "GetFileLinksLink",
        "summary": "Retrieve a file link",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/file_links/{link}",
        "verb": "post",
        "op_id": "PostFileLinksLink",
        "summary": "Update a file link",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "expires_at",
                "description": "A future timestamp after which the link will no longer be usable, or `now` to expire the link immediately."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            }
        ]
    },
    {
        "path": "/v1/files",
        "verb": "get",
        "op_id": "GetFiles",
        "summary": "List all files",
        "params": [
            {
                "name": "created",
                "description": "Only return files that were created during the given date interval."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "purpose",
                "description": "Filter queries by the file purpose. If you don't provide a purpose, the queries return unfiltered files."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/files",
        "verb": "post",
        "op_id": "PostFiles",
        "summary": "Create a file",
        "params": []
    },
    {
        "path": "/v1/files/{file}",
        "verb": "get",
        "op_id": "GetFilesFile",
        "summary": "Retrieve a file",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/financial_connections/accounts",
        "verb": "get",
        "op_id": "GetFinancialConnectionsAccounts",
        "summary": "List Accounts",
        "params": [
            {
                "name": "account_holder",
                "description": "If present, only return accounts that belong to the specified account holder. `account_holder[customer]` and `account_holder[account]` are mutually exclusive."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "session",
                "description": "If present, only return accounts that were collected as part of the given session."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/financial_connections/accounts/{account}",
        "verb": "get",
        "op_id": "GetFinancialConnectionsAccountsAccount",
        "summary": "Retrieve an Account",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/financial_connections/accounts/{account}/disconnect",
        "verb": "post",
        "op_id": "PostFinancialConnectionsAccountsAccountDisconnect",
        "summary": "Disconnect an Account",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/financial_connections/accounts/{account}/owners",
        "verb": "get",
        "op_id": "GetFinancialConnectionsAccountsAccountOwners",
        "summary": "List Account Owners",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "ownership",
                "description": "The ID of the ownership object to fetch owners from."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/financial_connections/accounts/{account}/refresh",
        "verb": "post",
        "op_id": "PostFinancialConnectionsAccountsAccountRefresh",
        "summary": "Refresh Account data",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "features",
                "description": "The list of account features that you would like to refresh."
            }
        ]
    },
    {
        "path": "/v1/financial_connections/accounts/{account}/subscribe",
        "verb": "post",
        "op_id": "PostFinancialConnectionsAccountsAccountSubscribe",
        "summary": "Subscribe to data refreshes for an Account",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "features",
                "description": "The list of account features to which you would like to subscribe."
            }
        ]
    },
    {
        "path": "/v1/financial_connections/accounts/{account}/unsubscribe",
        "verb": "post",
        "op_id": "PostFinancialConnectionsAccountsAccountUnsubscribe",
        "summary": "Unsubscribe from data refreshes for an Account",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "features",
                "description": "The list of account features from which you would like to unsubscribe."
            }
        ]
    },
    {
        "path": "/v1/financial_connections/sessions",
        "verb": "post",
        "op_id": "PostFinancialConnectionsSessions",
        "summary": "Create a Session",
        "params": [
            {
                "name": "account_holder",
                "description": "The account holder to link accounts for."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "filters",
                "description": "Filters to restrict the kinds of accounts to collect."
            },
            {
                "name": "permissions",
                "description": "List of data features that you would like to request access to.\n\nPossible values are `balances`, `transactions`, `ownership`, and `payment_method`."
            },
            {
                "name": "prefetch",
                "description": "List of data features that you would like to retrieve upon account creation."
            },
            {
                "name": "return_url",
                "description": "For webview integrations only. Upon completing OAuth login in the native browser, the user will be redirected to this URL to return to your app."
            }
        ]
    },
    {
        "path": "/v1/financial_connections/sessions/{session}",
        "verb": "get",
        "op_id": "GetFinancialConnectionsSessionsSession",
        "summary": "Retrieve a Session",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/financial_connections/transactions",
        "verb": "get",
        "op_id": "GetFinancialConnectionsTransactions",
        "summary": "List Transactions",
        "params": [
            {
                "name": "account",
                "description": "The ID of the Financial Connections Account whose transactions will be retrieved."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "transacted_at",
                "description": "A filter on the list based on the object `transacted_at` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with the following options:"
            },
            {
                "name": "transaction_refresh",
                "description": "A filter on the list based on the object `transaction_refresh` field. The value can be a dictionary with the following options:"
            }
        ]
    },
    {
        "path": "/v1/financial_connections/transactions/{transaction}",
        "verb": "get",
        "op_id": "GetFinancialConnectionsTransactionsTransaction",
        "summary": "Retrieve a Transaction",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/forwarding/requests",
        "verb": "get",
        "op_id": "GetForwardingRequests",
        "summary": "List all ForwardingRequests",
        "params": [
            {
                "name": "created",
                "description": "Similar to other List endpoints, filters results based on created timestamp. You can pass gt, gte, lt, and lte timestamp values."
            },
            {
                "name": "ending_before",
                "description": "A pagination cursor to fetch the previous page of the list. The value must be a ForwardingRequest ID."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A pagination cursor to fetch the next page of the list. The value must be a ForwardingRequest ID."
            }
        ]
    },
    {
        "path": "/v1/forwarding/requests",
        "verb": "post",
        "op_id": "PostForwardingRequests",
        "summary": "Create a ForwardingRequest",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "payment_method",
                "description": "The PaymentMethod to insert into the forwarded request. Forwarding previously consumed PaymentMethods is allowed."
            },
            {
                "name": "replacements",
                "description": "The field kinds to be replaced in the forwarded request."
            },
            {
                "name": "request",
                "description": "The request body and headers to be sent to the destination endpoint."
            },
            {
                "name": "url",
                "description": "The destination URL for the forwarded request. Must be supported by the config."
            }
        ]
    },
    {
        "path": "/v1/forwarding/requests/{id}",
        "verb": "get",
        "op_id": "GetForwardingRequestsId",
        "summary": "Retrieve a ForwardingRequest",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/identity/verification_reports",
        "verb": "get",
        "op_id": "GetIdentityVerificationReports",
        "summary": "List VerificationReports",
        "params": [
            {
                "name": "client_reference_id",
                "description": "A string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems."
            },
            {
                "name": "created",
                "description": "Only return VerificationReports that were created during the given date interval."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "type",
                "description": "Only return VerificationReports of this type"
            },
            {
                "name": "verification_session",
                "description": "Only return VerificationReports created by this VerificationSession ID. It is allowed to provide a VerificationIntent ID."
            }
        ]
    },
    {
        "path": "/v1/identity/verification_reports/{report}",
        "verb": "get",
        "op_id": "GetIdentityVerificationReportsReport",
        "summary": "Retrieve a VerificationReport",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/identity/verification_sessions",
        "verb": "get",
        "op_id": "GetIdentityVerificationSessions",
        "summary": "List VerificationSessions",
        "params": [
            {
                "name": "client_reference_id",
                "description": "A string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems."
            },
            {
                "name": "created",
                "description": "Only return VerificationSessions that were created during the given date interval."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "related_customer",
                "description": ""
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "status",
                "description": "Only return VerificationSessions with this status. [Learn more about the lifecycle of sessions](https://stripe.com/docs/identity/how-sessions-work)."
            }
        ]
    },
    {
        "path": "/v1/identity/verification_sessions",
        "verb": "post",
        "op_id": "PostIdentityVerificationSessions",
        "summary": "Create a VerificationSession",
        "params": [
            {
                "name": "client_reference_id",
                "description": "A string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "options",
                "description": "A set of options for the session\u2019s verification checks."
            },
            {
                "name": "provided_details",
                "description": "Details provided about the user being verified. These details may be shown to the user."
            },
            {
                "name": "related_customer",
                "description": "Customer ID"
            },
            {
                "name": "return_url",
                "description": "The URL that the user will be redirected to upon completing the verification flow."
            },
            {
                "name": "type",
                "description": "The type of [verification check](https://stripe.com/docs/identity/verification-checks) to be performed. You must provide a `type` if not passing `verification_flow`."
            },
            {
                "name": "verification_flow",
                "description": "The ID of a verification flow from the Dashboard. See https://docs.stripe.com/identity/verification-flows."
            }
        ]
    },
    {
        "path": "/v1/identity/verification_sessions/{session}",
        "verb": "get",
        "op_id": "GetIdentityVerificationSessionsSession",
        "summary": "Retrieve a VerificationSession",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/identity/verification_sessions/{session}",
        "verb": "post",
        "op_id": "PostIdentityVerificationSessionsSession",
        "summary": "Update a VerificationSession",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "options",
                "description": "A set of options for the session\u2019s verification checks."
            },
            {
                "name": "provided_details",
                "description": "Details provided about the user being verified. These details may be shown to the user."
            },
            {
                "name": "type",
                "description": "The type of [verification check](https://stripe.com/docs/identity/verification-checks) to be performed."
            }
        ]
    },
    {
        "path": "/v1/identity/verification_sessions/{session}/cancel",
        "verb": "post",
        "op_id": "PostIdentityVerificationSessionsSessionCancel",
        "summary": "Cancel a VerificationSession",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/identity/verification_sessions/{session}/redact",
        "verb": "post",
        "op_id": "PostIdentityVerificationSessionsSessionRedact",
        "summary": "Redact a VerificationSession",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/invoice_payments",
        "verb": "get",
        "op_id": "GetInvoicePayments",
        "summary": "List all payments for an invoice",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "invoice",
                "description": "The identifier of the invoice whose payments to return."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "payment",
                "description": "The payment details of the invoice payments to return."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "status",
                "description": "The status of the invoice payments to return."
            }
        ]
    },
    {
        "path": "/v1/invoice_payments/{invoice_payment}",
        "verb": "get",
        "op_id": "GetInvoicePaymentsInvoicePayment",
        "summary": "Retrieve an InvoicePayment",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/invoice_rendering_templates",
        "verb": "get",
        "op_id": "GetInvoiceRenderingTemplates",
        "summary": "List all invoice rendering templates",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "status",
                "description": ""
            }
        ]
    },
    {
        "path": "/v1/invoice_rendering_templates/{template}",
        "verb": "get",
        "op_id": "GetInvoiceRenderingTemplatesTemplate",
        "summary": "Retrieve an invoice rendering template",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "version",
                "description": ""
            }
        ]
    },
    {
        "path": "/v1/invoice_rendering_templates/{template}/archive",
        "verb": "post",
        "op_id": "PostInvoiceRenderingTemplatesTemplateArchive",
        "summary": "Archive an invoice rendering template",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/invoice_rendering_templates/{template}/unarchive",
        "verb": "post",
        "op_id": "PostInvoiceRenderingTemplatesTemplateUnarchive",
        "summary": "Unarchive an invoice rendering template",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/invoiceitems",
        "verb": "get",
        "op_id": "GetInvoiceitems",
        "summary": "List all invoice items",
        "params": [
            {
                "name": "created",
                "description": "Only return invoice items that were created during the given date interval."
            },
            {
                "name": "customer",
                "description": "The identifier of the customer whose invoice items to return. If none is provided, all invoice items will be returned."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "invoice",
                "description": "Only return invoice items belonging to this invoice. If none is provided, all invoice items will be returned. If specifying an invoice, no customer identifier is needed."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "pending",
                "description": "Set to `true` to only show pending invoice items, which are not yet attached to any invoices. Set to `false` to only show invoice items already attached to invoices. If unspecified, no filter is applied."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/invoiceitems",
        "verb": "post",
        "op_id": "PostInvoiceitems",
        "summary": "Create an invoice item",
        "params": [
            {
                "name": "amount",
                "description": "The integer amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. Passing in a negative `amount` will reduce the `amount_due` on the invoice."
            },
            {
                "name": "currency",
                "description": "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "customer",
                "description": "The ID of the customer who will be billed when this invoice item is billed."
            },
            {
                "name": "description",
                "description": "An arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking."
            },
            {
                "name": "discountable",
                "description": "Controls whether discounts apply to this invoice item. Defaults to false for prorations or negative invoice items, and true for all other invoice items."
            },
            {
                "name": "discounts",
                "description": "The coupons and promotion codes to redeem into discounts for the invoice item or invoice line item."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "invoice",
                "description": "The ID of an existing invoice to add this invoice item to. When left blank, the invoice item will be added to the next upcoming scheduled invoice. This is useful when adding invoice items in response to an invoice.created webhook. You can only add invoice items to draft invoices and there is a maximum of 250 items per invoice."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "period",
                "description": "The period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have [Stripe Revenue Recognition](https://stripe.com/docs/revenue-recognition) enabled, the period will be used to recognize and defer revenue. See the [Revenue Recognition documentation](https://stripe.com/docs/revenue-recognition/methodology/subscriptions-and-invoicing) for details."
            },
            {
                "name": "price_data",
                "description": "Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline."
            },
            {
                "name": "pricing",
                "description": "The pricing information for the invoice item."
            },
            {
                "name": "quantity",
                "description": "Non-negative integer. The quantity of units for the invoice item."
            },
            {
                "name": "subscription",
                "description": "The ID of a subscription to add this invoice item to. When left blank, the invoice item is added to the next upcoming scheduled invoice. When set, scheduled invoices for subscriptions other than the specified subscription will ignore the invoice item. Use this when you want to express that an invoice item has been accrued within the context of a particular subscription."
            },
            {
                "name": "tax_behavior",
                "description": "Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed."
            },
            {
                "name": "tax_code",
                "description": "A [tax code](https://stripe.com/docs/tax/tax-categories) ID."
            },
            {
                "name": "tax_rates",
                "description": "The tax rates which apply to the invoice item. When set, the `default_tax_rates` on the invoice do not apply to this invoice item."
            },
            {
                "name": "unit_amount_decimal",
                "description": "The decimal unit amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. This `unit_amount_decimal` will be multiplied by the quantity to get the full amount. Passing in a negative `unit_amount_decimal` will reduce the `amount_due` on the invoice. Accepts at most 12 decimal places."
            }
        ]
    },
    {
        "path": "/v1/invoiceitems/{invoiceitem}",
        "verb": "delete",
        "op_id": "DeleteInvoiceitemsInvoiceitem",
        "summary": "Delete an invoice item",
        "params": []
    },
    {
        "path": "/v1/invoiceitems/{invoiceitem}",
        "verb": "get",
        "op_id": "GetInvoiceitemsInvoiceitem",
        "summary": "Retrieve an invoice item",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/invoiceitems/{invoiceitem}",
        "verb": "post",
        "op_id": "PostInvoiceitemsInvoiceitem",
        "summary": "Update an invoice item",
        "params": [
            {
                "name": "amount",
                "description": "The integer amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. If you want to apply a credit to the customer's account, pass a negative amount."
            },
            {
                "name": "description",
                "description": "An arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking."
            },
            {
                "name": "discountable",
                "description": "Controls whether discounts apply to this invoice item. Defaults to false for prorations or negative invoice items, and true for all other invoice items. Cannot be set to true for prorations."
            },
            {
                "name": "discounts",
                "description": "The coupons, promotion codes & existing discounts which apply to the invoice item or invoice line item. Item discounts are applied before invoice discounts. Pass an empty string to remove previously-defined discounts."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "period",
                "description": "The period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have [Stripe Revenue Recognition](https://stripe.com/docs/revenue-recognition) enabled, the period will be used to recognize and defer revenue. See the [Revenue Recognition documentation](https://stripe.com/docs/revenue-recognition/methodology/subscriptions-and-invoicing) for details."
            },
            {
                "name": "price_data",
                "description": "Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline."
            },
            {
                "name": "pricing",
                "description": "The pricing information for the invoice item."
            },
            {
                "name": "quantity",
                "description": "Non-negative integer. The quantity of units for the invoice item."
            },
            {
                "name": "tax_behavior",
                "description": "Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed."
            },
            {
                "name": "tax_code",
                "description": "A [tax code](https://stripe.com/docs/tax/tax-categories) ID."
            },
            {
                "name": "tax_rates",
                "description": "The tax rates which apply to the invoice item. When set, the `default_tax_rates` on the invoice do not apply to this invoice item. Pass an empty string to remove previously-defined tax rates."
            },
            {
                "name": "unit_amount_decimal",
                "description": "The decimal unit amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. This `unit_amount_decimal` will be multiplied by the quantity to get the full amount. Passing in a negative `unit_amount_decimal` will reduce the `amount_due` on the invoice. Accepts at most 12 decimal places."
            }
        ]
    },
    {
        "path": "/v1/invoices",
        "verb": "get",
        "op_id": "GetInvoices",
        "summary": "List all invoices",
        "params": [
            {
                "name": "collection_method",
                "description": "The collection method of the invoice to retrieve. Either `charge_automatically` or `send_invoice`."
            },
            {
                "name": "created",
                "description": "Only return invoices that were created during the given date interval."
            },
            {
                "name": "customer",
                "description": "Only return invoices for the customer specified by this customer ID."
            },
            {
                "name": "due_date",
                "description": ""
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "status",
                "description": "The status of the invoice, one of `draft`, `open`, `paid`, `uncollectible`, or `void`. [Learn more](https://stripe.com/docs/billing/invoices/workflow#workflow-overview)"
            },
            {
                "name": "subscription",
                "description": "Only return invoices for the subscription specified by this subscription ID."
            }
        ]
    },
    {
        "path": "/v1/invoices",
        "verb": "post",
        "op_id": "PostInvoices",
        "summary": "Create an invoice",
        "params": [
            {
                "name": "account_tax_ids",
                "description": "The account tax IDs associated with the invoice. Only editable when the invoice is a draft."
            },
            {
                "name": "application_fee_amount",
                "description": "A fee in cents (or local equivalent) that will be applied to the invoice and transferred to the application owner's Stripe account. The request must be made with an OAuth key or the Stripe-Account header in order to take an application fee. For more information, see the application fees [documentation](https://stripe.com/docs/billing/invoices/connect#collecting-fees)."
            },
            {
                "name": "auto_advance",
                "description": "Controls whether Stripe performs [automatic collection](https://stripe.com/docs/invoicing/integration/automatic-advancement-collection) of the invoice. If `false`, the invoice's state doesn't automatically advance without an explicit action."
            },
            {
                "name": "automatic_tax",
                "description": "Settings for automatic tax lookup for this invoice."
            },
            {
                "name": "automatically_finalizes_at",
                "description": "The time when this invoice should be scheduled to finalize. The invoice will be finalized at this time if it is still in draft state."
            },
            {
                "name": "collection_method",
                "description": "Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this invoice using the default source attached to the customer. When sending an invoice, Stripe will email this invoice to the customer with payment instructions. Defaults to `charge_automatically`."
            },
            {
                "name": "currency",
                "description": "The currency to create this invoice in. Defaults to that of `customer` if not specified."
            },
            {
                "name": "custom_fields",
                "description": "A list of up to 4 custom fields to be displayed on the invoice."
            },
            {
                "name": "customer",
                "description": "The ID of the customer who will be billed."
            },
            {
                "name": "days_until_due",
                "description": "The number of days from when the invoice is created until it is due. Valid only for invoices where `collection_method=send_invoice`."
            },
            {
                "name": "default_payment_method",
                "description": "ID of the default payment method for the invoice. It must belong to the customer associated with the invoice. If not set, defaults to the subscription's default payment method, if any, or to the default payment method in the customer's invoice settings."
            },
            {
                "name": "default_source",
                "description": "ID of the default payment source for the invoice. It must belong to the customer associated with the invoice and be in a chargeable state. If not set, defaults to the subscription's default source, if any, or to the customer's default source."
            },
            {
                "name": "default_tax_rates",
                "description": "The tax rates that will apply to any line item that does not have `tax_rates` set."
            },
            {
                "name": "description",
                "description": "An arbitrary string attached to the object. Often useful for displaying to users. Referenced as 'memo' in the Dashboard."
            },
            {
                "name": "discounts",
                "description": "The coupons and promotion codes to redeem into discounts for the invoice. If not specified, inherits the discount from the invoice's customer. Pass an empty string to avoid inheriting any discounts."
            },
            {
                "name": "due_date",
                "description": "The date on which payment for this invoice is due. Valid only for invoices where `collection_method=send_invoice`."
            },
            {
                "name": "effective_at",
                "description": "The date when this invoice is in effect. Same as `finalized_at` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the invoice PDF and receipt."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "footer",
                "description": "Footer to be displayed on the invoice."
            },
            {
                "name": "from_invoice",
                "description": "Revise an existing invoice. The new invoice will be created in `status=draft`. See the [revision documentation](https://stripe.com/docs/invoicing/invoice-revisions) for more details."
            },
            {
                "name": "issuer",
                "description": "The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "number",
                "description": "Set the number for this invoice. If no number is present then a number will be assigned automatically when the invoice is finalized. In many markets, regulations require invoices to be unique, sequential and / or gapless. You are responsible for ensuring this is true across all your different invoicing systems in the event that you edit the invoice number using our API. If you use only Stripe for your invoices and do not change invoice numbers, Stripe handles this aspect of compliance for you automatically."
            },
            {
                "name": "on_behalf_of",
                "description": "The account (if any) for which the funds of the invoice payment are intended. If set, the invoice will be presented with the branding and support information of the specified account. See the [Invoices with Connect](https://stripe.com/docs/billing/invoices/connect) documentation for details."
            },
            {
                "name": "payment_settings",
                "description": "Configuration settings for the PaymentIntent that is generated when the invoice is finalized."
            },
            {
                "name": "pending_invoice_items_behavior",
                "description": "How to handle pending invoice items on invoice creation. Defaults to `exclude` if the parameter is omitted."
            },
            {
                "name": "rendering",
                "description": "The rendering-related settings that control how the invoice is displayed on customer-facing surfaces such as PDF and Hosted Invoice Page."
            },
            {
                "name": "shipping_cost",
                "description": "Settings for the cost of shipping for this invoice."
            },
            {
                "name": "shipping_details",
                "description": "Shipping details for the invoice. The Invoice PDF will use the `shipping_details` value if it is set, otherwise the PDF will render the shipping address from the customer."
            },
            {
                "name": "statement_descriptor",
                "description": "Extra information about a charge for the customer's credit card statement. It must contain at least one letter. If not specified and this invoice is part of a subscription, the default `statement_descriptor` will be set to the first subscription item's product's `statement_descriptor`."
            },
            {
                "name": "subscription",
                "description": "The ID of the subscription to invoice, if any. If set, the created invoice will only include pending invoice items for that subscription. The subscription's billing cycle and regular subscription events won't be affected."
            },
            {
                "name": "transfer_data",
                "description": "If specified, the funds from the invoice will be transferred to the destination and the ID of the resulting transfer will be found on the invoice's charge."
            }
        ]
    },
    {
        "path": "/v1/invoices/create_preview",
        "verb": "post",
        "op_id": "PostInvoicesCreatePreview",
        "summary": "Create a preview invoice",
        "params": [
            {
                "name": "automatic_tax",
                "description": "Settings for automatic tax lookup for this invoice preview."
            },
            {
                "name": "currency",
                "description": "The currency to preview this invoice in. Defaults to that of `customer` if not specified."
            },
            {
                "name": "customer",
                "description": "The identifier of the customer whose upcoming invoice you'd like to retrieve. If `automatic_tax` is enabled then one of `customer`, `customer_details`, `subscription`, or `schedule` must be set."
            },
            {
                "name": "customer_details",
                "description": "Details about the customer you want to invoice or overrides for an existing customer. If `automatic_tax` is enabled then one of `customer`, `customer_details`, `subscription`, or `schedule` must be set."
            },
            {
                "name": "discounts",
                "description": "The coupons to redeem into discounts for the invoice preview. If not specified, inherits the discount from the subscription or customer. This works for both coupons directly applied to an invoice and coupons applied to a subscription. Pass an empty string to avoid inheriting any discounts."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "invoice_items",
                "description": "List of invoice items to add or update in the upcoming invoice preview (up to 250)."
            },
            {
                "name": "issuer",
                "description": "The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account."
            },
            {
                "name": "on_behalf_of",
                "description": "The account (if any) for which the funds of the invoice payment are intended. If set, the invoice will be presented with the branding and support information of the specified account. See the [Invoices with Connect](https://stripe.com/docs/billing/invoices/connect) documentation for details."
            },
            {
                "name": "preview_mode",
                "description": "Customizes the types of values to include when calculating the invoice. Defaults to `next` if unspecified."
            },
            {
                "name": "schedule",
                "description": "The identifier of the schedule whose upcoming invoice you'd like to retrieve. Cannot be used with subscription or subscription fields."
            },
            {
                "name": "schedule_details",
                "description": "The schedule creation or modification params to apply as a preview. Cannot be used with `subscription` or `subscription_` prefixed fields."
            },
            {
                "name": "subscription",
                "description": "The identifier of the subscription for which you'd like to retrieve the upcoming invoice. If not provided, but a `subscription_details.items` is provided, you will preview creating a subscription with those items. If neither `subscription` nor `subscription_details.items` is provided, you will retrieve the next upcoming invoice from among the customer's subscriptions."
            },
            {
                "name": "subscription_details",
                "description": "The subscription creation or modification params to apply as a preview. Cannot be used with `schedule` or `schedule_details` fields."
            }
        ]
    },
    {
        "path": "/v1/invoices/search",
        "verb": "get",
        "op_id": "GetInvoicesSearch",
        "summary": "Search invoices",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "page",
                "description": "A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results."
            },
            {
                "name": "query",
                "description": "The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for invoices](https://stripe.com/docs/search#query-fields-for-invoices)."
            }
        ]
    },
    {
        "path": "/v1/invoices/{invoice}",
        "verb": "delete",
        "op_id": "DeleteInvoicesInvoice",
        "summary": "Delete a draft invoice",
        "params": []
    },
    {
        "path": "/v1/invoices/{invoice}",
        "verb": "get",
        "op_id": "GetInvoicesInvoice",
        "summary": "Retrieve an invoice",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/invoices/{invoice}",
        "verb": "post",
        "op_id": "PostInvoicesInvoice",
        "summary": "Update an invoice",
        "params": [
            {
                "name": "account_tax_ids",
                "description": "The account tax IDs associated with the invoice. Only editable when the invoice is a draft."
            },
            {
                "name": "application_fee_amount",
                "description": "A fee in cents (or local equivalent) that will be applied to the invoice and transferred to the application owner's Stripe account. The request must be made with an OAuth key or the Stripe-Account header in order to take an application fee. For more information, see the application fees [documentation](https://stripe.com/docs/billing/invoices/connect#collecting-fees)."
            },
            {
                "name": "auto_advance",
                "description": "Controls whether Stripe performs [automatic collection](https://stripe.com/docs/invoicing/integration/automatic-advancement-collection) of the invoice."
            },
            {
                "name": "automatic_tax",
                "description": "Settings for automatic tax lookup for this invoice."
            },
            {
                "name": "automatically_finalizes_at",
                "description": "The time when this invoice should be scheduled to finalize. The invoice will be finalized at this time if it is still in draft state. To turn off automatic finalization, set `auto_advance` to false."
            },
            {
                "name": "collection_method",
                "description": "Either `charge_automatically` or `send_invoice`. This field can be updated only on `draft` invoices."
            },
            {
                "name": "custom_fields",
                "description": "A list of up to 4 custom fields to be displayed on the invoice. If a value for `custom_fields` is specified, the list specified will replace the existing custom field list on this invoice. Pass an empty string to remove previously-defined fields."
            },
            {
                "name": "days_until_due",
                "description": "The number of days from which the invoice is created until it is due. Only valid for invoices where `collection_method=send_invoice`. This field can only be updated on `draft` invoices."
            },
            {
                "name": "default_payment_method",
                "description": "ID of the default payment method for the invoice. It must belong to the customer associated with the invoice. If not set, defaults to the subscription's default payment method, if any, or to the default payment method in the customer's invoice settings."
            },
            {
                "name": "default_source",
                "description": "ID of the default payment source for the invoice. It must belong to the customer associated with the invoice and be in a chargeable state. If not set, defaults to the subscription's default source, if any, or to the customer's default source."
            },
            {
                "name": "default_tax_rates",
                "description": "The tax rates that will apply to any line item that does not have `tax_rates` set. Pass an empty string to remove previously-defined tax rates."
            },
            {
                "name": "description",
                "description": "An arbitrary string attached to the object. Often useful for displaying to users. Referenced as 'memo' in the Dashboard."
            },
            {
                "name": "discounts",
                "description": "The discounts that will apply to the invoice. Pass an empty string to remove previously-defined discounts."
            },
            {
                "name": "due_date",
                "description": "The date on which payment for this invoice is due. Only valid for invoices where `collection_method=send_invoice`. This field can only be updated on `draft` invoices."
            },
            {
                "name": "effective_at",
                "description": "The date when this invoice is in effect. Same as `finalized_at` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the invoice PDF and receipt."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "footer",
                "description": "Footer to be displayed on the invoice."
            },
            {
                "name": "issuer",
                "description": "The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "number",
                "description": "Set the number for this invoice. If no number is present then a number will be assigned automatically when the invoice is finalized. In many markets, regulations require invoices to be unique, sequential and / or gapless. You are responsible for ensuring this is true across all your different invoicing systems in the event that you edit the invoice number using our API. If you use only Stripe for your invoices and do not change invoice numbers, Stripe handles this aspect of compliance for you automatically."
            },
            {
                "name": "on_behalf_of",
                "description": "The account (if any) for which the funds of the invoice payment are intended. If set, the invoice will be presented with the branding and support information of the specified account. See the [Invoices with Connect](https://stripe.com/docs/billing/invoices/connect) documentation for details."
            },
            {
                "name": "payment_settings",
                "description": "Configuration settings for the PaymentIntent that is generated when the invoice is finalized."
            },
            {
                "name": "rendering",
                "description": "The rendering-related settings that control how the invoice is displayed on customer-facing surfaces such as PDF and Hosted Invoice Page."
            },
            {
                "name": "shipping_cost",
                "description": "Settings for the cost of shipping for this invoice."
            },
            {
                "name": "shipping_details",
                "description": "Shipping details for the invoice. The Invoice PDF will use the `shipping_details` value if it is set, otherwise the PDF will render the shipping address from the customer."
            },
            {
                "name": "statement_descriptor",
                "description": "Extra information about a charge for the customer's credit card statement. It must contain at least one letter. If not specified and this invoice is part of a subscription, the default `statement_descriptor` will be set to the first subscription item's product's `statement_descriptor`."
            },
            {
                "name": "transfer_data",
                "description": "If specified, the funds from the invoice will be transferred to the destination and the ID of the resulting transfer will be found on the invoice's charge. This will be unset if you POST an empty value."
            }
        ]
    },
    {
        "path": "/v1/invoices/{invoice}/add_lines",
        "verb": "post",
        "op_id": "PostInvoicesInvoiceAddLines",
        "summary": "Bulk add invoice line items",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "invoice_metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "lines",
                "description": "The line items to add."
            }
        ]
    },
    {
        "path": "/v1/invoices/{invoice}/attach_payment",
        "verb": "post",
        "op_id": "PostInvoicesInvoiceAttachPayment",
        "summary": "Attach a payment to an Invoice",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "payment_intent",
                "description": "The ID of the PaymentIntent to attach to the invoice."
            }
        ]
    },
    {
        "path": "/v1/invoices/{invoice}/finalize",
        "verb": "post",
        "op_id": "PostInvoicesInvoiceFinalize",
        "summary": "Finalize an invoice",
        "params": [
            {
                "name": "auto_advance",
                "description": "Controls whether Stripe performs [automatic collection](https://stripe.com/docs/invoicing/integration/automatic-advancement-collection) of the invoice. If `false`, the invoice's state doesn't automatically advance without an explicit action."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/invoices/{invoice}/lines",
        "verb": "get",
        "op_id": "GetInvoicesInvoiceLines",
        "summary": "Retrieve an invoice's line items",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/invoices/{invoice}/lines/{line_item_id}",
        "verb": "post",
        "op_id": "PostInvoicesInvoiceLinesLineItemId",
        "summary": "Update an invoice's line item",
        "params": [
            {
                "name": "amount",
                "description": "The integer amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. If you want to apply a credit to the customer's account, pass a negative amount."
            },
            {
                "name": "description",
                "description": "An arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking."
            },
            {
                "name": "discountable",
                "description": "Controls whether discounts apply to this line item. Defaults to false for prorations or negative line items, and true for all other line items. Cannot be set to true for prorations."
            },
            {
                "name": "discounts",
                "description": "The coupons, promotion codes & existing discounts which apply to the line item. Item discounts are applied before invoice discounts. Pass an empty string to remove previously-defined discounts."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. For [type=subscription](https://stripe.com/docs/api/invoices/line_item#invoice_line_item_object-type) line items, the incoming metadata specified on the request is directly used to set this value, in contrast to [type=invoiceitem](api/invoices/line_item#invoice_line_item_object-type) line items, where any existing metadata on the invoice line is merged with the incoming data."
            },
            {
                "name": "period",
                "description": "The period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have [Stripe Revenue Recognition](https://stripe.com/docs/revenue-recognition) enabled, the period will be used to recognize and defer revenue. See the [Revenue Recognition documentation](https://stripe.com/docs/revenue-recognition/methodology/subscriptions-and-invoicing) for details."
            },
            {
                "name": "price_data",
                "description": "Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline."
            },
            {
                "name": "pricing",
                "description": "The pricing information for the invoice item."
            },
            {
                "name": "quantity",
                "description": "Non-negative integer. The quantity of units for the line item."
            },
            {
                "name": "tax_amounts",
                "description": "A list of up to 10 tax amounts for this line item. This can be useful if you calculate taxes on your own or use a third-party to calculate them. You cannot set tax amounts if any line item has [tax_rates](https://stripe.com/docs/api/invoices/line_item#invoice_line_item_object-tax_rates) or if the invoice has [default_tax_rates](https://stripe.com/docs/api/invoices/object#invoice_object-default_tax_rates) or uses [automatic tax](https://stripe.com/docs/tax/invoicing). Pass an empty string to remove previously defined tax amounts."
            },
            {
                "name": "tax_rates",
                "description": "The tax rates which apply to the line item. When set, the `default_tax_rates` on the invoice do not apply to this line item. Pass an empty string to remove previously-defined tax rates."
            }
        ]
    },
    {
        "path": "/v1/invoices/{invoice}/mark_uncollectible",
        "verb": "post",
        "op_id": "PostInvoicesInvoiceMarkUncollectible",
        "summary": "Mark an invoice as uncollectible",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/invoices/{invoice}/pay",
        "verb": "post",
        "op_id": "PostInvoicesInvoicePay",
        "summary": "Pay an invoice",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "forgive",
                "description": "In cases where the source used to pay the invoice has insufficient funds, passing `forgive=true` controls whether a charge should be attempted for the full amount available on the source, up to the amount to fully pay the invoice. This effectively forgives the difference between the amount available on the source and the amount due. \n\nPassing `forgive=false` will fail the charge if the source hasn't been pre-funded with the right amount. An example for this case is with ACH Credit Transfers and wires: if the amount wired is less than the amount due by a small amount, you might want to forgive the difference. Defaults to `false`."
            },
            {
                "name": "mandate",
                "description": "ID of the mandate to be used for this invoice. It must correspond to the payment method used to pay the invoice, including the payment_method param or the invoice's default_payment_method or default_source, if set."
            },
            {
                "name": "off_session",
                "description": "Indicates if a customer is on or off-session while an invoice payment is attempted. Defaults to `true` (off-session)."
            },
            {
                "name": "paid_out_of_band",
                "description": "Boolean representing whether an invoice is paid outside of Stripe. This will result in no charge being made. Defaults to `false`."
            },
            {
                "name": "payment_method",
                "description": "A PaymentMethod to be charged. The PaymentMethod must be the ID of a PaymentMethod belonging to the customer associated with the invoice being paid."
            },
            {
                "name": "source",
                "description": "A payment source to be charged. The source must be the ID of a source belonging to the customer associated with the invoice being paid."
            }
        ]
    },
    {
        "path": "/v1/invoices/{invoice}/remove_lines",
        "verb": "post",
        "op_id": "PostInvoicesInvoiceRemoveLines",
        "summary": "Bulk remove invoice line items",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "invoice_metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "lines",
                "description": "The line items to remove."
            }
        ]
    },
    {
        "path": "/v1/invoices/{invoice}/send",
        "verb": "post",
        "op_id": "PostInvoicesInvoiceSend",
        "summary": "Send an invoice for manual payment",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/invoices/{invoice}/update_lines",
        "verb": "post",
        "op_id": "PostInvoicesInvoiceUpdateLines",
        "summary": "Bulk update invoice line items",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "invoice_metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. For [type=subscription](https://stripe.com/docs/api/invoices/line_item#invoice_line_item_object-type) line items, the incoming metadata specified on the request is directly used to set this value, in contrast to [type=invoiceitem](api/invoices/line_item#invoice_line_item_object-type) line items, where any existing metadata on the invoice line is merged with the incoming data."
            },
            {
                "name": "lines",
                "description": "The line items to update."
            }
        ]
    },
    {
        "path": "/v1/invoices/{invoice}/void",
        "verb": "post",
        "op_id": "PostInvoicesInvoiceVoid",
        "summary": "Void an invoice",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/issuing/authorizations",
        "verb": "get",
        "op_id": "GetIssuingAuthorizations",
        "summary": "List all authorizations",
        "params": [
            {
                "name": "card",
                "description": "Only return authorizations that belong to the given card."
            },
            {
                "name": "cardholder",
                "description": "Only return authorizations that belong to the given cardholder."
            },
            {
                "name": "created",
                "description": "Only return authorizations that were created during the given date interval."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "status",
                "description": "Only return authorizations with the given status. One of `pending`, `closed`, or `reversed`."
            }
        ]
    },
    {
        "path": "/v1/issuing/authorizations/{authorization}",
        "verb": "get",
        "op_id": "GetIssuingAuthorizationsAuthorization",
        "summary": "Retrieve an authorization",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/issuing/authorizations/{authorization}",
        "verb": "post",
        "op_id": "PostIssuingAuthorizationsAuthorization",
        "summary": "Update an authorization",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            }
        ]
    },
    {
        "path": "/v1/issuing/authorizations/{authorization}/approve",
        "verb": "post",
        "op_id": "PostIssuingAuthorizationsAuthorizationApprove",
        "summary": "Approve an authorization",
        "params": [
            {
                "name": "amount",
                "description": "If the authorization's `pending_request.is_amount_controllable` property is `true`, you may provide this value to control how much to hold for the authorization. Must be positive (use [`decline`](https://stripe.com/docs/api/issuing/authorizations/decline) to decline an authorization request)."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            }
        ]
    },
    {
        "path": "/v1/issuing/authorizations/{authorization}/decline",
        "verb": "post",
        "op_id": "PostIssuingAuthorizationsAuthorizationDecline",
        "summary": "Decline an authorization",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            }
        ]
    },
    {
        "path": "/v1/issuing/cardholders",
        "verb": "get",
        "op_id": "GetIssuingCardholders",
        "summary": "List all cardholders",
        "params": [
            {
                "name": "created",
                "description": "Only return cardholders that were created during the given date interval."
            },
            {
                "name": "email",
                "description": "Only return cardholders that have the given email address."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "phone_number",
                "description": "Only return cardholders that have the given phone number."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "status",
                "description": "Only return cardholders that have the given status. One of `active`, `inactive`, or `blocked`."
            },
            {
                "name": "type",
                "description": "Only return cardholders that have the given type. One of `individual` or `company`."
            }
        ]
    },
    {
        "path": "/v1/issuing/cardholders",
        "verb": "post",
        "op_id": "PostIssuingCardholders",
        "summary": "Create a cardholder",
        "params": [
            {
                "name": "billing",
                "description": "The cardholder's billing address."
            },
            {
                "name": "company",
                "description": "Additional information about a `company` cardholder."
            },
            {
                "name": "email",
                "description": "The cardholder's email address."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "individual",
                "description": "Additional information about an `individual` cardholder."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "name",
                "description": "The cardholder's name. This will be printed on cards issued to them. The maximum length of this field is 24 characters. This field cannot contain any special characters or numbers."
            },
            {
                "name": "phone_number",
                "description": "The cardholder's phone number. This will be transformed to [E.164](https://en.wikipedia.org/wiki/E.164) if it is not provided in that format already. This is required for all cardholders who will be creating EU cards. See the [3D Secure documentation](https://stripe.com/docs/issuing/3d-secure#when-is-3d-secure-applied) for more details."
            },
            {
                "name": "preferred_locales",
                "description": "The cardholder\u2019s preferred locales (languages), ordered by preference. Locales can be `de`, `en`, `es`, `fr`, or `it`.\n This changes the language of the [3D Secure flow](https://stripe.com/docs/issuing/3d-secure) and one-time password messages sent to the cardholder."
            },
            {
                "name": "spending_controls",
                "description": "Rules that control spending across this cardholder's cards. Refer to our [documentation](https://stripe.com/docs/issuing/controls/spending-controls) for more details."
            },
            {
                "name": "status",
                "description": "Specifies whether to permit authorizations on this cardholder's cards. Defaults to `active`."
            },
            {
                "name": "type",
                "description": "One of `individual` or `company`. See [Choose a cardholder type](https://stripe.com/docs/issuing/other/choose-cardholder) for more details."
            }
        ]
    },
    {
        "path": "/v1/issuing/cardholders/{cardholder}",
        "verb": "get",
        "op_id": "GetIssuingCardholdersCardholder",
        "summary": "Retrieve a cardholder",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/issuing/cardholders/{cardholder}",
        "verb": "post",
        "op_id": "PostIssuingCardholdersCardholder",
        "summary": "Update a cardholder",
        "params": [
            {
                "name": "billing",
                "description": "The cardholder's billing address."
            },
            {
                "name": "company",
                "description": "Additional information about a `company` cardholder."
            },
            {
                "name": "email",
                "description": "The cardholder's email address."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "individual",
                "description": "Additional information about an `individual` cardholder."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "phone_number",
                "description": "The cardholder's phone number. This is required for all cardholders who will be creating EU cards. See the [3D Secure documentation](https://stripe.com/docs/issuing/3d-secure) for more details."
            },
            {
                "name": "preferred_locales",
                "description": "The cardholder\u2019s preferred locales (languages), ordered by preference. Locales can be `de`, `en`, `es`, `fr`, or `it`.\n This changes the language of the [3D Secure flow](https://stripe.com/docs/issuing/3d-secure) and one-time password messages sent to the cardholder."
            },
            {
                "name": "spending_controls",
                "description": "Rules that control spending across this cardholder's cards. Refer to our [documentation](https://stripe.com/docs/issuing/controls/spending-controls) for more details."
            },
            {
                "name": "status",
                "description": "Specifies whether to permit authorizations on this cardholder's cards."
            }
        ]
    },
    {
        "path": "/v1/issuing/cards",
        "verb": "get",
        "op_id": "GetIssuingCards",
        "summary": "List all cards",
        "params": [
            {
                "name": "cardholder",
                "description": "Only return cards belonging to the Cardholder with the provided ID."
            },
            {
                "name": "created",
                "description": "Only return cards that were issued during the given date interval."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "exp_month",
                "description": "Only return cards that have the given expiration month."
            },
            {
                "name": "exp_year",
                "description": "Only return cards that have the given expiration year."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "last4",
                "description": "Only return cards that have the given last four digits."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "personalization_design",
                "description": ""
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "status",
                "description": "Only return cards that have the given status. One of `active`, `inactive`, or `canceled`."
            },
            {
                "name": "type",
                "description": "Only return cards that have the given type. One of `virtual` or `physical`."
            }
        ]
    },
    {
        "path": "/v1/issuing/cards",
        "verb": "post",
        "op_id": "PostIssuingCards",
        "summary": "Create a card",
        "params": [
            {
                "name": "cardholder",
                "description": "The [Cardholder](https://stripe.com/docs/api#issuing_cardholder_object) object with which the card will be associated."
            },
            {
                "name": "currency",
                "description": "The currency for the card."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "financial_account",
                "description": "The new financial account ID the card will be associated with. This field allows a card to be reassigned to a different financial account."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "personalization_design",
                "description": "The personalization design object belonging to this card."
            },
            {
                "name": "pin",
                "description": "The desired PIN for this card."
            },
            {
                "name": "replacement_for",
                "description": "The card this is meant to be a replacement for (if any)."
            },
            {
                "name": "replacement_reason",
                "description": "If `replacement_for` is specified, this should indicate why that card is being replaced."
            },
            {
                "name": "second_line",
                "description": "The second line to print on the card. Max length: 24 characters."
            },
            {
                "name": "shipping",
                "description": "The address where the card will be shipped."
            },
            {
                "name": "spending_controls",
                "description": "Rules that control spending for this card. Refer to our [documentation](https://stripe.com/docs/issuing/controls/spending-controls) for more details."
            },
            {
                "name": "status",
                "description": "Whether authorizations can be approved on this card. May be blocked from activating cards depending on past-due Cardholder requirements. Defaults to `inactive`."
            },
            {
                "name": "type",
                "description": "The type of card to issue. Possible values are `physical` or `virtual`."
            }
        ]
    },
    {
        "path": "/v1/issuing/cards/{card}",
        "verb": "get",
        "op_id": "GetIssuingCardsCard",
        "summary": "Retrieve a card",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/issuing/cards/{card}",
        "verb": "post",
        "op_id": "PostIssuingCardsCard",
        "summary": "Update a card",
        "params": [
            {
                "name": "cancellation_reason",
                "description": "Reason why the `status` of this card is `canceled`."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "personalization_design",
                "description": ""
            },
            {
                "name": "pin",
                "description": "The desired new PIN for this card."
            },
            {
                "name": "shipping",
                "description": "Updated shipping information for the card."
            },
            {
                "name": "spending_controls",
                "description": "Rules that control spending for this card. Refer to our [documentation](https://stripe.com/docs/issuing/controls/spending-controls) for more details."
            },
            {
                "name": "status",
                "description": "Dictates whether authorizations can be approved on this card. May be blocked from activating cards depending on past-due Cardholder requirements. Defaults to `inactive`. If this card is being canceled because it was lost or stolen, this information should be provided as `cancellation_reason`."
            }
        ]
    },
    {
        "path": "/v1/issuing/disputes",
        "verb": "get",
        "op_id": "GetIssuingDisputes",
        "summary": "List all disputes",
        "params": [
            {
                "name": "created",
                "description": "Only return Issuing disputes that were created during the given date interval."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "status",
                "description": "Select Issuing disputes with the given status."
            },
            {
                "name": "transaction",
                "description": "Select the Issuing dispute for the given transaction."
            }
        ]
    },
    {
        "path": "/v1/issuing/disputes",
        "verb": "post",
        "op_id": "PostIssuingDisputes",
        "summary": "Create a dispute",
        "params": [
            {
                "name": "amount",
                "description": "The dispute amount in the card's currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). If not set, defaults to the full transaction amount."
            },
            {
                "name": "evidence",
                "description": "Evidence provided for the dispute."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "transaction",
                "description": "The ID of the issuing transaction to create a dispute for. For transaction on Treasury FinancialAccounts, use `treasury.received_debit`."
            },
            {
                "name": "treasury",
                "description": "Params for disputes related to Treasury FinancialAccounts"
            }
        ]
    },
    {
        "path": "/v1/issuing/disputes/{dispute}",
        "verb": "get",
        "op_id": "GetIssuingDisputesDispute",
        "summary": "Retrieve a dispute",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/issuing/disputes/{dispute}",
        "verb": "post",
        "op_id": "PostIssuingDisputesDispute",
        "summary": "Update a dispute",
        "params": [
            {
                "name": "amount",
                "description": "The dispute amount in the card's currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)."
            },
            {
                "name": "evidence",
                "description": "Evidence provided for the dispute."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            }
        ]
    },
    {
        "path": "/v1/issuing/disputes/{dispute}/submit",
        "verb": "post",
        "op_id": "PostIssuingDisputesDisputeSubmit",
        "summary": "Submit a dispute",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            }
        ]
    },
    {
        "path": "/v1/issuing/personalization_designs",
        "verb": "get",
        "op_id": "GetIssuingPersonalizationDesigns",
        "summary": "List all personalization designs",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "lookup_keys",
                "description": "Only return personalization designs with the given lookup keys."
            },
            {
                "name": "preferences",
                "description": "Only return personalization designs with the given preferences."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "status",
                "description": "Only return personalization designs with the given status."
            }
        ]
    },
    {
        "path": "/v1/issuing/personalization_designs",
        "verb": "post",
        "op_id": "PostIssuingPersonalizationDesigns",
        "summary": "Create a personalization design",
        "params": [
            {
                "name": "card_logo",
                "description": "The file for the card logo, for use with physical bundles that support card logos. Must have a `purpose` value of `issuing_logo`."
            },
            {
                "name": "carrier_text",
                "description": "Hash containing carrier text, for use with physical bundles that support carrier text."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "lookup_key",
                "description": "A lookup key used to retrieve personalization designs dynamically from a static string. This may be up to 200 characters."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "name",
                "description": "Friendly display name."
            },
            {
                "name": "physical_bundle",
                "description": "The physical bundle object belonging to this personalization design."
            },
            {
                "name": "preferences",
                "description": "Information on whether this personalization design is used to create cards when one is not specified."
            },
            {
                "name": "transfer_lookup_key",
                "description": "If set to true, will atomically remove the lookup key from the existing personalization design, and assign it to this personalization design."
            }
        ]
    },
    {
        "path": "/v1/issuing/personalization_designs/{personalization_design}",
        "verb": "get",
        "op_id": "GetIssuingPersonalizationDesignsPersonalizationDesign",
        "summary": "Retrieve a personalization design",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/issuing/personalization_designs/{personalization_design}",
        "verb": "post",
        "op_id": "PostIssuingPersonalizationDesignsPersonalizationDesign",
        "summary": "Update a personalization design",
        "params": [
            {
                "name": "card_logo",
                "description": "The file for the card logo, for use with physical bundles that support card logos. Must have a `purpose` value of `issuing_logo`."
            },
            {
                "name": "carrier_text",
                "description": "Hash containing carrier text, for use with physical bundles that support carrier text."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "lookup_key",
                "description": "A lookup key used to retrieve personalization designs dynamically from a static string. This may be up to 200 characters."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "name",
                "description": "Friendly display name. Providing an empty string will set the field to null."
            },
            {
                "name": "physical_bundle",
                "description": "The physical bundle object belonging to this personalization design."
            },
            {
                "name": "preferences",
                "description": "Information on whether this personalization design is used to create cards when one is not specified."
            },
            {
                "name": "transfer_lookup_key",
                "description": "If set to true, will atomically remove the lookup key from the existing personalization design, and assign it to this personalization design."
            }
        ]
    },
    {
        "path": "/v1/issuing/physical_bundles",
        "verb": "get",
        "op_id": "GetIssuingPhysicalBundles",
        "summary": "List all physical bundles",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "status",
                "description": "Only return physical bundles with the given status."
            },
            {
                "name": "type",
                "description": "Only return physical bundles with the given type."
            }
        ]
    },
    {
        "path": "/v1/issuing/physical_bundles/{physical_bundle}",
        "verb": "get",
        "op_id": "GetIssuingPhysicalBundlesPhysicalBundle",
        "summary": "Retrieve a physical bundle",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/issuing/settlements/{settlement}",
        "verb": "get",
        "op_id": "GetIssuingSettlementsSettlement",
        "summary": "Retrieve a settlement",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/issuing/settlements/{settlement}",
        "verb": "post",
        "op_id": "PostIssuingSettlementsSettlement",
        "summary": "Update a settlement",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            }
        ]
    },
    {
        "path": "/v1/issuing/tokens",
        "verb": "get",
        "op_id": "GetIssuingTokens",
        "summary": "List all issuing tokens for card",
        "params": [
            {
                "name": "card",
                "description": "The Issuing card identifier to list tokens for."
            },
            {
                "name": "created",
                "description": "Only return Issuing tokens that were created during the given date interval."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "status",
                "description": "Select Issuing tokens with the given status."
            }
        ]
    },
    {
        "path": "/v1/issuing/tokens/{token}",
        "verb": "get",
        "op_id": "GetIssuingTokensToken",
        "summary": "Retrieve an issuing token",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/issuing/tokens/{token}",
        "verb": "post",
        "op_id": "PostIssuingTokensToken",
        "summary": "Update a token status",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "status",
                "description": "Specifies which status the token should be updated to."
            }
        ]
    },
    {
        "path": "/v1/issuing/transactions",
        "verb": "get",
        "op_id": "GetIssuingTransactions",
        "summary": "List all transactions",
        "params": [
            {
                "name": "card",
                "description": "Only return transactions that belong to the given card."
            },
            {
                "name": "cardholder",
                "description": "Only return transactions that belong to the given cardholder."
            },
            {
                "name": "created",
                "description": "Only return transactions that were created during the given date interval."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "type",
                "description": "Only return transactions that have the given type. One of `capture` or `refund`."
            }
        ]
    },
    {
        "path": "/v1/issuing/transactions/{transaction}",
        "verb": "get",
        "op_id": "GetIssuingTransactionsTransaction",
        "summary": "Retrieve a transaction",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/issuing/transactions/{transaction}",
        "verb": "post",
        "op_id": "PostIssuingTransactionsTransaction",
        "summary": "Update a transaction",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            }
        ]
    },
    {
        "path": "/v1/link_account_sessions",
        "verb": "post",
        "op_id": "PostLinkAccountSessions",
        "summary": "Create a Session",
        "params": [
            {
                "name": "account_holder",
                "description": "The account holder to link accounts for."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "filters",
                "description": "Filters to restrict the kinds of accounts to collect."
            },
            {
                "name": "permissions",
                "description": "List of data features that you would like to request access to.\n\nPossible values are `balances`, `transactions`, `ownership`, and `payment_method`."
            },
            {
                "name": "prefetch",
                "description": "List of data features that you would like to retrieve upon account creation."
            },
            {
                "name": "return_url",
                "description": "For webview integrations only. Upon completing OAuth login in the native browser, the user will be redirected to this URL to return to your app."
            }
        ]
    },
    {
        "path": "/v1/link_account_sessions/{session}",
        "verb": "get",
        "op_id": "GetLinkAccountSessionsSession",
        "summary": "Retrieve a Session",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/linked_accounts",
        "verb": "get",
        "op_id": "GetLinkedAccounts",
        "summary": "List Accounts",
        "params": [
            {
                "name": "account_holder",
                "description": "If present, only return accounts that belong to the specified account holder. `account_holder[customer]` and `account_holder[account]` are mutually exclusive."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "session",
                "description": "If present, only return accounts that were collected as part of the given session."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/linked_accounts/{account}",
        "verb": "get",
        "op_id": "GetLinkedAccountsAccount",
        "summary": "Retrieve an Account",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/linked_accounts/{account}/disconnect",
        "verb": "post",
        "op_id": "PostLinkedAccountsAccountDisconnect",
        "summary": "Disconnect an Account",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/linked_accounts/{account}/owners",
        "verb": "get",
        "op_id": "GetLinkedAccountsAccountOwners",
        "summary": "List Account Owners",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "ownership",
                "description": "The ID of the ownership object to fetch owners from."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/linked_accounts/{account}/refresh",
        "verb": "post",
        "op_id": "PostLinkedAccountsAccountRefresh",
        "summary": "Refresh Account data",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "features",
                "description": "The list of account features that you would like to refresh."
            }
        ]
    },
    {
        "path": "/v1/mandates/{mandate}",
        "verb": "get",
        "op_id": "GetMandatesMandate",
        "summary": "Retrieve a Mandate",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/payment_intents",
        "verb": "get",
        "op_id": "GetPaymentIntents",
        "summary": "List all PaymentIntents",
        "params": [
            {
                "name": "created",
                "description": "A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp or a dictionary with a number of different query options."
            },
            {
                "name": "customer",
                "description": "Only return PaymentIntents for the customer that this customer ID specifies."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/payment_intents",
        "verb": "post",
        "op_id": "PostPaymentIntents",
        "summary": "Create a PaymentIntent",
        "params": [
            {
                "name": "amount",
                "description": "Amount intended to be collected by this PaymentIntent. A positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge \u00a5100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99)."
            },
            {
                "name": "application_fee_amount",
                "description": "The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total amount captured. For more information, see the PaymentIntents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts)."
            },
            {
                "name": "automatic_payment_methods",
                "description": "When you enable this parameter, this PaymentIntent accepts payment methods that you enable in the Dashboard and that are compatible with this PaymentIntent's other parameters."
            },
            {
                "name": "capture_method",
                "description": "Controls when the funds will be captured from the customer's account."
            },
            {
                "name": "confirm",
                "description": "Set to `true` to attempt to [confirm this PaymentIntent](https://stripe.com/docs/api/payment_intents/confirm) immediately. This parameter defaults to `false`. When creating and confirming a PaymentIntent at the same time, you can also provide the parameters available in the [Confirm API](https://stripe.com/docs/api/payment_intents/confirm)."
            },
            {
                "name": "confirmation_method",
                "description": "Describes whether we can confirm this PaymentIntent automatically, or if it requires customer action to confirm the payment."
            },
            {
                "name": "confirmation_token",
                "description": "ID of the ConfirmationToken used to confirm this PaymentIntent.\n\nIf the provided ConfirmationToken contains properties that are also being provided in this request, such as `payment_method`, then the values in this request will take precedence."
            },
            {
                "name": "currency",
                "description": "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "customer",
                "description": "ID of the Customer this PaymentIntent belongs to, if one exists.\n\nPayment methods attached to other Customers cannot be used with this PaymentIntent.\n\nIf [setup_future_usage](https://stripe.com/docs/api#payment_intent_object-setup_future_usage) is set and this PaymentIntent's payment method is not `card_present`, then the payment method attaches to the Customer after the PaymentIntent has been confirmed and any required actions from the user are complete. If the payment method is `card_present` and isn't a digital wallet, then a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card is created and attached to the Customer instead."
            },
            {
                "name": "description",
                "description": "An arbitrary string attached to the object. Often useful for displaying to users."
            },
            {
                "name": "error_on_requires_action",
                "description": "Set to `true` to fail the payment attempt if the PaymentIntent transitions into `requires_action`. Use this parameter for simpler integrations that don't handle customer actions, such as [saving cards without authentication](https://stripe.com/docs/payments/save-card-without-authentication). This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm)."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "mandate",
                "description": "ID of the mandate that's used for this payment. This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm)."
            },
            {
                "name": "mandate_data",
                "description": "This hash contains details about the Mandate to create. This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm)."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "off_session",
                "description": "Set to `true` to indicate that the customer isn't in your checkout flow during this payment attempt and can't authenticate. Use this parameter in scenarios where you collect card details and [charge them later](https://stripe.com/docs/payments/cards/charging-saved-cards). This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm)."
            },
            {
                "name": "on_behalf_of",
                "description": "The Stripe account ID that these funds are intended for. Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts)."
            },
            {
                "name": "payment_method",
                "description": "ID of the payment method (a PaymentMethod, Card, or [compatible Source](https://stripe.com/docs/payments/payment-methods/transitioning#compatibility) object) to attach to this PaymentIntent.\n\nIf you omit this parameter with `confirm=true`, `customer.default_source` attaches as this PaymentIntent's payment instrument to improve migration for users of the Charges API. We recommend that you explicitly provide the `payment_method` moving forward.\nIf the payment method is attached to a Customer, you must also provide the ID of that Customer as the [customer](https://stripe.com/docs/api#create_payment_intent-customer) parameter of this PaymentIntent."
            },
            {
                "name": "payment_method_configuration",
                "description": "The ID of the [payment method configuration](https://stripe.com/docs/api/payment_method_configurations) to use with this PaymentIntent."
            },
            {
                "name": "payment_method_data",
                "description": "If provided, this hash will be used to create a PaymentMethod. The new PaymentMethod will appear\nin the [payment_method](https://stripe.com/docs/api/payment_intents/object#payment_intent_object-payment_method)\nproperty on the PaymentIntent."
            },
            {
                "name": "payment_method_options",
                "description": "Payment method-specific configuration for this PaymentIntent."
            },
            {
                "name": "payment_method_types",
                "description": "The list of payment method types (for example, a card) that this PaymentIntent can use. If you don't provide this, Stripe will dynamically show relevant payment methods from your [payment method settings](https://dashboard.stripe.com/settings/payment_methods)."
            },
            {
                "name": "radar_options",
                "description": "Options to configure Radar. Learn more about [Radar Sessions](https://stripe.com/docs/radar/radar-session)."
            },
            {
                "name": "receipt_email",
                "description": "Email address to send the receipt to. If you specify `receipt_email` for a payment in live mode, you send a receipt regardless of your [email settings](https://dashboard.stripe.com/account/emails)."
            },
            {
                "name": "return_url",
                "description": "The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method's app or site. If you'd prefer to redirect to a mobile application, you can alternatively supply an application URI scheme. This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm)."
            },
            {
                "name": "setup_future_usage",
                "description": "Indicates that you intend to make future payments with this PaymentIntent's payment method.\n\nIf you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](/api/payment_methods/attach) the payment method to a Customer after the transaction completes.\n\nIf the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.\n\nWhen processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](/strong-customer-authentication)."
            },
            {
                "name": "shipping",
                "description": "Shipping information for this PaymentIntent."
            },
            {
                "name": "statement_descriptor",
                "description": "Text that appears on the customer's statement as the statement descriptor for a non-card charge. This value overrides the account's default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).\n\nSetting this value for a card charge returns an error. For card charges, set the [statement_descriptor_suffix](https://docs.stripe.com/get-started/account/statement-descriptors#dynamic) instead."
            },
            {
                "name": "statement_descriptor_suffix",
                "description": "Provides information about a card charge. Concatenated to the account's [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors#static) to form the complete statement descriptor that appears on the customer's statement."
            },
            {
                "name": "transfer_data",
                "description": "The parameters that you can use to automatically create a Transfer.\nLearn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts)."
            },
            {
                "name": "transfer_group",
                "description": "A string that identifies the resulting payment as part of a group. Learn more about the [use case for connected accounts](https://stripe.com/docs/connect/separate-charges-and-transfers)."
            },
            {
                "name": "use_stripe_sdk",
                "description": "Set to `true` when confirming server-side and using Stripe.js, iOS, or Android client-side SDKs to handle the next actions."
            }
        ]
    },
    {
        "path": "/v1/payment_intents/search",
        "verb": "get",
        "op_id": "GetPaymentIntentsSearch",
        "summary": "Search PaymentIntents",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "page",
                "description": "A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results."
            },
            {
                "name": "query",
                "description": "The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for payment intents](https://stripe.com/docs/search#query-fields-for-payment-intents)."
            }
        ]
    },
    {
        "path": "/v1/payment_intents/{intent}",
        "verb": "get",
        "op_id": "GetPaymentIntentsIntent",
        "summary": "Retrieve a PaymentIntent",
        "params": [
            {
                "name": "client_secret",
                "description": "The client secret of the PaymentIntent. We require it if you use a publishable key to retrieve the source."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/payment_intents/{intent}",
        "verb": "post",
        "op_id": "PostPaymentIntentsIntent",
        "summary": "Update a PaymentIntent",
        "params": [
            {
                "name": "amount",
                "description": "Amount intended to be collected by this PaymentIntent. A positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge \u00a5100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99)."
            },
            {
                "name": "application_fee_amount",
                "description": "The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total amount captured. For more information, see the PaymentIntents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts)."
            },
            {
                "name": "capture_method",
                "description": "Controls when the funds will be captured from the customer's account."
            },
            {
                "name": "currency",
                "description": "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "customer",
                "description": "ID of the Customer this PaymentIntent belongs to, if one exists.\n\nPayment methods attached to other Customers cannot be used with this PaymentIntent.\n\nIf [setup_future_usage](https://stripe.com/docs/api#payment_intent_object-setup_future_usage) is set and this PaymentIntent's payment method is not `card_present`, then the payment method attaches to the Customer after the PaymentIntent has been confirmed and any required actions from the user are complete. If the payment method is `card_present` and isn't a digital wallet, then a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card is created and attached to the Customer instead."
            },
            {
                "name": "description",
                "description": "An arbitrary string attached to the object. Often useful for displaying to users."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "payment_method",
                "description": "ID of the payment method (a PaymentMethod, Card, or [compatible Source](https://stripe.com/docs/payments/payment-methods/transitioning#compatibility) object) to attach to this PaymentIntent. To unset this field to null, pass in an empty string."
            },
            {
                "name": "payment_method_configuration",
                "description": "The ID of the [payment method configuration](https://stripe.com/docs/api/payment_method_configurations) to use with this PaymentIntent."
            },
            {
                "name": "payment_method_data",
                "description": "If provided, this hash will be used to create a PaymentMethod. The new PaymentMethod will appear\nin the [payment_method](https://stripe.com/docs/api/payment_intents/object#payment_intent_object-payment_method)\nproperty on the PaymentIntent."
            },
            {
                "name": "payment_method_options",
                "description": "Payment-method-specific configuration for this PaymentIntent."
            },
            {
                "name": "payment_method_types",
                "description": "The list of payment method types (for example, card) that this PaymentIntent can use. Use `automatic_payment_methods` to manage payment methods from the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)."
            },
            {
                "name": "receipt_email",
                "description": "Email address that the receipt for the resulting payment will be sent to. If `receipt_email` is specified for a payment in live mode, a receipt will be sent regardless of your [email settings](https://dashboard.stripe.com/account/emails)."
            },
            {
                "name": "setup_future_usage",
                "description": "Indicates that you intend to make future payments with this PaymentIntent's payment method.\n\nIf you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](/api/payment_methods/attach) the payment method to a Customer after the transaction completes.\n\nIf the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.\n\nWhen processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](/strong-customer-authentication).\n\nIf you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`."
            },
            {
                "name": "shipping",
                "description": "Shipping information for this PaymentIntent."
            },
            {
                "name": "statement_descriptor",
                "description": "Text that appears on the customer's statement as the statement descriptor for a non-card charge. This value overrides the account's default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).\n\nSetting this value for a card charge returns an error. For card charges, set the [statement_descriptor_suffix](https://docs.stripe.com/get-started/account/statement-descriptors#dynamic) instead."
            },
            {
                "name": "statement_descriptor_suffix",
                "description": "Provides information about a card charge. Concatenated to the account's [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors#static) to form the complete statement descriptor that appears on the customer's statement."
            },
            {
                "name": "transfer_data",
                "description": "Use this parameter to automatically create a Transfer when the payment succeeds. Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts)."
            },
            {
                "name": "transfer_group",
                "description": "A string that identifies the resulting payment as part of a group. You can only provide `transfer_group` if it hasn't been set. Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts)."
            }
        ]
    },
    {
        "path": "/v1/payment_intents/{intent}/apply_customer_balance",
        "verb": "post",
        "op_id": "PostPaymentIntentsIntentApplyCustomerBalance",
        "summary": "Reconcile a customer_balance PaymentIntent",
        "params": [
            {
                "name": "amount",
                "description": "Amount that you intend to apply to this PaymentIntent from the customer\u2019s cash balance. If the PaymentIntent was created by an Invoice, the full amount of the PaymentIntent is applied regardless of this parameter.\n\nA positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (for example, 100 cents to charge 1 USD or 100 to charge 100 JPY, a zero-decimal currency). The maximum amount is the amount of the PaymentIntent.\n\nWhen you omit the amount, it defaults to the remaining amount requested on the PaymentIntent."
            },
            {
                "name": "currency",
                "description": "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/payment_intents/{intent}/cancel",
        "verb": "post",
        "op_id": "PostPaymentIntentsIntentCancel",
        "summary": "Cancel a PaymentIntent",
        "params": [
            {
                "name": "cancellation_reason",
                "description": "Reason for canceling this PaymentIntent. Possible values are: `duplicate`, `fraudulent`, `requested_by_customer`, or `abandoned`"
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/payment_intents/{intent}/capture",
        "verb": "post",
        "op_id": "PostPaymentIntentsIntentCapture",
        "summary": "Capture a PaymentIntent",
        "params": [
            {
                "name": "amount_to_capture",
                "description": "The amount to capture from the PaymentIntent, which must be less than or equal to the original amount. Defaults to the full `amount_capturable` if it's not provided."
            },
            {
                "name": "application_fee_amount",
                "description": "The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total amount captured. For more information, see the PaymentIntents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts)."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "final_capture",
                "description": "Defaults to `true`. When capturing a PaymentIntent, setting `final_capture` to `false` notifies Stripe to not release the remaining uncaptured funds to make sure that they're captured in future requests. You can only use this setting when [multicapture](https://stripe.com/docs/payments/multicapture) is available for PaymentIntents."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "statement_descriptor",
                "description": "Text that appears on the customer's statement as the statement descriptor for a non-card charge. This value overrides the account's default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).\n\nSetting this value for a card charge returns an error. For card charges, set the [statement_descriptor_suffix](https://docs.stripe.com/get-started/account/statement-descriptors#dynamic) instead."
            },
            {
                "name": "statement_descriptor_suffix",
                "description": "Provides information about a card charge. Concatenated to the account's [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors#static) to form the complete statement descriptor that appears on the customer's statement."
            },
            {
                "name": "transfer_data",
                "description": "The parameters that you can use to automatically create a transfer after the payment\nis captured. Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts)."
            }
        ]
    },
    {
        "path": "/v1/payment_intents/{intent}/confirm",
        "verb": "post",
        "op_id": "PostPaymentIntentsIntentConfirm",
        "summary": "Confirm a PaymentIntent",
        "params": [
            {
                "name": "capture_method",
                "description": "Controls when the funds will be captured from the customer's account."
            },
            {
                "name": "client_secret",
                "description": "The client secret of the PaymentIntent."
            },
            {
                "name": "confirmation_token",
                "description": "ID of the ConfirmationToken used to confirm this PaymentIntent.\n\nIf the provided ConfirmationToken contains properties that are also being provided in this request, such as `payment_method`, then the values in this request will take precedence."
            },
            {
                "name": "error_on_requires_action",
                "description": "Set to `true` to fail the payment attempt if the PaymentIntent transitions into `requires_action`. This parameter is intended for simpler integrations that do not handle customer actions, like [saving cards without authentication](https://stripe.com/docs/payments/save-card-without-authentication)."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "mandate",
                "description": "ID of the mandate that's used for this payment."
            },
            {
                "name": "mandate_data",
                "description": ""
            },
            {
                "name": "off_session",
                "description": "Set to `true` to indicate that the customer isn't in your checkout flow during this payment attempt and can't authenticate. Use this parameter in scenarios where you collect card details and [charge them later](https://stripe.com/docs/payments/cards/charging-saved-cards)."
            },
            {
                "name": "payment_method",
                "description": "ID of the payment method (a PaymentMethod, Card, or [compatible Source](https://stripe.com/docs/payments/payment-methods/transitioning#compatibility) object) to attach to this PaymentIntent.\nIf the payment method is attached to a Customer, it must match the [customer](https://stripe.com/docs/api#create_payment_intent-customer) that is set on this PaymentIntent."
            },
            {
                "name": "payment_method_data",
                "description": "If provided, this hash will be used to create a PaymentMethod. The new PaymentMethod will appear\nin the [payment_method](https://stripe.com/docs/api/payment_intents/object#payment_intent_object-payment_method)\nproperty on the PaymentIntent."
            },
            {
                "name": "payment_method_options",
                "description": "Payment method-specific configuration for this PaymentIntent."
            },
            {
                "name": "payment_method_types",
                "description": "The list of payment method types (for example, a card) that this PaymentIntent can use. Use `automatic_payment_methods` to manage payment methods from the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods)."
            },
            {
                "name": "radar_options",
                "description": "Options to configure Radar. Learn more about [Radar Sessions](https://stripe.com/docs/radar/radar-session)."
            },
            {
                "name": "receipt_email",
                "description": "Email address that the receipt for the resulting payment will be sent to. If `receipt_email` is specified for a payment in live mode, a receipt will be sent regardless of your [email settings](https://dashboard.stripe.com/account/emails)."
            },
            {
                "name": "return_url",
                "description": "The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method's app or site.\nIf you'd prefer to redirect to a mobile application, you can alternatively supply an application URI scheme.\nThis parameter is only used for cards and other redirect-based payment methods."
            },
            {
                "name": "setup_future_usage",
                "description": "Indicates that you intend to make future payments with this PaymentIntent's payment method.\n\nIf you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](/api/payment_methods/attach) the payment method to a Customer after the transaction completes.\n\nIf the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.\n\nWhen processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](/strong-customer-authentication).\n\nIf you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`."
            },
            {
                "name": "shipping",
                "description": "Shipping information for this PaymentIntent."
            },
            {
                "name": "use_stripe_sdk",
                "description": "Set to `true` when confirming server-side and using Stripe.js, iOS, or Android client-side SDKs to handle the next actions."
            }
        ]
    },
    {
        "path": "/v1/payment_intents/{intent}/increment_authorization",
        "verb": "post",
        "op_id": "PostPaymentIntentsIntentIncrementAuthorization",
        "summary": "Increment an authorization",
        "params": [
            {
                "name": "amount",
                "description": "The updated total amount that you intend to collect from the cardholder. This amount must be greater than the currently authorized amount."
            },
            {
                "name": "application_fee_amount",
                "description": "The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total amount captured. For more information, see the PaymentIntents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts)."
            },
            {
                "name": "description",
                "description": "An arbitrary string attached to the object. Often useful for displaying to users."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "statement_descriptor",
                "description": "Text that appears on the customer's statement as the statement descriptor for a non-card or card charge. This value overrides the account's default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors)."
            },
            {
                "name": "transfer_data",
                "description": "The parameters used to automatically create a transfer after the payment is captured.\nLearn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts)."
            }
        ]
    },
    {
        "path": "/v1/payment_intents/{intent}/verify_microdeposits",
        "verb": "post",
        "op_id": "PostPaymentIntentsIntentVerifyMicrodeposits",
        "summary": "Verify microdeposits on a PaymentIntent",
        "params": [
            {
                "name": "amounts",
                "description": "Two positive integers, in *cents*, equal to the values of the microdeposits sent to the bank account."
            },
            {
                "name": "client_secret",
                "description": "The client secret of the PaymentIntent."
            },
            {
                "name": "descriptor_code",
                "description": "A six-character code starting with SM present in the microdeposit sent to the bank account."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/payment_links",
        "verb": "get",
        "op_id": "GetPaymentLinks",
        "summary": "List all payment links",
        "params": [
            {
                "name": "active",
                "description": "Only return payment links that are active or inactive (e.g., pass `false` to list all inactive payment links)."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/payment_links",
        "verb": "post",
        "op_id": "PostPaymentLinks",
        "summary": "Create a payment link",
        "params": [
            {
                "name": "after_completion",
                "description": "Behavior after the purchase is complete."
            },
            {
                "name": "allow_promotion_codes",
                "description": "Enables user redeemable promotion codes."
            },
            {
                "name": "application_fee_amount",
                "description": "The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. Can only be applied when there are no line items with recurring prices."
            },
            {
                "name": "application_fee_percent",
                "description": "A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. There must be at least 1 line item with a recurring price to use this field."
            },
            {
                "name": "automatic_tax",
                "description": "Configuration for automatic tax collection."
            },
            {
                "name": "billing_address_collection",
                "description": "Configuration for collecting the customer's billing address. Defaults to `auto`."
            },
            {
                "name": "consent_collection",
                "description": "Configure fields to gather active consent from customers."
            },
            {
                "name": "currency",
                "description": "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies) and supported by each line item's price."
            },
            {
                "name": "custom_fields",
                "description": "Collect additional information from your customer using custom fields. Up to 3 fields are supported."
            },
            {
                "name": "custom_text",
                "description": "Display additional text for your customers using custom text."
            },
            {
                "name": "customer_creation",
                "description": "Configures whether [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link create a [Customer](https://stripe.com/docs/api/customers)."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "inactive_message",
                "description": "The custom message to be displayed to a customer when a payment link is no longer active."
            },
            {
                "name": "invoice_creation",
                "description": "Generate a post-purchase Invoice for one-time payments."
            },
            {
                "name": "line_items",
                "description": "The line items representing what is being sold. Each line item represents an item being sold. Up to 20 line items are supported."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. Metadata associated with this Payment Link will automatically be copied to [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link."
            },
            {
                "name": "on_behalf_of",
                "description": "The account on behalf of which to charge."
            },
            {
                "name": "optional_items",
                "description": "A list of optional items the customer can add to their order at checkout. Use this parameter to pass one-time or recurring [Prices](https://stripe.com/docs/api/prices).\nThere is a maximum of 10 optional items allowed on a payment link, and the existing limits on the number of line items allowed on a payment link apply to the combined number of line items and optional items.\nThere is a maximum of 20 combined line items and optional items."
            },
            {
                "name": "payment_intent_data",
                "description": "A subset of parameters to be passed to PaymentIntent creation for Checkout Sessions in `payment` mode."
            },
            {
                "name": "payment_method_collection",
                "description": "Specify whether Checkout should collect a payment method. When set to `if_required`, Checkout will not collect a payment method when the total due for the session is 0.This may occur if the Checkout Session includes a free trial or a discount.\n\nCan only be set in `subscription` mode. Defaults to `always`.\n\nIf you'd like information on how to collect a payment method outside of Checkout, read the guide on [configuring subscriptions with a free trial](https://stripe.com/docs/payments/checkout/free-trials)."
            },
            {
                "name": "payment_method_types",
                "description": "The list of payment method types that customers can use. If no value is passed, Stripe will dynamically show relevant payment methods from your [payment method settings](https://dashboard.stripe.com/settings/payment_methods) (20+ payment methods [supported](https://stripe.com/docs/payments/payment-methods/integration-options#payment-method-product-support))."
            },
            {
                "name": "phone_number_collection",
                "description": "Controls phone number collection settings during checkout.\n\nWe recommend that you review your privacy policy and check with your legal contacts."
            },
            {
                "name": "restrictions",
                "description": "Settings that restrict the usage of a payment link."
            },
            {
                "name": "shipping_address_collection",
                "description": "Configuration for collecting the customer's shipping address."
            },
            {
                "name": "shipping_options",
                "description": "The shipping rate options to apply to [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link."
            },
            {
                "name": "submit_type",
                "description": "Describes the type of transaction being performed in order to customize relevant text on the page, such as the submit button. Changing this value will also affect the hostname in the [url](https://stripe.com/docs/api/payment_links/payment_links/object#url) property (example: `donate.stripe.com`)."
            },
            {
                "name": "subscription_data",
                "description": "When creating a subscription, the specified configuration data will be used. There must be at least one line item with a recurring price to use `subscription_data`."
            },
            {
                "name": "tax_id_collection",
                "description": "Controls tax ID collection during checkout."
            },
            {
                "name": "transfer_data",
                "description": "The account (if any) the payments will be attributed to for tax reporting, and where funds from each payment will be transferred to."
            }
        ]
    },
    {
        "path": "/v1/payment_links/{payment_link}",
        "verb": "get",
        "op_id": "GetPaymentLinksPaymentLink",
        "summary": "Retrieve payment link",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/payment_links/{payment_link}",
        "verb": "post",
        "op_id": "PostPaymentLinksPaymentLink",
        "summary": "Update a payment link",
        "params": [
            {
                "name": "active",
                "description": "Whether the payment link's `url` is active. If `false`, customers visiting the URL will be shown a page saying that the link has been deactivated."
            },
            {
                "name": "after_completion",
                "description": "Behavior after the purchase is complete."
            },
            {
                "name": "allow_promotion_codes",
                "description": "Enables user redeemable promotion codes."
            },
            {
                "name": "automatic_tax",
                "description": "Configuration for automatic tax collection."
            },
            {
                "name": "billing_address_collection",
                "description": "Configuration for collecting the customer's billing address. Defaults to `auto`."
            },
            {
                "name": "custom_fields",
                "description": "Collect additional information from your customer using custom fields. Up to 3 fields are supported."
            },
            {
                "name": "custom_text",
                "description": "Display additional text for your customers using custom text."
            },
            {
                "name": "customer_creation",
                "description": "Configures whether [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link create a [Customer](https://stripe.com/docs/api/customers)."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "inactive_message",
                "description": "The custom message to be displayed to a customer when a payment link is no longer active."
            },
            {
                "name": "invoice_creation",
                "description": "Generate a post-purchase Invoice for one-time payments."
            },
            {
                "name": "line_items",
                "description": "The line items representing what is being sold. Each line item represents an item being sold. Up to 20 line items are supported."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. Metadata associated with this Payment Link will automatically be copied to [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link."
            },
            {
                "name": "payment_intent_data",
                "description": "A subset of parameters to be passed to PaymentIntent creation for Checkout Sessions in `payment` mode."
            },
            {
                "name": "payment_method_collection",
                "description": "Specify whether Checkout should collect a payment method. When set to `if_required`, Checkout will not collect a payment method when the total due for the session is 0.This may occur if the Checkout Session includes a free trial or a discount.\n\nCan only be set in `subscription` mode. Defaults to `always`.\n\nIf you'd like information on how to collect a payment method outside of Checkout, read the guide on [configuring subscriptions with a free trial](https://stripe.com/docs/payments/checkout/free-trials)."
            },
            {
                "name": "payment_method_types",
                "description": "The list of payment method types that customers can use. Pass an empty string to enable dynamic payment methods that use your [payment method settings](https://dashboard.stripe.com/settings/payment_methods)."
            },
            {
                "name": "phone_number_collection",
                "description": "Controls phone number collection settings during checkout.\n\nWe recommend that you review your privacy policy and check with your legal contacts."
            },
            {
                "name": "restrictions",
                "description": "Settings that restrict the usage of a payment link."
            },
            {
                "name": "shipping_address_collection",
                "description": "Configuration for collecting the customer's shipping address."
            },
            {
                "name": "submit_type",
                "description": "Describes the type of transaction being performed in order to customize relevant text on the page, such as the submit button. Changing this value will also affect the hostname in the [url](https://stripe.com/docs/api/payment_links/payment_links/object#url) property (example: `donate.stripe.com`)."
            },
            {
                "name": "subscription_data",
                "description": "When creating a subscription, the specified configuration data will be used. There must be at least one line item with a recurring price to use `subscription_data`."
            },
            {
                "name": "tax_id_collection",
                "description": "Controls tax ID collection during checkout."
            }
        ]
    },
    {
        "path": "/v1/payment_links/{payment_link}/line_items",
        "verb": "get",
        "op_id": "GetPaymentLinksPaymentLinkLineItems",
        "summary": "Retrieve a payment link's line items",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/payment_method_configurations",
        "verb": "get",
        "op_id": "GetPaymentMethodConfigurations",
        "summary": "List payment method configurations",
        "params": [
            {
                "name": "application",
                "description": "The Connect application to filter by."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/payment_method_configurations",
        "verb": "post",
        "op_id": "PostPaymentMethodConfigurations",
        "summary": "Create a payment method configuration",
        "params": [
            {
                "name": "acss_debit",
                "description": "Canadian pre-authorized debit payments, check this [page](https://stripe.com/docs/payments/acss-debit) for more details like country availability."
            },
            {
                "name": "affirm",
                "description": "[Affirm](https://www.affirm.com/) gives your customers a way to split purchases over a series of payments. Depending on the purchase, they can pay with four interest-free payments (Split Pay) or pay over a longer term (Installments), which might include interest. Check this [page](https://stripe.com/docs/payments/affirm) for more details like country availability."
            },
            {
                "name": "afterpay_clearpay",
                "description": "Afterpay gives your customers a way to pay for purchases in installments, check this [page](https://stripe.com/docs/payments/afterpay-clearpay) for more details like country availability. Afterpay is particularly popular among businesses selling fashion, beauty, and sports products."
            },
            {
                "name": "alipay",
                "description": "Alipay is a digital wallet in China that has more than a billion active users worldwide. Alipay users can pay on the web or on a mobile device using login credentials or their Alipay app. Alipay has a low dispute rate and reduces fraud by authenticating payments using the customer's login credentials. Check this [page](https://stripe.com/docs/payments/alipay) for more details."
            },
            {
                "name": "alma",
                "description": "Alma is a Buy Now, Pay Later payment method that offers customers the ability to pay in 2, 3, or 4 installments."
            },
            {
                "name": "amazon_pay",
                "description": "Amazon Pay is a wallet payment method that lets your customers check out the same way as on Amazon."
            },
            {
                "name": "apple_pay",
                "description": "Stripe users can accept [Apple Pay](https://stripe.com/payments/apple-pay) in iOS applications in iOS 9 and later, and on the web in Safari starting with iOS 10 or macOS Sierra. There are no additional fees to process Apple Pay payments, and the [pricing](https://stripe.com/pricing) is the same as other card transactions. Check this [page](https://stripe.com/docs/apple-pay) for more details."
            },
            {
                "name": "apple_pay_later",
                "description": "Apple Pay Later, a payment method for customers to buy now and pay later, gives your customers a way to split purchases into four installments across six weeks."
            },
            {
                "name": "au_becs_debit",
                "description": "Stripe users in Australia can accept Bulk Electronic Clearing System (BECS) direct debit payments from customers with an Australian bank account. Check this [page](https://stripe.com/docs/payments/au-becs-debit) for more details."
            },
            {
                "name": "bacs_debit",
                "description": "Stripe users in the UK can accept Bacs Direct Debit payments from customers with a UK bank account, check this [page](https://stripe.com/docs/payments/payment-methods/bacs-debit) for more details."
            },
            {
                "name": "bancontact",
                "description": "Bancontact is the most popular online payment method in Belgium, with over 15 million cards in circulation. [Customers](https://stripe.com/docs/api/customers) use a Bancontact card or mobile app linked to a Belgian bank account to make online payments that are secure, guaranteed, and confirmed immediately. Check this [page](https://stripe.com/docs/payments/bancontact) for more details."
            },
            {
                "name": "billie",
                "description": "Billie is a [single-use](https://docs.stripe.com/payments/payment-methods#usage) payment method that offers businesses Pay by Invoice where they offer payment terms ranging from 7-120 days. Customers are redirected from your website or app, authorize the payment with Billie, then return to your website or app. You get [immediate notification](/payments/payment-methods#payment-notification) of whether the payment succeeded or failed."
            },
            {
                "name": "blik",
                "description": "BLIK is a [single use](https://stripe.com/docs/payments/payment-methods#usage) payment method that requires customers to authenticate their payments. When customers want to pay online using BLIK, they request a six-digit code from their banking application and enter it into the payment collection form. Check this [page](https://stripe.com/docs/payments/blik) for more details."
            },
            {
                "name": "boleto",
                "description": "Boleto is an official (regulated by the Central Bank of Brazil) payment method in Brazil. Check this [page](https://stripe.com/docs/payments/boleto) for more details."
            },
            {
                "name": "card",
                "description": "Cards are a popular way for consumers and businesses to pay online or in person. Stripe supports global and local card networks."
            },
            {
                "name": "cartes_bancaires",
                "description": "Cartes Bancaires is France's local card network. More than 95% of these cards are co-branded with either Visa or Mastercard, meaning you can process these cards over either Cartes Bancaires or the Visa or Mastercard networks. Check this [page](https://stripe.com/docs/payments/cartes-bancaires) for more details."
            },
            {
                "name": "cashapp",
                "description": "Cash App is a popular consumer app in the US that allows customers to bank, invest, send, and receive money using their digital wallet. Check this [page](https://stripe.com/docs/payments/cash-app-pay) for more details."
            },
            {
                "name": "customer_balance",
                "description": "Uses a customer\u2019s [cash balance](https://stripe.com/docs/payments/customer-balance) for the payment. The cash balance can be funded via a bank transfer. Check this [page](https://stripe.com/docs/payments/bank-transfers) for more details."
            },
            {
                "name": "eps",
                "description": "EPS is an Austria-based payment method that allows customers to complete transactions online using their bank credentials. EPS is supported by all Austrian banks and is accepted by over 80% of Austrian online retailers. Check this [page](https://stripe.com/docs/payments/eps) for more details."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "fpx",
                "description": "Financial Process Exchange (FPX) is a Malaysia-based payment method that allows customers to complete transactions online using their bank credentials. Bank Negara Malaysia (BNM), the Central Bank of Malaysia, and eleven other major Malaysian financial institutions are members of the PayNet Group, which owns and operates FPX. It is one of the most popular online payment methods in Malaysia, with nearly 90 million transactions in 2018 according to BNM. Check this [page](https://stripe.com/docs/payments/fpx) for more details."
            },
            {
                "name": "giropay",
                "description": "giropay is a German payment method based on online banking, introduced in 2006. It allows customers to complete transactions online using their online banking environment, with funds debited from their bank account. Depending on their bank, customers confirm payments on giropay using a second factor of authentication or a PIN. giropay accounts for 10% of online checkouts in Germany. Check this [page](https://stripe.com/docs/payments/giropay) for more details."
            },
            {
                "name": "google_pay",
                "description": "Google Pay allows customers to make payments in your app or website using any credit or debit card saved to their Google Account, including those from Google Play, YouTube, Chrome, or an Android device. Use the Google Pay API to request any credit or debit card stored in your customer's Google account. Check this [page](https://stripe.com/docs/google-pay) for more details."
            },
            {
                "name": "grabpay",
                "description": "GrabPay is a payment method developed by [Grab](https://www.grab.com/sg/consumer/finance/pay/). GrabPay is a digital wallet - customers maintain a balance in their wallets that they pay out with. Check this [page](https://stripe.com/docs/payments/grabpay) for more details."
            },
            {
                "name": "ideal",
                "description": "iDEAL is a Netherlands-based payment method that allows customers to complete transactions online using their bank credentials. All major Dutch banks are members of Currence, the scheme that operates iDEAL, making it the most popular online payment method in the Netherlands with a share of online transactions close to 55%. Check this [page](https://stripe.com/docs/payments/ideal) for more details."
            },
            {
                "name": "jcb",
                "description": "JCB is a credit card company based in Japan. JCB is currently available in Japan to businesses approved by JCB, and available to all businesses in Australia, Canada, Hong Kong, Japan, New Zealand, Singapore, Switzerland, United Kingdom, United States, and all countries in the European Economic Area except Iceland. Check this [page](https://support.stripe.com/questions/accepting-japan-credit-bureau-%28jcb%29-payments) for more details."
            },
            {
                "name": "kakao_pay",
                "description": "Kakao Pay is a popular local wallet available in South Korea."
            },
            {
                "name": "klarna",
                "description": "Klarna gives customers a range of [payment options](https://stripe.com/docs/payments/klarna#payment-options) during checkout. Available payment options vary depending on the customer's billing address and the transaction amount. These payment options make it convenient for customers to purchase items in all price ranges. Check this [page](https://stripe.com/docs/payments/klarna) for more details."
            },
            {
                "name": "konbini",
                "description": "Konbini allows customers in Japan to pay for bills and online purchases at convenience stores with cash. Check this [page](https://stripe.com/docs/payments/konbini) for more details."
            },
            {
                "name": "kr_card",
                "description": "Korean cards let users pay using locally issued cards from South Korea."
            },
            {
                "name": "link",
                "description": "[Link](https://stripe.com/docs/payments/link) is a payment method network. With Link, users save their payment details once, then reuse that information to pay with one click for any business on the network."
            },
            {
                "name": "mobilepay",
                "description": "MobilePay is a [single-use](https://stripe.com/docs/payments/payment-methods#usage) card wallet payment method used in Denmark and Finland. It allows customers to [authenticate and approve](https://stripe.com/docs/payments/payment-methods#customer-actions) payments using the MobilePay app. Check this [page](https://stripe.com/docs/payments/mobilepay) for more details."
            },
            {
                "name": "multibanco",
                "description": "Stripe users in Europe and the United States can accept Multibanco payments from customers in Portugal using [Sources](https://stripe.com/docs/sources)\u2014a single integration path for creating payments using any supported method."
            },
            {
                "name": "name",
                "description": "Configuration name."
            },
            {
                "name": "naver_pay",
                "description": "Naver Pay is a popular local wallet available in South Korea."
            },
            {
                "name": "nz_bank_account",
                "description": "Stripe users in New Zealand can accept Bulk Electronic Clearing System (BECS) direct debit payments from customers with a New Zeland bank account. Check this [page](https://stripe.com/docs/payments/nz-bank-account) for more details."
            },
            {
                "name": "oxxo",
                "description": "OXXO is a Mexican chain of convenience stores with thousands of locations across Latin America and represents nearly 20% of online transactions in Mexico. OXXO allows customers to pay bills and online purchases in-store with cash. Check this [page](https://stripe.com/docs/payments/oxxo) for more details."
            },
            {
                "name": "p24",
                "description": "Przelewy24 is a Poland-based payment method aggregator that allows customers to complete transactions online using bank transfers and other methods. Bank transfers account for 30% of online payments in Poland and Przelewy24 provides a way for customers to pay with over 165 banks. Check this [page](https://stripe.com/docs/payments/p24) for more details."
            },
            {
                "name": "parent",
                "description": "Configuration's parent configuration. Specify to create a child configuration."
            },
            {
                "name": "pay_by_bank",
                "description": "Pay by bank is a redirect payment method backed by bank transfers. A customer is redirected to their bank to authorize a bank transfer for a given amount. This removes a lot of the error risks inherent in waiting for the customer to initiate a transfer themselves, and is less expensive than card payments."
            },
            {
                "name": "payco",
                "description": "PAYCO is a [single-use](https://docs.stripe.com/payments/payment-methods#usage local wallet available in South Korea."
            },
            {
                "name": "paynow",
                "description": "PayNow is a Singapore-based payment method that allows customers to make a payment using their preferred app from participating banks and participating non-bank financial institutions. Check this [page](https://stripe.com/docs/payments/paynow) for more details."
            },
            {
                "name": "paypal",
                "description": "PayPal, a digital wallet popular with customers in Europe, allows your customers worldwide to pay using their PayPal account. Check this [page](https://stripe.com/docs/payments/paypal) for more details."
            },
            {
                "name": "pix",
                "description": "Pix is a payment method popular in Brazil. When paying with Pix, customers authenticate and approve payments by scanning a QR code in their preferred banking app. Check this [page](https://docs.stripe.com/payments/pix) for more details."
            },
            {
                "name": "promptpay",
                "description": "PromptPay is a Thailand-based payment method that allows customers to make a payment using their preferred app from participating banks. Check this [page](https://stripe.com/docs/payments/promptpay) for more details."
            },
            {
                "name": "revolut_pay",
                "description": "Revolut Pay, developed by Revolut, a global finance app, is a digital wallet payment method. Revolut Pay uses the customer\u2019s stored balance or cards to fund the payment, and offers the option for non-Revolut customers to save their details after their first purchase."
            },
            {
                "name": "samsung_pay",
                "description": "Samsung Pay is a [single-use](https://docs.stripe.com/payments/payment-methods#usage local wallet available in South Korea."
            },
            {
                "name": "satispay",
                "description": "Satispay is a [single-use](https://docs.stripe.com/payments/payment-methods#usage) payment method where customers are required to [authenticate](/payments/payment-methods#customer-actions) their payment. Customers pay by being redirected from your website or app, authorizing the payment with Satispay, then returning to your website or app. You get [immediate notification](/payments/payment-methods#payment-notification) of whether the payment succeeded or failed."
            },
            {
                "name": "sepa_debit",
                "description": "The [Single Euro Payments Area (SEPA)](https://en.wikipedia.org/wiki/Single_Euro_Payments_Area) is an initiative of the European Union to simplify payments within and across member countries. SEPA established and enforced banking standards to allow for the direct debiting of every EUR-denominated bank account within the SEPA region, check this [page](https://stripe.com/docs/payments/sepa-debit) for more details."
            },
            {
                "name": "sofort",
                "description": "Stripe users in Europe and the United States can use the [Payment Intents API](https://stripe.com/docs/payments/payment-intents)\u2014a single integration path for creating payments using any supported method\u2014to accept [Sofort](https://www.sofort.com/) payments from customers. Check this [page](https://stripe.com/docs/payments/sofort) for more details."
            },
            {
                "name": "swish",
                "description": "Swish is a [real-time](https://stripe.com/docs/payments/real-time) payment method popular in Sweden. It allows customers to [authenticate and approve](https://stripe.com/docs/payments/payment-methods#customer-actions) payments using the Swish mobile app and the Swedish BankID mobile app. Check this [page](https://stripe.com/docs/payments/swish) for more details."
            },
            {
                "name": "twint",
                "description": "Twint is a payment method popular in Switzerland. It allows customers to pay using their mobile phone. Check this [page](https://docs.stripe.com/payments/twint) for more details."
            },
            {
                "name": "us_bank_account",
                "description": "Stripe users in the United States can accept ACH direct debit payments from customers with a US bank account using the Automated Clearing House (ACH) payments system operated by Nacha. Check this [page](https://stripe.com/docs/payments/ach-direct-debit) for more details."
            },
            {
                "name": "wechat_pay",
                "description": "WeChat, owned by Tencent, is China's leading mobile app with over 1 billion monthly active users. Chinese consumers can use WeChat Pay to pay for goods and services inside of businesses' apps and websites. WeChat Pay users buy most frequently in gaming, e-commerce, travel, online education, and food/nutrition. Check this [page](https://stripe.com/docs/payments/wechat-pay) for more details."
            },
            {
                "name": "zip",
                "description": "Zip gives your customers a way to split purchases over a series of payments. Check this [page](https://stripe.com/docs/payments/zip) for more details like country availability."
            }
        ]
    },
    {
        "path": "/v1/payment_method_configurations/{configuration}",
        "verb": "get",
        "op_id": "GetPaymentMethodConfigurationsConfiguration",
        "summary": "Retrieve payment method configuration",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/payment_method_configurations/{configuration}",
        "verb": "post",
        "op_id": "PostPaymentMethodConfigurationsConfiguration",
        "summary": "Update payment method configuration",
        "params": [
            {
                "name": "acss_debit",
                "description": "Canadian pre-authorized debit payments, check this [page](https://stripe.com/docs/payments/acss-debit) for more details like country availability."
            },
            {
                "name": "active",
                "description": "Whether the configuration can be used for new payments."
            },
            {
                "name": "affirm",
                "description": "[Affirm](https://www.affirm.com/) gives your customers a way to split purchases over a series of payments. Depending on the purchase, they can pay with four interest-free payments (Split Pay) or pay over a longer term (Installments), which might include interest. Check this [page](https://stripe.com/docs/payments/affirm) for more details like country availability."
            },
            {
                "name": "afterpay_clearpay",
                "description": "Afterpay gives your customers a way to pay for purchases in installments, check this [page](https://stripe.com/docs/payments/afterpay-clearpay) for more details like country availability. Afterpay is particularly popular among businesses selling fashion, beauty, and sports products."
            },
            {
                "name": "alipay",
                "description": "Alipay is a digital wallet in China that has more than a billion active users worldwide. Alipay users can pay on the web or on a mobile device using login credentials or their Alipay app. Alipay has a low dispute rate and reduces fraud by authenticating payments using the customer's login credentials. Check this [page](https://stripe.com/docs/payments/alipay) for more details."
            },
            {
                "name": "alma",
                "description": "Alma is a Buy Now, Pay Later payment method that offers customers the ability to pay in 2, 3, or 4 installments."
            },
            {
                "name": "amazon_pay",
                "description": "Amazon Pay is a wallet payment method that lets your customers check out the same way as on Amazon."
            },
            {
                "name": "apple_pay",
                "description": "Stripe users can accept [Apple Pay](https://stripe.com/payments/apple-pay) in iOS applications in iOS 9 and later, and on the web in Safari starting with iOS 10 or macOS Sierra. There are no additional fees to process Apple Pay payments, and the [pricing](https://stripe.com/pricing) is the same as other card transactions. Check this [page](https://stripe.com/docs/apple-pay) for more details."
            },
            {
                "name": "apple_pay_later",
                "description": "Apple Pay Later, a payment method for customers to buy now and pay later, gives your customers a way to split purchases into four installments across six weeks."
            },
            {
                "name": "au_becs_debit",
                "description": "Stripe users in Australia can accept Bulk Electronic Clearing System (BECS) direct debit payments from customers with an Australian bank account. Check this [page](https://stripe.com/docs/payments/au-becs-debit) for more details."
            },
            {
                "name": "bacs_debit",
                "description": "Stripe users in the UK can accept Bacs Direct Debit payments from customers with a UK bank account, check this [page](https://stripe.com/docs/payments/payment-methods/bacs-debit) for more details."
            },
            {
                "name": "bancontact",
                "description": "Bancontact is the most popular online payment method in Belgium, with over 15 million cards in circulation. [Customers](https://stripe.com/docs/api/customers) use a Bancontact card or mobile app linked to a Belgian bank account to make online payments that are secure, guaranteed, and confirmed immediately. Check this [page](https://stripe.com/docs/payments/bancontact) for more details."
            },
            {
                "name": "billie",
                "description": "Billie is a [single-use](https://docs.stripe.com/payments/payment-methods#usage) payment method that offers businesses Pay by Invoice where they offer payment terms ranging from 7-120 days. Customers are redirected from your website or app, authorize the payment with Billie, then return to your website or app. You get [immediate notification](/payments/payment-methods#payment-notification) of whether the payment succeeded or failed."
            },
            {
                "name": "blik",
                "description": "BLIK is a [single use](https://stripe.com/docs/payments/payment-methods#usage) payment method that requires customers to authenticate their payments. When customers want to pay online using BLIK, they request a six-digit code from their banking application and enter it into the payment collection form. Check this [page](https://stripe.com/docs/payments/blik) for more details."
            },
            {
                "name": "boleto",
                "description": "Boleto is an official (regulated by the Central Bank of Brazil) payment method in Brazil. Check this [page](https://stripe.com/docs/payments/boleto) for more details."
            },
            {
                "name": "card",
                "description": "Cards are a popular way for consumers and businesses to pay online or in person. Stripe supports global and local card networks."
            },
            {
                "name": "cartes_bancaires",
                "description": "Cartes Bancaires is France's local card network. More than 95% of these cards are co-branded with either Visa or Mastercard, meaning you can process these cards over either Cartes Bancaires or the Visa or Mastercard networks. Check this [page](https://stripe.com/docs/payments/cartes-bancaires) for more details."
            },
            {
                "name": "cashapp",
                "description": "Cash App is a popular consumer app in the US that allows customers to bank, invest, send, and receive money using their digital wallet. Check this [page](https://stripe.com/docs/payments/cash-app-pay) for more details."
            },
            {
                "name": "customer_balance",
                "description": "Uses a customer\u2019s [cash balance](https://stripe.com/docs/payments/customer-balance) for the payment. The cash balance can be funded via a bank transfer. Check this [page](https://stripe.com/docs/payments/bank-transfers) for more details."
            },
            {
                "name": "eps",
                "description": "EPS is an Austria-based payment method that allows customers to complete transactions online using their bank credentials. EPS is supported by all Austrian banks and is accepted by over 80% of Austrian online retailers. Check this [page](https://stripe.com/docs/payments/eps) for more details."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "fpx",
                "description": "Financial Process Exchange (FPX) is a Malaysia-based payment method that allows customers to complete transactions online using their bank credentials. Bank Negara Malaysia (BNM), the Central Bank of Malaysia, and eleven other major Malaysian financial institutions are members of the PayNet Group, which owns and operates FPX. It is one of the most popular online payment methods in Malaysia, with nearly 90 million transactions in 2018 according to BNM. Check this [page](https://stripe.com/docs/payments/fpx) for more details."
            },
            {
                "name": "giropay",
                "description": "giropay is a German payment method based on online banking, introduced in 2006. It allows customers to complete transactions online using their online banking environment, with funds debited from their bank account. Depending on their bank, customers confirm payments on giropay using a second factor of authentication or a PIN. giropay accounts for 10% of online checkouts in Germany. Check this [page](https://stripe.com/docs/payments/giropay) for more details."
            },
            {
                "name": "google_pay",
                "description": "Google Pay allows customers to make payments in your app or website using any credit or debit card saved to their Google Account, including those from Google Play, YouTube, Chrome, or an Android device. Use the Google Pay API to request any credit or debit card stored in your customer's Google account. Check this [page](https://stripe.com/docs/google-pay) for more details."
            },
            {
                "name": "grabpay",
                "description": "GrabPay is a payment method developed by [Grab](https://www.grab.com/sg/consumer/finance/pay/). GrabPay is a digital wallet - customers maintain a balance in their wallets that they pay out with. Check this [page](https://stripe.com/docs/payments/grabpay) for more details."
            },
            {
                "name": "ideal",
                "description": "iDEAL is a Netherlands-based payment method that allows customers to complete transactions online using their bank credentials. All major Dutch banks are members of Currence, the scheme that operates iDEAL, making it the most popular online payment method in the Netherlands with a share of online transactions close to 55%. Check this [page](https://stripe.com/docs/payments/ideal) for more details."
            },
            {
                "name": "jcb",
                "description": "JCB is a credit card company based in Japan. JCB is currently available in Japan to businesses approved by JCB, and available to all businesses in Australia, Canada, Hong Kong, Japan, New Zealand, Singapore, Switzerland, United Kingdom, United States, and all countries in the European Economic Area except Iceland. Check this [page](https://support.stripe.com/questions/accepting-japan-credit-bureau-%28jcb%29-payments) for more details."
            },
            {
                "name": "kakao_pay",
                "description": "Kakao Pay is a popular local wallet available in South Korea."
            },
            {
                "name": "klarna",
                "description": "Klarna gives customers a range of [payment options](https://stripe.com/docs/payments/klarna#payment-options) during checkout. Available payment options vary depending on the customer's billing address and the transaction amount. These payment options make it convenient for customers to purchase items in all price ranges. Check this [page](https://stripe.com/docs/payments/klarna) for more details."
            },
            {
                "name": "konbini",
                "description": "Konbini allows customers in Japan to pay for bills and online purchases at convenience stores with cash. Check this [page](https://stripe.com/docs/payments/konbini) for more details."
            },
            {
                "name": "kr_card",
                "description": "Korean cards let users pay using locally issued cards from South Korea."
            },
            {
                "name": "link",
                "description": "[Link](https://stripe.com/docs/payments/link) is a payment method network. With Link, users save their payment details once, then reuse that information to pay with one click for any business on the network."
            },
            {
                "name": "mobilepay",
                "description": "MobilePay is a [single-use](https://stripe.com/docs/payments/payment-methods#usage) card wallet payment method used in Denmark and Finland. It allows customers to [authenticate and approve](https://stripe.com/docs/payments/payment-methods#customer-actions) payments using the MobilePay app. Check this [page](https://stripe.com/docs/payments/mobilepay) for more details."
            },
            {
                "name": "multibanco",
                "description": "Stripe users in Europe and the United States can accept Multibanco payments from customers in Portugal using [Sources](https://stripe.com/docs/sources)\u2014a single integration path for creating payments using any supported method."
            },
            {
                "name": "name",
                "description": "Configuration name."
            },
            {
                "name": "naver_pay",
                "description": "Naver Pay is a popular local wallet available in South Korea."
            },
            {
                "name": "nz_bank_account",
                "description": "Stripe users in New Zealand can accept Bulk Electronic Clearing System (BECS) direct debit payments from customers with a New Zeland bank account. Check this [page](https://stripe.com/docs/payments/nz-bank-account) for more details."
            },
            {
                "name": "oxxo",
                "description": "OXXO is a Mexican chain of convenience stores with thousands of locations across Latin America and represents nearly 20% of online transactions in Mexico. OXXO allows customers to pay bills and online purchases in-store with cash. Check this [page](https://stripe.com/docs/payments/oxxo) for more details."
            },
            {
                "name": "p24",
                "description": "Przelewy24 is a Poland-based payment method aggregator that allows customers to complete transactions online using bank transfers and other methods. Bank transfers account for 30% of online payments in Poland and Przelewy24 provides a way for customers to pay with over 165 banks. Check this [page](https://stripe.com/docs/payments/p24) for more details."
            },
            {
                "name": "pay_by_bank",
                "description": "Pay by bank is a redirect payment method backed by bank transfers. A customer is redirected to their bank to authorize a bank transfer for a given amount. This removes a lot of the error risks inherent in waiting for the customer to initiate a transfer themselves, and is less expensive than card payments."
            },
            {
                "name": "payco",
                "description": "PAYCO is a [single-use](https://docs.stripe.com/payments/payment-methods#usage local wallet available in South Korea."
            },
            {
                "name": "paynow",
                "description": "PayNow is a Singapore-based payment method that allows customers to make a payment using their preferred app from participating banks and participating non-bank financial institutions. Check this [page](https://stripe.com/docs/payments/paynow) for more details."
            },
            {
                "name": "paypal",
                "description": "PayPal, a digital wallet popular with customers in Europe, allows your customers worldwide to pay using their PayPal account. Check this [page](https://stripe.com/docs/payments/paypal) for more details."
            },
            {
                "name": "pix",
                "description": "Pix is a payment method popular in Brazil. When paying with Pix, customers authenticate and approve payments by scanning a QR code in their preferred banking app. Check this [page](https://docs.stripe.com/payments/pix) for more details."
            },
            {
                "name": "promptpay",
                "description": "PromptPay is a Thailand-based payment method that allows customers to make a payment using their preferred app from participating banks. Check this [page](https://stripe.com/docs/payments/promptpay) for more details."
            },
            {
                "name": "revolut_pay",
                "description": "Revolut Pay, developed by Revolut, a global finance app, is a digital wallet payment method. Revolut Pay uses the customer\u2019s stored balance or cards to fund the payment, and offers the option for non-Revolut customers to save their details after their first purchase."
            },
            {
                "name": "samsung_pay",
                "description": "Samsung Pay is a [single-use](https://docs.stripe.com/payments/payment-methods#usage local wallet available in South Korea."
            },
            {
                "name": "satispay",
                "description": "Satispay is a [single-use](https://docs.stripe.com/payments/payment-methods#usage) payment method where customers are required to [authenticate](/payments/payment-methods#customer-actions) their payment. Customers pay by being redirected from your website or app, authorizing the payment with Satispay, then returning to your website or app. You get [immediate notification](/payments/payment-methods#payment-notification) of whether the payment succeeded or failed."
            },
            {
                "name": "sepa_debit",
                "description": "The [Single Euro Payments Area (SEPA)](https://en.wikipedia.org/wiki/Single_Euro_Payments_Area) is an initiative of the European Union to simplify payments within and across member countries. SEPA established and enforced banking standards to allow for the direct debiting of every EUR-denominated bank account within the SEPA region, check this [page](https://stripe.com/docs/payments/sepa-debit) for more details."
            },
            {
                "name": "sofort",
                "description": "Stripe users in Europe and the United States can use the [Payment Intents API](https://stripe.com/docs/payments/payment-intents)\u2014a single integration path for creating payments using any supported method\u2014to accept [Sofort](https://www.sofort.com/) payments from customers. Check this [page](https://stripe.com/docs/payments/sofort) for more details."
            },
            {
                "name": "swish",
                "description": "Swish is a [real-time](https://stripe.com/docs/payments/real-time) payment method popular in Sweden. It allows customers to [authenticate and approve](https://stripe.com/docs/payments/payment-methods#customer-actions) payments using the Swish mobile app and the Swedish BankID mobile app. Check this [page](https://stripe.com/docs/payments/swish) for more details."
            },
            {
                "name": "twint",
                "description": "Twint is a payment method popular in Switzerland. It allows customers to pay using their mobile phone. Check this [page](https://docs.stripe.com/payments/twint) for more details."
            },
            {
                "name": "us_bank_account",
                "description": "Stripe users in the United States can accept ACH direct debit payments from customers with a US bank account using the Automated Clearing House (ACH) payments system operated by Nacha. Check this [page](https://stripe.com/docs/payments/ach-direct-debit) for more details."
            },
            {
                "name": "wechat_pay",
                "description": "WeChat, owned by Tencent, is China's leading mobile app with over 1 billion monthly active users. Chinese consumers can use WeChat Pay to pay for goods and services inside of businesses' apps and websites. WeChat Pay users buy most frequently in gaming, e-commerce, travel, online education, and food/nutrition. Check this [page](https://stripe.com/docs/payments/wechat-pay) for more details."
            },
            {
                "name": "zip",
                "description": "Zip gives your customers a way to split purchases over a series of payments. Check this [page](https://stripe.com/docs/payments/zip) for more details like country availability."
            }
        ]
    },
    {
        "path": "/v1/payment_method_domains",
        "verb": "get",
        "op_id": "GetPaymentMethodDomains",
        "summary": "List payment method domains",
        "params": [
            {
                "name": "domain_name",
                "description": "The domain name that this payment method domain object represents."
            },
            {
                "name": "enabled",
                "description": "Whether this payment method domain is enabled. If the domain is not enabled, payment methods will not appear in Elements or Embedded Checkout"
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/payment_method_domains",
        "verb": "post",
        "op_id": "PostPaymentMethodDomains",
        "summary": "Create a payment method domain",
        "params": [
            {
                "name": "domain_name",
                "description": "The domain name that this payment method domain object represents."
            },
            {
                "name": "enabled",
                "description": "Whether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements or Embedded Checkout."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/payment_method_domains/{payment_method_domain}",
        "verb": "get",
        "op_id": "GetPaymentMethodDomainsPaymentMethodDomain",
        "summary": "Retrieve a payment method domain",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/payment_method_domains/{payment_method_domain}",
        "verb": "post",
        "op_id": "PostPaymentMethodDomainsPaymentMethodDomain",
        "summary": "Update a payment method domain",
        "params": [
            {
                "name": "enabled",
                "description": "Whether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements or Embedded Checkout."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/payment_method_domains/{payment_method_domain}/validate",
        "verb": "post",
        "op_id": "PostPaymentMethodDomainsPaymentMethodDomainValidate",
        "summary": "Validate an existing payment method domain",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/payment_methods",
        "verb": "get",
        "op_id": "GetPaymentMethods",
        "summary": "List PaymentMethods",
        "params": [
            {
                "name": "customer",
                "description": "The ID of the customer whose PaymentMethods will be retrieved."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "type",
                "description": "An optional filter on the list, based on the object `type` field. Without the filter, the list includes all current and future payment method types. If your integration expects only one type of payment method in the response, make sure to provide a type value in the request."
            }
        ]
    },
    {
        "path": "/v1/payment_methods",
        "verb": "post",
        "op_id": "PostPaymentMethods",
        "summary": "Shares a PaymentMethod",
        "params": [
            {
                "name": "acss_debit",
                "description": "If this is an `acss_debit` PaymentMethod, this hash contains details about the ACSS Debit payment method."
            },
            {
                "name": "affirm",
                "description": "If this is an `affirm` PaymentMethod, this hash contains details about the Affirm payment method."
            },
            {
                "name": "afterpay_clearpay",
                "description": "If this is an `AfterpayClearpay` PaymentMethod, this hash contains details about the AfterpayClearpay payment method."
            },
            {
                "name": "alipay",
                "description": "If this is an `Alipay` PaymentMethod, this hash contains details about the Alipay payment method."
            },
            {
                "name": "allow_redisplay",
                "description": "This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to `unspecified`."
            },
            {
                "name": "alma",
                "description": "If this is a Alma PaymentMethod, this hash contains details about the Alma payment method."
            },
            {
                "name": "amazon_pay",
                "description": "If this is a AmazonPay PaymentMethod, this hash contains details about the AmazonPay payment method."
            },
            {
                "name": "au_becs_debit",
                "description": "If this is an `au_becs_debit` PaymentMethod, this hash contains details about the bank account."
            },
            {
                "name": "bacs_debit",
                "description": "If this is a `bacs_debit` PaymentMethod, this hash contains details about the Bacs Direct Debit bank account."
            },
            {
                "name": "bancontact",
                "description": "If this is a `bancontact` PaymentMethod, this hash contains details about the Bancontact payment method."
            },
            {
                "name": "billie",
                "description": "If this is a `billie` PaymentMethod, this hash contains details about the Billie payment method."
            },
            {
                "name": "billing_details",
                "description": "Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods."
            },
            {
                "name": "blik",
                "description": "If this is a `blik` PaymentMethod, this hash contains details about the BLIK payment method."
            },
            {
                "name": "boleto",
                "description": "If this is a `boleto` PaymentMethod, this hash contains details about the Boleto payment method."
            },
            {
                "name": "card",
                "description": "If this is a `card` PaymentMethod, this hash contains the user's card details. For backwards compatibility, you can alternatively provide a Stripe token (e.g., for Apple Pay, Amex Express Checkout, or legacy Checkout) into the card hash with format `card: {token: \"tok_visa\"}`. When providing a card number, you must meet the requirements for [PCI compliance](https://stripe.com/docs/security#validating-pci-compliance). We strongly recommend using Stripe.js instead of interacting with this API directly."
            },
            {
                "name": "cashapp",
                "description": "If this is a `cashapp` PaymentMethod, this hash contains details about the Cash App Pay payment method."
            },
            {
                "name": "customer",
                "description": "The `Customer` to whom the original PaymentMethod is attached."
            },
            {
                "name": "customer_balance",
                "description": "If this is a `customer_balance` PaymentMethod, this hash contains details about the CustomerBalance payment method."
            },
            {
                "name": "eps",
                "description": "If this is an `eps` PaymentMethod, this hash contains details about the EPS payment method."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "fpx",
                "description": "If this is an `fpx` PaymentMethod, this hash contains details about the FPX payment method."
            },
            {
                "name": "giropay",
                "description": "If this is a `giropay` PaymentMethod, this hash contains details about the Giropay payment method."
            },
            {
                "name": "grabpay",
                "description": "If this is a `grabpay` PaymentMethod, this hash contains details about the GrabPay payment method."
            },
            {
                "name": "ideal",
                "description": "If this is an `ideal` PaymentMethod, this hash contains details about the iDEAL payment method."
            },
            {
                "name": "interac_present",
                "description": "If this is an `interac_present` PaymentMethod, this hash contains details about the Interac Present payment method."
            },
            {
                "name": "kakao_pay",
                "description": "If this is a `kakao_pay` PaymentMethod, this hash contains details about the Kakao Pay payment method."
            },
            {
                "name": "klarna",
                "description": "If this is a `klarna` PaymentMethod, this hash contains details about the Klarna payment method."
            },
            {
                "name": "konbini",
                "description": "If this is a `konbini` PaymentMethod, this hash contains details about the Konbini payment method."
            },
            {
                "name": "kr_card",
                "description": "If this is a `kr_card` PaymentMethod, this hash contains details about the Korean Card payment method."
            },
            {
                "name": "link",
                "description": "If this is an `Link` PaymentMethod, this hash contains details about the Link payment method."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "mobilepay",
                "description": "If this is a `mobilepay` PaymentMethod, this hash contains details about the MobilePay payment method."
            },
            {
                "name": "multibanco",
                "description": "If this is a `multibanco` PaymentMethod, this hash contains details about the Multibanco payment method."
            },
            {
                "name": "naver_pay",
                "description": "If this is a `naver_pay` PaymentMethod, this hash contains details about the Naver Pay payment method."
            },
            {
                "name": "nz_bank_account",
                "description": "If this is an nz_bank_account PaymentMethod, this hash contains details about the nz_bank_account payment method."
            },
            {
                "name": "oxxo",
                "description": "If this is an `oxxo` PaymentMethod, this hash contains details about the OXXO payment method."
            },
            {
                "name": "p24",
                "description": "If this is a `p24` PaymentMethod, this hash contains details about the P24 payment method."
            },
            {
                "name": "pay_by_bank",
                "description": "If this is a `pay_by_bank` PaymentMethod, this hash contains details about the PayByBank payment method."
            },
            {
                "name": "payco",
                "description": "If this is a `payco` PaymentMethod, this hash contains details about the PAYCO payment method."
            },
            {
                "name": "payment_method",
                "description": "The PaymentMethod to share."
            },
            {
                "name": "paynow",
                "description": "If this is a `paynow` PaymentMethod, this hash contains details about the PayNow payment method."
            },
            {
                "name": "paypal",
                "description": "If this is a `paypal` PaymentMethod, this hash contains details about the PayPal payment method."
            },
            {
                "name": "pix",
                "description": "If this is a `pix` PaymentMethod, this hash contains details about the Pix payment method."
            },
            {
                "name": "promptpay",
                "description": "If this is a `promptpay` PaymentMethod, this hash contains details about the PromptPay payment method."
            },
            {
                "name": "radar_options",
                "description": "Options to configure Radar. See [Radar Session](https://stripe.com/docs/radar/radar-session) for more information."
            },
            {
                "name": "revolut_pay",
                "description": "If this is a `revolut_pay` PaymentMethod, this hash contains details about the Revolut Pay payment method."
            },
            {
                "name": "samsung_pay",
                "description": "If this is a `samsung_pay` PaymentMethod, this hash contains details about the SamsungPay payment method."
            },
            {
                "name": "satispay",
                "description": "If this is a `satispay` PaymentMethod, this hash contains details about the Satispay payment method."
            },
            {
                "name": "sepa_debit",
                "description": "If this is a `sepa_debit` PaymentMethod, this hash contains details about the SEPA debit bank account."
            },
            {
                "name": "sofort",
                "description": "If this is a `sofort` PaymentMethod, this hash contains details about the SOFORT payment method."
            },
            {
                "name": "swish",
                "description": "If this is a `swish` PaymentMethod, this hash contains details about the Swish payment method."
            },
            {
                "name": "twint",
                "description": "If this is a TWINT PaymentMethod, this hash contains details about the TWINT payment method."
            },
            {
                "name": "type",
                "description": "The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type."
            },
            {
                "name": "us_bank_account",
                "description": "If this is an `us_bank_account` PaymentMethod, this hash contains details about the US bank account payment method."
            },
            {
                "name": "wechat_pay",
                "description": "If this is an `wechat_pay` PaymentMethod, this hash contains details about the wechat_pay payment method."
            },
            {
                "name": "zip",
                "description": "If this is a `zip` PaymentMethod, this hash contains details about the Zip payment method."
            }
        ]
    },
    {
        "path": "/v1/payment_methods/{payment_method}",
        "verb": "get",
        "op_id": "GetPaymentMethodsPaymentMethod",
        "summary": "Retrieve a PaymentMethod",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/payment_methods/{payment_method}",
        "verb": "post",
        "op_id": "PostPaymentMethodsPaymentMethod",
        "summary": "Update a PaymentMethod",
        "params": [
            {
                "name": "allow_redisplay",
                "description": "This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to `unspecified`."
            },
            {
                "name": "billing_details",
                "description": "Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods."
            },
            {
                "name": "card",
                "description": "If this is a `card` PaymentMethod, this hash contains the user's card details."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "link",
                "description": "If this is an `Link` PaymentMethod, this hash contains details about the Link payment method."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "pay_by_bank",
                "description": "If this is a `pay_by_bank` PaymentMethod, this hash contains details about the PayByBank payment method."
            },
            {
                "name": "us_bank_account",
                "description": "If this is an `us_bank_account` PaymentMethod, this hash contains details about the US bank account payment method."
            }
        ]
    },
    {
        "path": "/v1/payment_methods/{payment_method}/attach",
        "verb": "post",
        "op_id": "PostPaymentMethodsPaymentMethodAttach",
        "summary": "Attach a PaymentMethod to a Customer",
        "params": [
            {
                "name": "customer",
                "description": "The ID of the customer to which to attach the PaymentMethod."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/payment_methods/{payment_method}/detach",
        "verb": "post",
        "op_id": "PostPaymentMethodsPaymentMethodDetach",
        "summary": "Detach a PaymentMethod from a Customer",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/payouts",
        "verb": "get",
        "op_id": "GetPayouts",
        "summary": "List all payouts",
        "params": [
            {
                "name": "arrival_date",
                "description": "Only return payouts that are expected to arrive during the given date interval."
            },
            {
                "name": "created",
                "description": "Only return payouts that were created during the given date interval."
            },
            {
                "name": "destination",
                "description": "The ID of an external account - only return payouts sent to this external account."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "status",
                "description": "Only return payouts that have the given status: `pending`, `paid`, `failed`, or `canceled`."
            }
        ]
    },
    {
        "path": "/v1/payouts",
        "verb": "post",
        "op_id": "PostPayouts",
        "summary": "Create a payout",
        "params": [
            {
                "name": "amount",
                "description": "A positive integer in cents representing how much to payout."
            },
            {
                "name": "currency",
                "description": "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "description",
                "description": "An arbitrary string attached to the object. Often useful for displaying to users."
            },
            {
                "name": "destination",
                "description": "The ID of a bank account or a card to send the payout to. If you don't provide a destination, we use the default external account for the specified currency."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "method",
                "description": "The method used to send this payout, which is `standard` or `instant`. We support `instant` for payouts to debit cards and bank accounts in certain countries. Learn more about [bank support for Instant Payouts](https://stripe.com/docs/payouts/instant-payouts-banks)."
            },
            {
                "name": "source_type",
                "description": "The balance type of your Stripe balance to draw this payout from. Balances for different payment sources are kept separately. You can find the amounts with the Balances API. One of `bank_account`, `card`, or `fpx`."
            },
            {
                "name": "statement_descriptor",
                "description": "A string that displays on the recipient's bank or card statement (up to 22 characters). A `statement_descriptor` that's longer than 22 characters return an error. Most banks truncate this information and display it inconsistently. Some banks might not display it at all."
            }
        ]
    },
    {
        "path": "/v1/payouts/{payout}",
        "verb": "get",
        "op_id": "GetPayoutsPayout",
        "summary": "Retrieve a payout",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/payouts/{payout}",
        "verb": "post",
        "op_id": "PostPayoutsPayout",
        "summary": "Update a payout",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            }
        ]
    },
    {
        "path": "/v1/payouts/{payout}/cancel",
        "verb": "post",
        "op_id": "PostPayoutsPayoutCancel",
        "summary": "Cancel a payout",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/payouts/{payout}/reverse",
        "verb": "post",
        "op_id": "PostPayoutsPayoutReverse",
        "summary": "Reverse a payout",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            }
        ]
    },
    {
        "path": "/v1/plans",
        "verb": "get",
        "op_id": "GetPlans",
        "summary": "List all plans",
        "params": [
            {
                "name": "active",
                "description": "Only return plans that are active or inactive (e.g., pass `false` to list all inactive plans)."
            },
            {
                "name": "created",
                "description": "A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "product",
                "description": "Only return plans for the given product."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/plans",
        "verb": "post",
        "op_id": "PostPlans",
        "summary": "Create a plan",
        "params": [
            {
                "name": "active",
                "description": "Whether the plan is currently available for new subscriptions. Defaults to `true`."
            },
            {
                "name": "amount",
                "description": "A positive integer in cents (or local equivalent) (or 0 for a free plan) representing how much to charge on a recurring basis."
            },
            {
                "name": "amount_decimal",
                "description": "Same as `amount`, but accepts a decimal value with at most 12 decimal places. Only one of `amount` and `amount_decimal` can be set."
            },
            {
                "name": "billing_scheme",
                "description": "Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `amount`) will be charged per unit in `quantity` (for plans with `usage_type=licensed`), or per unit of total usage (for plans with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes."
            },
            {
                "name": "currency",
                "description": "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "id",
                "description": "An identifier randomly generated by Stripe. Used to identify this plan when subscribing a customer. You can optionally override this ID, but the ID must be unique across all plans in your Stripe account. You can, however, use the same plan ID in both live and test modes."
            },
            {
                "name": "interval",
                "description": "Specifies billing frequency. Either `day`, `week`, `month` or `year`."
            },
            {
                "name": "interval_count",
                "description": "The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of three years interval allowed (3 years, 36 months, or 156 weeks)."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "meter",
                "description": "The meter tracking the usage of a metered price"
            },
            {
                "name": "nickname",
                "description": "A brief description of the plan, hidden from customers."
            },
            {
                "name": "product",
                "description": ""
            },
            {
                "name": "tiers",
                "description": "Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`."
            },
            {
                "name": "tiers_mode",
                "description": "Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price, in `graduated` tiering pricing can successively change as the quantity grows."
            },
            {
                "name": "transform_usage",
                "description": "Apply a transformation to the reported usage or set quantity before computing the billed price. Cannot be combined with `tiers`."
            },
            {
                "name": "trial_period_days",
                "description": "Default number of trial days when subscribing a customer to this plan using [`trial_from_plan=true`](https://stripe.com/docs/api#create_subscription-trial_from_plan)."
            },
            {
                "name": "usage_type",
                "description": "Configures how the quantity per period should be determined. Can be either `metered` or `licensed`. `licensed` automatically bills the `quantity` set when adding it to a subscription. `metered` aggregates the total usage based on usage records. Defaults to `licensed`."
            }
        ]
    },
    {
        "path": "/v1/plans/{plan}",
        "verb": "delete",
        "op_id": "DeletePlansPlan",
        "summary": "Delete a plan",
        "params": []
    },
    {
        "path": "/v1/plans/{plan}",
        "verb": "get",
        "op_id": "GetPlansPlan",
        "summary": "Retrieve a plan",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/plans/{plan}",
        "verb": "post",
        "op_id": "PostPlansPlan",
        "summary": "Update a plan",
        "params": [
            {
                "name": "active",
                "description": "Whether the plan is currently available for new subscriptions."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "nickname",
                "description": "A brief description of the plan, hidden from customers."
            },
            {
                "name": "product",
                "description": "The product the plan belongs to. This cannot be changed once it has been used in a subscription or subscription schedule."
            },
            {
                "name": "trial_period_days",
                "description": "Default number of trial days when subscribing a customer to this plan using [`trial_from_plan=true`](https://stripe.com/docs/api#create_subscription-trial_from_plan)."
            }
        ]
    },
    {
        "path": "/v1/prices",
        "verb": "get",
        "op_id": "GetPrices",
        "summary": "List all prices",
        "params": [
            {
                "name": "active",
                "description": "Only return prices that are active or inactive (e.g., pass `false` to list all inactive prices)."
            },
            {
                "name": "created",
                "description": "A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options."
            },
            {
                "name": "currency",
                "description": "Only return prices for the given currency."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "lookup_keys",
                "description": "Only return the price with these lookup_keys, if any exist. You can specify up to 10 lookup_keys."
            },
            {
                "name": "product",
                "description": "Only return prices for the given product."
            },
            {
                "name": "recurring",
                "description": "Only return prices with these recurring fields."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "type",
                "description": "Only return prices of type `recurring` or `one_time`."
            }
        ]
    },
    {
        "path": "/v1/prices",
        "verb": "post",
        "op_id": "PostPrices",
        "summary": "Create a price",
        "params": [
            {
                "name": "active",
                "description": "Whether the price can be used for new purchases. Defaults to `true`."
            },
            {
                "name": "billing_scheme",
                "description": "Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `unit_amount` or `unit_amount_decimal`) will be charged per unit in `quantity` (for prices with `usage_type=licensed`), or per unit of total usage (for prices with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes."
            },
            {
                "name": "currency",
                "description": "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "currency_options",
                "description": "Prices defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "custom_unit_amount",
                "description": "When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "lookup_key",
                "description": "A lookup key used to retrieve prices dynamically from a static string. This may be up to 200 characters."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "nickname",
                "description": "A brief description of the price, hidden from customers."
            },
            {
                "name": "product",
                "description": "The ID of the [Product](https://docs.stripe.com/api/products) that this [Price](https://docs.stripe.com/api/prices) will belong to."
            },
            {
                "name": "product_data",
                "description": "These fields can be used to create a new product that this price will belong to."
            },
            {
                "name": "recurring",
                "description": "The recurring components of a price such as `interval` and `usage_type`."
            },
            {
                "name": "tax_behavior",
                "description": "Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed."
            },
            {
                "name": "tiers",
                "description": "Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`."
            },
            {
                "name": "tiers_mode",
                "description": "Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price, in `graduated` tiering pricing can successively change as the quantity grows."
            },
            {
                "name": "transfer_lookup_key",
                "description": "If set to true, will atomically remove the lookup key from the existing price, and assign it to this price."
            },
            {
                "name": "transform_quantity",
                "description": "Apply a transformation to the reported usage or set quantity before computing the billed price. Cannot be combined with `tiers`."
            },
            {
                "name": "unit_amount",
                "description": "A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge. One of `unit_amount`, `unit_amount_decimal`, or `custom_unit_amount` is required, unless `billing_scheme=tiered`."
            },
            {
                "name": "unit_amount_decimal",
                "description": "Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set."
            }
        ]
    },
    {
        "path": "/v1/prices/search",
        "verb": "get",
        "op_id": "GetPricesSearch",
        "summary": "Search prices",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "page",
                "description": "A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results."
            },
            {
                "name": "query",
                "description": "The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for prices](https://stripe.com/docs/search#query-fields-for-prices)."
            }
        ]
    },
    {
        "path": "/v1/prices/{price}",
        "verb": "get",
        "op_id": "GetPricesPrice",
        "summary": "Retrieve a price",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/prices/{price}",
        "verb": "post",
        "op_id": "PostPricesPrice",
        "summary": "Update a price",
        "params": [
            {
                "name": "active",
                "description": "Whether the price can be used for new purchases. Defaults to `true`."
            },
            {
                "name": "currency_options",
                "description": "Prices defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "lookup_key",
                "description": "A lookup key used to retrieve prices dynamically from a static string. This may be up to 200 characters."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "nickname",
                "description": "A brief description of the price, hidden from customers."
            },
            {
                "name": "tax_behavior",
                "description": "Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed."
            },
            {
                "name": "transfer_lookup_key",
                "description": "If set to true, will atomically remove the lookup key from the existing price, and assign it to this price."
            }
        ]
    },
    {
        "path": "/v1/products",
        "verb": "get",
        "op_id": "GetProducts",
        "summary": "List all products",
        "params": [
            {
                "name": "active",
                "description": "Only return products that are active or inactive (e.g., pass `false` to list all inactive products)."
            },
            {
                "name": "created",
                "description": "Only return products that were created during the given date interval."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "ids",
                "description": "Only return products with the given IDs. Cannot be used with [starting_after](https://stripe.com/docs/api#list_products-starting_after) or [ending_before](https://stripe.com/docs/api#list_products-ending_before)."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "shippable",
                "description": "Only return products that can be shipped (i.e., physical, not digital products)."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "url",
                "description": "Only return products with the given url."
            }
        ]
    },
    {
        "path": "/v1/products",
        "verb": "post",
        "op_id": "PostProducts",
        "summary": "Create a product",
        "params": [
            {
                "name": "active",
                "description": "Whether the product is currently available for purchase. Defaults to `true`."
            },
            {
                "name": "default_price_data",
                "description": "Data used to generate a new [Price](https://stripe.com/docs/api/prices) object. This Price will be set as the default price for this product."
            },
            {
                "name": "description",
                "description": "The product's description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "id",
                "description": "An identifier will be randomly generated by Stripe. You can optionally override this ID, but the ID must be unique across all products in your Stripe account."
            },
            {
                "name": "images",
                "description": "A list of up to 8 URLs of images for this product, meant to be displayable to the customer."
            },
            {
                "name": "marketing_features",
                "description": "A list of up to 15 marketing features for this product. These are displayed in [pricing tables](https://stripe.com/docs/payments/checkout/pricing-table)."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "name",
                "description": "The product's name, meant to be displayable to the customer."
            },
            {
                "name": "package_dimensions",
                "description": "The dimensions of this product for shipping purposes."
            },
            {
                "name": "shippable",
                "description": "Whether this product is shipped (i.e., physical goods)."
            },
            {
                "name": "statement_descriptor",
                "description": "An arbitrary string to be displayed on your customer's credit card or bank statement. While most banks display this information consistently, some may display it incorrectly or not at all.\n\nThis may be up to 22 characters. The statement description may not include `<`, `>`, `\\`, `\"`, `'` characters, and will appear on your customer's statement in capital letters. Non-ASCII characters are automatically stripped.\n It must contain at least one letter. Only used for subscription payments."
            },
            {
                "name": "tax_code",
                "description": "A [tax code](https://stripe.com/docs/tax/tax-categories) ID."
            },
            {
                "name": "unit_label",
                "description": "A label that represents units of this product. When set, this will be included in customers' receipts, invoices, Checkout, and the customer portal."
            },
            {
                "name": "url",
                "description": "A URL of a publicly-accessible webpage for this product."
            }
        ]
    },
    {
        "path": "/v1/products/search",
        "verb": "get",
        "op_id": "GetProductsSearch",
        "summary": "Search products",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "page",
                "description": "A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results."
            },
            {
                "name": "query",
                "description": "The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for products](https://stripe.com/docs/search#query-fields-for-products)."
            }
        ]
    },
    {
        "path": "/v1/products/{id}",
        "verb": "delete",
        "op_id": "DeleteProductsId",
        "summary": "Delete a product",
        "params": []
    },
    {
        "path": "/v1/products/{id}",
        "verb": "get",
        "op_id": "GetProductsId",
        "summary": "Retrieve a product",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/products/{id}",
        "verb": "post",
        "op_id": "PostProductsId",
        "summary": "Update a product",
        "params": [
            {
                "name": "active",
                "description": "Whether the product is available for purchase."
            },
            {
                "name": "default_price",
                "description": "The ID of the [Price](https://stripe.com/docs/api/prices) object that is the default price for this product."
            },
            {
                "name": "description",
                "description": "The product's description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "images",
                "description": "A list of up to 8 URLs of images for this product, meant to be displayable to the customer."
            },
            {
                "name": "marketing_features",
                "description": "A list of up to 15 marketing features for this product. These are displayed in [pricing tables](https://stripe.com/docs/payments/checkout/pricing-table)."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "name",
                "description": "The product's name, meant to be displayable to the customer."
            },
            {
                "name": "package_dimensions",
                "description": "The dimensions of this product for shipping purposes."
            },
            {
                "name": "shippable",
                "description": "Whether this product is shipped (i.e., physical goods)."
            },
            {
                "name": "statement_descriptor",
                "description": "An arbitrary string to be displayed on your customer's credit card or bank statement. While most banks display this information consistently, some may display it incorrectly or not at all.\n\nThis may be up to 22 characters. The statement description may not include `<`, `>`, `\\`, `\"`, `'` characters, and will appear on your customer's statement in capital letters. Non-ASCII characters are automatically stripped.\n It must contain at least one letter. May only be set if `type=service`. Only used for subscription payments."
            },
            {
                "name": "tax_code",
                "description": "A [tax code](https://stripe.com/docs/tax/tax-categories) ID."
            },
            {
                "name": "unit_label",
                "description": "A label that represents units of this product. When set, this will be included in customers' receipts, invoices, Checkout, and the customer portal. May only be set if `type=service`."
            },
            {
                "name": "url",
                "description": "A URL of a publicly-accessible webpage for this product."
            }
        ]
    },
    {
        "path": "/v1/products/{product}/features",
        "verb": "get",
        "op_id": "GetProductsProductFeatures",
        "summary": "List all features attached to a product",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/products/{product}/features",
        "verb": "post",
        "op_id": "PostProductsProductFeatures",
        "summary": "Attach a feature to a product",
        "params": [
            {
                "name": "entitlement_feature",
                "description": "The ID of the [Feature](https://stripe.com/docs/api/entitlements/feature) object attached to this product."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/products/{product}/features/{id}",
        "verb": "delete",
        "op_id": "DeleteProductsProductFeaturesId",
        "summary": "Remove a feature from a product",
        "params": []
    },
    {
        "path": "/v1/products/{product}/features/{id}",
        "verb": "get",
        "op_id": "GetProductsProductFeaturesId",
        "summary": "Retrieve a product_feature",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/promotion_codes",
        "verb": "get",
        "op_id": "GetPromotionCodes",
        "summary": "List all promotion codes",
        "params": [
            {
                "name": "active",
                "description": "Filter promotion codes by whether they are active."
            },
            {
                "name": "code",
                "description": "Only return promotion codes that have this case-insensitive code."
            },
            {
                "name": "coupon",
                "description": "Only return promotion codes for this coupon."
            },
            {
                "name": "created",
                "description": "A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options."
            },
            {
                "name": "customer",
                "description": "Only return promotion codes that are restricted to this customer."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/promotion_codes",
        "verb": "post",
        "op_id": "PostPromotionCodes",
        "summary": "Create a promotion code",
        "params": [
            {
                "name": "active",
                "description": "Whether the promotion code is currently active."
            },
            {
                "name": "code",
                "description": "The customer-facing code. Regardless of case, this code must be unique across all active promotion codes for a specific customer. Valid characters are lower case letters (a-z), upper case letters (A-Z), and digits (0-9).\n\nIf left blank, we will generate one automatically."
            },
            {
                "name": "coupon",
                "description": "The coupon for this promotion code."
            },
            {
                "name": "customer",
                "description": "The customer that this promotion code can be used by. If not set, the promotion code can be used by all customers."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "expires_at",
                "description": "The timestamp at which this promotion code will expire. If the coupon has specified a `redeems_by`, then this value cannot be after the coupon's `redeems_by`."
            },
            {
                "name": "max_redemptions",
                "description": "A positive integer specifying the number of times the promotion code can be redeemed. If the coupon has specified a `max_redemptions`, then this value cannot be greater than the coupon's `max_redemptions`."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "restrictions",
                "description": "Settings that restrict the redemption of the promotion code."
            }
        ]
    },
    {
        "path": "/v1/promotion_codes/{promotion_code}",
        "verb": "get",
        "op_id": "GetPromotionCodesPromotionCode",
        "summary": "Retrieve a promotion code",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/promotion_codes/{promotion_code}",
        "verb": "post",
        "op_id": "PostPromotionCodesPromotionCode",
        "summary": "Update a promotion code",
        "params": [
            {
                "name": "active",
                "description": "Whether the promotion code is currently active. A promotion code can only be reactivated when the coupon is still valid and the promotion code is otherwise redeemable."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "restrictions",
                "description": "Settings that restrict the redemption of the promotion code."
            }
        ]
    },
    {
        "path": "/v1/quotes",
        "verb": "get",
        "op_id": "GetQuotes",
        "summary": "List all quotes",
        "params": [
            {
                "name": "customer",
                "description": "The ID of the customer whose quotes will be retrieved."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "status",
                "description": "The status of the quote."
            },
            {
                "name": "test_clock",
                "description": "Provides a list of quotes that are associated with the specified test clock. The response will not include quotes with test clocks if this and the customer parameter is not set."
            }
        ]
    },
    {
        "path": "/v1/quotes",
        "verb": "post",
        "op_id": "PostQuotes",
        "summary": "Create a quote",
        "params": [
            {
                "name": "application_fee_amount",
                "description": "The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. There cannot be any line items with recurring prices when using this field."
            },
            {
                "name": "application_fee_percent",
                "description": "A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. There must be at least 1 line item with a recurring price to use this field."
            },
            {
                "name": "automatic_tax",
                "description": "Settings for automatic tax lookup for this quote and resulting invoices and subscriptions."
            },
            {
                "name": "collection_method",
                "description": "Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay invoices at the end of the subscription cycle or at invoice finalization using the default payment method attached to the subscription or customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`."
            },
            {
                "name": "customer",
                "description": "The customer for which this quote belongs to. A customer is required before finalizing the quote. Once specified, it cannot be changed."
            },
            {
                "name": "default_tax_rates",
                "description": "The tax rates that will apply to any line item that does not have `tax_rates` set."
            },
            {
                "name": "description",
                "description": "A description that will be displayed on the quote PDF. If no value is passed, the default description configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used."
            },
            {
                "name": "discounts",
                "description": "The discounts applied to the quote."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "expires_at",
                "description": "A future timestamp on which the quote will be canceled if in `open` or `draft` status. Measured in seconds since the Unix epoch. If no value is passed, the default expiration date configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used."
            },
            {
                "name": "footer",
                "description": "A footer that will be displayed on the quote PDF. If no value is passed, the default footer configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used."
            },
            {
                "name": "from_quote",
                "description": "Clone an existing quote. The new quote will be created in `status=draft`. When using this parameter, you cannot specify any other parameters except for `expires_at`."
            },
            {
                "name": "header",
                "description": "A header that will be displayed on the quote PDF. If no value is passed, the default header configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used."
            },
            {
                "name": "invoice_settings",
                "description": "All invoices will be billed using the specified settings."
            },
            {
                "name": "line_items",
                "description": "A list of line items the customer is being quoted for. Each line item includes information about the product, the quantity, and the resulting cost."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "on_behalf_of",
                "description": "The account on behalf of which to charge."
            },
            {
                "name": "subscription_data",
                "description": "When creating a subscription or subscription schedule, the specified configuration data will be used. There must be at least one line item with a recurring price for a subscription or subscription schedule to be created. A subscription schedule is created if `subscription_data[effective_date]` is present and in the future, otherwise a subscription is created."
            },
            {
                "name": "test_clock",
                "description": "ID of the test clock to attach to the quote."
            },
            {
                "name": "transfer_data",
                "description": "The data with which to automatically create a Transfer for each of the invoices."
            }
        ]
    },
    {
        "path": "/v1/quotes/{quote}",
        "verb": "get",
        "op_id": "GetQuotesQuote",
        "summary": "Retrieve a quote",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/quotes/{quote}",
        "verb": "post",
        "op_id": "PostQuotesQuote",
        "summary": "Update a quote",
        "params": [
            {
                "name": "application_fee_amount",
                "description": "The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. There cannot be any line items with recurring prices when using this field."
            },
            {
                "name": "application_fee_percent",
                "description": "A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. There must be at least 1 line item with a recurring price to use this field."
            },
            {
                "name": "automatic_tax",
                "description": "Settings for automatic tax lookup for this quote and resulting invoices and subscriptions."
            },
            {
                "name": "collection_method",
                "description": "Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay invoices at the end of the subscription cycle or at invoice finalization using the default payment method attached to the subscription or customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`."
            },
            {
                "name": "customer",
                "description": "The customer for which this quote belongs to. A customer is required before finalizing the quote. Once specified, it cannot be changed."
            },
            {
                "name": "default_tax_rates",
                "description": "The tax rates that will apply to any line item that does not have `tax_rates` set."
            },
            {
                "name": "description",
                "description": "A description that will be displayed on the quote PDF."
            },
            {
                "name": "discounts",
                "description": "The discounts applied to the quote."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "expires_at",
                "description": "A future timestamp on which the quote will be canceled if in `open` or `draft` status. Measured in seconds since the Unix epoch."
            },
            {
                "name": "footer",
                "description": "A footer that will be displayed on the quote PDF."
            },
            {
                "name": "header",
                "description": "A header that will be displayed on the quote PDF."
            },
            {
                "name": "invoice_settings",
                "description": "All invoices will be billed using the specified settings."
            },
            {
                "name": "line_items",
                "description": "A list of line items the customer is being quoted for. Each line item includes information about the product, the quantity, and the resulting cost."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "on_behalf_of",
                "description": "The account on behalf of which to charge."
            },
            {
                "name": "subscription_data",
                "description": "When creating a subscription or subscription schedule, the specified configuration data will be used. There must be at least one line item with a recurring price for a subscription or subscription schedule to be created. A subscription schedule is created if `subscription_data[effective_date]` is present and in the future, otherwise a subscription is created."
            },
            {
                "name": "transfer_data",
                "description": "The data with which to automatically create a Transfer for each of the invoices."
            }
        ]
    },
    {
        "path": "/v1/quotes/{quote}/accept",
        "verb": "post",
        "op_id": "PostQuotesQuoteAccept",
        "summary": "Accept a quote",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/quotes/{quote}/cancel",
        "verb": "post",
        "op_id": "PostQuotesQuoteCancel",
        "summary": "Cancel a quote",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/quotes/{quote}/computed_upfront_line_items",
        "verb": "get",
        "op_id": "GetQuotesQuoteComputedUpfrontLineItems",
        "summary": "Retrieve a quote's upfront line items",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/quotes/{quote}/finalize",
        "verb": "post",
        "op_id": "PostQuotesQuoteFinalize",
        "summary": "Finalize a quote",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "expires_at",
                "description": "A future timestamp on which the quote will be canceled if in `open` or `draft` status. Measured in seconds since the Unix epoch."
            }
        ]
    },
    {
        "path": "/v1/quotes/{quote}/line_items",
        "verb": "get",
        "op_id": "GetQuotesQuoteLineItems",
        "summary": "Retrieve a quote's line items",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/quotes/{quote}/pdf",
        "verb": "get",
        "op_id": "GetQuotesQuotePdf",
        "summary": "Download quote PDF",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/radar/early_fraud_warnings",
        "verb": "get",
        "op_id": "GetRadarEarlyFraudWarnings",
        "summary": "List all early fraud warnings",
        "params": [
            {
                "name": "charge",
                "description": "Only return early fraud warnings for the charge specified by this charge ID."
            },
            {
                "name": "created",
                "description": "Only return early fraud warnings that were created during the given date interval."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "payment_intent",
                "description": "Only return early fraud warnings for charges that were created by the PaymentIntent specified by this PaymentIntent ID."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/radar/early_fraud_warnings/{early_fraud_warning}",
        "verb": "get",
        "op_id": "GetRadarEarlyFraudWarningsEarlyFraudWarning",
        "summary": "Retrieve an early fraud warning",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/radar/value_list_items",
        "verb": "get",
        "op_id": "GetRadarValueListItems",
        "summary": "List all value list items",
        "params": [
            {
                "name": "created",
                "description": "Only return items that were created during the given date interval."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "value",
                "description": "Return items belonging to the parent list whose value matches the specified value (using an \"is like\" match)."
            },
            {
                "name": "value_list",
                "description": "Identifier for the parent value list this item belongs to."
            }
        ]
    },
    {
        "path": "/v1/radar/value_list_items",
        "verb": "post",
        "op_id": "PostRadarValueListItems",
        "summary": "Create a value list item",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "value",
                "description": "The value of the item (whose type must match the type of the parent value list)."
            },
            {
                "name": "value_list",
                "description": "The identifier of the value list which the created item will be added to."
            }
        ]
    },
    {
        "path": "/v1/radar/value_list_items/{item}",
        "verb": "delete",
        "op_id": "DeleteRadarValueListItemsItem",
        "summary": "Delete a value list item",
        "params": []
    },
    {
        "path": "/v1/radar/value_list_items/{item}",
        "verb": "get",
        "op_id": "GetRadarValueListItemsItem",
        "summary": "Retrieve a value list item",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/radar/value_lists",
        "verb": "get",
        "op_id": "GetRadarValueLists",
        "summary": "List all value lists",
        "params": [
            {
                "name": "alias",
                "description": "The alias used to reference the value list when writing rules."
            },
            {
                "name": "contains",
                "description": "A value contained within a value list - returns all value lists containing this value."
            },
            {
                "name": "created",
                "description": "Only return value lists that were created during the given date interval."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/radar/value_lists",
        "verb": "post",
        "op_id": "PostRadarValueLists",
        "summary": "Create a value list",
        "params": [
            {
                "name": "alias",
                "description": "The name of the value list for use in rules."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "item_type",
                "description": "Type of the items in the value list. One of `card_fingerprint`, `us_bank_account_fingerprint`, `sepa_debit_fingerprint`, `card_bin`, `email`, `ip_address`, `country`, `string`, `case_sensitive_string`, or `customer_id`. Use `string` if the item type is unknown or mixed."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "name",
                "description": "The human-readable name of the value list."
            }
        ]
    },
    {
        "path": "/v1/radar/value_lists/{value_list}",
        "verb": "delete",
        "op_id": "DeleteRadarValueListsValueList",
        "summary": "Delete a value list",
        "params": []
    },
    {
        "path": "/v1/radar/value_lists/{value_list}",
        "verb": "get",
        "op_id": "GetRadarValueListsValueList",
        "summary": "Retrieve a value list",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/radar/value_lists/{value_list}",
        "verb": "post",
        "op_id": "PostRadarValueListsValueList",
        "summary": "Update a value list",
        "params": [
            {
                "name": "alias",
                "description": "The name of the value list for use in rules."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "name",
                "description": "The human-readable name of the value list."
            }
        ]
    },
    {
        "path": "/v1/refunds",
        "verb": "get",
        "op_id": "GetRefunds",
        "summary": "List all refunds",
        "params": [
            {
                "name": "charge",
                "description": "Only return refunds for the charge specified by this charge ID."
            },
            {
                "name": "created",
                "description": "Only return refunds that were created during the given date interval."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "payment_intent",
                "description": "Only return refunds for the PaymentIntent specified by this ID."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/refunds",
        "verb": "post",
        "op_id": "PostRefunds",
        "summary": "Create customer balance refund",
        "params": [
            {
                "name": "amount",
                "description": ""
            },
            {
                "name": "charge",
                "description": "The identifier of the charge to refund."
            },
            {
                "name": "currency",
                "description": "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "customer",
                "description": "Customer whose customer balance to refund from."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "instructions_email",
                "description": "For payment methods without native refund support (e.g., Konbini, PromptPay), use this email from the customer to receive refund instructions."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "origin",
                "description": "Origin of the refund"
            },
            {
                "name": "payment_intent",
                "description": "The identifier of the PaymentIntent to refund."
            },
            {
                "name": "reason",
                "description": "String indicating the reason for the refund. If set, possible values are `duplicate`, `fraudulent`, and `requested_by_customer`. If you believe the charge to be fraudulent, specifying `fraudulent` as the reason will add the associated card and email to your [block lists](https://stripe.com/docs/radar/lists), and will also help us improve our fraud detection algorithms."
            },
            {
                "name": "refund_application_fee",
                "description": "Boolean indicating whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded. An application fee can be refunded only by the application that created the charge."
            },
            {
                "name": "reverse_transfer",
                "description": "Boolean indicating whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount).<br><br>A transfer can be reversed only by the application that created the charge."
            }
        ]
    },
    {
        "path": "/v1/refunds/{refund}",
        "verb": "get",
        "op_id": "GetRefundsRefund",
        "summary": "Retrieve a refund",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/refunds/{refund}",
        "verb": "post",
        "op_id": "PostRefundsRefund",
        "summary": "Update a refund",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            }
        ]
    },
    {
        "path": "/v1/refunds/{refund}/cancel",
        "verb": "post",
        "op_id": "PostRefundsRefundCancel",
        "summary": "Cancel a refund",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/reporting/report_runs",
        "verb": "get",
        "op_id": "GetReportingReportRuns",
        "summary": "List all Report Runs",
        "params": [
            {
                "name": "created",
                "description": "Only return Report Runs that were created during the given date interval."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/reporting/report_runs",
        "verb": "post",
        "op_id": "PostReportingReportRuns",
        "summary": "Create a Report Run",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "parameters",
                "description": "Parameters specifying how the report should be run. Different Report Types have different required and optional parameters, listed in the [API Access to Reports](https://stripe.com/docs/reporting/statements/api) documentation."
            },
            {
                "name": "report_type",
                "description": "The ID of the [report type](https://stripe.com/docs/reporting/statements/api#report-types) to run, such as `\"balance.summary.1\"`."
            }
        ]
    },
    {
        "path": "/v1/reporting/report_runs/{report_run}",
        "verb": "get",
        "op_id": "GetReportingReportRunsReportRun",
        "summary": "Retrieve a Report Run",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/reporting/report_types",
        "verb": "get",
        "op_id": "GetReportingReportTypes",
        "summary": "List all Report Types",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/reporting/report_types/{report_type}",
        "verb": "get",
        "op_id": "GetReportingReportTypesReportType",
        "summary": "Retrieve a Report Type",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/reviews",
        "verb": "get",
        "op_id": "GetReviews",
        "summary": "List all open reviews",
        "params": [
            {
                "name": "created",
                "description": "Only return reviews that were created during the given date interval."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/reviews/{review}",
        "verb": "get",
        "op_id": "GetReviewsReview",
        "summary": "Retrieve a review",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/reviews/{review}/approve",
        "verb": "post",
        "op_id": "PostReviewsReviewApprove",
        "summary": "Approve a review",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/setup_attempts",
        "verb": "get",
        "op_id": "GetSetupAttempts",
        "summary": "List all SetupAttempts",
        "params": [
            {
                "name": "created",
                "description": "A filter on the list, based on the object `created` field. The value\ncan be a string with an integer Unix timestamp or a\ndictionary with a number of different query options."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "setup_intent",
                "description": "Only return SetupAttempts created by the SetupIntent specified by\nthis ID."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/setup_intents",
        "verb": "get",
        "op_id": "GetSetupIntents",
        "summary": "List all SetupIntents",
        "params": [
            {
                "name": "attach_to_self",
                "description": "If present, the SetupIntent's payment method will be attached to the in-context Stripe Account.\n\nIt can only be used for this Stripe Account\u2019s own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer."
            },
            {
                "name": "created",
                "description": "A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options."
            },
            {
                "name": "customer",
                "description": "Only return SetupIntents for the customer specified by this customer ID."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "payment_method",
                "description": "Only return SetupIntents that associate with the specified payment method."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/setup_intents",
        "verb": "post",
        "op_id": "PostSetupIntents",
        "summary": "Create a SetupIntent",
        "params": [
            {
                "name": "attach_to_self",
                "description": "If present, the SetupIntent's payment method will be attached to the in-context Stripe Account.\n\nIt can only be used for this Stripe Account\u2019s own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer."
            },
            {
                "name": "automatic_payment_methods",
                "description": "When you enable this parameter, this SetupIntent accepts payment methods that you enable in the Dashboard and that are compatible with its other parameters."
            },
            {
                "name": "confirm",
                "description": "Set to `true` to attempt to confirm this SetupIntent immediately. This parameter defaults to `false`. If a card is the attached payment method, you can provide a `return_url` in case further authentication is necessary."
            },
            {
                "name": "confirmation_token",
                "description": "ID of the ConfirmationToken used to confirm this SetupIntent.\n\nIf the provided ConfirmationToken contains properties that are also being provided in this request, such as `payment_method`, then the values in this request will take precedence."
            },
            {
                "name": "customer",
                "description": "ID of the Customer this SetupIntent belongs to, if one exists.\n\nIf present, the SetupIntent's payment method will be attached to the Customer on successful setup. Payment methods attached to other Customers cannot be used with this SetupIntent."
            },
            {
                "name": "description",
                "description": "An arbitrary string attached to the object. Often useful for displaying to users."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "flow_directions",
                "description": "Indicates the directions of money movement for which this payment method is intended to be used.\n\nInclude `inbound` if you intend to use the payment method as the origin to pull funds from. Include `outbound` if you intend to use the payment method as the destination to send funds to. You can include both if you intend to use the payment method for both purposes."
            },
            {
                "name": "mandate_data",
                "description": "This hash contains details about the mandate to create. This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/setup_intents/create#create_setup_intent-confirm)."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "on_behalf_of",
                "description": "The Stripe account ID created for this SetupIntent."
            },
            {
                "name": "payment_method",
                "description": "ID of the payment method (a PaymentMethod, Card, or saved Source object) to attach to this SetupIntent."
            },
            {
                "name": "payment_method_configuration",
                "description": "The ID of the [payment method configuration](https://stripe.com/docs/api/payment_method_configurations) to use with this SetupIntent."
            },
            {
                "name": "payment_method_data",
                "description": "When included, this hash creates a PaymentMethod that is set as the [`payment_method`](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-payment_method)\nvalue in the SetupIntent."
            },
            {
                "name": "payment_method_options",
                "description": "Payment method-specific configuration for this SetupIntent."
            },
            {
                "name": "payment_method_types",
                "description": "The list of payment method types (for example, card) that this SetupIntent can use. If you don't provide this, Stripe will dynamically show relevant payment methods from your [payment method settings](https://dashboard.stripe.com/settings/payment_methods)."
            },
            {
                "name": "return_url",
                "description": "The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method's app or site. To redirect to a mobile application, you can alternatively supply an application URI scheme. This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/setup_intents/create#create_setup_intent-confirm)."
            },
            {
                "name": "single_use",
                "description": "If you populate this hash, this SetupIntent generates a `single_use` mandate after successful completion.\n\nSingle-use mandates are only valid for the following payment methods: `acss_debit`, `alipay`, `au_becs_debit`, `bacs_debit`, `bancontact`, `boleto`, `ideal`, `link`, `sepa_debit`, and `us_bank_account`."
            },
            {
                "name": "usage",
                "description": "Indicates how the payment method is intended to be used in the future. If not provided, this value defaults to `off_session`."
            },
            {
                "name": "use_stripe_sdk",
                "description": "Set to `true` when confirming server-side and using Stripe.js, iOS, or Android client-side SDKs to handle the next actions."
            }
        ]
    },
    {
        "path": "/v1/setup_intents/{intent}",
        "verb": "get",
        "op_id": "GetSetupIntentsIntent",
        "summary": "Retrieve a SetupIntent",
        "params": [
            {
                "name": "client_secret",
                "description": "The client secret of the SetupIntent. We require this string if you use a publishable key to retrieve the SetupIntent."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/setup_intents/{intent}",
        "verb": "post",
        "op_id": "PostSetupIntentsIntent",
        "summary": "Update a SetupIntent",
        "params": [
            {
                "name": "attach_to_self",
                "description": "If present, the SetupIntent's payment method will be attached to the in-context Stripe Account.\n\nIt can only be used for this Stripe Account\u2019s own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer."
            },
            {
                "name": "customer",
                "description": "ID of the Customer this SetupIntent belongs to, if one exists.\n\nIf present, the SetupIntent's payment method will be attached to the Customer on successful setup. Payment methods attached to other Customers cannot be used with this SetupIntent."
            },
            {
                "name": "description",
                "description": "An arbitrary string attached to the object. Often useful for displaying to users."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "flow_directions",
                "description": "Indicates the directions of money movement for which this payment method is intended to be used.\n\nInclude `inbound` if you intend to use the payment method as the origin to pull funds from. Include `outbound` if you intend to use the payment method as the destination to send funds to. You can include both if you intend to use the payment method for both purposes."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "payment_method",
                "description": "ID of the payment method (a PaymentMethod, Card, or saved Source object) to attach to this SetupIntent. To unset this field to null, pass in an empty string."
            },
            {
                "name": "payment_method_configuration",
                "description": "The ID of the [payment method configuration](https://stripe.com/docs/api/payment_method_configurations) to use with this SetupIntent."
            },
            {
                "name": "payment_method_data",
                "description": "When included, this hash creates a PaymentMethod that is set as the [`payment_method`](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-payment_method)\nvalue in the SetupIntent."
            },
            {
                "name": "payment_method_options",
                "description": "Payment method-specific configuration for this SetupIntent."
            },
            {
                "name": "payment_method_types",
                "description": "The list of payment method types (for example, card) that this SetupIntent can set up. If you don't provide this, Stripe will dynamically show relevant payment methods from your [payment method settings](https://dashboard.stripe.com/settings/payment_methods)."
            }
        ]
    },
    {
        "path": "/v1/setup_intents/{intent}/cancel",
        "verb": "post",
        "op_id": "PostSetupIntentsIntentCancel",
        "summary": "Cancel a SetupIntent",
        "params": [
            {
                "name": "cancellation_reason",
                "description": "Reason for canceling this SetupIntent. Possible values are: `abandoned`, `requested_by_customer`, or `duplicate`"
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/setup_intents/{intent}/confirm",
        "verb": "post",
        "op_id": "PostSetupIntentsIntentConfirm",
        "summary": "Confirm a SetupIntent",
        "params": [
            {
                "name": "client_secret",
                "description": "The client secret of the SetupIntent."
            },
            {
                "name": "confirmation_token",
                "description": "ID of the ConfirmationToken used to confirm this SetupIntent.\n\nIf the provided ConfirmationToken contains properties that are also being provided in this request, such as `payment_method`, then the values in this request will take precedence."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "mandate_data",
                "description": ""
            },
            {
                "name": "payment_method",
                "description": "ID of the payment method (a PaymentMethod, Card, or saved Source object) to attach to this SetupIntent."
            },
            {
                "name": "payment_method_data",
                "description": "When included, this hash creates a PaymentMethod that is set as the [`payment_method`](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-payment_method)\nvalue in the SetupIntent."
            },
            {
                "name": "payment_method_options",
                "description": "Payment method-specific configuration for this SetupIntent."
            },
            {
                "name": "return_url",
                "description": "The URL to redirect your customer back to after they authenticate on the payment method's app or site.\nIf you'd prefer to redirect to a mobile application, you can alternatively supply an application URI scheme.\nThis parameter is only used for cards and other redirect-based payment methods."
            },
            {
                "name": "use_stripe_sdk",
                "description": "Set to `true` when confirming server-side and using Stripe.js, iOS, or Android client-side SDKs to handle the next actions."
            }
        ]
    },
    {
        "path": "/v1/setup_intents/{intent}/verify_microdeposits",
        "verb": "post",
        "op_id": "PostSetupIntentsIntentVerifyMicrodeposits",
        "summary": "Verify microdeposits on a SetupIntent",
        "params": [
            {
                "name": "amounts",
                "description": "Two positive integers, in *cents*, equal to the values of the microdeposits sent to the bank account."
            },
            {
                "name": "client_secret",
                "description": "The client secret of the SetupIntent."
            },
            {
                "name": "descriptor_code",
                "description": "A six-character code starting with SM present in the microdeposit sent to the bank account."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/shipping_rates",
        "verb": "get",
        "op_id": "GetShippingRates",
        "summary": "List all shipping rates",
        "params": [
            {
                "name": "active",
                "description": "Only return shipping rates that are active or inactive."
            },
            {
                "name": "created",
                "description": "A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options."
            },
            {
                "name": "currency",
                "description": "Only return shipping rates for the given currency."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/shipping_rates",
        "verb": "post",
        "op_id": "PostShippingRates",
        "summary": "Create a shipping rate",
        "params": [
            {
                "name": "delivery_estimate",
                "description": "The estimated range for how long shipping will take, meant to be displayable to the customer. This will appear on CheckoutSessions."
            },
            {
                "name": "display_name",
                "description": "The name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "fixed_amount",
                "description": "Describes a fixed amount to charge for shipping. Must be present if type is `fixed_amount`."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "tax_behavior",
                "description": "Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`."
            },
            {
                "name": "tax_code",
                "description": "A [tax code](https://stripe.com/docs/tax/tax-categories) ID. The Shipping tax code is `txcd_92010001`."
            },
            {
                "name": "type",
                "description": "The type of calculation to use on the shipping rate."
            }
        ]
    },
    {
        "path": "/v1/shipping_rates/{shipping_rate_token}",
        "verb": "get",
        "op_id": "GetShippingRatesShippingRateToken",
        "summary": "Retrieve a shipping rate",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/shipping_rates/{shipping_rate_token}",
        "verb": "post",
        "op_id": "PostShippingRatesShippingRateToken",
        "summary": "Update a shipping rate",
        "params": [
            {
                "name": "active",
                "description": "Whether the shipping rate can be used for new purchases. Defaults to `true`."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "fixed_amount",
                "description": "Describes a fixed amount to charge for shipping. Must be present if type is `fixed_amount`."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "tax_behavior",
                "description": "Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`."
            }
        ]
    },
    {
        "path": "/v1/sigma/saved_queries/{id}",
        "verb": "post",
        "op_id": "PostSigmaSavedQueriesId",
        "summary": "Update an existing Sigma Query",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "name",
                "description": "The name of the query to update."
            },
            {
                "name": "sql",
                "description": "The sql statement to update the specified query statement with. This should be a valid Trino SQL statement that can be run in Sigma."
            }
        ]
    },
    {
        "path": "/v1/sigma/scheduled_query_runs",
        "verb": "get",
        "op_id": "GetSigmaScheduledQueryRuns",
        "summary": "List all scheduled query runs",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/sigma/scheduled_query_runs/{scheduled_query_run}",
        "verb": "get",
        "op_id": "GetSigmaScheduledQueryRunsScheduledQueryRun",
        "summary": "Retrieve a scheduled query run",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/sources",
        "verb": "post",
        "op_id": "PostSources",
        "summary": "Shares a source",
        "params": [
            {
                "name": "amount",
                "description": "Amount associated with the source. This is the amount for which the source will be chargeable once ready. Required for `single_use` sources. Not supported for `receiver` type sources, where charge amount may not be specified until funds land."
            },
            {
                "name": "currency",
                "description": "Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) associated with the source. This is the currency for which the source will be chargeable once ready."
            },
            {
                "name": "customer",
                "description": "The `Customer` to whom the original source is attached to. Must be set when the original source is not a `Source` (e.g., `Card`)."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "flow",
                "description": "The authentication `flow` of the source to create. `flow` is one of `redirect`, `receiver`, `code_verification`, `none`. It is generally inferred unless a type supports multiple flows."
            },
            {
                "name": "mandate",
                "description": "Information about a mandate possibility attached to a source object (generally for bank debits) as well as its acceptance status."
            },
            {
                "name": "metadata",
                "description": ""
            },
            {
                "name": "original_source",
                "description": "The source to share."
            },
            {
                "name": "owner",
                "description": "Information about the owner of the payment instrument that may be used or required by particular source types."
            },
            {
                "name": "receiver",
                "description": "Optional parameters for the receiver flow. Can be set only if the source is a receiver (`flow` is `receiver`)."
            },
            {
                "name": "redirect",
                "description": "Parameters required for the redirect flow. Required if the source is authenticated by a redirect (`flow` is `redirect`)."
            },
            {
                "name": "source_order",
                "description": "Information about the items and shipping associated with the source. Required for transactional credit (for example Klarna) sources before you can charge it."
            },
            {
                "name": "statement_descriptor",
                "description": "An arbitrary string to be displayed on your customer's statement. As an example, if your website is `RunClub` and the item you're charging for is a race ticket, you may want to specify a `statement_descriptor` of `RunClub 5K race ticket.` While many payment types will display this information, some may not display it at all."
            },
            {
                "name": "token",
                "description": "An optional token used to create the source. When passed, token properties will override source parameters."
            },
            {
                "name": "type",
                "description": "The `type` of the source to create. Required unless `customer` and `original_source` are specified (see the [Cloning card Sources](https://stripe.com/docs/sources/connect#cloning-card-sources) guide)"
            },
            {
                "name": "usage",
                "description": ""
            }
        ]
    },
    {
        "path": "/v1/sources/{source}",
        "verb": "get",
        "op_id": "GetSourcesSource",
        "summary": "Retrieve a source",
        "params": [
            {
                "name": "client_secret",
                "description": "The client secret of the source. Required if a publishable key is used to retrieve the source."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/sources/{source}",
        "verb": "post",
        "op_id": "PostSourcesSource",
        "summary": "Update a source",
        "params": [
            {
                "name": "amount",
                "description": "Amount associated with the source."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "mandate",
                "description": "Information about a mandate possibility attached to a source object (generally for bank debits) as well as its acceptance status."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "owner",
                "description": "Information about the owner of the payment instrument that may be used or required by particular source types."
            },
            {
                "name": "source_order",
                "description": "Information about the items and shipping associated with the source. Required for transactional credit (for example Klarna) sources before you can charge it."
            }
        ]
    },
    {
        "path": "/v1/sources/{source}/mandate_notifications/{mandate_notification}",
        "verb": "get",
        "op_id": "GetSourcesSourceMandateNotificationsMandateNotification",
        "summary": "Retrieve a Source MandateNotification",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/sources/{source}/source_transactions",
        "verb": "get",
        "op_id": "GetSourcesSourceSourceTransactions",
        "summary": "",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/sources/{source}/source_transactions/{source_transaction}",
        "verb": "get",
        "op_id": "GetSourcesSourceSourceTransactionsSourceTransaction",
        "summary": "Retrieve a source transaction",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/sources/{source}/verify",
        "verb": "post",
        "op_id": "PostSourcesSourceVerify",
        "summary": "",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "values",
                "description": "The values needed to verify the source."
            }
        ]
    },
    {
        "path": "/v1/subscription_items",
        "verb": "get",
        "op_id": "GetSubscriptionItems",
        "summary": "List all subscription items",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "subscription",
                "description": "The ID of the subscription whose items will be retrieved."
            }
        ]
    },
    {
        "path": "/v1/subscription_items",
        "verb": "post",
        "op_id": "PostSubscriptionItems",
        "summary": "Create a subscription item",
        "params": [
            {
                "name": "billing_thresholds",
                "description": "Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. Pass an empty string to remove previously-defined thresholds."
            },
            {
                "name": "discounts",
                "description": "The coupons to redeem into discounts for the subscription item."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "payment_behavior",
                "description": "Use `allow_incomplete` to transition the subscription to `status=past_due` if a payment is required but cannot be paid. This allows you to manage scenarios where additional user actions are needed to pay a subscription's invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication) for Billing to learn more. This is the default behavior.\n\nUse `default_incomplete` to transition the subscription to `status=past_due` when payment is required and await explicit confirmation of the invoice's payment intent. This allows simpler management of scenarios where additional user actions are needed to pay a subscription\u2019s invoice. Such as failed payments, [SCA regulation](https://stripe.com/docs/billing/migration/strong-customer-authentication), or collecting a mandate for a bank debit payment method.\n\nUse `pending_if_incomplete` to update the subscription using [pending updates](https://stripe.com/docs/billing/subscriptions/pending-updates). When you use `pending_if_incomplete` you can only pass the parameters [supported by pending updates](https://stripe.com/docs/billing/pending-updates-reference#supported-attributes).\n\nUse `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription's invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not update the subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://stripe.com/docs/upgrades#2019-03-14) to learn more."
            },
            {
                "name": "price",
                "description": "The ID of the price object."
            },
            {
                "name": "price_data",
                "description": "Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline."
            },
            {
                "name": "proration_behavior",
                "description": "Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`."
            },
            {
                "name": "proration_date",
                "description": "If set, the proration will be calculated as though the subscription was updated at the given time. This can be used to apply the same proration that was previewed with the [upcoming invoice](https://stripe.com/docs/api#retrieve_customer_invoice) endpoint."
            },
            {
                "name": "quantity",
                "description": "The quantity you'd like to apply to the subscription item you're creating."
            },
            {
                "name": "subscription",
                "description": "The identifier of the subscription to modify."
            },
            {
                "name": "tax_rates",
                "description": "A list of [Tax Rate](https://stripe.com/docs/api/tax_rates) ids. These Tax Rates will override the [`default_tax_rates`](https://stripe.com/docs/api/subscriptions/create#create_subscription-default_tax_rates) on the Subscription. When updating, pass an empty string to remove previously-defined tax rates."
            }
        ]
    },
    {
        "path": "/v1/subscription_items/{item}",
        "verb": "delete",
        "op_id": "DeleteSubscriptionItemsItem",
        "summary": "Delete a subscription item",
        "params": [
            {
                "name": "clear_usage",
                "description": "Delete all usage for the given subscription item. Allowed only when the current plan's `usage_type` is `metered`."
            },
            {
                "name": "proration_behavior",
                "description": "Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`."
            },
            {
                "name": "proration_date",
                "description": "If set, the proration will be calculated as though the subscription was updated at the given time. This can be used to apply the same proration that was previewed with the [upcoming invoice](https://stripe.com/docs/api#retrieve_customer_invoice) endpoint."
            }
        ]
    },
    {
        "path": "/v1/subscription_items/{item}",
        "verb": "get",
        "op_id": "GetSubscriptionItemsItem",
        "summary": "Retrieve a subscription item",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/subscription_items/{item}",
        "verb": "post",
        "op_id": "PostSubscriptionItemsItem",
        "summary": "Update a subscription item",
        "params": [
            {
                "name": "billing_thresholds",
                "description": "Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. Pass an empty string to remove previously-defined thresholds."
            },
            {
                "name": "discounts",
                "description": "The coupons to redeem into discounts for the subscription item."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "off_session",
                "description": "Indicates if a customer is on or off-session while an invoice payment is attempted. Defaults to `false` (on-session)."
            },
            {
                "name": "payment_behavior",
                "description": "Use `allow_incomplete` to transition the subscription to `status=past_due` if a payment is required but cannot be paid. This allows you to manage scenarios where additional user actions are needed to pay a subscription's invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication) for Billing to learn more. This is the default behavior.\n\nUse `default_incomplete` to transition the subscription to `status=past_due` when payment is required and await explicit confirmation of the invoice's payment intent. This allows simpler management of scenarios where additional user actions are needed to pay a subscription\u2019s invoice. Such as failed payments, [SCA regulation](https://stripe.com/docs/billing/migration/strong-customer-authentication), or collecting a mandate for a bank debit payment method.\n\nUse `pending_if_incomplete` to update the subscription using [pending updates](https://stripe.com/docs/billing/subscriptions/pending-updates). When you use `pending_if_incomplete` you can only pass the parameters [supported by pending updates](https://stripe.com/docs/billing/pending-updates-reference#supported-attributes).\n\nUse `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription's invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not update the subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://stripe.com/docs/upgrades#2019-03-14) to learn more."
            },
            {
                "name": "price",
                "description": "The ID of the price object. One of `price` or `price_data` is required. When changing a subscription item's price, `quantity` is set to 1 unless a `quantity` parameter is provided."
            },
            {
                "name": "price_data",
                "description": "Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline. One of `price` or `price_data` is required."
            },
            {
                "name": "proration_behavior",
                "description": "Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`."
            },
            {
                "name": "proration_date",
                "description": "If set, the proration will be calculated as though the subscription was updated at the given time. This can be used to apply the same proration that was previewed with the [upcoming invoice](https://stripe.com/docs/api#retrieve_customer_invoice) endpoint."
            },
            {
                "name": "quantity",
                "description": "The quantity you'd like to apply to the subscription item you're creating."
            },
            {
                "name": "tax_rates",
                "description": "A list of [Tax Rate](https://stripe.com/docs/api/tax_rates) ids. These Tax Rates will override the [`default_tax_rates`](https://stripe.com/docs/api/subscriptions/create#create_subscription-default_tax_rates) on the Subscription. When updating, pass an empty string to remove previously-defined tax rates."
            }
        ]
    },
    {
        "path": "/v1/subscription_schedules",
        "verb": "get",
        "op_id": "GetSubscriptionSchedules",
        "summary": "List all schedules",
        "params": [
            {
                "name": "canceled_at",
                "description": "Only return subscription schedules that were created canceled the given date interval."
            },
            {
                "name": "completed_at",
                "description": "Only return subscription schedules that completed during the given date interval."
            },
            {
                "name": "created",
                "description": "Only return subscription schedules that were created during the given date interval."
            },
            {
                "name": "customer",
                "description": "Only return subscription schedules for the given customer."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "released_at",
                "description": "Only return subscription schedules that were released during the given date interval."
            },
            {
                "name": "scheduled",
                "description": "Only return subscription schedules that have not started yet."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/subscription_schedules",
        "verb": "post",
        "op_id": "PostSubscriptionSchedules",
        "summary": "Create a schedule",
        "params": [
            {
                "name": "customer",
                "description": "The identifier of the customer to create the subscription schedule for."
            },
            {
                "name": "default_settings",
                "description": "Object representing the subscription schedule's default settings."
            },
            {
                "name": "end_behavior",
                "description": "Behavior of the subscription schedule and underlying subscription when it ends. Possible values are `release` or `cancel` with the default being `release`. `release` will end the subscription schedule and keep the underlying subscription running. `cancel` will end the subscription schedule and cancel the underlying subscription."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "from_subscription",
                "description": "Migrate an existing subscription to be managed by a subscription schedule. If this parameter is set, a subscription schedule will be created using the subscription's item(s), set to auto-renew using the subscription's interval. When using this parameter, other parameters (such as phase values) cannot be set. To create a subscription schedule with other modifications, we recommend making two separate API calls."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "phases",
                "description": "List representing phases of the subscription schedule. Each phase can be customized to have different durations, plans, and coupons. If there are multiple phases, the `end_date` of one phase will always equal the `start_date` of the next phase."
            },
            {
                "name": "start_date",
                "description": "When the subscription schedule starts. We recommend using `now` so that it starts the subscription immediately. You can also use a Unix timestamp to backdate the subscription so that it starts on a past date, or set a future date for the subscription to start on."
            }
        ]
    },
    {
        "path": "/v1/subscription_schedules/{schedule}",
        "verb": "get",
        "op_id": "GetSubscriptionSchedulesSchedule",
        "summary": "Retrieve a schedule",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/subscription_schedules/{schedule}",
        "verb": "post",
        "op_id": "PostSubscriptionSchedulesSchedule",
        "summary": "Update a schedule",
        "params": [
            {
                "name": "default_settings",
                "description": "Object representing the subscription schedule's default settings."
            },
            {
                "name": "end_behavior",
                "description": "Behavior of the subscription schedule and underlying subscription when it ends. Possible values are `release` or `cancel` with the default being `release`. `release` will end the subscription schedule and keep the underlying subscription running. `cancel` will end the subscription schedule and cancel the underlying subscription."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "phases",
                "description": "List representing phases of the subscription schedule. Each phase can be customized to have different durations, plans, and coupons. If there are multiple phases, the `end_date` of one phase will always equal the `start_date` of the next phase. Note that past phases can be omitted."
            },
            {
                "name": "proration_behavior",
                "description": "If the update changes the billing configuration (item price, quantity, etc.) of the current phase, indicates how prorations from this change should be handled. The default value is `create_prorations`."
            }
        ]
    },
    {
        "path": "/v1/subscription_schedules/{schedule}/cancel",
        "verb": "post",
        "op_id": "PostSubscriptionSchedulesScheduleCancel",
        "summary": "Cancel a schedule",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "invoice_now",
                "description": "If the subscription schedule is `active`, indicates if a final invoice will be generated that contains any un-invoiced metered usage and new/pending proration invoice items. Defaults to `true`."
            },
            {
                "name": "prorate",
                "description": "If the subscription schedule is `active`, indicates if the cancellation should be prorated. Defaults to `true`."
            }
        ]
    },
    {
        "path": "/v1/subscription_schedules/{schedule}/release",
        "verb": "post",
        "op_id": "PostSubscriptionSchedulesScheduleRelease",
        "summary": "Release a schedule",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "preserve_cancel_date",
                "description": "Keep any cancellation on the subscription that the schedule has set"
            }
        ]
    },
    {
        "path": "/v1/subscriptions",
        "verb": "get",
        "op_id": "GetSubscriptions",
        "summary": "List subscriptions",
        "params": [
            {
                "name": "automatic_tax",
                "description": "Filter subscriptions by their automatic tax settings."
            },
            {
                "name": "collection_method",
                "description": "The collection method of the subscriptions to retrieve. Either `charge_automatically` or `send_invoice`."
            },
            {
                "name": "created",
                "description": "Only return subscriptions that were created during the given date interval."
            },
            {
                "name": "current_period_end",
                "description": "Only return subscriptions whose current_period_end falls within the given date interval."
            },
            {
                "name": "current_period_start",
                "description": "Only return subscriptions whose current_period_start falls within the given date interval."
            },
            {
                "name": "customer",
                "description": "The ID of the customer whose subscriptions will be retrieved."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "price",
                "description": "Filter for subscriptions that contain this recurring price ID."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "status",
                "description": "The status of the subscriptions to retrieve. Passing in a value of `canceled` will return all canceled subscriptions, including those belonging to deleted customers. Pass `ended` to find subscriptions that are canceled and subscriptions that are expired due to [incomplete payment](https://stripe.com/docs/billing/subscriptions/overview#subscription-statuses). Passing in a value of `all` will return subscriptions of all statuses. If no value is supplied, all subscriptions that have not been canceled are returned."
            },
            {
                "name": "test_clock",
                "description": "Filter for subscriptions that are associated with the specified test clock. The response will not include subscriptions with test clocks if this and the customer parameter is not set."
            }
        ]
    },
    {
        "path": "/v1/subscriptions",
        "verb": "post",
        "op_id": "PostSubscriptions",
        "summary": "Create a subscription",
        "params": [
            {
                "name": "add_invoice_items",
                "description": "A list of prices and quantities that will generate invoice items appended to the next invoice for this subscription. You may pass up to 20 items."
            },
            {
                "name": "application_fee_percent",
                "description": "A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions)."
            },
            {
                "name": "automatic_tax",
                "description": "Automatic tax settings for this subscription. We recommend you only include this parameter when the existing value is being changed."
            },
            {
                "name": "backdate_start_date",
                "description": "For new subscriptions, a past timestamp to backdate the subscription's start date to. If set, the first invoice will contain a proration for the timespan between the start date and the current time. Can be combined with trials and the billing cycle anchor."
            },
            {
                "name": "billing_cycle_anchor",
                "description": "A future timestamp in UTC format to anchor the subscription's [billing cycle](https://stripe.com/docs/subscriptions/billing-cycle). The anchor is the reference point that aligns future billing cycle dates. It sets the day of week for `week` intervals, the day of month for `month` and `year` intervals, and the month of year for `year` intervals."
            },
            {
                "name": "billing_cycle_anchor_config",
                "description": "Mutually exclusive with billing_cycle_anchor and only valid with monthly and yearly price intervals. When provided, the billing_cycle_anchor is set to the next occurence of the day_of_month at the hour, minute, and second UTC."
            },
            {
                "name": "billing_thresholds",
                "description": "Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. When updating, pass an empty string to remove previously-defined thresholds."
            },
            {
                "name": "cancel_at",
                "description": "A timestamp at which the subscription should cancel. If set to a date before the current period ends, this will cause a proration if prorations have been enabled using `proration_behavior`. If set during a future period, this will always cause a proration for that period."
            },
            {
                "name": "cancel_at_period_end",
                "description": "Indicate whether this subscription should cancel at the end of the current period (`current_period_end`). Defaults to `false`. This param will be removed in a future API version. Please use `cancel_at` instead."
            },
            {
                "name": "collection_method",
                "description": "Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`."
            },
            {
                "name": "currency",
                "description": "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "customer",
                "description": "The identifier of the customer to subscribe."
            },
            {
                "name": "days_until_due",
                "description": "Number of days a customer has to pay invoices generated by this subscription. Valid only for subscriptions where `collection_method` is set to `send_invoice`."
            },
            {
                "name": "default_payment_method",
                "description": "ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over `default_source`. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source)."
            },
            {
                "name": "default_source",
                "description": "ID of the default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If `default_payment_method` is also set, `default_payment_method` will take precedence. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source)."
            },
            {
                "name": "default_tax_rates",
                "description": "The tax rates that will apply to any subscription item that does not have `tax_rates` set. Invoices created will have their `default_tax_rates` populated from the subscription."
            },
            {
                "name": "description",
                "description": "The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs."
            },
            {
                "name": "discounts",
                "description": "The coupons to redeem into discounts for the subscription. If not specified or empty, inherits the discount from the subscription's customer."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "invoice_settings",
                "description": "All invoices will be billed using the specified settings."
            },
            {
                "name": "items",
                "description": "A list of up to 20 subscription items, each with an attached price."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "off_session",
                "description": "Indicates if a customer is on or off-session while an invoice payment is attempted. Defaults to `false` (on-session)."
            },
            {
                "name": "on_behalf_of",
                "description": "The account on behalf of which to charge, for each of the subscription's invoices."
            },
            {
                "name": "payment_behavior",
                "description": "Only applies to subscriptions with `collection_method=charge_automatically`.\n\nUse `allow_incomplete` to create Subscriptions with `status=incomplete` if the first invoice can't be paid. Creating Subscriptions with this status allows you to manage scenarios where additional customer actions are needed to pay a subscription's invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication) for Billing to learn more. This is the default behavior.\n\nUse `default_incomplete` to create Subscriptions with `status=incomplete` when the first invoice requires payment, otherwise start as active. Subscriptions transition to `status=active` when successfully confirming the PaymentIntent on the first invoice. This allows simpler management of scenarios where additional customer actions are needed to pay a subscription\u2019s invoice, such as failed payments, [SCA regulation](https://stripe.com/docs/billing/migration/strong-customer-authentication), or collecting a mandate for a bank debit payment method. If the PaymentIntent is not confirmed within 23 hours Subscriptions transition to `status=incomplete_expired`, which is a terminal state.\n\nUse `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription's first invoice can't be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further customer action is needed, this parameter doesn't create a Subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://stripe.com/docs/upgrades#2019-03-14) to learn more.\n\n`pending_if_incomplete` is only used with updates and cannot be passed when creating a Subscription.\n\nSubscriptions with `collection_method=send_invoice` are automatically activated regardless of the first Invoice status."
            },
            {
                "name": "payment_settings",
                "description": "Payment settings to pass to invoices created by the subscription."
            },
            {
                "name": "pending_invoice_item_interval",
                "description": "Specifies an interval for how often to bill for any pending invoice items. It is analogous to calling [Create an invoice](https://stripe.com/docs/api#create_invoice) for the given subscription at the specified interval."
            },
            {
                "name": "proration_behavior",
                "description": "Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) resulting from the `billing_cycle_anchor`. If no value is passed, the default is `create_prorations`."
            },
            {
                "name": "transfer_data",
                "description": "If specified, the funds from the subscription's invoices will be transferred to the destination and the ID of the resulting transfers will be found on the resulting charges."
            },
            {
                "name": "trial_end",
                "description": "Unix timestamp representing the end of the trial period the customer will get before being charged for the first time. If set, trial_end will override the default trial period of the plan the customer is being subscribed to. The special value `now` can be provided to end the customer's trial immediately. Can be at most two years from `billing_cycle_anchor`. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more."
            },
            {
                "name": "trial_from_plan",
                "description": "Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more."
            },
            {
                "name": "trial_period_days",
                "description": "Integer representing the number of trial period days before the customer is charged for the first time. This will always overwrite any trials that might apply via a subscribed plan. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more."
            },
            {
                "name": "trial_settings",
                "description": "Settings related to subscription trials."
            }
        ]
    },
    {
        "path": "/v1/subscriptions/search",
        "verb": "get",
        "op_id": "GetSubscriptionsSearch",
        "summary": "Search subscriptions",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "page",
                "description": "A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results."
            },
            {
                "name": "query",
                "description": "The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for subscriptions](https://stripe.com/docs/search#query-fields-for-subscriptions)."
            }
        ]
    },
    {
        "path": "/v1/subscriptions/{subscription_exposed_id}",
        "verb": "delete",
        "op_id": "DeleteSubscriptionsSubscriptionExposedId",
        "summary": "Cancel a subscription",
        "params": [
            {
                "name": "cancellation_details",
                "description": "Details about why this subscription was cancelled"
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "invoice_now",
                "description": "Will generate a final invoice that invoices for any un-invoiced metered usage and new/pending proration invoice items. Defaults to `false`."
            },
            {
                "name": "prorate",
                "description": "Will generate a proration invoice item that credits remaining unused time until the subscription period end. Defaults to `false`."
            }
        ]
    },
    {
        "path": "/v1/subscriptions/{subscription_exposed_id}",
        "verb": "get",
        "op_id": "GetSubscriptionsSubscriptionExposedId",
        "summary": "Retrieve a subscription",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/subscriptions/{subscription_exposed_id}",
        "verb": "post",
        "op_id": "PostSubscriptionsSubscriptionExposedId",
        "summary": "Update a subscription",
        "params": [
            {
                "name": "add_invoice_items",
                "description": "A list of prices and quantities that will generate invoice items appended to the next invoice for this subscription. You may pass up to 20 items."
            },
            {
                "name": "application_fee_percent",
                "description": "A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions)."
            },
            {
                "name": "automatic_tax",
                "description": "Automatic tax settings for this subscription. We recommend you only include this parameter when the existing value is being changed."
            },
            {
                "name": "billing_cycle_anchor",
                "description": "Either `now` or `unchanged`. Setting the value to `now` resets the subscription's billing cycle anchor to the current time (in UTC). For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle)."
            },
            {
                "name": "billing_thresholds",
                "description": "Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. When updating, pass an empty string to remove previously-defined thresholds."
            },
            {
                "name": "cancel_at",
                "description": "A timestamp at which the subscription should cancel. If set to a date before the current period ends, this will cause a proration if prorations have been enabled using `proration_behavior`. If set during a future period, this will always cause a proration for that period."
            },
            {
                "name": "cancel_at_period_end",
                "description": "Indicate whether this subscription should cancel at the end of the current period (`current_period_end`). Defaults to `false`. This param will be removed in a future API version. Please use `cancel_at` instead."
            },
            {
                "name": "cancellation_details",
                "description": "Details about why this subscription was cancelled"
            },
            {
                "name": "collection_method",
                "description": "Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`."
            },
            {
                "name": "days_until_due",
                "description": "Number of days a customer has to pay invoices generated by this subscription. Valid only for subscriptions where `collection_method` is set to `send_invoice`."
            },
            {
                "name": "default_payment_method",
                "description": "ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over `default_source`. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source)."
            },
            {
                "name": "default_source",
                "description": "ID of the default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If `default_payment_method` is also set, `default_payment_method` will take precedence. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source)."
            },
            {
                "name": "default_tax_rates",
                "description": "The tax rates that will apply to any subscription item that does not have `tax_rates` set. Invoices created will have their `default_tax_rates` populated from the subscription. Pass an empty string to remove previously-defined tax rates."
            },
            {
                "name": "description",
                "description": "The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs."
            },
            {
                "name": "discounts",
                "description": "The coupons to redeem into discounts for the subscription. If not specified or empty, inherits the discount from the subscription's customer."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "invoice_settings",
                "description": "All invoices will be billed using the specified settings."
            },
            {
                "name": "items",
                "description": "A list of up to 20 subscription items, each with an attached price."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "off_session",
                "description": "Indicates if a customer is on or off-session while an invoice payment is attempted. Defaults to `false` (on-session)."
            },
            {
                "name": "on_behalf_of",
                "description": "The account on behalf of which to charge, for each of the subscription's invoices."
            },
            {
                "name": "pause_collection",
                "description": "If specified, payment collection for this subscription will be paused. Note that the subscription status will be unchanged and will not be updated to `paused`. Learn more about [pausing collection](https://stripe.com/docs/billing/subscriptions/pause-payment)."
            },
            {
                "name": "payment_behavior",
                "description": "Use `allow_incomplete` to transition the subscription to `status=past_due` if a payment is required but cannot be paid. This allows you to manage scenarios where additional user actions are needed to pay a subscription's invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication) for Billing to learn more. This is the default behavior.\n\nUse `default_incomplete` to transition the subscription to `status=past_due` when payment is required and await explicit confirmation of the invoice's payment intent. This allows simpler management of scenarios where additional user actions are needed to pay a subscription\u2019s invoice. Such as failed payments, [SCA regulation](https://stripe.com/docs/billing/migration/strong-customer-authentication), or collecting a mandate for a bank debit payment method.\n\nUse `pending_if_incomplete` to update the subscription using [pending updates](https://stripe.com/docs/billing/subscriptions/pending-updates). When you use `pending_if_incomplete` you can only pass the parameters [supported by pending updates](https://stripe.com/docs/billing/pending-updates-reference#supported-attributes).\n\nUse `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription's invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not update the subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://stripe.com/docs/upgrades#2019-03-14) to learn more."
            },
            {
                "name": "payment_settings",
                "description": "Payment settings to pass to invoices created by the subscription."
            },
            {
                "name": "pending_invoice_item_interval",
                "description": "Specifies an interval for how often to bill for any pending invoice items. It is analogous to calling [Create an invoice](https://stripe.com/docs/api#create_invoice) for the given subscription at the specified interval."
            },
            {
                "name": "proration_behavior",
                "description": "Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`."
            },
            {
                "name": "proration_date",
                "description": "If set, prorations will be calculated as though the subscription was updated at the given time. This can be used to apply exactly the same prorations that were previewed with the [create preview](https://stripe.com/docs/api/invoices/create_preview) endpoint. `proration_date` can also be used to implement custom proration logic, such as prorating by day instead of by second, by providing the time that you wish to use for proration calculations."
            },
            {
                "name": "transfer_data",
                "description": "If specified, the funds from the subscription's invoices will be transferred to the destination and the ID of the resulting transfers will be found on the resulting charges. This will be unset if you POST an empty value."
            },
            {
                "name": "trial_end",
                "description": "Unix timestamp representing the end of the trial period the customer will get before being charged for the first time. This will always overwrite any trials that might apply via a subscribed plan. If set, `trial_end` will override the default trial period of the plan the customer is being subscribed to. The `billing_cycle_anchor` will be updated to the `trial_end` value. The special value `now` can be provided to end the customer's trial immediately. Can be at most two years from `billing_cycle_anchor`."
            },
            {
                "name": "trial_from_plan",
                "description": "Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more."
            },
            {
                "name": "trial_settings",
                "description": "Settings related to subscription trials."
            }
        ]
    },
    {
        "path": "/v1/subscriptions/{subscription_exposed_id}/discount",
        "verb": "delete",
        "op_id": "DeleteSubscriptionsSubscriptionExposedIdDiscount",
        "summary": "Delete a subscription discount",
        "params": []
    },
    {
        "path": "/v1/subscriptions/{subscription}/resume",
        "verb": "post",
        "op_id": "PostSubscriptionsSubscriptionResume",
        "summary": "Resume a subscription",
        "params": [
            {
                "name": "billing_cycle_anchor",
                "description": "The billing cycle anchor that applies when the subscription is resumed. Either `now` or `unchanged`. The default is `now`. For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle)."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "proration_behavior",
                "description": "Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) resulting from the `billing_cycle_anchor` being `unchanged`. When the `billing_cycle_anchor` is set to `now` (default value), no prorations are generated. If no value is passed, the default is `create_prorations`."
            },
            {
                "name": "proration_date",
                "description": "If set, prorations will be calculated as though the subscription was resumed at the given time. This can be used to apply exactly the same prorations that were previewed with the [create preview](https://stripe.com/docs/api/invoices/create_preview) endpoint."
            }
        ]
    },
    {
        "path": "/v1/tax/calculations",
        "verb": "post",
        "op_id": "PostTaxCalculations",
        "summary": "Create a Tax Calculation",
        "params": [
            {
                "name": "currency",
                "description": "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "customer",
                "description": "The ID of an existing customer to use for this calculation. If provided, the customer's address and tax IDs are copied to `customer_details`."
            },
            {
                "name": "customer_details",
                "description": "Details about the customer, including address and tax IDs."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "line_items",
                "description": "A list of items the customer is purchasing."
            },
            {
                "name": "ship_from_details",
                "description": "Details about the address from which the goods are being shipped."
            },
            {
                "name": "shipping_cost",
                "description": "Shipping cost details to be used for the calculation."
            },
            {
                "name": "tax_date",
                "description": "Timestamp of date at which the tax rules and rates in effect applies for the calculation. Measured in seconds since the Unix epoch. Can be up to 48 hours in the past, and up to 48 hours in the future."
            }
        ]
    },
    {
        "path": "/v1/tax/calculations/{calculation}",
        "verb": "get",
        "op_id": "GetTaxCalculationsCalculation",
        "summary": "Retrieve a Tax Calculation",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/tax/calculations/{calculation}/line_items",
        "verb": "get",
        "op_id": "GetTaxCalculationsCalculationLineItems",
        "summary": "Retrieve a calculation's line items",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/tax/registrations",
        "verb": "get",
        "op_id": "GetTaxRegistrations",
        "summary": "List registrations",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "status",
                "description": "The status of the Tax Registration."
            }
        ]
    },
    {
        "path": "/v1/tax/registrations",
        "verb": "post",
        "op_id": "PostTaxRegistrations",
        "summary": "Create a registration",
        "params": [
            {
                "name": "active_from",
                "description": "Time at which the Tax Registration becomes active. It can be either `now` to indicate the current time, or a future timestamp measured in seconds since the Unix epoch."
            },
            {
                "name": "country",
                "description": "Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2))."
            },
            {
                "name": "country_options",
                "description": "Specific options for a registration in the specified `country`."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "expires_at",
                "description": "If set, the Tax Registration stops being active at this time. If not set, the Tax Registration will be active indefinitely. Timestamp measured in seconds since the Unix epoch."
            }
        ]
    },
    {
        "path": "/v1/tax/registrations/{id}",
        "verb": "get",
        "op_id": "GetTaxRegistrationsId",
        "summary": "Retrieve a registration",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/tax/registrations/{id}",
        "verb": "post",
        "op_id": "PostTaxRegistrationsId",
        "summary": "Update a registration",
        "params": [
            {
                "name": "active_from",
                "description": "Time at which the registration becomes active. It can be either `now` to indicate the current time, or a timestamp measured in seconds since the Unix epoch."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "expires_at",
                "description": "If set, the registration stops being active at this time. If not set, the registration will be active indefinitely. It can be either `now` to indicate the current time, or a timestamp measured in seconds since the Unix epoch."
            }
        ]
    },
    {
        "path": "/v1/tax/settings",
        "verb": "get",
        "op_id": "GetTaxSettings",
        "summary": "Retrieve settings",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/tax/settings",
        "verb": "post",
        "op_id": "PostTaxSettings",
        "summary": "Update settings",
        "params": [
            {
                "name": "defaults",
                "description": "Default configuration to be used on Stripe Tax calculations."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "head_office",
                "description": "The place where your business is located."
            }
        ]
    },
    {
        "path": "/v1/tax/transactions/create_from_calculation",
        "verb": "post",
        "op_id": "PostTaxTransactionsCreateFromCalculation",
        "summary": "Create a transaction from a calculation",
        "params": [
            {
                "name": "calculation",
                "description": "Tax Calculation ID to be used as input when creating the transaction."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "posted_at",
                "description": "The Unix timestamp representing when the tax liability is assumed or reduced, which determines the liability posting period and handling in tax liability reports. The timestamp must fall within the `tax_date` and the current time, unless the `tax_date` is scheduled in advance. Defaults to the current time."
            },
            {
                "name": "reference",
                "description": "A custom order or sale identifier, such as 'myOrder_123'. Must be unique across all transactions, including reversals."
            }
        ]
    },
    {
        "path": "/v1/tax/transactions/create_reversal",
        "verb": "post",
        "op_id": "PostTaxTransactionsCreateReversal",
        "summary": "Create a reversal transaction",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "flat_amount",
                "description": "A flat amount to reverse across the entire transaction, in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) in negative. This value represents the total amount to refund from the transaction, including taxes."
            },
            {
                "name": "line_items",
                "description": "The line item amounts to reverse."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "mode",
                "description": "If `partial`, the provided line item or shipping cost amounts are reversed. If `full`, the original transaction is fully reversed."
            },
            {
                "name": "original_transaction",
                "description": "The ID of the Transaction to partially or fully reverse."
            },
            {
                "name": "reference",
                "description": "A custom identifier for this reversal, such as `myOrder_123-refund_1`, which must be unique across all transactions. The reference helps identify this reversal transaction in exported [tax reports](https://stripe.com/docs/tax/reports)."
            },
            {
                "name": "shipping_cost",
                "description": "The shipping cost to reverse."
            }
        ]
    },
    {
        "path": "/v1/tax/transactions/{transaction}",
        "verb": "get",
        "op_id": "GetTaxTransactionsTransaction",
        "summary": "Retrieve a transaction",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/tax/transactions/{transaction}/line_items",
        "verb": "get",
        "op_id": "GetTaxTransactionsTransactionLineItems",
        "summary": "Retrieve a transaction's line items",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/tax_codes",
        "verb": "get",
        "op_id": "GetTaxCodes",
        "summary": "List all tax codes",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/tax_codes/{id}",
        "verb": "get",
        "op_id": "GetTaxCodesId",
        "summary": "Retrieve a tax code",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/tax_ids",
        "verb": "get",
        "op_id": "GetTaxIds",
        "summary": "List all tax IDs",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "owner",
                "description": "The account or customer the tax ID belongs to. Defaults to `owner[type]=self`."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/tax_ids",
        "verb": "post",
        "op_id": "PostTaxIds",
        "summary": "Create a tax ID",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "owner",
                "description": "The account or customer the tax ID belongs to. Defaults to `owner[type]=self`."
            },
            {
                "name": "type",
                "description": "Type of the tax ID, one of `ad_nrt`, `ae_trn`, `al_tin`, `am_tin`, `ao_tin`, `ar_cuit`, `au_abn`, `au_arn`, `aw_tin`, `az_tin`, `ba_tin`, `bb_tin`, `bd_bin`, `bf_ifu`, `bg_uic`, `bh_vat`, `bj_ifu`, `bo_tin`, `br_cnpj`, `br_cpf`, `bs_tin`, `by_tin`, `ca_bn`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `ca_qst`, `cd_nif`, `ch_uid`, `ch_vat`, `cl_tin`, `cm_niu`, `cn_tin`, `co_nit`, `cr_tin`, `cv_nif`, `de_stn`, `do_rcn`, `ec_ruc`, `eg_tin`, `es_cif`, `et_tin`, `eu_oss_vat`, `eu_vat`, `gb_vat`, `ge_vat`, `gn_nif`, `hk_br`, `hr_oib`, `hu_tin`, `id_npwp`, `il_vat`, `in_gst`, `is_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `ke_pin`, `kg_tin`, `kh_tin`, `kr_brn`, `kz_bin`, `la_tin`, `li_uid`, `li_vat`, `ma_vat`, `md_vat`, `me_pib`, `mk_vat`, `mr_nif`, `mx_rfc`, `my_frp`, `my_itn`, `my_sst`, `ng_tin`, `no_vat`, `no_voec`, `np_pan`, `nz_gst`, `om_vat`, `pe_ruc`, `ph_tin`, `ro_tin`, `rs_pib`, `ru_inn`, `ru_kpp`, `sa_vat`, `sg_gst`, `sg_uen`, `si_tin`, `sn_ninea`, `sr_fin`, `sv_nit`, `th_vat`, `tj_tin`, `tr_tin`, `tw_vat`, `tz_vat`, `ua_vat`, `ug_tin`, `us_ein`, `uy_ruc`, `uz_tin`, `uz_vat`, `ve_rif`, `vn_tin`, `za_vat`, `zm_tin`, or `zw_tin`"
            },
            {
                "name": "value",
                "description": "Value of the tax ID."
            }
        ]
    },
    {
        "path": "/v1/tax_ids/{id}",
        "verb": "delete",
        "op_id": "DeleteTaxIdsId",
        "summary": "Delete a tax ID",
        "params": []
    },
    {
        "path": "/v1/tax_ids/{id}",
        "verb": "get",
        "op_id": "GetTaxIdsId",
        "summary": "Retrieve a tax ID",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/tax_rates",
        "verb": "get",
        "op_id": "GetTaxRates",
        "summary": "List all tax rates",
        "params": [
            {
                "name": "active",
                "description": "Optional flag to filter by tax rates that are either active or inactive (archived)."
            },
            {
                "name": "created",
                "description": "Optional range for filtering created date."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "inclusive",
                "description": "Optional flag to filter by tax rates that are inclusive (or those that are not inclusive)."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/tax_rates",
        "verb": "post",
        "op_id": "PostTaxRates",
        "summary": "Create a tax rate",
        "params": [
            {
                "name": "active",
                "description": "Flag determining whether the tax rate is active or inactive (archived). Inactive tax rates cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set."
            },
            {
                "name": "country",
                "description": "Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2))."
            },
            {
                "name": "description",
                "description": "An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers."
            },
            {
                "name": "display_name",
                "description": "The display name of the tax rate, which will be shown to users."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "inclusive",
                "description": "This specifies if the tax rate is inclusive or exclusive."
            },
            {
                "name": "jurisdiction",
                "description": "The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer\u2019s invoice."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "percentage",
                "description": "This represents the tax rate percent out of 100."
            },
            {
                "name": "state",
                "description": "[ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, \"NY\" for New York, United States."
            },
            {
                "name": "tax_type",
                "description": "The high-level tax type, such as `vat` or `sales_tax`."
            }
        ]
    },
    {
        "path": "/v1/tax_rates/{tax_rate}",
        "verb": "get",
        "op_id": "GetTaxRatesTaxRate",
        "summary": "Retrieve a tax rate",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/tax_rates/{tax_rate}",
        "verb": "post",
        "op_id": "PostTaxRatesTaxRate",
        "summary": "Update a tax rate",
        "params": [
            {
                "name": "active",
                "description": "Flag determining whether the tax rate is active or inactive (archived). Inactive tax rates cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set."
            },
            {
                "name": "country",
                "description": "Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2))."
            },
            {
                "name": "description",
                "description": "An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers."
            },
            {
                "name": "display_name",
                "description": "The display name of the tax rate, which will be shown to users."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "jurisdiction",
                "description": "The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer\u2019s invoice."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "state",
                "description": "[ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, \"NY\" for New York, United States."
            },
            {
                "name": "tax_type",
                "description": "The high-level tax type, such as `vat` or `sales_tax`."
            }
        ]
    },
    {
        "path": "/v1/terminal/configurations",
        "verb": "get",
        "op_id": "GetTerminalConfigurations",
        "summary": "List all Configurations",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "is_account_default",
                "description": "if present, only return the account default or non-default configurations."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/terminal/configurations",
        "verb": "post",
        "op_id": "PostTerminalConfigurations",
        "summary": "Create a Configuration",
        "params": [
            {
                "name": "bbpos_wisepos_e",
                "description": "An object containing device type specific settings for BBPOS WisePOS E readers"
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "name",
                "description": "Name of the configuration"
            },
            {
                "name": "offline",
                "description": "Configurations for collecting transactions offline."
            },
            {
                "name": "reboot_window",
                "description": "Reboot time settings for readers that support customized reboot time configuration."
            },
            {
                "name": "stripe_s700",
                "description": "An object containing device type specific settings for Stripe S700 readers"
            },
            {
                "name": "tipping",
                "description": "Tipping configurations for readers supporting on-reader tips"
            },
            {
                "name": "verifone_p400",
                "description": "An object containing device type specific settings for Verifone P400 readers"
            },
            {
                "name": "wifi",
                "description": "Configurations for connecting to a WiFi network."
            }
        ]
    },
    {
        "path": "/v1/terminal/configurations/{configuration}",
        "verb": "delete",
        "op_id": "DeleteTerminalConfigurationsConfiguration",
        "summary": "Delete a Configuration",
        "params": []
    },
    {
        "path": "/v1/terminal/configurations/{configuration}",
        "verb": "get",
        "op_id": "GetTerminalConfigurationsConfiguration",
        "summary": "Retrieve a Configuration",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/terminal/configurations/{configuration}",
        "verb": "post",
        "op_id": "PostTerminalConfigurationsConfiguration",
        "summary": "Update a Configuration",
        "params": [
            {
                "name": "bbpos_wisepos_e",
                "description": "An object containing device type specific settings for BBPOS WisePOS E readers"
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "name",
                "description": "Name of the configuration"
            },
            {
                "name": "offline",
                "description": "Configurations for collecting transactions offline."
            },
            {
                "name": "reboot_window",
                "description": "Reboot time settings for readers that support customized reboot time configuration."
            },
            {
                "name": "stripe_s700",
                "description": "An object containing device type specific settings for Stripe S700 readers"
            },
            {
                "name": "tipping",
                "description": "Tipping configurations for readers supporting on-reader tips"
            },
            {
                "name": "verifone_p400",
                "description": "An object containing device type specific settings for Verifone P400 readers"
            },
            {
                "name": "wifi",
                "description": "Configurations for connecting to a WiFi network."
            }
        ]
    },
    {
        "path": "/v1/terminal/connection_tokens",
        "verb": "post",
        "op_id": "PostTerminalConnectionTokens",
        "summary": "Create a Connection Token",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "location",
                "description": "The id of the location that this connection token is scoped to. If specified the connection token will only be usable with readers assigned to that location, otherwise the connection token will be usable with all readers. Note that location scoping only applies to internet-connected readers. For more details, see [the docs on scoping connection tokens](https://docs.stripe.com/terminal/fleet/locations-and-zones?dashboard-or-api=api#connection-tokens)."
            }
        ]
    },
    {
        "path": "/v1/terminal/locations",
        "verb": "get",
        "op_id": "GetTerminalLocations",
        "summary": "List all Locations",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/terminal/locations",
        "verb": "post",
        "op_id": "PostTerminalLocations",
        "summary": "Create a Location",
        "params": [
            {
                "name": "address",
                "description": "The full address of the location."
            },
            {
                "name": "configuration_overrides",
                "description": "The ID of a configuration that will be used to customize all readers in this location."
            },
            {
                "name": "display_name",
                "description": "A name for the location. Maximum length is 1000 characters."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            }
        ]
    },
    {
        "path": "/v1/terminal/locations/{location}",
        "verb": "delete",
        "op_id": "DeleteTerminalLocationsLocation",
        "summary": "Delete a Location",
        "params": []
    },
    {
        "path": "/v1/terminal/locations/{location}",
        "verb": "get",
        "op_id": "GetTerminalLocationsLocation",
        "summary": "Retrieve a Location",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/terminal/locations/{location}",
        "verb": "post",
        "op_id": "PostTerminalLocationsLocation",
        "summary": "Update a Location",
        "params": [
            {
                "name": "address",
                "description": "The full address of the location. You can't change the location's `country`. If you need to modify the `country` field, create a new `Location` object and re-register any existing readers to that location."
            },
            {
                "name": "configuration_overrides",
                "description": "The ID of a configuration that will be used to customize all readers in this location."
            },
            {
                "name": "display_name",
                "description": "A name for the location."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            }
        ]
    },
    {
        "path": "/v1/terminal/readers",
        "verb": "get",
        "op_id": "GetTerminalReaders",
        "summary": "List all Readers",
        "params": [
            {
                "name": "device_type",
                "description": "Filters readers by device type"
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "location",
                "description": "A location ID to filter the response list to only readers at the specific location"
            },
            {
                "name": "serial_number",
                "description": "Filters readers by serial number"
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "status",
                "description": "A status filter to filter readers to only offline or online readers"
            }
        ]
    },
    {
        "path": "/v1/terminal/readers",
        "verb": "post",
        "op_id": "PostTerminalReaders",
        "summary": "Create a Reader",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "label",
                "description": "Custom label given to the reader for easier identification. If no label is specified, the registration code will be used."
            },
            {
                "name": "location",
                "description": "The location to assign the reader to."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "registration_code",
                "description": "A code generated by the reader used for registering to an account."
            }
        ]
    },
    {
        "path": "/v1/terminal/readers/{reader}",
        "verb": "delete",
        "op_id": "DeleteTerminalReadersReader",
        "summary": "Delete a Reader",
        "params": []
    },
    {
        "path": "/v1/terminal/readers/{reader}",
        "verb": "get",
        "op_id": "GetTerminalReadersReader",
        "summary": "Retrieve a Reader",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/terminal/readers/{reader}",
        "verb": "post",
        "op_id": "PostTerminalReadersReader",
        "summary": "Update a Reader",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "label",
                "description": "The new label of the reader."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            }
        ]
    },
    {
        "path": "/v1/terminal/readers/{reader}/cancel_action",
        "verb": "post",
        "op_id": "PostTerminalReadersReaderCancelAction",
        "summary": "Cancel the current reader action",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/terminal/readers/{reader}/collect_inputs",
        "verb": "post",
        "op_id": "PostTerminalReadersReaderCollectInputs",
        "summary": "Collect inputs using a Reader",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "inputs",
                "description": "List of inputs to be collected using the Reader"
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            }
        ]
    },
    {
        "path": "/v1/terminal/readers/{reader}/process_payment_intent",
        "verb": "post",
        "op_id": "PostTerminalReadersReaderProcessPaymentIntent",
        "summary": "Hand-off a PaymentIntent to a Reader",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "payment_intent",
                "description": "PaymentIntent ID"
            },
            {
                "name": "process_config",
                "description": "Configuration overrides"
            }
        ]
    },
    {
        "path": "/v1/terminal/readers/{reader}/process_setup_intent",
        "verb": "post",
        "op_id": "PostTerminalReadersReaderProcessSetupIntent",
        "summary": "Hand-off a SetupIntent to a Reader",
        "params": [
            {
                "name": "allow_redisplay",
                "description": "This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "process_config",
                "description": "Configuration overrides"
            },
            {
                "name": "setup_intent",
                "description": "SetupIntent ID"
            }
        ]
    },
    {
        "path": "/v1/terminal/readers/{reader}/refund_payment",
        "verb": "post",
        "op_id": "PostTerminalReadersReaderRefundPayment",
        "summary": "Refund a Charge or a PaymentIntent in-person",
        "params": [
            {
                "name": "amount",
                "description": "A positive integer in __cents__ representing how much of this charge to refund."
            },
            {
                "name": "charge",
                "description": "ID of the Charge to refund."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "payment_intent",
                "description": "ID of the PaymentIntent to refund."
            },
            {
                "name": "refund_application_fee",
                "description": "Boolean indicating whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded. An application fee can be refunded only by the application that created the charge."
            },
            {
                "name": "refund_payment_config",
                "description": "Configuration overrides"
            },
            {
                "name": "reverse_transfer",
                "description": "Boolean indicating whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount). A transfer can be reversed only by the application that created the charge."
            }
        ]
    },
    {
        "path": "/v1/terminal/readers/{reader}/set_reader_display",
        "verb": "post",
        "op_id": "PostTerminalReadersReaderSetReaderDisplay",
        "summary": "Set reader display",
        "params": [
            {
                "name": "cart",
                "description": "Cart"
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "type",
                "description": "Type"
            }
        ]
    },
    {
        "path": "/v1/test_helpers/confirmation_tokens",
        "verb": "post",
        "op_id": "PostTestHelpersConfirmationTokens",
        "summary": "Create a test Confirmation Token",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "payment_method",
                "description": "ID of an existing PaymentMethod."
            },
            {
                "name": "payment_method_data",
                "description": "If provided, this hash will be used to create a PaymentMethod."
            },
            {
                "name": "payment_method_options",
                "description": "Payment-method-specific configuration for this ConfirmationToken."
            },
            {
                "name": "return_url",
                "description": "Return URL used to confirm the Intent."
            },
            {
                "name": "setup_future_usage",
                "description": "Indicates that you intend to make future payments with this ConfirmationToken's payment method.\n\nThe presence of this property will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete."
            },
            {
                "name": "shipping",
                "description": "Shipping information for this ConfirmationToken."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/customers/{customer}/fund_cash_balance",
        "verb": "post",
        "op_id": "PostTestHelpersCustomersCustomerFundCashBalance",
        "summary": "Fund a test mode cash balance",
        "params": [
            {
                "name": "amount",
                "description": "Amount to be used for this test cash balance transaction. A positive integer representing how much to fund in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to fund $1.00 or 100 to fund \u00a5100, a zero-decimal currency)."
            },
            {
                "name": "currency",
                "description": "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "reference",
                "description": "A description of the test funding. This simulates free-text references supplied by customers when making bank transfers to their cash balance. You can use this to test how Stripe's [reconciliation algorithm](https://stripe.com/docs/payments/customer-balance/reconciliation) applies to different user inputs."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/issuing/authorizations",
        "verb": "post",
        "op_id": "PostTestHelpersIssuingAuthorizations",
        "summary": "Create a test-mode authorization",
        "params": [
            {
                "name": "amount",
                "description": "The total amount to attempt to authorize. This amount is in the provided currency, or defaults to the card's currency, and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)."
            },
            {
                "name": "amount_details",
                "description": "Detailed breakdown of amount components. These amounts are denominated in `currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)."
            },
            {
                "name": "authorization_method",
                "description": "How the card details were provided. Defaults to online."
            },
            {
                "name": "card",
                "description": "Card associated with this authorization."
            },
            {
                "name": "currency",
                "description": "The currency of the authorization. If not provided, defaults to the currency of the card. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "fleet",
                "description": "Fleet-specific information for authorizations using Fleet cards."
            },
            {
                "name": "fuel",
                "description": "Information about fuel that was purchased with this transaction."
            },
            {
                "name": "is_amount_controllable",
                "description": "If set `true`, you may provide [amount](https://stripe.com/docs/api/issuing/authorizations/approve#approve_issuing_authorization-amount) to control how much to hold for the authorization."
            },
            {
                "name": "merchant_amount",
                "description": "The total amount to attempt to authorize. This amount is in the provided merchant currency, and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)."
            },
            {
                "name": "merchant_currency",
                "description": "The currency of the authorization. If not provided, defaults to the currency of the card. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "merchant_data",
                "description": "Details about the seller (grocery store, e-commerce website, etc.) where the card authorization happened."
            },
            {
                "name": "network_data",
                "description": "Details about the authorization, such as identifiers, set by the card network."
            },
            {
                "name": "verification_data",
                "description": "Verifications that Stripe performed on information that the cardholder provided to the merchant."
            },
            {
                "name": "wallet",
                "description": "The digital wallet used for this transaction. One of `apple_pay`, `google_pay`, or `samsung_pay`. Will populate as `null` when no digital wallet was utilized."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/issuing/authorizations/{authorization}/capture",
        "verb": "post",
        "op_id": "PostTestHelpersIssuingAuthorizationsAuthorizationCapture",
        "summary": "Capture a test-mode authorization",
        "params": [
            {
                "name": "capture_amount",
                "description": "The amount to capture from the authorization. If not provided, the full amount of the authorization will be captured. This amount is in the authorization currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)."
            },
            {
                "name": "close_authorization",
                "description": "Whether to close the authorization after capture. Defaults to true. Set to false to enable multi-capture flows."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "purchase_details",
                "description": "Additional purchase information that is optionally provided by the merchant."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/issuing/authorizations/{authorization}/expire",
        "verb": "post",
        "op_id": "PostTestHelpersIssuingAuthorizationsAuthorizationExpire",
        "summary": "Expire a test-mode authorization",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/issuing/authorizations/{authorization}/finalize_amount",
        "verb": "post",
        "op_id": "PostTestHelpersIssuingAuthorizationsAuthorizationFinalizeAmount",
        "summary": "Finalize a test-mode authorization's amount",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "final_amount",
                "description": "The final authorization amount that will be captured by the merchant. This amount is in the authorization currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)."
            },
            {
                "name": "fleet",
                "description": "Fleet-specific information for authorizations using Fleet cards."
            },
            {
                "name": "fuel",
                "description": "Information about fuel that was purchased with this transaction."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/issuing/authorizations/{authorization}/fraud_challenges/respond",
        "verb": "post",
        "op_id": "PostTestHelpersIssuingAuthorizationsAuthorizationFraudChallengesRespond",
        "summary": "Respond to fraud challenge",
        "params": [
            {
                "name": "confirmed",
                "description": "Whether to simulate the user confirming that the transaction was legitimate (true) or telling Stripe that it was fraudulent (false)."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/issuing/authorizations/{authorization}/increment",
        "verb": "post",
        "op_id": "PostTestHelpersIssuingAuthorizationsAuthorizationIncrement",
        "summary": "Increment a test-mode authorization",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "increment_amount",
                "description": "The amount to increment the authorization by. This amount is in the authorization currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)."
            },
            {
                "name": "is_amount_controllable",
                "description": "If set `true`, you may provide [amount](https://stripe.com/docs/api/issuing/authorizations/approve#approve_issuing_authorization-amount) to control how much to hold for the authorization."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/issuing/authorizations/{authorization}/reverse",
        "verb": "post",
        "op_id": "PostTestHelpersIssuingAuthorizationsAuthorizationReverse",
        "summary": "Reverse a test-mode authorization",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "reverse_amount",
                "description": "The amount to reverse from the authorization. If not provided, the full amount of the authorization will be reversed. This amount is in the authorization currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/issuing/cards/{card}/shipping/deliver",
        "verb": "post",
        "op_id": "PostTestHelpersIssuingCardsCardShippingDeliver",
        "summary": "Deliver a testmode card",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/issuing/cards/{card}/shipping/fail",
        "verb": "post",
        "op_id": "PostTestHelpersIssuingCardsCardShippingFail",
        "summary": "Fail a testmode card",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/issuing/cards/{card}/shipping/return",
        "verb": "post",
        "op_id": "PostTestHelpersIssuingCardsCardShippingReturn",
        "summary": "Return a testmode card",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/issuing/cards/{card}/shipping/ship",
        "verb": "post",
        "op_id": "PostTestHelpersIssuingCardsCardShippingShip",
        "summary": "Ship a testmode card",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/issuing/cards/{card}/shipping/submit",
        "verb": "post",
        "op_id": "PostTestHelpersIssuingCardsCardShippingSubmit",
        "summary": "Submit a testmode card",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/issuing/personalization_designs/{personalization_design}/activate",
        "verb": "post",
        "op_id": "PostTestHelpersIssuingPersonalizationDesignsPersonalizationDesignActivate",
        "summary": "Activate a testmode personalization design",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/issuing/personalization_designs/{personalization_design}/deactivate",
        "verb": "post",
        "op_id": "PostTestHelpersIssuingPersonalizationDesignsPersonalizationDesignDeactivate",
        "summary": "Deactivate a testmode personalization design",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/issuing/personalization_designs/{personalization_design}/reject",
        "verb": "post",
        "op_id": "PostTestHelpersIssuingPersonalizationDesignsPersonalizationDesignReject",
        "summary": "Reject a testmode personalization design",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "rejection_reasons",
                "description": "The reason(s) the personalization design was rejected."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/issuing/settlements",
        "verb": "post",
        "op_id": "PostTestHelpersIssuingSettlements",
        "summary": "Create a test-mode settlement",
        "params": [
            {
                "name": "bin",
                "description": "The Bank Identification Number reflecting this settlement record."
            },
            {
                "name": "clearing_date",
                "description": "The date that the transactions are cleared and posted to user's accounts."
            },
            {
                "name": "currency",
                "description": "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "interchange_fees_amount",
                "description": "The total interchange received as reimbursement for the transactions."
            },
            {
                "name": "net_total_amount",
                "description": "The total net amount required to settle with the network."
            },
            {
                "name": "network",
                "description": "The card network for this settlement. One of [\"visa\", \"maestro\"]"
            },
            {
                "name": "network_settlement_identifier",
                "description": "The Settlement Identification Number assigned by the network."
            },
            {
                "name": "transaction_amount",
                "description": "The total transaction amount reflected in this settlement."
            },
            {
                "name": "transaction_count",
                "description": "The total number of transactions reflected in this settlement."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/issuing/settlements/{settlement}/complete",
        "verb": "post",
        "op_id": "PostTestHelpersIssuingSettlementsSettlementComplete",
        "summary": "Complete a test-mode settlement",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/issuing/transactions/create_force_capture",
        "verb": "post",
        "op_id": "PostTestHelpersIssuingTransactionsCreateForceCapture",
        "summary": "Create a test-mode force capture",
        "params": [
            {
                "name": "amount",
                "description": "The total amount to attempt to capture. This amount is in the provided currency, or defaults to the cards currency, and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)."
            },
            {
                "name": "card",
                "description": "Card associated with this transaction."
            },
            {
                "name": "currency",
                "description": "The currency of the capture. If not provided, defaults to the currency of the card. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "merchant_data",
                "description": "Details about the seller (grocery store, e-commerce website, etc.) where the card authorization happened."
            },
            {
                "name": "purchase_details",
                "description": "Additional purchase information that is optionally provided by the merchant."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/issuing/transactions/create_unlinked_refund",
        "verb": "post",
        "op_id": "PostTestHelpersIssuingTransactionsCreateUnlinkedRefund",
        "summary": "Create a test-mode unlinked refund",
        "params": [
            {
                "name": "amount",
                "description": "The total amount to attempt to refund. This amount is in the provided currency, or defaults to the cards currency, and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)."
            },
            {
                "name": "card",
                "description": "Card associated with this unlinked refund transaction."
            },
            {
                "name": "currency",
                "description": "The currency of the unlinked refund. If not provided, defaults to the currency of the card. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "merchant_data",
                "description": "Details about the seller (grocery store, e-commerce website, etc.) where the card authorization happened."
            },
            {
                "name": "purchase_details",
                "description": "Additional purchase information that is optionally provided by the merchant."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/issuing/transactions/{transaction}/refund",
        "verb": "post",
        "op_id": "PostTestHelpersIssuingTransactionsTransactionRefund",
        "summary": "Refund a test-mode transaction",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "refund_amount",
                "description": "The total amount to attempt to refund. This amount is in the provided currency, or defaults to the cards currency, and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/refunds/{refund}/expire",
        "verb": "post",
        "op_id": "PostTestHelpersRefundsRefundExpire",
        "summary": "Expire a pending refund.",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/terminal/readers/{reader}/present_payment_method",
        "verb": "post",
        "op_id": "PostTestHelpersTerminalReadersReaderPresentPaymentMethod",
        "summary": "Simulate presenting a payment method",
        "params": [
            {
                "name": "amount_tip",
                "description": "Simulated on-reader tip amount."
            },
            {
                "name": "card_present",
                "description": "Simulated data for the card_present payment method."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "interac_present",
                "description": "Simulated data for the interac_present payment method."
            },
            {
                "name": "type",
                "description": "Simulated payment type."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/terminal/readers/{reader}/succeed_input_collection",
        "verb": "post",
        "op_id": "PostTestHelpersTerminalReadersReaderSucceedInputCollection",
        "summary": "Simulate a successful input collection",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "skip_non_required_inputs",
                "description": "This parameter defines the skip behavior for input collection."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/terminal/readers/{reader}/timeout_input_collection",
        "verb": "post",
        "op_id": "PostTestHelpersTerminalReadersReaderTimeoutInputCollection",
        "summary": "Simulate an input collection timeout",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/test_clocks",
        "verb": "get",
        "op_id": "GetTestHelpersTestClocks",
        "summary": "List all test clocks",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/test_clocks",
        "verb": "post",
        "op_id": "PostTestHelpersTestClocks",
        "summary": "Create a test clock",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "frozen_time",
                "description": "The initial frozen time for this test clock."
            },
            {
                "name": "name",
                "description": "The name for this test clock."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/test_clocks/{test_clock}",
        "verb": "delete",
        "op_id": "DeleteTestHelpersTestClocksTestClock",
        "summary": "Delete a test clock",
        "params": []
    },
    {
        "path": "/v1/test_helpers/test_clocks/{test_clock}",
        "verb": "get",
        "op_id": "GetTestHelpersTestClocksTestClock",
        "summary": "Retrieve a test clock",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/test_clocks/{test_clock}/advance",
        "verb": "post",
        "op_id": "PostTestHelpersTestClocksTestClockAdvance",
        "summary": "Advance a test clock",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "frozen_time",
                "description": "The time to advance the test clock. Must be after the test clock's current frozen time. Cannot be more than two intervals in the future from the shortest subscription in this test clock. If there are no subscriptions in this test clock, it cannot be more than two years in the future."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/treasury/inbound_transfers/{id}/fail",
        "verb": "post",
        "op_id": "PostTestHelpersTreasuryInboundTransfersIdFail",
        "summary": "Test mode: Fail an InboundTransfer",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "failure_details",
                "description": "Details about a failed InboundTransfer."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/treasury/inbound_transfers/{id}/return",
        "verb": "post",
        "op_id": "PostTestHelpersTreasuryInboundTransfersIdReturn",
        "summary": "Test mode: Return an InboundTransfer",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/treasury/inbound_transfers/{id}/succeed",
        "verb": "post",
        "op_id": "PostTestHelpersTreasuryInboundTransfersIdSucceed",
        "summary": "Test mode: Succeed an InboundTransfer",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/treasury/outbound_payments/{id}",
        "verb": "post",
        "op_id": "PostTestHelpersTreasuryOutboundPaymentsId",
        "summary": "Test mode: Update an OutboundPayment",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "tracking_details",
                "description": "Details about network-specific tracking information."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/treasury/outbound_payments/{id}/fail",
        "verb": "post",
        "op_id": "PostTestHelpersTreasuryOutboundPaymentsIdFail",
        "summary": "Test mode: Fail an OutboundPayment",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/treasury/outbound_payments/{id}/post",
        "verb": "post",
        "op_id": "PostTestHelpersTreasuryOutboundPaymentsIdPost",
        "summary": "Test mode: Post an OutboundPayment",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/treasury/outbound_payments/{id}/return",
        "verb": "post",
        "op_id": "PostTestHelpersTreasuryOutboundPaymentsIdReturn",
        "summary": "Test mode: Return an OutboundPayment",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "returned_details",
                "description": "Optional hash to set the return code."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}",
        "verb": "post",
        "op_id": "PostTestHelpersTreasuryOutboundTransfersOutboundTransfer",
        "summary": "Test mode: Update an OutboundTransfer",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "tracking_details",
                "description": "Details about network-specific tracking information."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/fail",
        "verb": "post",
        "op_id": "PostTestHelpersTreasuryOutboundTransfersOutboundTransferFail",
        "summary": "Test mode: Fail an OutboundTransfer",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/post",
        "verb": "post",
        "op_id": "PostTestHelpersTreasuryOutboundTransfersOutboundTransferPost",
        "summary": "Test mode: Post an OutboundTransfer",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/treasury/outbound_transfers/{outbound_transfer}/return",
        "verb": "post",
        "op_id": "PostTestHelpersTreasuryOutboundTransfersOutboundTransferReturn",
        "summary": "Test mode: Return an OutboundTransfer",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "returned_details",
                "description": "Details about a returned OutboundTransfer."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/treasury/received_credits",
        "verb": "post",
        "op_id": "PostTestHelpersTreasuryReceivedCredits",
        "summary": "Test mode: Create a ReceivedCredit",
        "params": [
            {
                "name": "amount",
                "description": "Amount (in cents) to be transferred."
            },
            {
                "name": "currency",
                "description": "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "description",
                "description": "An arbitrary string attached to the object. Often useful for displaying to users."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "financial_account",
                "description": "The FinancialAccount to send funds to."
            },
            {
                "name": "initiating_payment_method_details",
                "description": "Initiating payment method details for the object."
            },
            {
                "name": "network",
                "description": "Specifies the network rails to be used. If not set, will default to the PaymentMethod's preferred network. See the [docs](https://stripe.com/docs/treasury/money-movement/timelines) to learn more about money movement timelines for each network type."
            }
        ]
    },
    {
        "path": "/v1/test_helpers/treasury/received_debits",
        "verb": "post",
        "op_id": "PostTestHelpersTreasuryReceivedDebits",
        "summary": "Test mode: Create a ReceivedDebit",
        "params": [
            {
                "name": "amount",
                "description": "Amount (in cents) to be transferred."
            },
            {
                "name": "currency",
                "description": "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "description",
                "description": "An arbitrary string attached to the object. Often useful for displaying to users."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "financial_account",
                "description": "The FinancialAccount to pull funds from."
            },
            {
                "name": "initiating_payment_method_details",
                "description": "Initiating payment method details for the object."
            },
            {
                "name": "network",
                "description": "Specifies the network rails to be used. If not set, will default to the PaymentMethod's preferred network. See the [docs](https://stripe.com/docs/treasury/money-movement/timelines) to learn more about money movement timelines for each network type."
            }
        ]
    },
    {
        "path": "/v1/tokens",
        "verb": "post",
        "op_id": "PostTokens",
        "summary": "Create a CVC update token",
        "params": [
            {
                "name": "account",
                "description": "Information for the account this token represents."
            },
            {
                "name": "bank_account",
                "description": "The bank account this token will represent."
            },
            {
                "name": "card",
                "description": "The card this token will represent. If you also pass in a customer, the card must be the ID of a card belonging to the customer. Otherwise, if you do not pass in a customer, this is a dictionary containing a user's credit card details, with the options described below."
            },
            {
                "name": "customer",
                "description": "Create a token for the customer, which is owned by the application's account. You can only use this with an [OAuth access token](https://stripe.com/docs/connect/standard-accounts) or [Stripe-Account header](https://stripe.com/docs/connect/authentication). Learn more about [cloning saved payment methods](https://stripe.com/docs/connect/cloning-saved-payment-methods)."
            },
            {
                "name": "cvc_update",
                "description": "The updated CVC value this token represents."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "person",
                "description": "Information for the person this token represents."
            },
            {
                "name": "pii",
                "description": "The PII this token represents."
            }
        ]
    },
    {
        "path": "/v1/tokens/{token}",
        "verb": "get",
        "op_id": "GetTokensToken",
        "summary": "Retrieve a token",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/topups",
        "verb": "get",
        "op_id": "GetTopups",
        "summary": "List all top-ups",
        "params": [
            {
                "name": "amount",
                "description": "A positive integer representing how much to transfer."
            },
            {
                "name": "created",
                "description": "A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "status",
                "description": "Only return top-ups that have the given status. One of `canceled`, `failed`, `pending` or `succeeded`."
            }
        ]
    },
    {
        "path": "/v1/topups",
        "verb": "post",
        "op_id": "PostTopups",
        "summary": "Create a top-up",
        "params": [
            {
                "name": "amount",
                "description": "A positive integer representing how much to transfer."
            },
            {
                "name": "currency",
                "description": "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "description",
                "description": "An arbitrary string attached to the object. Often useful for displaying to users."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "source",
                "description": "The ID of a source to transfer funds from. For most users, this should be left unspecified which will use the bank account that was set up in the dashboard for the specified currency. In test mode, this can be a test bank token (see [Testing Top-ups](https://stripe.com/docs/connect/testing#testing-top-ups))."
            },
            {
                "name": "statement_descriptor",
                "description": "Extra information about a top-up for the source's bank statement. Limited to 15 ASCII characters."
            },
            {
                "name": "transfer_group",
                "description": "A string that identifies this top-up as part of a group."
            }
        ]
    },
    {
        "path": "/v1/topups/{topup}",
        "verb": "get",
        "op_id": "GetTopupsTopup",
        "summary": "Retrieve a top-up",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/topups/{topup}",
        "verb": "post",
        "op_id": "PostTopupsTopup",
        "summary": "Update a top-up",
        "params": [
            {
                "name": "description",
                "description": "An arbitrary string attached to the object. Often useful for displaying to users."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            }
        ]
    },
    {
        "path": "/v1/topups/{topup}/cancel",
        "verb": "post",
        "op_id": "PostTopupsTopupCancel",
        "summary": "Cancel a top-up",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/transfers",
        "verb": "get",
        "op_id": "GetTransfers",
        "summary": "List all transfers",
        "params": [
            {
                "name": "created",
                "description": "Only return transfers that were created during the given date interval."
            },
            {
                "name": "destination",
                "description": "Only return transfers for the destination specified by this account ID."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "transfer_group",
                "description": "Only return transfers with the specified transfer group."
            }
        ]
    },
    {
        "path": "/v1/transfers",
        "verb": "post",
        "op_id": "PostTransfers",
        "summary": "Create a transfer",
        "params": [
            {
                "name": "amount",
                "description": "A positive integer in cents (or local equivalent) representing how much to transfer."
            },
            {
                "name": "currency",
                "description": "Three-letter [ISO code for currency](https://www.iso.org/iso-4217-currency-codes.html) in lowercase. Must be a [supported currency](https://docs.stripe.com/currencies)."
            },
            {
                "name": "description",
                "description": "An arbitrary string attached to the object. Often useful for displaying to users."
            },
            {
                "name": "destination",
                "description": "The ID of a connected Stripe account. <a href=\"/docs/connect/separate-charges-and-transfers\">See the Connect documentation</a> for details."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "source_transaction",
                "description": "You can use this parameter to transfer funds from a charge before they are added to your available balance. A pending balance will transfer immediately but the funds will not become available until the original charge becomes available. [See the Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-availability) for details."
            },
            {
                "name": "source_type",
                "description": "The source balance to use for this transfer. One of `bank_account`, `card`, or `fpx`. For most users, this will default to `card`."
            },
            {
                "name": "transfer_group",
                "description": "A string that identifies this transaction as part of a group. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options) for details."
            }
        ]
    },
    {
        "path": "/v1/transfers/{id}/reversals",
        "verb": "get",
        "op_id": "GetTransfersIdReversals",
        "summary": "List all reversals",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/transfers/{id}/reversals",
        "verb": "post",
        "op_id": "PostTransfersIdReversals",
        "summary": "Create a transfer reversal",
        "params": [
            {
                "name": "amount",
                "description": "A positive integer in cents (or local equivalent) representing how much of this transfer to reverse. Can only reverse up to the unreversed amount remaining of the transfer. Partial transfer reversals are only allowed for transfers to Stripe Accounts. Defaults to the entire transfer amount."
            },
            {
                "name": "description",
                "description": "An arbitrary string which you can attach to a reversal object. This will be unset if you POST an empty value."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "refund_application_fee",
                "description": "Boolean indicating whether the application fee should be refunded when reversing this transfer. If a full transfer reversal is given, the full application fee will be refunded. Otherwise, the application fee will be refunded with an amount proportional to the amount of the transfer reversed."
            }
        ]
    },
    {
        "path": "/v1/transfers/{transfer}",
        "verb": "get",
        "op_id": "GetTransfersTransfer",
        "summary": "Retrieve a transfer",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/transfers/{transfer}",
        "verb": "post",
        "op_id": "PostTransfersTransfer",
        "summary": "Update a transfer",
        "params": [
            {
                "name": "description",
                "description": "An arbitrary string attached to the object. Often useful for displaying to users."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            }
        ]
    },
    {
        "path": "/v1/transfers/{transfer}/reversals/{id}",
        "verb": "get",
        "op_id": "GetTransfersTransferReversalsId",
        "summary": "Retrieve a reversal",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/transfers/{transfer}/reversals/{id}",
        "verb": "post",
        "op_id": "PostTransfersTransferReversalsId",
        "summary": "Update a reversal",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            }
        ]
    },
    {
        "path": "/v1/treasury/credit_reversals",
        "verb": "get",
        "op_id": "GetTreasuryCreditReversals",
        "summary": "List all CreditReversals",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "financial_account",
                "description": "Returns objects associated with this FinancialAccount."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "received_credit",
                "description": "Only return CreditReversals for the ReceivedCredit ID."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "status",
                "description": "Only return CreditReversals for a given status."
            }
        ]
    },
    {
        "path": "/v1/treasury/credit_reversals",
        "verb": "post",
        "op_id": "PostTreasuryCreditReversals",
        "summary": "Create a CreditReversal",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "received_credit",
                "description": "The ReceivedCredit to reverse."
            }
        ]
    },
    {
        "path": "/v1/treasury/credit_reversals/{credit_reversal}",
        "verb": "get",
        "op_id": "GetTreasuryCreditReversalsCreditReversal",
        "summary": "Retrieve a CreditReversal",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/treasury/debit_reversals",
        "verb": "get",
        "op_id": "GetTreasuryDebitReversals",
        "summary": "List all DebitReversals",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "financial_account",
                "description": "Returns objects associated with this FinancialAccount."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "received_debit",
                "description": "Only return DebitReversals for the ReceivedDebit ID."
            },
            {
                "name": "resolution",
                "description": "Only return DebitReversals for a given resolution."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "status",
                "description": "Only return DebitReversals for a given status."
            }
        ]
    },
    {
        "path": "/v1/treasury/debit_reversals",
        "verb": "post",
        "op_id": "PostTreasuryDebitReversals",
        "summary": "Create a DebitReversal",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "received_debit",
                "description": "The ReceivedDebit to reverse."
            }
        ]
    },
    {
        "path": "/v1/treasury/debit_reversals/{debit_reversal}",
        "verb": "get",
        "op_id": "GetTreasuryDebitReversalsDebitReversal",
        "summary": "Retrieve a DebitReversal",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/treasury/financial_accounts",
        "verb": "get",
        "op_id": "GetTreasuryFinancialAccounts",
        "summary": "List all FinancialAccounts",
        "params": [
            {
                "name": "created",
                "description": "Only return FinancialAccounts that were created during the given date interval."
            },
            {
                "name": "ending_before",
                "description": "An object ID cursor for use in pagination."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit ranging from 1 to 100 (defaults to 10)."
            },
            {
                "name": "starting_after",
                "description": "An object ID cursor for use in pagination."
            }
        ]
    },
    {
        "path": "/v1/treasury/financial_accounts",
        "verb": "post",
        "op_id": "PostTreasuryFinancialAccounts",
        "summary": "Create a FinancialAccount",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "features",
                "description": "Encodes whether a FinancialAccount has access to a particular feature. Stripe or the platform can control features via the requested field."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "nickname",
                "description": "The nickname for the FinancialAccount."
            },
            {
                "name": "platform_restrictions",
                "description": "The set of functionalities that the platform can restrict on the FinancialAccount."
            },
            {
                "name": "supported_currencies",
                "description": "The currencies the FinancialAccount can hold a balance in."
            }
        ]
    },
    {
        "path": "/v1/treasury/financial_accounts/{financial_account}",
        "verb": "get",
        "op_id": "GetTreasuryFinancialAccountsFinancialAccount",
        "summary": "Retrieve a FinancialAccount",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/treasury/financial_accounts/{financial_account}",
        "verb": "post",
        "op_id": "PostTreasuryFinancialAccountsFinancialAccount",
        "summary": "Update a FinancialAccount",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "features",
                "description": "Encodes whether a FinancialAccount has access to a particular feature, with a status enum and associated `status_details`. Stripe or the platform may control features via the requested field."
            },
            {
                "name": "forwarding_settings",
                "description": "A different bank account where funds can be deposited/debited in order to get the closing FA's balance to $0"
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "nickname",
                "description": "The nickname for the FinancialAccount."
            },
            {
                "name": "platform_restrictions",
                "description": "The set of functionalities that the platform can restrict on the FinancialAccount."
            }
        ]
    },
    {
        "path": "/v1/treasury/financial_accounts/{financial_account}/close",
        "verb": "post",
        "op_id": "PostTreasuryFinancialAccountsFinancialAccountClose",
        "summary": "Close a FinancialAccount",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "forwarding_settings",
                "description": "A different bank account where funds can be deposited/debited in order to get the closing FA's balance to $0"
            }
        ]
    },
    {
        "path": "/v1/treasury/financial_accounts/{financial_account}/features",
        "verb": "get",
        "op_id": "GetTreasuryFinancialAccountsFinancialAccountFeatures",
        "summary": "Retrieve FinancialAccount Features",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/treasury/financial_accounts/{financial_account}/features",
        "verb": "post",
        "op_id": "PostTreasuryFinancialAccountsFinancialAccountFeatures",
        "summary": "Update FinancialAccount Features",
        "params": [
            {
                "name": "card_issuing",
                "description": "Encodes the FinancialAccount's ability to be used with the Issuing product, including attaching cards to and drawing funds from the FinancialAccount."
            },
            {
                "name": "deposit_insurance",
                "description": "Represents whether this FinancialAccount is eligible for deposit insurance. Various factors determine the insurance amount."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "financial_addresses",
                "description": "Contains Features that add FinancialAddresses to the FinancialAccount."
            },
            {
                "name": "inbound_transfers",
                "description": "Contains settings related to adding funds to a FinancialAccount from another Account with the same owner."
            },
            {
                "name": "intra_stripe_flows",
                "description": "Represents the ability for the FinancialAccount to send money to, or receive money from other FinancialAccounts (for example, via OutboundPayment)."
            },
            {
                "name": "outbound_payments",
                "description": "Includes Features related to initiating money movement out of the FinancialAccount to someone else's bucket of money."
            },
            {
                "name": "outbound_transfers",
                "description": "Contains a Feature and settings related to moving money out of the FinancialAccount into another Account with the same owner."
            }
        ]
    },
    {
        "path": "/v1/treasury/inbound_transfers",
        "verb": "get",
        "op_id": "GetTreasuryInboundTransfers",
        "summary": "List all InboundTransfers",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "financial_account",
                "description": "Returns objects associated with this FinancialAccount."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "status",
                "description": "Only return InboundTransfers that have the given status: `processing`, `succeeded`, `failed` or `canceled`."
            }
        ]
    },
    {
        "path": "/v1/treasury/inbound_transfers",
        "verb": "post",
        "op_id": "PostTreasuryInboundTransfers",
        "summary": "Create an InboundTransfer",
        "params": [
            {
                "name": "amount",
                "description": "Amount (in cents) to be transferred."
            },
            {
                "name": "currency",
                "description": "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "description",
                "description": "An arbitrary string attached to the object. Often useful for displaying to users."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "financial_account",
                "description": "The FinancialAccount to send funds to."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "origin_payment_method",
                "description": "The origin payment method to be debited for the InboundTransfer."
            },
            {
                "name": "statement_descriptor",
                "description": "The complete description that appears on your customers' statements. Maximum 10 characters."
            }
        ]
    },
    {
        "path": "/v1/treasury/inbound_transfers/{id}",
        "verb": "get",
        "op_id": "GetTreasuryInboundTransfersId",
        "summary": "Retrieve an InboundTransfer",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/treasury/inbound_transfers/{inbound_transfer}/cancel",
        "verb": "post",
        "op_id": "PostTreasuryInboundTransfersInboundTransferCancel",
        "summary": "Cancel an InboundTransfer",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/treasury/outbound_payments",
        "verb": "get",
        "op_id": "GetTreasuryOutboundPayments",
        "summary": "List all OutboundPayments",
        "params": [
            {
                "name": "created",
                "description": "Only return OutboundPayments that were created during the given date interval."
            },
            {
                "name": "customer",
                "description": "Only return OutboundPayments sent to this customer."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "financial_account",
                "description": "Returns objects associated with this FinancialAccount."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "status",
                "description": "Only return OutboundPayments that have the given status: `processing`, `failed`, `posted`, `returned`, or `canceled`."
            }
        ]
    },
    {
        "path": "/v1/treasury/outbound_payments",
        "verb": "post",
        "op_id": "PostTreasuryOutboundPayments",
        "summary": "Create an OutboundPayment",
        "params": [
            {
                "name": "amount",
                "description": "Amount (in cents) to be transferred."
            },
            {
                "name": "currency",
                "description": "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "customer",
                "description": "ID of the customer to whom the OutboundPayment is sent. Must match the Customer attached to the `destination_payment_method` passed in."
            },
            {
                "name": "description",
                "description": "An arbitrary string attached to the object. Often useful for displaying to users."
            },
            {
                "name": "destination_payment_method",
                "description": "The PaymentMethod to use as the payment instrument for the OutboundPayment. Exclusive with `destination_payment_method_data`."
            },
            {
                "name": "destination_payment_method_data",
                "description": "Hash used to generate the PaymentMethod to be used for this OutboundPayment. Exclusive with `destination_payment_method`."
            },
            {
                "name": "destination_payment_method_options",
                "description": "Payment method-specific configuration for this OutboundPayment."
            },
            {
                "name": "end_user_details",
                "description": "End user details."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "financial_account",
                "description": "The FinancialAccount to pull funds from."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "statement_descriptor",
                "description": "The description that appears on the receiving end for this OutboundPayment (for example, bank statement for external bank transfer). Maximum 10 characters for `ach` payments, 140 characters for `us_domestic_wire` payments, or 500 characters for `stripe` network transfers. The default value is \"payment\"."
            }
        ]
    },
    {
        "path": "/v1/treasury/outbound_payments/{id}",
        "verb": "get",
        "op_id": "GetTreasuryOutboundPaymentsId",
        "summary": "Retrieve an OutboundPayment",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/treasury/outbound_payments/{id}/cancel",
        "verb": "post",
        "op_id": "PostTreasuryOutboundPaymentsIdCancel",
        "summary": "Cancel an OutboundPayment",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/treasury/outbound_transfers",
        "verb": "get",
        "op_id": "GetTreasuryOutboundTransfers",
        "summary": "List all OutboundTransfers",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "financial_account",
                "description": "Returns objects associated with this FinancialAccount."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "status",
                "description": "Only return OutboundTransfers that have the given status: `processing`, `canceled`, `failed`, `posted`, or `returned`."
            }
        ]
    },
    {
        "path": "/v1/treasury/outbound_transfers",
        "verb": "post",
        "op_id": "PostTreasuryOutboundTransfers",
        "summary": "Create an OutboundTransfer",
        "params": [
            {
                "name": "amount",
                "description": "Amount (in cents) to be transferred."
            },
            {
                "name": "currency",
                "description": "Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies)."
            },
            {
                "name": "description",
                "description": "An arbitrary string attached to the object. Often useful for displaying to users."
            },
            {
                "name": "destination_payment_method",
                "description": "The PaymentMethod to use as the payment instrument for the OutboundTransfer."
            },
            {
                "name": "destination_payment_method_data",
                "description": "Hash used to generate the PaymentMethod to be used for this OutboundTransfer. Exclusive with `destination_payment_method`."
            },
            {
                "name": "destination_payment_method_options",
                "description": "Hash describing payment method configuration details."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "financial_account",
                "description": "The FinancialAccount to pull funds from."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "statement_descriptor",
                "description": "Statement descriptor to be shown on the receiving end of an OutboundTransfer. Maximum 10 characters for `ach` transfers or 140 characters for `us_domestic_wire` transfers. The default value is \"transfer\"."
            }
        ]
    },
    {
        "path": "/v1/treasury/outbound_transfers/{outbound_transfer}",
        "verb": "get",
        "op_id": "GetTreasuryOutboundTransfersOutboundTransfer",
        "summary": "Retrieve an OutboundTransfer",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/treasury/outbound_transfers/{outbound_transfer}/cancel",
        "verb": "post",
        "op_id": "PostTreasuryOutboundTransfersOutboundTransferCancel",
        "summary": "Cancel an OutboundTransfer",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/treasury/received_credits",
        "verb": "get",
        "op_id": "GetTreasuryReceivedCredits",
        "summary": "List all ReceivedCredits",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "financial_account",
                "description": "The FinancialAccount that received the funds."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "linked_flows",
                "description": "Only return ReceivedCredits described by the flow."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "status",
                "description": "Only return ReceivedCredits that have the given status: `succeeded` or `failed`."
            }
        ]
    },
    {
        "path": "/v1/treasury/received_credits/{id}",
        "verb": "get",
        "op_id": "GetTreasuryReceivedCreditsId",
        "summary": "Retrieve a ReceivedCredit",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/treasury/received_debits",
        "verb": "get",
        "op_id": "GetTreasuryReceivedDebits",
        "summary": "List all ReceivedDebits",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "financial_account",
                "description": "The FinancialAccount that funds were pulled from."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "status",
                "description": "Only return ReceivedDebits that have the given status: `succeeded` or `failed`."
            }
        ]
    },
    {
        "path": "/v1/treasury/received_debits/{id}",
        "verb": "get",
        "op_id": "GetTreasuryReceivedDebitsId",
        "summary": "Retrieve a ReceivedDebit",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/treasury/transaction_entries",
        "verb": "get",
        "op_id": "GetTreasuryTransactionEntries",
        "summary": "List all TransactionEntries",
        "params": [
            {
                "name": "created",
                "description": "Only return TransactionEntries that were created during the given date interval."
            },
            {
                "name": "effective_at",
                "description": ""
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "financial_account",
                "description": "Returns objects associated with this FinancialAccount."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "order_by",
                "description": "The results are in reverse chronological order by `created` or `effective_at`. The default is `created`."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "transaction",
                "description": "Only return TransactionEntries associated with this Transaction."
            }
        ]
    },
    {
        "path": "/v1/treasury/transaction_entries/{id}",
        "verb": "get",
        "op_id": "GetTreasuryTransactionEntriesId",
        "summary": "Retrieve a TransactionEntry",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/treasury/transactions",
        "verb": "get",
        "op_id": "GetTreasuryTransactions",
        "summary": "List all Transactions",
        "params": [
            {
                "name": "created",
                "description": "Only return Transactions that were created during the given date interval."
            },
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "financial_account",
                "description": "Returns objects associated with this FinancialAccount."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "order_by",
                "description": "The results are in reverse chronological order by `created` or `posted_at`. The default is `created`."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            },
            {
                "name": "status",
                "description": "Only return Transactions that have the given status: `open`, `posted`, or `void`."
            },
            {
                "name": "status_transitions",
                "description": "A filter for the `status_transitions.posted_at` timestamp. When using this filter, `status=posted` and `order_by=posted_at` must also be specified."
            }
        ]
    },
    {
        "path": "/v1/treasury/transactions/{id}",
        "verb": "get",
        "op_id": "GetTreasuryTransactionsId",
        "summary": "Retrieve a Transaction",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/webhook_endpoints",
        "verb": "get",
        "op_id": "GetWebhookEndpoints",
        "summary": "List all webhook endpoints",
        "params": [
            {
                "name": "ending_before",
                "description": "A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "limit",
                "description": "A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10."
            },
            {
                "name": "starting_after",
                "description": "A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."
            }
        ]
    },
    {
        "path": "/v1/webhook_endpoints",
        "verb": "post",
        "op_id": "PostWebhookEndpoints",
        "summary": "Create a webhook endpoint",
        "params": [
            {
                "name": "api_version",
                "description": "Events sent to this endpoint will be generated with this Stripe Version instead of your account's default Stripe Version."
            },
            {
                "name": "connect",
                "description": "Whether this endpoint should receive events from connected accounts (`true`), or from your account (`false`). Defaults to `false`."
            },
            {
                "name": "description",
                "description": "An optional description of what the webhook is used for."
            },
            {
                "name": "enabled_events",
                "description": "The list of events to enable for this endpoint. You may specify `['*']` to enable all events, except those that require explicit selection."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "url",
                "description": "The URL of the webhook endpoint."
            }
        ]
    },
    {
        "path": "/v1/webhook_endpoints/{webhook_endpoint}",
        "verb": "delete",
        "op_id": "DeleteWebhookEndpointsWebhookEndpoint",
        "summary": "Delete a webhook endpoint",
        "params": []
    },
    {
        "path": "/v1/webhook_endpoints/{webhook_endpoint}",
        "verb": "get",
        "op_id": "GetWebhookEndpointsWebhookEndpoint",
        "summary": "Retrieve a webhook endpoint",
        "params": [
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            }
        ]
    },
    {
        "path": "/v1/webhook_endpoints/{webhook_endpoint}",
        "verb": "post",
        "op_id": "PostWebhookEndpointsWebhookEndpoint",
        "summary": "Update a webhook endpoint",
        "params": [
            {
                "name": "description",
                "description": "An optional description of what the webhook is used for."
            },
            {
                "name": "disabled",
                "description": "Disable the webhook endpoint if set to true."
            },
            {
                "name": "enabled_events",
                "description": "The list of events to enable for this endpoint. You may specify `['*']` to enable all events, except those that require explicit selection."
            },
            {
                "name": "expand",
                "description": "Specifies which fields in the response should be expanded."
            },
            {
                "name": "metadata",
                "description": "Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."
            },
            {
                "name": "url",
                "description": "The URL of the webhook endpoint."
            }
        ]
    }
]