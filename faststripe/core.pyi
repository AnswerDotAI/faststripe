"""Fill in a module description here"""
__all__ = ['stripe_api_url', 'StripeApi']
from collections import defaultdict
from fastcore.all import *
from faststripe.endpoints import eps
from inspect import Parameter, Signature
import httpx, re
stripe_api_url = 'https://api.stripe.com'

def _flatten_data(data, prefix=''):
    """Flatten a dictionary of data so that it can be used in a request body."""
    ...

def _parse_operation_id(op_id):
    """Parse the operation ID to get the resource and verb"""
    ...

def _mk_func(path, verb, param_info, summary, hdrs={}):
    """Create a function from the Stripe API endpoint"""
    ...

class StripeApi:

    def __init__(self, api_key=None, base_url=stripe_api_url):
        ...

    def find_product(self, name: str):
        """Find a product by name"""
        ...

    def find_prices(self, product_id: str):
        """Find all prices associated with a product id"""
        ...

    def priced_product(self, product_name, amount_cents, currency='usd', recurring=None, description=None):
        """Create a product and price if they don't exist"""
        ...

    def one_time_payment(self, product_name, amount_cents, success_url, cancel_url, currency='usd', **kw):
        """Create a simple one-time payment checkout"""
        ...

    def subscription(self, product_name, amount_cents, success_url, cancel_url, currency='usd', interval='month', **kw):
        """Create a simple recurring subscription"""
        ...    account: Account
    account_links: Account_Links
    account_sessions: Account_Sessions
    accounts: Accounts
    accounts_account: Accounts_Account
    accounts_account_bank_accounts: Accounts_Account_Bank_Accounts
    accounts_account_bank_accounts_id: Accounts_Account_Bank_Accounts_Id
    accounts_account_capabilities: Accounts_Account_Capabilities
    accounts_account_capabilities_capability: Accounts_Account_Capabilities_Capability
    accounts_account_external_accounts: Accounts_Account_External_Accounts
    accounts_account_external_accounts_id: Accounts_Account_External_Accounts_Id
    accounts_account_login_links: Accounts_Account_Login_Links
    accounts_account_people: Accounts_Account_People
    accounts_account_people_person: Accounts_Account_People_Person
    accounts_account_persons: Accounts_Account_Persons
    accounts_account_persons_person: Accounts_Account_Persons_Person
    accounts_account_reject: Accounts_Account_Reject
    apple_pay_domains: Apple_Pay_Domains
    apple_pay_domains_domain: Apple_Pay_Domains_Domain
    application_fees: Application_Fees
    application_fees_fee_refunds_id: Application_Fees_Fee_Refunds_Id
    application_fees_id: Application_Fees_Id
    application_fees_id_refund: Application_Fees_Id_Refund
    application_fees_id_refunds: Application_Fees_Id_Refunds
    apps_secrets: Apps_Secrets
    apps_secrets_delete: Apps_Secrets_Delete
    apps_secrets_find: Apps_Secrets_Find
    balance: Balance
    balance_history: Balance_History
    balance_history_id: Balance_History_Id
    balance_transactions: Balance_Transactions
    balance_transactions_id: Balance_Transactions_Id
    billing_alerts: Billing_Alerts
    billing_alerts_id: Billing_Alerts_Id
    billing_alerts_id_activate: Billing_Alerts_Id_Activate
    billing_alerts_id_archive: Billing_Alerts_Id_Archive
    billing_alerts_id_deactivate: Billing_Alerts_Id_Deactivate
    billing_credit_balance_summary: Billing_Credit_Balance_Summary
    billing_credit_balance_transactions: Billing_Credit_Balance_Transactions
    billing_credit_balance_transactions_id: Billing_Credit_Balance_Transactions_Id
    billing_credit_grants: Billing_Credit_Grants
    billing_credit_grants_id: Billing_Credit_Grants_Id
    billing_credit_grants_id_expire: Billing_Credit_Grants_Id_Expire
    billing_credit_grants_id_void: Billing_Credit_Grants_Id_Void
    billing_meter_event_adjustments: Billing_Meter_Event_Adjustments
    billing_meter_events: Billing_Meter_Events
    billing_meters: Billing_Meters
    billing_meters_id: Billing_Meters_Id
    billing_meters_id_deactivate: Billing_Meters_Id_Deactivate
    billing_meters_id_event_summaries: Billing_Meters_Id_Event_Summaries
    billing_meters_id_reactivate: Billing_Meters_Id_Reactivate
    billing_portal_configurations: Billing_Portal_Configurations
    billing_portal_configurations_configuration: Billing_Portal_Configurations_Configuration
    billing_portal_sessions: Billing_Portal_Sessions
    charges: Charges
    charges_search: Charges_Search
    charges_charge: Charges_Charge
    charges_charge_capture: Charges_Charge_Capture
    charges_charge_dispute: Charges_Charge_Dispute
    charges_charge_dispute_close: Charges_Charge_Dispute_Close
    charges_charge_refund: Charges_Charge_Refund
    charges_charge_refunds: Charges_Charge_Refunds
    charges_charge_refunds_refund: Charges_Charge_Refunds_Refund
    checkout_sessions: Checkout_Sessions
    checkout_sessions_session: Checkout_Sessions_Session
    checkout_sessions_session_expire: Checkout_Sessions_Session_Expire
    checkout_sessions_session_line_items: Checkout_Sessions_Session_Line_Items
    climate_orders: Climate_Orders
    climate_orders_order: Climate_Orders_Order
    climate_orders_order_cancel: Climate_Orders_Order_Cancel
    climate_products: Climate_Products
    climate_products_product: Climate_Products_Product
    climate_suppliers: Climate_Suppliers
    climate_suppliers_supplier: Climate_Suppliers_Supplier
    confirmation_tokens_confirmation_token: Confirmation_Tokens_Confirmation_Token
    country_specs: Country_Specs
    country_specs_country: Country_Specs_Country
    coupons: Coupons
    coupons_coupon: Coupons_Coupon
    credit_notes: Credit_Notes
    credit_notes_preview: Credit_Notes_Preview
    credit_notes_preview_lines: Credit_Notes_Preview_Lines
    credit_notes_credit_note_lines: Credit_Notes_Credit_Note_Lines
    credit_notes_id: Credit_Notes_Id
    credit_notes_id_void: Credit_Notes_Id_Void
    customer_sessions: Customer_Sessions
    customers: Customers
    customers_search: Customers_Search
    customers_customer: Customers_Customer
    customers_customer_balance_transactions: Customers_Customer_Balance_Transactions
    customers_customer_balance_transactions_transaction: Customers_Customer_Balance_Transactions_Transaction
    customers_customer_bank_accounts: Customers_Customer_Bank_Accounts
    customers_customer_bank_accounts_id: Customers_Customer_Bank_Accounts_Id
    customers_customer_bank_accounts_id_verify: Customers_Customer_Bank_Accounts_Id_Verify
    customers_customer_cards: Customers_Customer_Cards
    customers_customer_cards_id: Customers_Customer_Cards_Id
    customers_customer_cash_balance: Customers_Customer_Cash_Balance
    customers_customer_cash_balance_transactions: Customers_Customer_Cash_Balance_Transactions
    customers_customer_cash_balance_transactions_transaction: Customers_Customer_Cash_Balance_Transactions_Transaction
    customers_customer_discount: Customers_Customer_Discount
    customers_customer_funding_instructions: Customers_Customer_Funding_Instructions
    customers_customer_payment_methods: Customers_Customer_Payment_Methods
    customers_customer_payment_methods_payment_method: Customers_Customer_Payment_Methods_Payment_Method
    customers_customer_sources: Customers_Customer_Sources
    customers_customer_sources_id: Customers_Customer_Sources_Id
    customers_customer_sources_id_verify: Customers_Customer_Sources_Id_Verify
    customers_customer_subscriptions: Customers_Customer_Subscriptions
    customers_customer_subscriptions_subscription_exposed_id: Customers_Customer_Subscriptions_Subscription_Exposed_Id
    customers_customer_subscriptions_subscription_exposed_id_discount: Customers_Customer_Subscriptions_Subscription_Exposed_Id_Discount
    customers_customer_tax_ids: Customers_Customer_Tax_Ids
    customers_customer_tax_ids_id: Customers_Customer_Tax_Ids_Id
    disputes: Disputes
    disputes_dispute: Disputes_Dispute
    disputes_dispute_close: Disputes_Dispute_Close
    entitlements_active_entitlements: Entitlements_Active_Entitlements
    entitlements_active_entitlements_id: Entitlements_Active_Entitlements_Id
    entitlements_features: Entitlements_Features
    entitlements_features_id: Entitlements_Features_Id
    ephemeral_keys: Ephemeral_Keys
    ephemeral_keys_key: Ephemeral_Keys_Key
    events: Events
    events_id: Events_Id
    exchange_rates: Exchange_Rates
    exchange_rates_rate_id: Exchange_Rates_Rate_Id
    external_accounts_id: External_Accounts_Id
    file_links: File_Links
    file_links_link: File_Links_Link
    files: Files
    files_file: Files_File
    financial_connections_accounts: Financial_Connections_Accounts
    financial_connections_accounts_account: Financial_Connections_Accounts_Account
    financial_connections_accounts_account_disconnect: Financial_Connections_Accounts_Account_Disconnect
    financial_connections_accounts_account_owners: Financial_Connections_Accounts_Account_Owners
    financial_connections_accounts_account_refresh: Financial_Connections_Accounts_Account_Refresh
    financial_connections_accounts_account_subscribe: Financial_Connections_Accounts_Account_Subscribe
    financial_connections_accounts_account_unsubscribe: Financial_Connections_Accounts_Account_Unsubscribe
    financial_connections_sessions: Financial_Connections_Sessions
    financial_connections_sessions_session: Financial_Connections_Sessions_Session
    financial_connections_transactions: Financial_Connections_Transactions
    financial_connections_transactions_transaction: Financial_Connections_Transactions_Transaction
    forwarding_requests: Forwarding_Requests
    forwarding_requests_id: Forwarding_Requests_Id
    identity_verification_reports: Identity_Verification_Reports
    identity_verification_reports_report: Identity_Verification_Reports_Report
    identity_verification_sessions: Identity_Verification_Sessions
    identity_verification_sessions_session: Identity_Verification_Sessions_Session
    identity_verification_sessions_session_cancel: Identity_Verification_Sessions_Session_Cancel
    identity_verification_sessions_session_redact: Identity_Verification_Sessions_Session_Redact
    invoice_payments: Invoice_Payments
    invoice_payments_invoice_payment: Invoice_Payments_Invoice_Payment
    invoice_rendering_templates: Invoice_Rendering_Templates
    invoice_rendering_templates_template: Invoice_Rendering_Templates_Template
    invoice_rendering_templates_template_archive: Invoice_Rendering_Templates_Template_Archive
    invoice_rendering_templates_template_unarchive: Invoice_Rendering_Templates_Template_Unarchive
    invoiceitems: Invoiceitems
    invoiceitems_invoiceitem: Invoiceitems_Invoiceitem
    invoices: Invoices
    invoices_create_preview: Invoices_Create_Preview
    invoices_search: Invoices_Search
    invoices_invoice: Invoices_Invoice
    invoices_invoice_add_lines: Invoices_Invoice_Add_Lines
    invoices_invoice_attach_payment: Invoices_Invoice_Attach_Payment
    invoices_invoice_finalize: Invoices_Invoice_Finalize
    invoices_invoice_lines: Invoices_Invoice_Lines
    invoices_invoice_lines_line_item_id: Invoices_Invoice_Lines_Line_Item_Id
    invoices_invoice_mark_uncollectible: Invoices_Invoice_Mark_Uncollectible
    invoices_invoice_pay: Invoices_Invoice_Pay
    invoices_invoice_remove_lines: Invoices_Invoice_Remove_Lines
    invoices_invoice_send: Invoices_Invoice_Send
    invoices_invoice_update_lines: Invoices_Invoice_Update_Lines
    invoices_invoice_void: Invoices_Invoice_Void
    issuing_authorizations: Issuing_Authorizations
    issuing_authorizations_authorization: Issuing_Authorizations_Authorization
    issuing_authorizations_authorization_approve: Issuing_Authorizations_Authorization_Approve
    issuing_authorizations_authorization_decline: Issuing_Authorizations_Authorization_Decline
    issuing_cardholders: Issuing_Cardholders
    issuing_cardholders_cardholder: Issuing_Cardholders_Cardholder
    issuing_cards: Issuing_Cards
    issuing_cards_card: Issuing_Cards_Card
    issuing_disputes: Issuing_Disputes
    issuing_disputes_dispute: Issuing_Disputes_Dispute
    issuing_disputes_dispute_submit: Issuing_Disputes_Dispute_Submit
    issuing_personalization_designs: Issuing_Personalization_Designs
    issuing_personalization_designs_personalization_design: Issuing_Personalization_Designs_Personalization_Design
    issuing_physical_bundles: Issuing_Physical_Bundles
    issuing_physical_bundles_physical_bundle: Issuing_Physical_Bundles_Physical_Bundle
    issuing_settlements_settlement: Issuing_Settlements_Settlement
    issuing_tokens: Issuing_Tokens
    issuing_tokens_token: Issuing_Tokens_Token
    issuing_transactions: Issuing_Transactions
    issuing_transactions_transaction: Issuing_Transactions_Transaction
    link_account_sessions: Link_Account_Sessions
    link_account_sessions_session: Link_Account_Sessions_Session
    linked_accounts: Linked_Accounts
    linked_accounts_account: Linked_Accounts_Account
    linked_accounts_account_disconnect: Linked_Accounts_Account_Disconnect
    linked_accounts_account_owners: Linked_Accounts_Account_Owners
    linked_accounts_account_refresh: Linked_Accounts_Account_Refresh
    mandates_mandate: Mandates_Mandate
    payment_intents: Payment_Intents
    payment_intents_search: Payment_Intents_Search
    payment_intents_intent: Payment_Intents_Intent
    payment_intents_intent_apply_customer_balance: Payment_Intents_Intent_Apply_Customer_Balance
    payment_intents_intent_cancel: Payment_Intents_Intent_Cancel
    payment_intents_intent_capture: Payment_Intents_Intent_Capture
    payment_intents_intent_confirm: Payment_Intents_Intent_Confirm
    payment_intents_intent_increment_authorization: Payment_Intents_Intent_Increment_Authorization
    payment_intents_intent_verify_microdeposits: Payment_Intents_Intent_Verify_Microdeposits
    payment_links: Payment_Links
    payment_links_payment_link: Payment_Links_Payment_Link
    payment_links_payment_link_line_items: Payment_Links_Payment_Link_Line_Items
    payment_method_configurations: Payment_Method_Configurations
    payment_method_configurations_configuration: Payment_Method_Configurations_Configuration
    payment_method_domains: Payment_Method_Domains
    payment_method_domains_payment_method_domain: Payment_Method_Domains_Payment_Method_Domain
    payment_method_domains_payment_method_domain_validate: Payment_Method_Domains_Payment_Method_Domain_Validate
    payment_methods: Payment_Methods
    payment_methods_payment_method: Payment_Methods_Payment_Method
    payment_methods_payment_method_attach: Payment_Methods_Payment_Method_Attach
    payment_methods_payment_method_detach: Payment_Methods_Payment_Method_Detach
    payouts: Payouts
    payouts_payout: Payouts_Payout
    payouts_payout_cancel: Payouts_Payout_Cancel
    payouts_payout_reverse: Payouts_Payout_Reverse
    plans: Plans
    plans_plan: Plans_Plan
    prices: Prices
    prices_search: Prices_Search
    prices_price: Prices_Price
    products: Products
    products_search: Products_Search
    products_id: Products_Id
    products_product_features: Products_Product_Features
    products_product_features_id: Products_Product_Features_Id
    promotion_codes: Promotion_Codes
    promotion_codes_promotion_code: Promotion_Codes_Promotion_Code
    quotes: Quotes
    quotes_quote: Quotes_Quote
    quotes_quote_accept: Quotes_Quote_Accept
    quotes_quote_cancel: Quotes_Quote_Cancel
    quotes_quote_computed_upfront_line_items: Quotes_Quote_Computed_Upfront_Line_Items
    quotes_quote_finalize: Quotes_Quote_Finalize
    quotes_quote_line_items: Quotes_Quote_Line_Items
    quotes_quote_pdf: Quotes_Quote_Pdf
    radar_early_fraud_warnings: Radar_Early_Fraud_Warnings
    radar_early_fraud_warnings_early_fraud_warning: Radar_Early_Fraud_Warnings_Early_Fraud_Warning
    radar_value_list_items: Radar_Value_List_Items
    radar_value_list_items_item: Radar_Value_List_Items_Item
    radar_value_lists: Radar_Value_Lists
    radar_value_lists_value_list: Radar_Value_Lists_Value_List
    refunds: Refunds
    refunds_refund: Refunds_Refund
    refunds_refund_cancel: Refunds_Refund_Cancel
    reporting_report_runs: Reporting_Report_Runs
    reporting_report_runs_report_run: Reporting_Report_Runs_Report_Run
    reporting_report_types: Reporting_Report_Types
    reporting_report_types_report_type: Reporting_Report_Types_Report_Type
    reviews: Reviews
    reviews_review: Reviews_Review
    reviews_review_approve: Reviews_Review_Approve
    setup_attempts: Setup_Attempts
    setup_intents: Setup_Intents
    setup_intents_intent: Setup_Intents_Intent
    setup_intents_intent_cancel: Setup_Intents_Intent_Cancel
    setup_intents_intent_confirm: Setup_Intents_Intent_Confirm
    setup_intents_intent_verify_microdeposits: Setup_Intents_Intent_Verify_Microdeposits
    shipping_rates: Shipping_Rates
    shipping_rates_shipping_rate_token: Shipping_Rates_Shipping_Rate_Token
    sigma_saved_queries_id: Sigma_Saved_Queries_Id
    sigma_scheduled_query_runs: Sigma_Scheduled_Query_Runs
    sigma_scheduled_query_runs_scheduled_query_run: Sigma_Scheduled_Query_Runs_Scheduled_Query_Run
    sources: Sources
    sources_source: Sources_Source
    sources_source_mandate_notifications_mandate_notification: Sources_Source_Mandate_Notifications_Mandate_Notification
    sources_source_source_transactions: Sources_Source_Source_Transactions
    sources_source_source_transactions_source_transaction: Sources_Source_Source_Transactions_Source_Transaction
    sources_source_verify: Sources_Source_Verify
    subscription_items: Subscription_Items
    subscription_items_item: Subscription_Items_Item
    subscription_schedules: Subscription_Schedules
    subscription_schedules_schedule: Subscription_Schedules_Schedule
    subscription_schedules_schedule_cancel: Subscription_Schedules_Schedule_Cancel
    subscription_schedules_schedule_release: Subscription_Schedules_Schedule_Release
    subscriptions: Subscriptions
    subscriptions_search: Subscriptions_Search
    subscriptions_subscription_exposed_id: Subscriptions_Subscription_Exposed_Id
    subscriptions_subscription_exposed_id_discount: Subscriptions_Subscription_Exposed_Id_Discount
    subscriptions_subscription_resume: Subscriptions_Subscription_Resume
    tax_calculations: Tax_Calculations
    tax_calculations_calculation: Tax_Calculations_Calculation
    tax_calculations_calculation_line_items: Tax_Calculations_Calculation_Line_Items
    tax_registrations: Tax_Registrations
    tax_registrations_id: Tax_Registrations_Id
    tax_settings: Tax_Settings
    tax_transactions_create_from_calculation: Tax_Transactions_Create_From_Calculation
    tax_transactions_create_reversal: Tax_Transactions_Create_Reversal
    tax_transactions_transaction: Tax_Transactions_Transaction
    tax_transactions_transaction_line_items: Tax_Transactions_Transaction_Line_Items
    tax_codes: Tax_Codes
    tax_codes_id: Tax_Codes_Id
    tax_ids: Tax_Ids
    tax_ids_id: Tax_Ids_Id
    tax_rates: Tax_Rates
    tax_rates_tax_rate: Tax_Rates_Tax_Rate
    terminal_configurations: Terminal_Configurations
    terminal_configurations_configuration: Terminal_Configurations_Configuration
    terminal_connection_tokens: Terminal_Connection_Tokens
    terminal_locations: Terminal_Locations
    terminal_locations_location: Terminal_Locations_Location
    terminal_readers: Terminal_Readers
    terminal_readers_reader: Terminal_Readers_Reader
    terminal_readers_reader_cancel_action: Terminal_Readers_Reader_Cancel_Action
    terminal_readers_reader_collect_inputs: Terminal_Readers_Reader_Collect_Inputs
    terminal_readers_reader_process_payment_intent: Terminal_Readers_Reader_Process_Payment_Intent
    terminal_readers_reader_process_setup_intent: Terminal_Readers_Reader_Process_Setup_Intent
    terminal_readers_reader_refund_payment: Terminal_Readers_Reader_Refund_Payment
    terminal_readers_reader_set_reader_display: Terminal_Readers_Reader_Set_Reader_Display
    test_helpers_confirmation_tokens: Test_Helpers_Confirmation_Tokens
    test_helpers_customers_customer_fund_cash_balance: Test_Helpers_Customers_Customer_Fund_Cash_Balance
    test_helpers_issuing_authorizations: Test_Helpers_Issuing_Authorizations
    test_helpers_issuing_authorizations_authorization_capture: Test_Helpers_Issuing_Authorizations_Authorization_Capture
    test_helpers_issuing_authorizations_authorization_expire: Test_Helpers_Issuing_Authorizations_Authorization_Expire
    test_helpers_issuing_authorizations_authorization_finalize_amount: Test_Helpers_Issuing_Authorizations_Authorization_Finalize_Amount
    test_helpers_issuing_authorizations_authorization_fraud_challenges_respond: Test_Helpers_Issuing_Authorizations_Authorization_Fraud_Challenges_Respond
    test_helpers_issuing_authorizations_authorization_increment: Test_Helpers_Issuing_Authorizations_Authorization_Increment
    test_helpers_issuing_authorizations_authorization_reverse: Test_Helpers_Issuing_Authorizations_Authorization_Reverse
    test_helpers_issuing_cards_card_shipping_deliver: Test_Helpers_Issuing_Cards_Card_Shipping_Deliver
    test_helpers_issuing_cards_card_shipping_fail: Test_Helpers_Issuing_Cards_Card_Shipping_Fail
    test_helpers_issuing_cards_card_shipping_return: Test_Helpers_Issuing_Cards_Card_Shipping_Return
    test_helpers_issuing_cards_card_shipping_ship: Test_Helpers_Issuing_Cards_Card_Shipping_Ship
    test_helpers_issuing_cards_card_shipping_submit: Test_Helpers_Issuing_Cards_Card_Shipping_Submit
    test_helpers_issuing_personalization_designs_personalization_design_activate: Test_Helpers_Issuing_Personalization_Designs_Personalization_Design_Activate
    test_helpers_issuing_personalization_designs_personalization_design_deactivate: Test_Helpers_Issuing_Personalization_Designs_Personalization_Design_Deactivate
    test_helpers_issuing_personalization_designs_personalization_design_reject: Test_Helpers_Issuing_Personalization_Designs_Personalization_Design_Reject
    test_helpers_issuing_settlements: Test_Helpers_Issuing_Settlements
    test_helpers_issuing_settlements_settlement_complete: Test_Helpers_Issuing_Settlements_Settlement_Complete
    test_helpers_issuing_transactions_create_force_capture: Test_Helpers_Issuing_Transactions_Create_Force_Capture
    test_helpers_issuing_transactions_create_unlinked_refund: Test_Helpers_Issuing_Transactions_Create_Unlinked_Refund
    test_helpers_issuing_transactions_transaction_refund: Test_Helpers_Issuing_Transactions_Transaction_Refund
    test_helpers_refunds_refund_expire: Test_Helpers_Refunds_Refund_Expire
    test_helpers_terminal_readers_reader_present_payment_method: Test_Helpers_Terminal_Readers_Reader_Present_Payment_Method
    test_helpers_terminal_readers_reader_succeed_input_collection: Test_Helpers_Terminal_Readers_Reader_Succeed_Input_Collection
    test_helpers_terminal_readers_reader_timeout_input_collection: Test_Helpers_Terminal_Readers_Reader_Timeout_Input_Collection
    test_helpers_test_clocks: Test_Helpers_Test_Clocks
    test_helpers_test_clocks_test_clock: Test_Helpers_Test_Clocks_Test_Clock
    test_helpers_test_clocks_test_clock_advance: Test_Helpers_Test_Clocks_Test_Clock_Advance
    test_helpers_treasury_inbound_transfers_id_fail: Test_Helpers_Treasury_Inbound_Transfers_Id_Fail
    test_helpers_treasury_inbound_transfers_id_return: Test_Helpers_Treasury_Inbound_Transfers_Id_Return
    test_helpers_treasury_inbound_transfers_id_succeed: Test_Helpers_Treasury_Inbound_Transfers_Id_Succeed
    test_helpers_treasury_outbound_payments_id: Test_Helpers_Treasury_Outbound_Payments_Id
    test_helpers_treasury_outbound_payments_id_fail: Test_Helpers_Treasury_Outbound_Payments_Id_Fail
    test_helpers_treasury_outbound_payments_id_post: Test_Helpers_Treasury_Outbound_Payments_Id_Post
    test_helpers_treasury_outbound_payments_id_return: Test_Helpers_Treasury_Outbound_Payments_Id_Return
    test_helpers_treasury_outbound_transfers_outbound_transfer: Test_Helpers_Treasury_Outbound_Transfers_Outbound_Transfer
    test_helpers_treasury_outbound_transfers_outbound_transfer_fail: Test_Helpers_Treasury_Outbound_Transfers_Outbound_Transfer_Fail
    test_helpers_treasury_outbound_transfers_outbound_transfer_post: Test_Helpers_Treasury_Outbound_Transfers_Outbound_Transfer_Post
    test_helpers_treasury_outbound_transfers_outbound_transfer_return: Test_Helpers_Treasury_Outbound_Transfers_Outbound_Transfer_Return
    test_helpers_treasury_received_credits: Test_Helpers_Treasury_Received_Credits
    test_helpers_treasury_received_debits: Test_Helpers_Treasury_Received_Debits
    tokens: Tokens
    tokens_token: Tokens_Token
    topups: Topups
    topups_topup: Topups_Topup
    topups_topup_cancel: Topups_Topup_Cancel
    transfers: Transfers
    transfers_id_reversals: Transfers_Id_Reversals
    transfers_transfer: Transfers_Transfer
    transfers_transfer_reversals_id: Transfers_Transfer_Reversals_Id
    treasury_credit_reversals: Treasury_Credit_Reversals
    treasury_credit_reversals_credit_reversal: Treasury_Credit_Reversals_Credit_Reversal
    treasury_debit_reversals: Treasury_Debit_Reversals
    treasury_debit_reversals_debit_reversal: Treasury_Debit_Reversals_Debit_Reversal
    treasury_financial_accounts: Treasury_Financial_Accounts
    treasury_financial_accounts_financial_account: Treasury_Financial_Accounts_Financial_Account
    treasury_financial_accounts_financial_account_close: Treasury_Financial_Accounts_Financial_Account_Close
    treasury_financial_accounts_financial_account_features: Treasury_Financial_Accounts_Financial_Account_Features
    treasury_inbound_transfers: Treasury_Inbound_Transfers
    treasury_inbound_transfers_id: Treasury_Inbound_Transfers_Id
    treasury_inbound_transfers_inbound_transfer_cancel: Treasury_Inbound_Transfers_Inbound_Transfer_Cancel
    treasury_outbound_payments: Treasury_Outbound_Payments
    treasury_outbound_payments_id: Treasury_Outbound_Payments_Id
    treasury_outbound_payments_id_cancel: Treasury_Outbound_Payments_Id_Cancel
    treasury_outbound_transfers: Treasury_Outbound_Transfers
    treasury_outbound_transfers_outbound_transfer: Treasury_Outbound_Transfers_Outbound_Transfer
    treasury_outbound_transfers_outbound_transfer_cancel: Treasury_Outbound_Transfers_Outbound_Transfer_Cancel
    treasury_received_credits: Treasury_Received_Credits
    treasury_received_credits_id: Treasury_Received_Credits_Id
    treasury_received_debits: Treasury_Received_Debits
    treasury_received_debits_id: Treasury_Received_Debits_Id
    treasury_transaction_entries: Treasury_Transaction_Entries
    treasury_transaction_entries_id: Treasury_Transaction_Entries_Id
    treasury_transactions: Treasury_Transactions
    treasury_transactions_id: Treasury_Transactions_Id
    webhook_endpoints: Webhook_Endpoints
    webhook_endpoints_webhook_endpoint: Webhook_Endpoints_Webhook_Endpoint

class _StripeResourceGroup:
    """Base class for Stripe resource groups with dynamic methods"""
    def create(self, **kwargs): ...
    def fetch(self, **kwargs): ...
    def delete(self, **kwargs): ...
    def update(self, **kwargs): ...

class Account(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve account

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Account_Links(_StripeResourceGroup):
	def create(*, account=None, collect=None, collection_options=None, expand=None, refresh_url=None, return_url=None, type=None):
		"""Create an account link

Parameters:
    account: The identifier of the account to create an account link for.
    collect: The collect parameter is deprecated. Use `collection_options` instead.
    collection_options: Specifies the requirements that Stripe collects from connected accounts in the Connect Onboarding flow.
    expand: Specifies which fields in the response should be expanded.
    refresh_url: The URL the user will be redirected to if the account link is expired, has been previously-visited, or is otherwise invalid. The URL you specify should attempt to generate a new account link with the same parameters used to create the original account link, then redirect the user to the new account link's URL so they can continue with Connect Onboarding. If a new account link cannot be generated or the redirect fails you should display a useful error to the user.
    return_url: The URL that the user will be redirected to upon leaving or completing the linked flow.
    type: The type of account link the user is requesting. Possible values are `account_onboarding` or `account_update`."""
		...


class Account_Sessions(_StripeResourceGroup):
	def create(*, account=None, components=None, expand=None):
		"""Create an Account Session

Parameters:
    account: The identifier of the account to create an Account Session for.
    components: Each key of the dictionary represents an embedded component, and each embedded component maps to its configuration (e.g. whether it has been enabled or not).
    expand: Specifies which fields in the response should be expanded."""
		...


class Accounts(_StripeResourceGroup):
	def fetch(*, created=None, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List all connected accounts

Parameters:
    created: Only return connected accounts that were created during the given date interval.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, account_token=None, bank_account=None, business_profile=None, business_type=None, capabilities=None, company=None, controller=None, country=None, default_currency=None, documents=None, email=None, expand=None, external_account=None, groups=None, individual=None, metadata=None, settings=None, tos_acceptance=None, type=None):
		"""

Parameters:
    account_token: An [account token](https://stripe.com/docs/api#create_account_token), used to securely provide details to the account.
    bank_account: Either a token, like the ones returned by [Stripe.js](https://stripe.com/docs/js), or a dictionary containing a user's bank account details.
    business_profile: Business information about the account.
    business_type: The business type. Once you create an [Account Link](/api/account_links) or [Account Session](/api/account_sessions), this property can only be updated for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts.
    capabilities: Each key of the dictionary represents a capability, and each capability
maps to its settings (for example, whether it has been requested or not). Each
capability is inactive until you have provided its specific
requirements and Stripe has verified them. An account might have some
of its requested capabilities be active and some be inactive.

Required when [account.controller.stripe_dashboard.type](/api/accounts/create#create_account-controller-dashboard-type)
is `none`, which includes Custom accounts.
    company: Information about the company or business. This field is available for any `business_type`. Once you create an [Account Link](/api/account_links) or [Account Session](/api/account_sessions), this property can only be updated for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts.
    controller: A hash of configuration describing the account controller's attributes.
    country: The country in which the account holder resides, or in which the business is legally established. This should be an ISO 3166-1 alpha-2 country code. For example, if you are in the United States and the business for which you're creating an account is legally represented in Canada, you would use `CA` as the country for the account being created. Available countries include [Stripe's global markets](https://stripe.com/global) as well as countries where [cross-border payouts](https://stripe.com/docs/connect/cross-border-payouts) are supported.
    default_currency: Three-letter ISO currency code representing the default currency for the account. This must be a currency that [Stripe supports in the account's country](https://docs.stripe.com/payouts).
    documents: Documents that may be submitted to satisfy various informational requests.
    email: The email address of the account holder. This is only to make the account easier to identify to you. If [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts, Stripe doesn't email the account without your consent.
    expand: Specifies which fields in the response should be expanded.
    external_account: A card or bank account to attach to the account for receiving [payouts](/connect/bank-debit-card-payouts) (you won’t be able to use it for top-ups). You can provide either a token, like the ones returned by [Stripe.js](/js), or a dictionary, as documented in the `external_account` parameter for [bank account](/api#account_create_bank_account) creation. <br><br>By default, providing an external account sets it as the new default external account for its currency, and deletes the old default if one exists. To add additional external accounts without replacing the existing default for the currency, use the [bank account](/api#account_create_bank_account) or [card creation](/api#account_create_card) APIs. After you create an [Account Link](/api/account_links) or [Account Session](/api/account_sessions), this property can only be updated for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts.
    groups: A hash of account group type to tokens. These are account groups this account should be added to.
    individual: Information about the person represented by the account. This field is null unless `business_type` is set to `individual`. Once you create an [Account Link](/api/account_links) or [Account Session](/api/account_sessions), this property can only be updated for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    settings: Options for customizing how the account functions within Stripe.
    tos_acceptance: Details on the account's acceptance of the [Stripe Services Agreement](/connect/updating-accounts#tos-acceptance). This property can only be updated for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts. This property defaults to a `full` service agreement when empty.
    type: The type of Stripe account to create. May be one of `custom`, `express` or `standard`."""
		...


class Accounts_Account(_StripeResourceGroup):
	def delete():
		"""Delete an account"""
		...
	def fetch(*, expand=None):
		"""Retrieve account

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, account_token=None, business_profile=None, business_type=None, capabilities=None, company=None, default_currency=None, documents=None, email=None, expand=None, external_account=None, groups=None, individual=None, metadata=None, settings=None, tos_acceptance=None):
		"""Update an account

Parameters:
    account_token: An [account token](https://stripe.com/docs/api#create_account_token), used to securely provide details to the account.
    business_profile: Business information about the account.
    business_type: The business type. Once you create an [Account Link](/api/account_links) or [Account Session](/api/account_sessions), this property can only be updated for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts.
    capabilities: Each key of the dictionary represents a capability, and each capability
maps to its settings (for example, whether it has been requested or not). Each
capability is inactive until you have provided its specific
requirements and Stripe has verified them. An account might have some
of its requested capabilities be active and some be inactive.

Required when [account.controller.stripe_dashboard.type](/api/accounts/create#create_account-controller-dashboard-type)
is `none`, which includes Custom accounts.
    company: Information about the company or business. This field is available for any `business_type`. Once you create an [Account Link](/api/account_links) or [Account Session](/api/account_sessions), this property can only be updated for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts.
    default_currency: Three-letter ISO currency code representing the default currency for the account. This must be a currency that [Stripe supports in the account's country](https://docs.stripe.com/payouts).
    documents: Documents that may be submitted to satisfy various informational requests.
    email: The email address of the account holder. This is only to make the account easier to identify to you. If [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts, Stripe doesn't email the account without your consent.
    expand: Specifies which fields in the response should be expanded.
    external_account: A card or bank account to attach to the account for receiving [payouts](/connect/bank-debit-card-payouts) (you won’t be able to use it for top-ups). You can provide either a token, like the ones returned by [Stripe.js](/js), or a dictionary, as documented in the `external_account` parameter for [bank account](/api#account_create_bank_account) creation. <br><br>By default, providing an external account sets it as the new default external account for its currency, and deletes the old default if one exists. To add additional external accounts without replacing the existing default for the currency, use the [bank account](/api#account_create_bank_account) or [card creation](/api#account_create_card) APIs. After you create an [Account Link](/api/account_links) or [Account Session](/api/account_sessions), this property can only be updated for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts.
    groups: A hash of account group type to tokens. These are account groups this account should be added to.
    individual: Information about the person represented by the account. This field is null unless `business_type` is set to `individual`. Once you create an [Account Link](/api/account_links) or [Account Session](/api/account_sessions), this property can only be updated for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    settings: Options for customizing how the account functions within Stripe.
    tos_acceptance: Details on the account's acceptance of the [Stripe Services Agreement](/connect/updating-accounts#tos-acceptance). This property can only be updated for accounts where [controller.requirement_collection](/api/accounts/object#account_object-controller-requirement_collection) is `application`, which includes Custom accounts. This property defaults to a `full` service agreement when empty."""
		...


class Accounts_Account_Bank_Accounts(_StripeResourceGroup):
	def create(*, bank_account=None, default_for_currency=None, expand=None, external_account=None, metadata=None):
		"""Create an external account

Parameters:
    bank_account: Either a token, like the ones returned by [Stripe.js](https://stripe.com/docs/js), or a dictionary containing a user's bank account details.
    default_for_currency: When set to true, or if this is the first external account added in this currency, this account becomes the default external account for its currency.
    expand: Specifies which fields in the response should be expanded.
    external_account: A token, like the ones returned by [Stripe.js](https://stripe.com/docs/js) or a dictionary containing a user's external account details (with the options shown below). Please refer to full [documentation](https://stripe.com/docs/api/external_accounts) instead.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."""
		...


class Accounts_Account_Bank_Accounts_Id(_StripeResourceGroup):
	def delete():
		"""Delete an external account"""
		...
	def fetch(*, expand=None):
		"""Retrieve an external account

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, account_holder_name=None, account_holder_type=None, account_type=None, address_city=None, address_country=None, address_line1=None, address_line2=None, address_state=None, address_zip=None, default_for_currency=None, documents=None, exp_month=None, exp_year=None, expand=None, metadata=None, name=None):
		"""

Parameters:
    account_holder_name: The name of the person or business that owns the bank account.
    account_holder_type: The type of entity that holds the account. This can be either `individual` or `company`.
    account_type: The bank account type. This can only be `checking` or `savings` in most countries. In Japan, this can only be `futsu` or `toza`.
    address_city: City/District/Suburb/Town/Village.
    address_country: Billing address country, if provided when creating card.
    address_line1: Address line 1 (Street address/PO Box/Company name).
    address_line2: Address line 2 (Apartment/Suite/Unit/Building).
    address_state: State/County/Province/Region.
    address_zip: ZIP or postal code.
    default_for_currency: When set to true, this becomes the default external account for its currency.
    documents: Documents that may be submitted to satisfy various informational requests.
    exp_month: Two digit number representing the card’s expiration month.
    exp_year: Four digit number representing the card’s expiration year.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    name: Cardholder name."""
		...


class Accounts_Account_Capabilities(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""List all account capabilities

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Accounts_Account_Capabilities_Capability(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve an Account Capability

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, expand=None, requested=None):
		"""Update an Account Capability

Parameters:
    expand: Specifies which fields in the response should be expanded.
    requested: To request a new capability for an account, pass true. There can be a delay before the requested capability becomes active. If the capability has any activation requirements, the response includes them in the `requirements` arrays.

If a capability isn't permanent, you can remove it from the account by passing false. Some capabilities are permanent after they've been requested. Attempting to remove a permanent capability returns an error."""
		...


class Accounts_Account_External_Accounts(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, object=None, starting_after=None):
		"""List all external accounts

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    object: Filter external accounts according to a particular object type.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, bank_account=None, default_for_currency=None, expand=None, external_account=None, metadata=None):
		"""Create an external account

Parameters:
    bank_account: Either a token, like the ones returned by [Stripe.js](https://stripe.com/docs/js), or a dictionary containing a user's bank account details.
    default_for_currency: When set to true, or if this is the first external account added in this currency, this account becomes the default external account for its currency.
    expand: Specifies which fields in the response should be expanded.
    external_account: A token, like the ones returned by [Stripe.js](https://stripe.com/docs/js) or a dictionary containing a user's external account details (with the options shown below). Please refer to full [documentation](https://stripe.com/docs/api/external_accounts) instead.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."""
		...


class Accounts_Account_External_Accounts_Id(_StripeResourceGroup):
	def delete():
		"""Delete an external account"""
		...
	def fetch(*, expand=None):
		"""Retrieve an external account

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, account_holder_name=None, account_holder_type=None, account_type=None, address_city=None, address_country=None, address_line1=None, address_line2=None, address_state=None, address_zip=None, default_for_currency=None, documents=None, exp_month=None, exp_year=None, expand=None, metadata=None, name=None):
		"""

Parameters:
    account_holder_name: The name of the person or business that owns the bank account.
    account_holder_type: The type of entity that holds the account. This can be either `individual` or `company`.
    account_type: The bank account type. This can only be `checking` or `savings` in most countries. In Japan, this can only be `futsu` or `toza`.
    address_city: City/District/Suburb/Town/Village.
    address_country: Billing address country, if provided when creating card.
    address_line1: Address line 1 (Street address/PO Box/Company name).
    address_line2: Address line 2 (Apartment/Suite/Unit/Building).
    address_state: State/County/Province/Region.
    address_zip: ZIP or postal code.
    default_for_currency: When set to true, this becomes the default external account for its currency.
    documents: Documents that may be submitted to satisfy various informational requests.
    exp_month: Two digit number representing the card’s expiration month.
    exp_year: Four digit number representing the card’s expiration year.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    name: Cardholder name."""
		...


class Accounts_Account_Login_Links(_StripeResourceGroup):
	def create(*, expand=None):
		"""Create a login link

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Accounts_Account_People(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, relationship=None, starting_after=None):
		"""List all persons

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    relationship: Filters on the list of people returned based on the person's relationship to the account's company.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, additional_tos_acceptances=None, address=None, address_kana=None, address_kanji=None, dob=None, documents=None, email=None, expand=None, first_name=None, first_name_kana=None, first_name_kanji=None, full_name_aliases=None, gender=None, id_number=None, id_number_secondary=None, last_name=None, last_name_kana=None, last_name_kanji=None, maiden_name=None, metadata=None, nationality=None, person_token=None, phone=None, political_exposure=None, registered_address=None, relationship=None, ssn_last_4=None, us_cfpb_data=None, verification=None):
		"""Create a person

Parameters:
    additional_tos_acceptances: Details on the legal guardian's or authorizer's acceptance of the required Stripe agreements.
    address: The person's address.
    address_kana: The Kana variation of the person's address (Japan only).
    address_kanji: The Kanji variation of the person's address (Japan only).
    dob: The person's date of birth.
    documents: Documents that may be submitted to satisfy various informational requests.
    email: The person's email address.
    expand: Specifies which fields in the response should be expanded.
    first_name: The person's first name.
    first_name_kana: The Kana variation of the person's first name (Japan only).
    first_name_kanji: The Kanji variation of the person's first name (Japan only).
    full_name_aliases: A list of alternate names or aliases that the person is known by.
    gender: The person's gender (International regulations require either "male" or "female").
    id_number: The person's ID number, as appropriate for their country. For example, a social security number in the U.S., social insurance number in Canada, etc. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii).
    id_number_secondary: The person's secondary ID number, as appropriate for their country, will be used for enhanced verification checks. In Thailand, this would be the laser code found on the back of an ID card. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii).
    last_name: The person's last name.
    last_name_kana: The Kana variation of the person's last name (Japan only).
    last_name_kanji: The Kanji variation of the person's last name (Japan only).
    maiden_name: The person's maiden name.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    nationality: The country where the person is a national. Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)), or "XX" if unavailable.
    person_token: A [person token](https://docs.stripe.com/connect/account-tokens), used to securely provide details to the person.
    phone: The person's phone number.
    political_exposure: Indicates if the person or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction.
    registered_address: The person's registered address.
    relationship: The relationship that this person has with the account's legal entity.
    ssn_last_4: The last four digits of the person's Social Security number (U.S. only).
    us_cfpb_data: Demographic data related to the person.
    verification: The person's verification status."""
		...


class Accounts_Account_People_Person(_StripeResourceGroup):
	def delete():
		"""Delete a person"""
		...
	def fetch(*, expand=None):
		"""Retrieve a person

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, additional_tos_acceptances=None, address=None, address_kana=None, address_kanji=None, dob=None, documents=None, email=None, expand=None, first_name=None, first_name_kana=None, first_name_kanji=None, full_name_aliases=None, gender=None, id_number=None, id_number_secondary=None, last_name=None, last_name_kana=None, last_name_kanji=None, maiden_name=None, metadata=None, nationality=None, person_token=None, phone=None, political_exposure=None, registered_address=None, relationship=None, ssn_last_4=None, us_cfpb_data=None, verification=None):
		"""Update a person

Parameters:
    additional_tos_acceptances: Details on the legal guardian's or authorizer's acceptance of the required Stripe agreements.
    address: The person's address.
    address_kana: The Kana variation of the person's address (Japan only).
    address_kanji: The Kanji variation of the person's address (Japan only).
    dob: The person's date of birth.
    documents: Documents that may be submitted to satisfy various informational requests.
    email: The person's email address.
    expand: Specifies which fields in the response should be expanded.
    first_name: The person's first name.
    first_name_kana: The Kana variation of the person's first name (Japan only).
    first_name_kanji: The Kanji variation of the person's first name (Japan only).
    full_name_aliases: A list of alternate names or aliases that the person is known by.
    gender: The person's gender (International regulations require either "male" or "female").
    id_number: The person's ID number, as appropriate for their country. For example, a social security number in the U.S., social insurance number in Canada, etc. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii).
    id_number_secondary: The person's secondary ID number, as appropriate for their country, will be used for enhanced verification checks. In Thailand, this would be the laser code found on the back of an ID card. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii).
    last_name: The person's last name.
    last_name_kana: The Kana variation of the person's last name (Japan only).
    last_name_kanji: The Kanji variation of the person's last name (Japan only).
    maiden_name: The person's maiden name.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    nationality: The country where the person is a national. Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)), or "XX" if unavailable.
    person_token: A [person token](https://docs.stripe.com/connect/account-tokens), used to securely provide details to the person.
    phone: The person's phone number.
    political_exposure: Indicates if the person or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction.
    registered_address: The person's registered address.
    relationship: The relationship that this person has with the account's legal entity.
    ssn_last_4: The last four digits of the person's Social Security number (U.S. only).
    us_cfpb_data: Demographic data related to the person.
    verification: The person's verification status."""
		...


class Accounts_Account_Persons(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, relationship=None, starting_after=None):
		"""List all persons

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    relationship: Filters on the list of people returned based on the person's relationship to the account's company.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, additional_tos_acceptances=None, address=None, address_kana=None, address_kanji=None, dob=None, documents=None, email=None, expand=None, first_name=None, first_name_kana=None, first_name_kanji=None, full_name_aliases=None, gender=None, id_number=None, id_number_secondary=None, last_name=None, last_name_kana=None, last_name_kanji=None, maiden_name=None, metadata=None, nationality=None, person_token=None, phone=None, political_exposure=None, registered_address=None, relationship=None, ssn_last_4=None, us_cfpb_data=None, verification=None):
		"""Create a person

Parameters:
    additional_tos_acceptances: Details on the legal guardian's or authorizer's acceptance of the required Stripe agreements.
    address: The person's address.
    address_kana: The Kana variation of the person's address (Japan only).
    address_kanji: The Kanji variation of the person's address (Japan only).
    dob: The person's date of birth.
    documents: Documents that may be submitted to satisfy various informational requests.
    email: The person's email address.
    expand: Specifies which fields in the response should be expanded.
    first_name: The person's first name.
    first_name_kana: The Kana variation of the person's first name (Japan only).
    first_name_kanji: The Kanji variation of the person's first name (Japan only).
    full_name_aliases: A list of alternate names or aliases that the person is known by.
    gender: The person's gender (International regulations require either "male" or "female").
    id_number: The person's ID number, as appropriate for their country. For example, a social security number in the U.S., social insurance number in Canada, etc. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii).
    id_number_secondary: The person's secondary ID number, as appropriate for their country, will be used for enhanced verification checks. In Thailand, this would be the laser code found on the back of an ID card. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii).
    last_name: The person's last name.
    last_name_kana: The Kana variation of the person's last name (Japan only).
    last_name_kanji: The Kanji variation of the person's last name (Japan only).
    maiden_name: The person's maiden name.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    nationality: The country where the person is a national. Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)), or "XX" if unavailable.
    person_token: A [person token](https://docs.stripe.com/connect/account-tokens), used to securely provide details to the person.
    phone: The person's phone number.
    political_exposure: Indicates if the person or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction.
    registered_address: The person's registered address.
    relationship: The relationship that this person has with the account's legal entity.
    ssn_last_4: The last four digits of the person's Social Security number (U.S. only).
    us_cfpb_data: Demographic data related to the person.
    verification: The person's verification status."""
		...


class Accounts_Account_Persons_Person(_StripeResourceGroup):
	def delete():
		"""Delete a person"""
		...
	def fetch(*, expand=None):
		"""Retrieve a person

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, additional_tos_acceptances=None, address=None, address_kana=None, address_kanji=None, dob=None, documents=None, email=None, expand=None, first_name=None, first_name_kana=None, first_name_kanji=None, full_name_aliases=None, gender=None, id_number=None, id_number_secondary=None, last_name=None, last_name_kana=None, last_name_kanji=None, maiden_name=None, metadata=None, nationality=None, person_token=None, phone=None, political_exposure=None, registered_address=None, relationship=None, ssn_last_4=None, us_cfpb_data=None, verification=None):
		"""Update a person

Parameters:
    additional_tos_acceptances: Details on the legal guardian's or authorizer's acceptance of the required Stripe agreements.
    address: The person's address.
    address_kana: The Kana variation of the person's address (Japan only).
    address_kanji: The Kanji variation of the person's address (Japan only).
    dob: The person's date of birth.
    documents: Documents that may be submitted to satisfy various informational requests.
    email: The person's email address.
    expand: Specifies which fields in the response should be expanded.
    first_name: The person's first name.
    first_name_kana: The Kana variation of the person's first name (Japan only).
    first_name_kanji: The Kanji variation of the person's first name (Japan only).
    full_name_aliases: A list of alternate names or aliases that the person is known by.
    gender: The person's gender (International regulations require either "male" or "female").
    id_number: The person's ID number, as appropriate for their country. For example, a social security number in the U.S., social insurance number in Canada, etc. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii).
    id_number_secondary: The person's secondary ID number, as appropriate for their country, will be used for enhanced verification checks. In Thailand, this would be the laser code found on the back of an ID card. Instead of the number itself, you can also provide a [PII token provided by Stripe.js](https://docs.stripe.com/js/tokens/create_token?type=pii).
    last_name: The person's last name.
    last_name_kana: The Kana variation of the person's last name (Japan only).
    last_name_kanji: The Kanji variation of the person's last name (Japan only).
    maiden_name: The person's maiden name.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    nationality: The country where the person is a national. Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)), or "XX" if unavailable.
    person_token: A [person token](https://docs.stripe.com/connect/account-tokens), used to securely provide details to the person.
    phone: The person's phone number.
    political_exposure: Indicates if the person or any of their representatives, family members, or other closely related persons, declares that they hold or have held an important public job or function, in any jurisdiction.
    registered_address: The person's registered address.
    relationship: The relationship that this person has with the account's legal entity.
    ssn_last_4: The last four digits of the person's Social Security number (U.S. only).
    us_cfpb_data: Demographic data related to the person.
    verification: The person's verification status."""
		...


class Accounts_Account_Reject(_StripeResourceGroup):
	def create(*, expand=None, reason=None):
		"""Reject an account

Parameters:
    expand: Specifies which fields in the response should be expanded.
    reason: The reason for rejecting the account. Can be `fraud`, `terms_of_service`, or `other`."""
		...


class Apple_Pay_Domains(_StripeResourceGroup):
	def fetch(*, domain_name=None, ending_before=None, expand=None, limit=None, starting_after=None):
		"""

Parameters:
    domain_name: 
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, domain_name=None, expand=None):
		"""

Parameters:
    domain_name: 
    expand: Specifies which fields in the response should be expanded."""
		...


class Apple_Pay_Domains_Domain(_StripeResourceGroup):
	def delete():
		""""""
		...
	def fetch(*, expand=None):
		"""

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Application_Fees(_StripeResourceGroup):
	def fetch(*, charge=None, created=None, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List all application fees

Parameters:
    charge: Only return application fees for the charge specified by this charge ID.
    created: Only return applications fees that were created during the given date interval.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...


class Application_Fees_Fee_Refunds_Id(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve an application fee refund

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, expand=None, metadata=None):
		"""Update an application fee refund

Parameters:
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."""
		...


class Application_Fees_Id(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve an application fee

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Application_Fees_Id_Refund(_StripeResourceGroup):
	def create(*, amount=None, directive=None, expand=None):
		"""

Parameters:
    amount: 
    directive: 
    expand: Specifies which fields in the response should be expanded."""
		...


class Application_Fees_Id_Refunds(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List all application fee refunds

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, amount=None, expand=None, metadata=None):
		"""Create an application fee refund

Parameters:
    amount: A positive integer, in _cents (or local equivalent)_, representing how much of this fee to refund. Can refund only up to the remaining unrefunded amount of the fee.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."""
		...


class Apps_Secrets(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, scope=None, starting_after=None):
		"""List secrets

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    scope: Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, expand=None, expires_at=None, name=None, payload=None, scope=None):
		"""Set a Secret

Parameters:
    expand: Specifies which fields in the response should be expanded.
    expires_at: The Unix timestamp for the expiry time of the secret, after which the secret deletes.
    name: A name for the secret that's unique within the scope.
    payload: The plaintext secret value to be stored.
    scope: Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user."""
		...


class Apps_Secrets_Delete(_StripeResourceGroup):
	def create(*, expand=None, name=None, scope=None):
		"""Delete a Secret

Parameters:
    expand: Specifies which fields in the response should be expanded.
    name: A name for the secret that's unique within the scope.
    scope: Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user."""
		...


class Apps_Secrets_Find(_StripeResourceGroup):
	def fetch(*, expand=None, name=None, scope=None):
		"""Find a Secret

Parameters:
    expand: Specifies which fields in the response should be expanded.
    name: A name for the secret that's unique within the scope.
    scope: Specifies the scoping of the secret. Requests originating from UI extensions can only access account-scoped secrets or secrets scoped to their own user."""
		...


class Balance(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve balance

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Balance_History(_StripeResourceGroup):
	def fetch(*, created=None, currency=None, ending_before=None, expand=None, limit=None, payout=None, source=None, starting_after=None, type=None):
		"""List all balance transactions

Parameters:
    created: Only return transactions that were created during the given date interval.
    currency: Only return transactions in a certain currency. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    payout: For automatic Stripe payouts only, only returns transactions that were paid out on the specified payout ID.
    source: Only returns the original transaction.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    type: Only returns transactions of the given type. One of: `adjustment`, `advance`, `advance_funding`, `anticipation_repayment`, `application_fee`, `application_fee_refund`, `charge`, `climate_order_purchase`, `climate_order_refund`, `connect_collection_transfer`, `contribution`, `issuing_authorization_hold`, `issuing_authorization_release`, `issuing_dispute`, `issuing_transaction`, `obligation_outbound`, `obligation_reversal_inbound`, `payment`, `payment_failure_refund`, `payment_network_reserve_hold`, `payment_network_reserve_release`, `payment_refund`, `payment_reversal`, `payment_unreconciled`, `payout`, `payout_cancel`, `payout_failure`, `payout_minimum_balance_hold`, `payout_minimum_balance_release`, `refund`, `refund_failure`, `reserve_transaction`, `reserved_funds`, `stripe_fee`, `stripe_fx_fee`, `stripe_balance_payment_debit`, `stripe_balance_payment_debit_reversal`, `tax_fee`, `topup`, `topup_reversal`, `transfer`, `transfer_cancel`, `transfer_failure`, or `transfer_refund`."""
		...


class Balance_History_Id(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a balance transaction

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Balance_Transactions(_StripeResourceGroup):
	def fetch(*, created=None, currency=None, ending_before=None, expand=None, limit=None, payout=None, source=None, starting_after=None, type=None):
		"""List all balance transactions

Parameters:
    created: Only return transactions that were created during the given date interval.
    currency: Only return transactions in a certain currency. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    payout: For automatic Stripe payouts only, only returns transactions that were paid out on the specified payout ID.
    source: Only returns the original transaction.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    type: Only returns transactions of the given type. One of: `adjustment`, `advance`, `advance_funding`, `anticipation_repayment`, `application_fee`, `application_fee_refund`, `charge`, `climate_order_purchase`, `climate_order_refund`, `connect_collection_transfer`, `contribution`, `issuing_authorization_hold`, `issuing_authorization_release`, `issuing_dispute`, `issuing_transaction`, `obligation_outbound`, `obligation_reversal_inbound`, `payment`, `payment_failure_refund`, `payment_network_reserve_hold`, `payment_network_reserve_release`, `payment_refund`, `payment_reversal`, `payment_unreconciled`, `payout`, `payout_cancel`, `payout_failure`, `payout_minimum_balance_hold`, `payout_minimum_balance_release`, `refund`, `refund_failure`, `reserve_transaction`, `reserved_funds`, `stripe_fee`, `stripe_fx_fee`, `stripe_balance_payment_debit`, `stripe_balance_payment_debit_reversal`, `tax_fee`, `topup`, `topup_reversal`, `transfer`, `transfer_cancel`, `transfer_failure`, or `transfer_refund`."""
		...


class Balance_Transactions_Id(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a balance transaction

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Billing_Alerts(_StripeResourceGroup):
	def fetch(*, alert_type=None, ending_before=None, expand=None, limit=None, meter=None, starting_after=None):
		"""List billing alerts

Parameters:
    alert_type: Filter results to only include this type of alert.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    meter: Filter results to only include alerts with the given meter.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, alert_type=None, expand=None, title=None, usage_threshold=None):
		"""Create a billing alert

Parameters:
    alert_type: The type of alert to create.
    expand: Specifies which fields in the response should be expanded.
    title: The title of the alert.
    usage_threshold: The configuration of the usage threshold."""
		...


class Billing_Alerts_Id(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a billing alert

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Billing_Alerts_Id_Activate(_StripeResourceGroup):
	def create(*, expand=None):
		"""Activate a billing alert

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Billing_Alerts_Id_Archive(_StripeResourceGroup):
	def create(*, expand=None):
		"""Archive a billing alert

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Billing_Alerts_Id_Deactivate(_StripeResourceGroup):
	def create(*, expand=None):
		"""Deactivate a billing alert

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Billing_Credit_Balance_Summary(_StripeResourceGroup):
	def fetch(*, customer=None, expand=None, filter=None):
		"""Retrieve the credit balance summary for a customer

Parameters:
    customer: The customer for which to fetch credit balance summary.
    expand: Specifies which fields in the response should be expanded.
    filter: The filter criteria for the credit balance summary."""
		...


class Billing_Credit_Balance_Transactions(_StripeResourceGroup):
	def fetch(*, credit_grant=None, customer=None, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List credit balance transactions

Parameters:
    credit_grant: The credit grant for which to fetch credit balance transactions.
    customer: The customer for which to fetch credit balance transactions.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...


class Billing_Credit_Balance_Transactions_Id(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a credit balance transaction

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Billing_Credit_Grants(_StripeResourceGroup):
	def fetch(*, customer=None, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List credit grants

Parameters:
    customer: Only return credit grants for this customer.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, amount=None, applicability_config=None, category=None, customer=None, effective_at=None, expand=None, expires_at=None, metadata=None, name=None, priority=None):
		"""Create a credit grant

Parameters:
    amount: Amount of this credit grant.
    applicability_config: Configuration specifying what this credit grant applies to. We currently only support `metered` prices that have a [Billing Meter](https://docs.stripe.com/api/billing/meter) attached to them.
    category: The category of this credit grant.
    customer: ID of the customer to receive the billing credits.
    effective_at: The time when the billing credits become effective-when they're eligible for use. It defaults to the current timestamp if not specified.
    expand: Specifies which fields in the response should be expanded.
    expires_at: The time when the billing credits expire. If not specified, the billing credits don't expire.
    metadata: Set of key-value pairs that you can attach to an object. You can use this to store additional information about the object (for example, cost basis) in a structured format.
    name: A descriptive name shown in the Dashboard.
    priority: The desired priority for applying this credit grant. If not specified, it will be set to the default value of 50. The highest priority is 0 and the lowest is 100."""
		...


class Billing_Credit_Grants_Id(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a credit grant

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, expand=None, expires_at=None, metadata=None):
		"""Update a credit grant

Parameters:
    expand: Specifies which fields in the response should be expanded.
    expires_at: The time when the billing credits created by this credit grant expire. If set to empty, the billing credits never expire.
    metadata: Set of key-value pairs you can attach to an object. You can use this to store additional information about the object (for example, cost basis) in a structured format."""
		...


class Billing_Credit_Grants_Id_Expire(_StripeResourceGroup):
	def create(*, expand=None):
		"""Expire a credit grant

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Billing_Credit_Grants_Id_Void(_StripeResourceGroup):
	def create(*, expand=None):
		"""Void a credit grant

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Billing_Meter_Event_Adjustments(_StripeResourceGroup):
	def create(*, cancel=None, event_name=None, expand=None, type=None):
		"""Create a billing meter event adjustment

Parameters:
    cancel: Specifies which event to cancel.
    event_name: The name of the meter event. Corresponds with the `event_name` field on a meter.
    expand: Specifies which fields in the response should be expanded.
    type: Specifies whether to cancel a single event or a range of events for a time period. Time period cancellation is not supported yet."""
		...


class Billing_Meter_Events(_StripeResourceGroup):
	def create(*, event_name=None, expand=None, identifier=None, payload=None, timestamp=None):
		"""Create a billing meter event

Parameters:
    event_name: The name of the meter event. Corresponds with the `event_name` field on a meter.
    expand: Specifies which fields in the response should be expanded.
    identifier: A unique identifier for the event. If not provided, one is generated. We recommend using UUID-like identifiers. We will enforce uniqueness within a rolling period of at least 24 hours. The enforcement of uniqueness primarily addresses issues arising from accidental retries or other problems occurring within extremely brief time intervals. This approach helps prevent duplicate entries and ensures data integrity in high-frequency operations.
    payload: The payload of the event. This must contain the fields corresponding to a meter's `customer_mapping.event_payload_key` (default is `stripe_customer_id`) and `value_settings.event_payload_key` (default is `value`). Read more about the [payload](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage#payload-key-overrides).
    timestamp: The time of the event. Measured in seconds since the Unix epoch. Must be within the past 35 calendar days or up to 5 minutes in the future. Defaults to current timestamp if not specified."""
		...


class Billing_Meters(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None, status=None):
		"""List billing meters

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    status: Filter results to only include meters with the given status."""
		...
	def create(*, customer_mapping=None, default_aggregation=None, display_name=None, event_name=None, event_time_window=None, expand=None, value_settings=None):
		"""Create a billing meter

Parameters:
    customer_mapping: Fields that specify how to map a meter event to a customer.
    default_aggregation: The default settings to aggregate a meter's events with.
    display_name: The meter’s name. Not visible to the customer.
    event_name: The name of the meter event to record usage for. Corresponds with the `event_name` field on meter events.
    event_time_window: The time window to pre-aggregate meter events for, if any.
    expand: Specifies which fields in the response should be expanded.
    value_settings: Fields that specify how to calculate a meter event's value."""
		...


class Billing_Meters_Id(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a billing meter

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, display_name=None, expand=None):
		"""Update a billing meter

Parameters:
    display_name: The meter’s name. Not visible to the customer.
    expand: Specifies which fields in the response should be expanded."""
		...


class Billing_Meters_Id_Deactivate(_StripeResourceGroup):
	def create(*, expand=None):
		"""Deactivate a billing meter

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Billing_Meters_Id_Event_Summaries(_StripeResourceGroup):
	def fetch(*, customer=None, end_time=None, ending_before=None, expand=None, limit=None, start_time=None, starting_after=None, value_grouping_window=None):
		"""List billing meter event summaries

Parameters:
    customer: The customer for which to fetch event summaries.
    end_time: The timestamp from when to stop aggregating meter events (exclusive). Must be aligned with minute boundaries.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    start_time: The timestamp from when to start aggregating meter events (inclusive). Must be aligned with minute boundaries.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    value_grouping_window: Specifies what granularity to use when generating event summaries. If not specified, a single event summary would be returned for the specified time range. For hourly granularity, start and end times must align with hour boundaries (e.g., 00:00, 01:00, ..., 23:00). For daily granularity, start and end times must align with UTC day boundaries (00:00 UTC)."""
		...


class Billing_Meters_Id_Reactivate(_StripeResourceGroup):
	def create(*, expand=None):
		"""Reactivate a billing meter

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Billing_Portal_Configurations(_StripeResourceGroup):
	def fetch(*, active=None, ending_before=None, expand=None, is_default=None, limit=None, starting_after=None):
		"""List portal configurations

Parameters:
    active: Only return configurations that are active or inactive (e.g., pass `true` to only list active configurations).
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    is_default: Only return the default or non-default configurations (e.g., pass `true` to only list the default configuration).
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, business_profile=None, default_return_url=None, expand=None, features=None, login_page=None, metadata=None):
		"""Create a portal configuration

Parameters:
    business_profile: The business information shown to customers in the portal.
    default_return_url: The default URL to redirect customers to when they click on the portal's link to return to your website. This can be [overriden](https://stripe.com/docs/api/customer_portal/sessions/create#create_portal_session-return_url) when creating the session.
    expand: Specifies which fields in the response should be expanded.
    features: Information about the features available in the portal.
    login_page: The hosted login page for this configuration. Learn more about the portal login page in our [integration docs](https://stripe.com/docs/billing/subscriptions/integrating-customer-portal#share).
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."""
		...


class Billing_Portal_Configurations_Configuration(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a portal configuration

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, active=None, business_profile=None, default_return_url=None, expand=None, features=None, login_page=None, metadata=None):
		"""Update a portal configuration

Parameters:
    active: Whether the configuration is active and can be used to create portal sessions.
    business_profile: The business information shown to customers in the portal.
    default_return_url: The default URL to redirect customers to when they click on the portal's link to return to your website. This can be [overriden](https://stripe.com/docs/api/customer_portal/sessions/create#create_portal_session-return_url) when creating the session.
    expand: Specifies which fields in the response should be expanded.
    features: Information about the features available in the portal.
    login_page: The hosted login page for this configuration. Learn more about the portal login page in our [integration docs](https://stripe.com/docs/billing/subscriptions/integrating-customer-portal#share).
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."""
		...


class Billing_Portal_Sessions(_StripeResourceGroup):
	def create(*, configuration=None, customer=None, expand=None, flow_data=None, locale=None, on_behalf_of=None, return_url=None):
		"""Create a portal session

Parameters:
    configuration: The ID of an existing [configuration](https://stripe.com/docs/api/customer_portal/configuration) to use for this session, describing its functionality and features. If not specified, the session uses the default configuration.
    customer: The ID of an existing customer.
    expand: Specifies which fields in the response should be expanded.
    flow_data: Information about a specific flow for the customer to go through. See the [docs](https://stripe.com/docs/customer-management/portal-deep-links) to learn more about using customer portal deep links and flows.
    locale: The IETF language tag of the locale customer portal is displayed in. If blank or auto, the customer’s `preferred_locales` or browser’s locale is used.
    on_behalf_of: The `on_behalf_of` account to use for this session. When specified, only subscriptions and invoices with this `on_behalf_of` account appear in the portal. For more information, see the [docs](https://stripe.com/docs/connect/separate-charges-and-transfers#settlement-merchant). Use the [Accounts API](https://stripe.com/docs/api/accounts/object#account_object-settings-branding) to modify the `on_behalf_of` account's branding settings, which the portal displays.
    return_url: The default URL to redirect customers to when they click on the portal's link to return to your website."""
		...


class Charges(_StripeResourceGroup):
	def fetch(*, created=None, customer=None, ending_before=None, expand=None, limit=None, payment_intent=None, starting_after=None, transfer_group=None):
		"""List all charges

Parameters:
    created: Only return charges that were created during the given date interval.
    customer: Only return charges for the customer specified by this customer ID.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    payment_intent: Only return charges that were created by the PaymentIntent specified by this PaymentIntent ID.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    transfer_group: Only return charges for this transfer group, limited to 100."""
		...
	def create(*, amount=None, application_fee=None, application_fee_amount=None, capture=None, card=None, currency=None, customer=None, description=None, destination=None, expand=None, metadata=None, on_behalf_of=None, radar_options=None, receipt_email=None, shipping=None, source=None, statement_descriptor=None, statement_descriptor_suffix=None, transfer_data=None, transfer_group=None):
		"""

Parameters:
    amount: Amount intended to be collected by this payment. A positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).
    application_fee: 
    application_fee_amount: A fee in cents (or local equivalent) that will be applied to the charge and transferred to the application owner's Stripe account. The request must be made with an OAuth key or the `Stripe-Account` header in order to take an application fee. For more information, see the application fees [documentation](https://stripe.com/docs/connect/direct-charges#collect-fees).
    capture: Whether to immediately capture the charge. Defaults to `true`. When `false`, the charge issues an authorization (or pre-authorization), and will need to be [captured](https://stripe.com/docs/api#capture_charge) later. Uncaptured charges expire after a set number of days (7 by default). For more information, see the [authorizing charges and settling later](https://stripe.com/docs/charges/placing-a-hold) documentation.
    card: A token, like the ones returned by [Stripe.js](https://stripe.com/docs/js).
    currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    customer: The ID of an existing customer that will be charged in this request.
    description: An arbitrary string which you can attach to a `Charge` object. It is displayed when in the web interface alongside the charge. Note that if you use Stripe to send automatic email receipts to your customers, your receipt emails will include the `description` of the charge(s) that they are describing.
    destination: 
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    on_behalf_of: The Stripe account ID for which these funds are intended. Automatically set if you use the `destination` parameter. For details, see [Creating Separate Charges and Transfers](https://stripe.com/docs/connect/separate-charges-and-transfers#settlement-merchant).
    radar_options: Options to configure Radar. See [Radar Session](https://stripe.com/docs/radar/radar-session) for more information.
    receipt_email: The email address to which this charge's [receipt](https://stripe.com/docs/dashboard/receipts) will be sent. The receipt will not be sent until the charge is paid, and no receipts will be sent for test mode charges. If this charge is for a [Customer](https://stripe.com/docs/api/customers/object), the email address specified here will override the customer's email address. If `receipt_email` is specified for a charge in live mode, a receipt will be sent regardless of your [email settings](https://dashboard.stripe.com/account/emails).
    shipping: Shipping information for the charge. Helps prevent fraud on charges for physical goods.
    source: A payment source to be charged. This can be the ID of a [card](https://stripe.com/docs/api#cards) (i.e., credit or debit card), a [bank account](https://stripe.com/docs/api#bank_accounts), a [source](https://stripe.com/docs/api#sources), a [token](https://stripe.com/docs/api#tokens), or a [connected account](https://stripe.com/docs/connect/account-debits#charging-a-connected-account). For certain sources---namely, [cards](https://stripe.com/docs/api#cards), [bank accounts](https://stripe.com/docs/api#bank_accounts), and attached [sources](https://stripe.com/docs/api#sources)---you must also pass the ID of the associated customer.
    statement_descriptor: For a non-card charge, text that appears on the customer's statement as the statement descriptor. This value overrides the account's default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).

For a card charge, this value is ignored unless you don't specify a `statement_descriptor_suffix`, in which case this value is used as the suffix.
    statement_descriptor_suffix: Provides information about a card charge. Concatenated to the account's [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors#static) to form the complete statement descriptor that appears on the customer's statement. If the account has no prefix value, the suffix is concatenated to the account's statement descriptor.
    transfer_data: An optional dictionary including the account to automatically transfer to as part of a destination charge. [See the Connect documentation](https://stripe.com/docs/connect/destination-charges) for details.
    transfer_group: A string that identifies this transaction as part of a group. For details, see [Grouping transactions](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options)."""
		...


class Charges_Search(_StripeResourceGroup):
	def fetch(*, expand=None, limit=None, page=None, query=None):
		"""Search charges

Parameters:
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
    query: The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for charges](https://stripe.com/docs/search#query-fields-for-charges)."""
		...


class Charges_Charge(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a charge

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, customer=None, description=None, expand=None, fraud_details=None, metadata=None, receipt_email=None, shipping=None, transfer_group=None):
		"""Update a charge

Parameters:
    customer: The ID of an existing customer that will be associated with this request. This field may only be updated if there is no existing associated customer with this charge.
    description: An arbitrary string which you can attach to a charge object. It is displayed when in the web interface alongside the charge. Note that if you use Stripe to send automatic email receipts to your customers, your receipt emails will include the `description` of the charge(s) that they are describing.
    expand: Specifies which fields in the response should be expanded.
    fraud_details: A set of key-value pairs you can attach to a charge giving information about its riskiness. If you believe a charge is fraudulent, include a `user_report` key with a value of `fraudulent`. If you believe a charge is safe, include a `user_report` key with a value of `safe`. Stripe will use the information you send to improve our fraud detection algorithms.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    receipt_email: This is the email address that the receipt for this charge will be sent to. If this field is updated, then a new email receipt will be sent to the updated address.
    shipping: Shipping information for the charge. Helps prevent fraud on charges for physical goods.
    transfer_group: A string that identifies this transaction as part of a group. `transfer_group` may only be provided if it has not been set. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options) for details."""
		...


class Charges_Charge_Capture(_StripeResourceGroup):
	def create(*, amount=None, application_fee=None, application_fee_amount=None, expand=None, receipt_email=None, statement_descriptor=None, statement_descriptor_suffix=None, transfer_data=None, transfer_group=None):
		"""Capture a payment

Parameters:
    amount: The amount to capture, which must be less than or equal to the original amount.
    application_fee: An application fee to add on to this charge.
    application_fee_amount: An application fee amount to add on to this charge, which must be less than or equal to the original amount.
    expand: Specifies which fields in the response should be expanded.
    receipt_email: The email address to send this charge's receipt to. This will override the previously-specified email address for this charge, if one was set. Receipts will not be sent in test mode.
    statement_descriptor: For a non-card charge, text that appears on the customer's statement as the statement descriptor. This value overrides the account's default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).

For a card charge, this value is ignored unless you don't specify a `statement_descriptor_suffix`, in which case this value is used as the suffix.
    statement_descriptor_suffix: Provides information about a card charge. Concatenated to the account's [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors#static) to form the complete statement descriptor that appears on the customer's statement. If the account has no prefix value, the suffix is concatenated to the account's statement descriptor.
    transfer_data: An optional dictionary including the account to automatically transfer to as part of a destination charge. [See the Connect documentation](https://stripe.com/docs/connect/destination-charges) for details.
    transfer_group: A string that identifies this transaction as part of a group. `transfer_group` may only be provided if it has not been set. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options) for details."""
		...


class Charges_Charge_Dispute(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, evidence=None, expand=None, metadata=None, submit=None):
		"""

Parameters:
    evidence: Evidence to upload, to respond to a dispute. Updating any field in the hash will submit all fields in the hash for review. The combined character count of all fields is limited to 150,000.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    submit: Whether to immediately submit evidence to the bank. If `false`, evidence is staged on the dispute. Staged evidence is visible in the API and Dashboard, and can be submitted to the bank by making another request with this attribute set to `true` (the default)."""
		...


class Charges_Charge_Dispute_Close(_StripeResourceGroup):
	def create(*, expand=None):
		"""

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Charges_Charge_Refund(_StripeResourceGroup):
	def create(*, amount=None, expand=None, instructions_email=None, metadata=None, payment_intent=None, reason=None, refund_application_fee=None, reverse_transfer=None):
		"""Create a refund

Parameters:
    amount: A positive integer in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) representing how much of this charge to refund. Can refund only up to the remaining, unrefunded amount of the charge.
    expand: Specifies which fields in the response should be expanded.
    instructions_email: For payment methods without native refund support (e.g., Konbini, PromptPay), use this email from the customer to receive refund instructions.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    payment_intent: The identifier of the PaymentIntent to refund.
    reason: String indicating the reason for the refund. If set, possible values are `duplicate`, `fraudulent`, and `requested_by_customer`. If you believe the charge to be fraudulent, specifying `fraudulent` as the reason will add the associated card and email to your [block lists](https://stripe.com/docs/radar/lists), and will also help us improve our fraud detection algorithms.
    refund_application_fee: Boolean indicating whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded. An application fee can be refunded only by the application that created the charge.
    reverse_transfer: Boolean indicating whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount).<br><br>A transfer can be reversed only by the application that created the charge."""
		...


class Charges_Charge_Refunds(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List all refunds

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, amount=None, currency=None, customer=None, expand=None, instructions_email=None, metadata=None, origin=None, payment_intent=None, reason=None, refund_application_fee=None, reverse_transfer=None):
		"""Create customer balance refund

Parameters:
    amount: 
    currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    customer: Customer whose customer balance to refund from.
    expand: Specifies which fields in the response should be expanded.
    instructions_email: For payment methods without native refund support (e.g., Konbini, PromptPay), use this email from the customer to receive refund instructions.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    origin: Origin of the refund
    payment_intent: The identifier of the PaymentIntent to refund.
    reason: String indicating the reason for the refund. If set, possible values are `duplicate`, `fraudulent`, and `requested_by_customer`. If you believe the charge to be fraudulent, specifying `fraudulent` as the reason will add the associated card and email to your [block lists](https://stripe.com/docs/radar/lists), and will also help us improve our fraud detection algorithms.
    refund_application_fee: Boolean indicating whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded. An application fee can be refunded only by the application that created the charge.
    reverse_transfer: Boolean indicating whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount).<br><br>A transfer can be reversed only by the application that created the charge."""
		...


class Charges_Charge_Refunds_Refund(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, expand=None, metadata=None):
		"""

Parameters:
    expand: Specifies which fields in the response should be expanded.
    metadata: """
		...


class Checkout_Sessions(_StripeResourceGroup):
	def fetch(*, created=None, customer=None, customer_details=None, ending_before=None, expand=None, limit=None, payment_intent=None, payment_link=None, starting_after=None, status=None, subscription=None):
		"""List all Checkout Sessions

Parameters:
    created: Only return Checkout Sessions that were created during the given date interval.
    customer: Only return the Checkout Sessions for the Customer specified.
    customer_details: Only return the Checkout Sessions for the Customer details specified.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    payment_intent: Only return the Checkout Session for the PaymentIntent specified.
    payment_link: Only return the Checkout Sessions for the Payment Link specified.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    status: Only return the Checkout Sessions matching the given status.
    subscription: Only return the Checkout Session for the subscription specified."""
		...
	def create(*, adaptive_pricing=None, after_expiration=None, allow_promotion_codes=None, automatic_tax=None, billing_address_collection=None, cancel_url=None, client_reference_id=None, consent_collection=None, currency=None, custom_fields=None, custom_text=None, customer=None, customer_creation=None, customer_email=None, customer_update=None, discounts=None, expand=None, expires_at=None, invoice_creation=None, line_items=None, locale=None, metadata=None, mode=None, optional_items=None, payment_intent_data=None, payment_method_collection=None, payment_method_configuration=None, payment_method_data=None, payment_method_options=None, payment_method_types=None, permissions=None, phone_number_collection=None, redirect_on_completion=None, return_url=None, saved_payment_method_options=None, setup_intent_data=None, shipping_address_collection=None, shipping_options=None, submit_type=None, subscription_data=None, success_url=None, tax_id_collection=None, ui_mode=None, wallet_options=None):
		"""Create a Checkout Session

Parameters:
    adaptive_pricing: Settings for price localization with [Adaptive Pricing](https://docs.stripe.com/payments/checkout/adaptive-pricing).
    after_expiration: Configure actions after a Checkout Session has expired.
    allow_promotion_codes: Enables user redeemable promotion codes.
    automatic_tax: Settings for automatic tax lookup for this session and resulting payments, invoices, and subscriptions.
    billing_address_collection: Specify whether Checkout should collect the customer's billing address. Defaults to `auto`.
    cancel_url: If set, Checkout displays a back button and customers will be directed to this URL if they decide to cancel payment and return to your website. This parameter is not allowed if ui_mode is `embedded` or `custom`.
    client_reference_id: A unique string to reference the Checkout Session. This can be a
customer ID, a cart ID, or similar, and can be used to reconcile the
session with your internal systems.
    consent_collection: Configure fields for the Checkout Session to gather active consent from customers.
    currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). Required in `setup` mode when `payment_method_types` is not set.
    custom_fields: Collect additional information from your customer using custom fields. Up to 3 fields are supported.
    custom_text: Display additional text for your customers using custom text.
    customer: ID of an existing Customer, if one exists. In `payment` mode, the customer’s most recently saved card
payment method will be used to prefill the email, name, card details, and billing address
on the Checkout page. In `subscription` mode, the customer’s [default payment method](https://stripe.com/docs/api/customers/update#update_customer-invoice_settings-default_payment_method)
will be used if it’s a card, otherwise the most recently saved card will be used. A valid billing address, billing name and billing email are required on the payment method for Checkout to prefill the customer's card details.

If the Customer already has a valid [email](https://stripe.com/docs/api/customers/object#customer_object-email) set, the email will be prefilled and not editable in Checkout.
If the Customer does not have a valid `email`, Checkout will set the email entered during the session on the Customer.

If blank for Checkout Sessions in `subscription` mode or with `customer_creation` set as `always` in `payment` mode, Checkout will create a new Customer object based on information provided during the payment flow.

You can set [`payment_intent_data.setup_future_usage`](https://stripe.com/docs/api/checkout/sessions/create#create_checkout_session-payment_intent_data-setup_future_usage) to have Checkout automatically attach the payment method to the Customer you pass in for future reuse.
    customer_creation: Configure whether a Checkout Session creates a [Customer](https://stripe.com/docs/api/customers) during Session confirmation.

When a Customer is not created, you can still retrieve email, address, and other customer data entered in Checkout
with [customer_details](https://stripe.com/docs/api/checkout/sessions/object#checkout_session_object-customer_details).

Sessions that don't create Customers instead are grouped by [guest customers](https://stripe.com/docs/payments/checkout/guest-customers)
in the Dashboard. Promotion codes limited to first time customers will return invalid for these Sessions.

Can only be set in `payment` and `setup` mode.
    customer_email: If provided, this value will be used when the Customer object is created.
If not provided, customers will be asked to enter their email address.
Use this parameter to prefill customer data if you already have an email
on file. To access information about the customer once a session is
complete, use the `customer` field.
    customer_update: Controls what fields on Customer can be updated by the Checkout Session. Can only be provided when `customer` is provided.
    discounts: The coupon or promotion code to apply to this Session. Currently, only up to one may be specified.
    expand: Specifies which fields in the response should be expanded.
    expires_at: The Epoch time in seconds at which the Checkout Session will expire. It can be anywhere from 30 minutes to 24 hours after Checkout Session creation. By default, this value is 24 hours from creation.
    invoice_creation: Generate a post-purchase Invoice for one-time payments.
    line_items: A list of items the customer is purchasing. Use this parameter to pass one-time or recurring [Prices](https://stripe.com/docs/api/prices).

For `payment` mode, there is a maximum of 100 line items, however it is recommended to consolidate line items if there are more than a few dozen.

For `subscription` mode, there is a maximum of 20 line items with recurring Prices and 20 line items with one-time Prices. Line items with one-time Prices will be on the initial invoice only.
    locale: The IETF language tag of the locale Checkout is displayed in. If blank or `auto`, the browser's locale is used.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    mode: The mode of the Checkout Session. Pass `subscription` if the Checkout Session includes at least one recurring item.
    optional_items: A list of optional items the customer can add to their order at checkout. Use this parameter to pass one-time or recurring [Prices](https://stripe.com/docs/api/prices).

There is a maximum of 10 optional items allowed on a Checkout Session, and the existing limits on the number of line items allowed on a Checkout Session apply to the combined number of line items and optional items.

For `payment` mode, there is a maximum of 100 combined line items and optional items, however it is recommended to consolidate items if there are more than a few dozen.

For `subscription` mode, there is a maximum of 20 line items and optional items with recurring Prices and 20 line items and optional items with one-time Prices.
    payment_intent_data: A subset of parameters to be passed to PaymentIntent creation for Checkout Sessions in `payment` mode.
    payment_method_collection: Specify whether Checkout should collect a payment method. When set to `if_required`, Checkout will not collect a payment method when the total due for the session is 0.
This may occur if the Checkout Session includes a free trial or a discount.

Can only be set in `subscription` mode. Defaults to `always`.

If you'd like information on how to collect a payment method outside of Checkout, read the guide on configuring [subscriptions with a free trial](https://stripe.com/docs/payments/checkout/free-trials).
    payment_method_configuration: The ID of the payment method configuration to use with this Checkout session.
    payment_method_data: This parameter allows you to set some attributes on the payment method created during a Checkout session.
    payment_method_options: Payment-method-specific configuration.
    payment_method_types: A list of the types of payment methods (e.g., `card`) this Checkout Session can accept.

You can omit this attribute to manage your payment methods from the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods).
See [Dynamic Payment Methods](https://stripe.com/docs/payments/payment-methods/integration-options#using-dynamic-payment-methods) for more details.

Read more about the supported payment methods and their requirements in our [payment
method details guide](/docs/payments/checkout/payment-methods).

If multiple payment methods are passed, Checkout will dynamically reorder them to
prioritize the most relevant payment methods based on the customer's location and
other characteristics.
    permissions: This property is used to set up permissions for various actions (e.g., update) on the CheckoutSession object. Can only be set when creating `embedded` or `custom` sessions.

For specific permissions, please refer to their dedicated subsections, such as `permissions.update_shipping_details`.
    phone_number_collection: Controls phone number collection settings for the session.

We recommend that you review your privacy policy and check with your legal contacts
before using this feature. Learn more about [collecting phone numbers with Checkout](https://stripe.com/docs/payments/checkout/phone-numbers).
    redirect_on_completion: This parameter applies to `ui_mode: embedded`. Learn more about the [redirect behavior](https://stripe.com/docs/payments/checkout/custom-success-page?payment-ui=embedded-form) of embedded sessions. Defaults to `always`.
    return_url: The URL to redirect your customer back to after they authenticate or cancel their payment on the
payment method's app or site. This parameter is required if `ui_mode` is `embedded` or `custom`
and redirect-based payment methods are enabled on the session.
    saved_payment_method_options: Controls saved payment method settings for the session. Only available in `payment` and `subscription` mode.
    setup_intent_data: A subset of parameters to be passed to SetupIntent creation for Checkout Sessions in `setup` mode.
    shipping_address_collection: When set, provides configuration for Checkout to collect a shipping address from a customer.
    shipping_options: The shipping rate options to apply to this Session. Up to a maximum of 5.
    submit_type: Describes the type of transaction being performed by Checkout in order
to customize relevant text on the page, such as the submit button.
 `submit_type` can only be specified on Checkout Sessions in
`payment` or `subscription` mode. If blank or `auto`, `pay` is used.
    subscription_data: A subset of parameters to be passed to subscription creation for Checkout Sessions in `subscription` mode.
    success_url: The URL to which Stripe should send customers when payment or setup
is complete.
This parameter is not allowed if ui_mode is `embedded` or `custom`. If you'd like to use
information from the successful Checkout Session on your page, read the
guide on [customizing your success page](https://stripe.com/docs/payments/checkout/custom-success-page).
    tax_id_collection: Controls tax ID collection during checkout.
    ui_mode: The UI mode of the Session. Defaults to `hosted`.
    wallet_options: Wallet-specific configuration."""
		...


class Checkout_Sessions_Session(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a Checkout Session

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, collected_information=None, expand=None, metadata=None, shipping_options=None):
		"""Update a Checkout Session

Parameters:
    collected_information: Information about the customer collected within the Checkout Session. Can only be set when updating `embedded` or `custom` sessions.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    shipping_options: The shipping rate options to apply to this Session. Up to a maximum of 5."""
		...


class Checkout_Sessions_Session_Expire(_StripeResourceGroup):
	def create(*, expand=None):
		"""Expire a Checkout Session

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Checkout_Sessions_Session_Line_Items(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None):
		"""Retrieve a Checkout Session's line items

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...


class Climate_Orders(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List orders

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, amount=None, beneficiary=None, currency=None, expand=None, metadata=None, metric_tons=None, product=None):
		"""Create an order

Parameters:
    amount: Requested amount of carbon removal units. Either this or `metric_tons` must be specified.
    beneficiary: Publicly sharable reference for the end beneficiary of carbon removal. Assumed to be the Stripe account if not set.
    currency: Request currency for the order as a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a supported [settlement currency for your account](https://stripe.com/docs/currencies). If omitted, the account's default currency will be used.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    metric_tons: Requested number of tons for the order. Either this or `amount` must be specified.
    product: Unique identifier of the Climate product."""
		...


class Climate_Orders_Order(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve an order

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, beneficiary=None, expand=None, metadata=None):
		"""Update an order

Parameters:
    beneficiary: Publicly sharable reference for the end beneficiary of carbon removal. Assumed to be the Stripe account if not set.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."""
		...


class Climate_Orders_Order_Cancel(_StripeResourceGroup):
	def create(*, expand=None):
		"""Cancel an order

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Climate_Products(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List products

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...


class Climate_Products_Product(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a product

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Climate_Suppliers(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List suppliers

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...


class Climate_Suppliers_Supplier(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a supplier

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Confirmation_Tokens_Confirmation_Token(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a ConfirmationToken

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Country_Specs(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List Country Specs

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...


class Country_Specs_Country(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a Country Spec

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Coupons(_StripeResourceGroup):
	def fetch(*, created=None, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List all coupons

Parameters:
    created: A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, amount_off=None, applies_to=None, currency=None, currency_options=None, duration=None, duration_in_months=None, expand=None, id=None, max_redemptions=None, metadata=None, name=None, percent_off=None, redeem_by=None):
		"""Create a coupon

Parameters:
    amount_off: A positive integer representing the amount to subtract from an invoice total (required if `percent_off` is not passed).
    applies_to: A hash containing directions for what this Coupon will apply discounts to.
    currency: Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) of the `amount_off` parameter (required if `amount_off` is passed).
    currency_options: Coupons defined in each available currency option (only supported if `amount_off` is passed). Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
    duration: Specifies how long the discount will be in effect if used on a subscription. Defaults to `once`.
    duration_in_months: Required only if `duration` is `repeating`, in which case it must be a positive integer that specifies the number of months the discount will be in effect.
    expand: Specifies which fields in the response should be expanded.
    id: Unique string of your choice that will be used to identify this coupon when applying it to a customer. If you don't want to specify a particular code, you can leave the ID blank and we'll generate a random code for you.
    max_redemptions: A positive integer specifying the number of times the coupon can be redeemed before it's no longer valid. For example, you might have a 50% off coupon that the first 20 readers of your blog can use.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    name: Name of the coupon displayed to customers on, for instance invoices, or receipts. By default the `id` is shown if `name` is not set.
    percent_off: A positive float larger than 0, and smaller or equal to 100, that represents the discount the coupon will apply (required if `amount_off` is not passed).
    redeem_by: Unix timestamp specifying the last time at which the coupon can be redeemed. After the redeem_by date, the coupon can no longer be applied to new customers."""
		...


class Coupons_Coupon(_StripeResourceGroup):
	def delete():
		"""Delete a coupon"""
		...
	def fetch(*, expand=None):
		"""Retrieve a coupon

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, currency_options=None, expand=None, metadata=None, name=None):
		"""Update a coupon

Parameters:
    currency_options: Coupons defined in each available currency option (only supported if the coupon is amount-based). Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    name: Name of the coupon displayed to customers on, for instance invoices, or receipts. By default the `id` is shown if `name` is not set."""
		...


class Credit_Notes(_StripeResourceGroup):
	def fetch(*, created=None, customer=None, ending_before=None, expand=None, invoice=None, limit=None, starting_after=None):
		"""List all credit notes

Parameters:
    created: Only return credit notes that were created during the given date interval.
    customer: Only return credit notes for the customer specified by this customer ID.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    invoice: Only return credit notes for the invoice specified by this invoice ID.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, amount=None, credit_amount=None, effective_at=None, email_type=None, expand=None, invoice=None, lines=None, memo=None, metadata=None, out_of_band_amount=None, reason=None, refund_amount=None, refunds=None, shipping_cost=None):
		"""Create a credit note

Parameters:
    amount: The integer amount in cents (or local equivalent) representing the total amount of the credit note.
    credit_amount: The integer amount in cents (or local equivalent) representing the amount to credit the customer's balance, which will be automatically applied to their next invoice.
    effective_at: The date when this credit note is in effect. Same as `created` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the credit note PDF.
    email_type: Type of email to send to the customer, one of `credit_note` or `none` and the default is `credit_note`.
    expand: Specifies which fields in the response should be expanded.
    invoice: ID of the invoice.
    lines: Line items that make up the credit note.
    memo: The credit note's memo appears on the credit note PDF.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    out_of_band_amount: The integer amount in cents (or local equivalent) representing the amount that is credited outside of Stripe.
    reason: Reason for issuing this credit note, one of `duplicate`, `fraudulent`, `order_change`, or `product_unsatisfactory`
    refund_amount: The integer amount in cents (or local equivalent) representing the amount to refund. If set, a refund will be created for the charge associated with the invoice.
    refunds: Refunds to link to this credit note.
    shipping_cost: When shipping_cost contains the shipping_rate from the invoice, the shipping_cost is included in the credit note."""
		...


class Credit_Notes_Preview(_StripeResourceGroup):
	def fetch(*, amount=None, credit_amount=None, effective_at=None, email_type=None, expand=None, invoice=None, lines=None, memo=None, metadata=None, out_of_band_amount=None, reason=None, refund_amount=None, refunds=None, shipping_cost=None):
		"""Preview a credit note

Parameters:
    amount: The integer amount in cents (or local equivalent) representing the total amount of the credit note.
    credit_amount: The integer amount in cents (or local equivalent) representing the amount to credit the customer's balance, which will be automatically applied to their next invoice.
    effective_at: The date when this credit note is in effect. Same as `created` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the credit note PDF.
    email_type: Type of email to send to the customer, one of `credit_note` or `none` and the default is `credit_note`.
    expand: Specifies which fields in the response should be expanded.
    invoice: ID of the invoice.
    lines: Line items that make up the credit note.
    memo: The credit note's memo appears on the credit note PDF.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    out_of_band_amount: The integer amount in cents (or local equivalent) representing the amount that is credited outside of Stripe.
    reason: Reason for issuing this credit note, one of `duplicate`, `fraudulent`, `order_change`, or `product_unsatisfactory`
    refund_amount: The integer amount in cents (or local equivalent) representing the amount to refund. If set, a refund will be created for the charge associated with the invoice.
    refunds: Refunds to link to this credit note.
    shipping_cost: When shipping_cost contains the shipping_rate from the invoice, the shipping_cost is included in the credit note."""
		...


class Credit_Notes_Preview_Lines(_StripeResourceGroup):
	def fetch(*, amount=None, credit_amount=None, effective_at=None, email_type=None, ending_before=None, expand=None, invoice=None, limit=None, lines=None, memo=None, metadata=None, out_of_band_amount=None, reason=None, refund_amount=None, refunds=None, shipping_cost=None, starting_after=None):
		"""Retrieve a credit note preview's line items

Parameters:
    amount: The integer amount in cents (or local equivalent) representing the total amount of the credit note.
    credit_amount: The integer amount in cents (or local equivalent) representing the amount to credit the customer's balance, which will be automatically applied to their next invoice.
    effective_at: The date when this credit note is in effect. Same as `created` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the credit note PDF.
    email_type: Type of email to send to the customer, one of `credit_note` or `none` and the default is `credit_note`.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    invoice: ID of the invoice.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    lines: Line items that make up the credit note.
    memo: The credit note's memo appears on the credit note PDF.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    out_of_band_amount: The integer amount in cents (or local equivalent) representing the amount that is credited outside of Stripe.
    reason: Reason for issuing this credit note, one of `duplicate`, `fraudulent`, `order_change`, or `product_unsatisfactory`
    refund_amount: The integer amount in cents (or local equivalent) representing the amount to refund. If set, a refund will be created for the charge associated with the invoice.
    refunds: Refunds to link to this credit note.
    shipping_cost: When shipping_cost contains the shipping_rate from the invoice, the shipping_cost is included in the credit note.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...


class Credit_Notes_Credit_Note_Lines(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None):
		"""Retrieve a credit note's line items

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...


class Credit_Notes_Id(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a credit note

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, expand=None, memo=None, metadata=None):
		"""Update a credit note

Parameters:
    expand: Specifies which fields in the response should be expanded.
    memo: Credit note memo.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."""
		...


class Credit_Notes_Id_Void(_StripeResourceGroup):
	def create(*, expand=None):
		"""Void a credit note

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Customer_Sessions(_StripeResourceGroup):
	def create(*, components=None, customer=None, expand=None):
		"""Create a Customer Session

Parameters:
    components: Configuration for each component. Exactly 1 component must be enabled.
    customer: The ID of an existing customer for which to create the Customer Session.
    expand: Specifies which fields in the response should be expanded."""
		...


class Customers(_StripeResourceGroup):
	def fetch(*, created=None, email=None, ending_before=None, expand=None, limit=None, starting_after=None, test_clock=None):
		"""List all customers

Parameters:
    created: Only return customers that were created during the given date interval.
    email: A case-sensitive filter on the list based on the customer's `email` field. The value must be a string.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    test_clock: Provides a list of customers that are associated with the specified test clock. The response will not include customers with test clocks if this parameter is not set."""
		...
	def create(*, address=None, balance=None, cash_balance=None, description=None, email=None, expand=None, invoice_prefix=None, invoice_settings=None, metadata=None, name=None, next_invoice_sequence=None, payment_method=None, phone=None, preferred_locales=None, shipping=None, source=None, tax=None, tax_exempt=None, tax_id_data=None, test_clock=None):
		"""Create a customer

Parameters:
    address: The customer's address.
    balance: An integer amount in cents (or local equivalent) that represents the customer's current balance, which affect the customer's future invoices. A negative amount represents a credit that decreases the amount due on an invoice; a positive amount increases the amount due on an invoice.
    cash_balance: Balance information and default balance settings for this customer.
    description: An arbitrary string that you can attach to a customer object. It is displayed alongside the customer in the dashboard.
    email: Customer's email address. It's displayed alongside the customer in your dashboard and can be useful for searching and tracking. This may be up to *512 characters*.
    expand: Specifies which fields in the response should be expanded.
    invoice_prefix: The prefix for the customer used to generate unique invoice numbers. Must be 3–12 uppercase letters or numbers.
    invoice_settings: Default invoice settings for this customer.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    name: The customer's full name or business name.
    next_invoice_sequence: The sequence to be used on the customer's next invoice. Defaults to 1.
    payment_method: 
    phone: The customer's phone number.
    preferred_locales: Customer's preferred languages, ordered by preference.
    shipping: The customer's shipping information. Appears on invoices emailed to this customer.
    source: 
    tax: Tax details about the customer.
    tax_exempt: The customer's tax exemption. One of `none`, `exempt`, or `reverse`.
    tax_id_data: The customer's tax IDs.
    test_clock: ID of the test clock to attach to the customer."""
		...


class Customers_Search(_StripeResourceGroup):
	def fetch(*, expand=None, limit=None, page=None, query=None):
		"""Search customers

Parameters:
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
    query: The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for customers](https://stripe.com/docs/search#query-fields-for-customers)."""
		...


class Customers_Customer(_StripeResourceGroup):
	def delete():
		"""Delete a customer"""
		...
	def fetch(*, expand=None):
		"""Retrieve a customer

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, address=None, balance=None, bank_account=None, card=None, cash_balance=None, default_alipay_account=None, default_bank_account=None, default_card=None, default_source=None, description=None, email=None, expand=None, invoice_prefix=None, invoice_settings=None, metadata=None, name=None, next_invoice_sequence=None, phone=None, preferred_locales=None, shipping=None, source=None, tax=None, tax_exempt=None):
		"""Update a customer

Parameters:
    address: The customer's address.
    balance: An integer amount in cents (or local equivalent) that represents the customer's current balance, which affect the customer's future invoices. A negative amount represents a credit that decreases the amount due on an invoice; a positive amount increases the amount due on an invoice.
    bank_account: Either a token, like the ones returned by [Stripe.js](https://stripe.com/docs/js), or a dictionary containing a user's bank account details.
    card: A token, like the ones returned by [Stripe.js](https://stripe.com/docs/js).
    cash_balance: Balance information and default balance settings for this customer.
    default_alipay_account: ID of Alipay account to make the customer's new default for invoice payments.
    default_bank_account: ID of bank account to make the customer's new default for invoice payments.
    default_card: ID of card to make the customer's new default for invoice payments.
    default_source: If you are using payment methods created via the PaymentMethods API, see the [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/update#update_customer-invoice_settings-default_payment_method) parameter.

Provide the ID of a payment source already attached to this customer to make it this customer's default payment source.

If you want to add a new payment source and make it the default, see the [source](https://stripe.com/docs/api/customers/update#update_customer-source) property.
    description: An arbitrary string that you can attach to a customer object. It is displayed alongside the customer in the dashboard.
    email: Customer's email address. It's displayed alongside the customer in your dashboard and can be useful for searching and tracking. This may be up to *512 characters*.
    expand: Specifies which fields in the response should be expanded.
    invoice_prefix: The prefix for the customer used to generate unique invoice numbers. Must be 3–12 uppercase letters or numbers.
    invoice_settings: Default invoice settings for this customer.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    name: The customer's full name or business name.
    next_invoice_sequence: The sequence to be used on the customer's next invoice. Defaults to 1.
    phone: The customer's phone number.
    preferred_locales: Customer's preferred languages, ordered by preference.
    shipping: The customer's shipping information. Appears on invoices emailed to this customer.
    source: 
    tax: Tax details about the customer.
    tax_exempt: The customer's tax exemption. One of `none`, `exempt`, or `reverse`."""
		...


class Customers_Customer_Balance_Transactions(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List customer balance transactions

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, amount=None, currency=None, description=None, expand=None, metadata=None):
		"""Create a customer balance transaction

Parameters:
    amount: The integer amount in **cents (or local equivalent)** to apply to the customer's credit balance.
    currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies). Specifies the [`invoice_credit_balance`](https://stripe.com/docs/api/customers/object#customer_object-invoice_credit_balance) that this transaction will apply to. If the customer's `currency` is not set, it will be updated to this value.
    description: An arbitrary string attached to the object. Often useful for displaying to users.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."""
		...


class Customers_Customer_Balance_Transactions_Transaction(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a customer balance transaction

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, description=None, expand=None, metadata=None):
		"""Update a customer credit balance transaction

Parameters:
    description: An arbitrary string attached to the object. Often useful for displaying to users.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."""
		...


class Customers_Customer_Bank_Accounts(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List all bank accounts

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, alipay_account=None, bank_account=None, card=None, expand=None, metadata=None, source=None):
		"""Create a card

Parameters:
    alipay_account: A token returned by [Stripe.js](https://stripe.com/docs/js) representing the user’s Alipay account details.
    bank_account: Either a token, like the ones returned by [Stripe.js](https://stripe.com/docs/js), or a dictionary containing a user's bank account details.
    card: A token, like the ones returned by [Stripe.js](https://stripe.com/docs/js).
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    source: Please refer to full [documentation](https://stripe.com/docs/api) instead."""
		...


class Customers_Customer_Bank_Accounts_Id(_StripeResourceGroup):
	def delete(*, expand=None):
		"""Delete a customer source

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def fetch(*, expand=None):
		"""Retrieve a bank account

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, account_holder_name=None, account_holder_type=None, address_city=None, address_country=None, address_line1=None, address_line2=None, address_state=None, address_zip=None, exp_month=None, exp_year=None, expand=None, metadata=None, name=None, owner=None):
		"""

Parameters:
    account_holder_name: The name of the person or business that owns the bank account.
    account_holder_type: The type of entity that holds the account. This can be either `individual` or `company`.
    address_city: City/District/Suburb/Town/Village.
    address_country: Billing address country, if provided when creating card.
    address_line1: Address line 1 (Street address/PO Box/Company name).
    address_line2: Address line 2 (Apartment/Suite/Unit/Building).
    address_state: State/County/Province/Region.
    address_zip: ZIP or postal code.
    exp_month: Two digit number representing the card’s expiration month.
    exp_year: Four digit number representing the card’s expiration year.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    name: Cardholder name.
    owner: """
		...


class Customers_Customer_Bank_Accounts_Id_Verify(_StripeResourceGroup):
	def create(*, amounts=None, expand=None):
		"""Verify a bank account

Parameters:
    amounts: Two positive integers, in *cents*, equal to the values of the microdeposits sent to the bank account.
    expand: Specifies which fields in the response should be expanded."""
		...


class Customers_Customer_Cards(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List all cards

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, alipay_account=None, bank_account=None, card=None, expand=None, metadata=None, source=None):
		"""Create a card

Parameters:
    alipay_account: A token returned by [Stripe.js](https://stripe.com/docs/js) representing the user’s Alipay account details.
    bank_account: Either a token, like the ones returned by [Stripe.js](https://stripe.com/docs/js), or a dictionary containing a user's bank account details.
    card: A token, like the ones returned by [Stripe.js](https://stripe.com/docs/js).
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    source: Please refer to full [documentation](https://stripe.com/docs/api) instead."""
		...


class Customers_Customer_Cards_Id(_StripeResourceGroup):
	def delete(*, expand=None):
		"""Delete a customer source

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def fetch(*, expand=None):
		"""Retrieve a card

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, account_holder_name=None, account_holder_type=None, address_city=None, address_country=None, address_line1=None, address_line2=None, address_state=None, address_zip=None, exp_month=None, exp_year=None, expand=None, metadata=None, name=None, owner=None):
		"""

Parameters:
    account_holder_name: The name of the person or business that owns the bank account.
    account_holder_type: The type of entity that holds the account. This can be either `individual` or `company`.
    address_city: City/District/Suburb/Town/Village.
    address_country: Billing address country, if provided when creating card.
    address_line1: Address line 1 (Street address/PO Box/Company name).
    address_line2: Address line 2 (Apartment/Suite/Unit/Building).
    address_state: State/County/Province/Region.
    address_zip: ZIP or postal code.
    exp_month: Two digit number representing the card’s expiration month.
    exp_year: Four digit number representing the card’s expiration year.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    name: Cardholder name.
    owner: """
		...


class Customers_Customer_Cash_Balance(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a cash balance

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, expand=None, settings=None):
		"""Update a cash balance's settings

Parameters:
    expand: Specifies which fields in the response should be expanded.
    settings: A hash of settings for this cash balance."""
		...


class Customers_Customer_Cash_Balance_Transactions(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List cash balance transactions

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...


class Customers_Customer_Cash_Balance_Transactions_Transaction(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a cash balance transaction

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Customers_Customer_Discount(_StripeResourceGroup):
	def delete():
		"""Delete a customer discount"""
		...
	def fetch(*, expand=None):
		"""

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Customers_Customer_Funding_Instructions(_StripeResourceGroup):
	def create(*, bank_transfer=None, currency=None, expand=None, funding_type=None):
		"""Create or retrieve funding instructions for a customer cash balance

Parameters:
    bank_transfer: Additional parameters for `bank_transfer` funding types
    currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    expand: Specifies which fields in the response should be expanded.
    funding_type: The `funding_type` to get the instructions for."""
		...


class Customers_Customer_Payment_Methods(_StripeResourceGroup):
	def fetch(*, allow_redisplay=None, ending_before=None, expand=None, limit=None, starting_after=None, type=None):
		"""List a Customer's PaymentMethods

Parameters:
    allow_redisplay: This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    type: An optional filter on the list, based on the object `type` field. Without the filter, the list includes all current and future payment method types. If your integration expects only one type of payment method in the response, make sure to provide a type value in the request."""
		...


class Customers_Customer_Payment_Methods_Payment_Method(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a Customer's PaymentMethod

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Customers_Customer_Sources(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, object=None, starting_after=None):
		"""

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    object: Filter sources according to a particular object type.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, alipay_account=None, bank_account=None, card=None, expand=None, metadata=None, source=None):
		"""Create a card

Parameters:
    alipay_account: A token returned by [Stripe.js](https://stripe.com/docs/js) representing the user’s Alipay account details.
    bank_account: Either a token, like the ones returned by [Stripe.js](https://stripe.com/docs/js), or a dictionary containing a user's bank account details.
    card: A token, like the ones returned by [Stripe.js](https://stripe.com/docs/js).
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    source: Please refer to full [documentation](https://stripe.com/docs/api) instead."""
		...


class Customers_Customer_Sources_Id(_StripeResourceGroup):
	def delete(*, expand=None):
		"""Delete a customer source

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def fetch(*, expand=None):
		"""

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, account_holder_name=None, account_holder_type=None, address_city=None, address_country=None, address_line1=None, address_line2=None, address_state=None, address_zip=None, exp_month=None, exp_year=None, expand=None, metadata=None, name=None, owner=None):
		"""

Parameters:
    account_holder_name: The name of the person or business that owns the bank account.
    account_holder_type: The type of entity that holds the account. This can be either `individual` or `company`.
    address_city: City/District/Suburb/Town/Village.
    address_country: Billing address country, if provided when creating card.
    address_line1: Address line 1 (Street address/PO Box/Company name).
    address_line2: Address line 2 (Apartment/Suite/Unit/Building).
    address_state: State/County/Province/Region.
    address_zip: ZIP or postal code.
    exp_month: Two digit number representing the card’s expiration month.
    exp_year: Four digit number representing the card’s expiration year.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    name: Cardholder name.
    owner: """
		...


class Customers_Customer_Sources_Id_Verify(_StripeResourceGroup):
	def create(*, amounts=None, expand=None):
		"""Verify a bank account

Parameters:
    amounts: Two positive integers, in *cents*, equal to the values of the microdeposits sent to the bank account.
    expand: Specifies which fields in the response should be expanded."""
		...


class Customers_Customer_Subscriptions(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List active subscriptions

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, add_invoice_items=None, application_fee_percent=None, automatic_tax=None, backdate_start_date=None, billing_cycle_anchor=None, billing_thresholds=None, cancel_at=None, cancel_at_period_end=None, collection_method=None, currency=None, days_until_due=None, default_payment_method=None, default_source=None, default_tax_rates=None, discounts=None, expand=None, invoice_settings=None, items=None, metadata=None, off_session=None, payment_behavior=None, payment_settings=None, pending_invoice_item_interval=None, proration_behavior=None, transfer_data=None, trial_end=None, trial_from_plan=None, trial_period_days=None, trial_settings=None):
		"""Create a subscription

Parameters:
    add_invoice_items: A list of prices and quantities that will generate invoice items appended to the next invoice for this subscription. You may pass up to 20 items.
    application_fee_percent: A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions).
    automatic_tax: Automatic tax settings for this subscription. We recommend you only include this parameter when the existing value is being changed.
    backdate_start_date: For new subscriptions, a past timestamp to backdate the subscription's start date to. If set, the first invoice will contain a proration for the timespan between the start date and the current time. Can be combined with trials and the billing cycle anchor.
    billing_cycle_anchor: A future timestamp in UTC format to anchor the subscription's [billing cycle](https://stripe.com/docs/subscriptions/billing-cycle). The anchor is the reference point that aligns future billing cycle dates. It sets the day of week for `week` intervals, the day of month for `month` and `year` intervals, and the month of year for `year` intervals.
    billing_thresholds: Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. When updating, pass an empty string to remove previously-defined thresholds.
    cancel_at: A timestamp at which the subscription should cancel. If set to a date before the current period ends, this will cause a proration if prorations have been enabled using `proration_behavior`. If set during a future period, this will always cause a proration for that period.
    cancel_at_period_end: Indicate whether this subscription should cancel at the end of the current period (`current_period_end`). Defaults to `false`. This param will be removed in a future API version. Please use `cancel_at` instead.
    collection_method: Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`.
    currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    days_until_due: Number of days a customer has to pay invoices generated by this subscription. Valid only for subscriptions where `collection_method` is set to `send_invoice`.
    default_payment_method: ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over `default_source`. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source).
    default_source: ID of the default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If `default_payment_method` is also set, `default_payment_method` will take precedence. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source).
    default_tax_rates: The tax rates that will apply to any subscription item that does not have `tax_rates` set. Invoices created will have their `default_tax_rates` populated from the subscription.
    discounts: The coupons to redeem into discounts for the subscription. If not specified or empty, inherits the discount from the subscription's customer.
    expand: Specifies which fields in the response should be expanded.
    invoice_settings: All invoices will be billed using the specified settings.
    items: A list of up to 20 subscription items, each with an attached price.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    off_session: Indicates if a customer is on or off-session while an invoice payment is attempted. Defaults to `false` (on-session).
    payment_behavior: Only applies to subscriptions with `collection_method=charge_automatically`.

Use `allow_incomplete` to create Subscriptions with `status=incomplete` if the first invoice can't be paid. Creating Subscriptions with this status allows you to manage scenarios where additional customer actions are needed to pay a subscription's invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication) for Billing to learn more. This is the default behavior.

Use `default_incomplete` to create Subscriptions with `status=incomplete` when the first invoice requires payment, otherwise start as active. Subscriptions transition to `status=active` when successfully confirming the PaymentIntent on the first invoice. This allows simpler management of scenarios where additional customer actions are needed to pay a subscription’s invoice, such as failed payments, [SCA regulation](https://stripe.com/docs/billing/migration/strong-customer-authentication), or collecting a mandate for a bank debit payment method. If the PaymentIntent is not confirmed within 23 hours Subscriptions transition to `status=incomplete_expired`, which is a terminal state.

Use `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription's first invoice can't be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further customer action is needed, this parameter doesn't create a Subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://stripe.com/docs/upgrades#2019-03-14) to learn more.

`pending_if_incomplete` is only used with updates and cannot be passed when creating a Subscription.

Subscriptions with `collection_method=send_invoice` are automatically activated regardless of the first Invoice status.
    payment_settings: Payment settings to pass to invoices created by the subscription.
    pending_invoice_item_interval: Specifies an interval for how often to bill for any pending invoice items. It is analogous to calling [Create an invoice](https://stripe.com/docs/api#create_invoice) for the given subscription at the specified interval.
    proration_behavior: Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) resulting from the `billing_cycle_anchor`. If no value is passed, the default is `create_prorations`.
    transfer_data: If specified, the funds from the subscription's invoices will be transferred to the destination and the ID of the resulting transfers will be found on the resulting charges.
    trial_end: Unix timestamp representing the end of the trial period the customer will get before being charged for the first time. If set, trial_end will override the default trial period of the plan the customer is being subscribed to. The special value `now` can be provided to end the customer's trial immediately. Can be at most two years from `billing_cycle_anchor`. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more.
    trial_from_plan: Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more.
    trial_period_days: Integer representing the number of trial period days before the customer is charged for the first time. This will always overwrite any trials that might apply via a subscribed plan. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more.
    trial_settings: Settings related to subscription trials."""
		...


class Customers_Customer_Subscriptions_Subscription_Exposed_Id(_StripeResourceGroup):
	def delete(*, expand=None, invoice_now=None, prorate=None):
		"""Cancel a subscription

Parameters:
    expand: Specifies which fields in the response should be expanded.
    invoice_now: Can be set to `true` if `at_period_end` is not set to `true`. Will generate a final invoice that invoices for any un-invoiced metered usage and new/pending proration invoice items.
    prorate: Can be set to `true` if `at_period_end` is not set to `true`. Will generate a proration invoice item that credits remaining unused time until the subscription period end."""
		...
	def fetch(*, expand=None):
		"""Retrieve a subscription

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, add_invoice_items=None, application_fee_percent=None, automatic_tax=None, billing_cycle_anchor=None, billing_thresholds=None, cancel_at=None, cancel_at_period_end=None, cancellation_details=None, collection_method=None, days_until_due=None, default_payment_method=None, default_source=None, default_tax_rates=None, discounts=None, expand=None, invoice_settings=None, items=None, metadata=None, off_session=None, pause_collection=None, payment_behavior=None, payment_settings=None, pending_invoice_item_interval=None, proration_behavior=None, proration_date=None, transfer_data=None, trial_end=None, trial_from_plan=None, trial_settings=None):
		"""Update a subscription on a customer

Parameters:
    add_invoice_items: A list of prices and quantities that will generate invoice items appended to the next invoice for this subscription. You may pass up to 20 items.
    application_fee_percent: A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions).
    automatic_tax: Automatic tax settings for this subscription. We recommend you only include this parameter when the existing value is being changed.
    billing_cycle_anchor: Either `now` or `unchanged`. Setting the value to `now` resets the subscription's billing cycle anchor to the current time. For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle).
    billing_thresholds: Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. When updating, pass an empty string to remove previously-defined thresholds.
    cancel_at: A timestamp at which the subscription should cancel. If set to a date before the current period ends, this will cause a proration if prorations have been enabled using `proration_behavior`. If set during a future period, this will always cause a proration for that period.
    cancel_at_period_end: Indicate whether this subscription should cancel at the end of the current period (`current_period_end`). Defaults to `false`. This param will be removed in a future API version. Please use `cancel_at` instead.
    cancellation_details: Details about why this subscription was cancelled
    collection_method: Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`.
    days_until_due: Number of days a customer has to pay invoices generated by this subscription. Valid only for subscriptions where `collection_method` is set to `send_invoice`.
    default_payment_method: ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over `default_source`. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source).
    default_source: ID of the default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If `default_payment_method` is also set, `default_payment_method` will take precedence. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source).
    default_tax_rates: The tax rates that will apply to any subscription item that does not have `tax_rates` set. Invoices created will have their `default_tax_rates` populated from the subscription. Pass an empty string to remove previously-defined tax rates.
    discounts: The coupons to redeem into discounts for the subscription. If not specified or empty, inherits the discount from the subscription's customer.
    expand: Specifies which fields in the response should be expanded.
    invoice_settings: All invoices will be billed using the specified settings.
    items: A list of up to 20 subscription items, each with an attached price.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    off_session: Indicates if a customer is on or off-session while an invoice payment is attempted. Defaults to `false` (on-session).
    pause_collection: If specified, payment collection for this subscription will be paused. Note that the subscription status will be unchanged and will not be updated to `paused`. Learn more about [pausing collection](https://stripe.com/docs/billing/subscriptions/pause-payment).
    payment_behavior: Use `allow_incomplete` to transition the subscription to `status=past_due` if a payment is required but cannot be paid. This allows you to manage scenarios where additional user actions are needed to pay a subscription's invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication) for Billing to learn more. This is the default behavior.

Use `default_incomplete` to transition the subscription to `status=past_due` when payment is required and await explicit confirmation of the invoice's payment intent. This allows simpler management of scenarios where additional user actions are needed to pay a subscription’s invoice. Such as failed payments, [SCA regulation](https://stripe.com/docs/billing/migration/strong-customer-authentication), or collecting a mandate for a bank debit payment method.

Use `pending_if_incomplete` to update the subscription using [pending updates](https://stripe.com/docs/billing/subscriptions/pending-updates). When you use `pending_if_incomplete` you can only pass the parameters [supported by pending updates](https://stripe.com/docs/billing/pending-updates-reference#supported-attributes).

Use `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription's invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not update the subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://stripe.com/docs/upgrades#2019-03-14) to learn more.
    payment_settings: Payment settings to pass to invoices created by the subscription.
    pending_invoice_item_interval: Specifies an interval for how often to bill for any pending invoice items. It is analogous to calling [Create an invoice](https://stripe.com/docs/api#create_invoice) for the given subscription at the specified interval.
    proration_behavior: Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`.
    proration_date: If set, prorations will be calculated as though the subscription was updated at the given time. This can be used to apply exactly the same prorations that were previewed with the [create preview](https://stripe.com/docs/api/invoices/create_preview) endpoint. `proration_date` can also be used to implement custom proration logic, such as prorating by day instead of by second, by providing the time that you wish to use for proration calculations.
    transfer_data: If specified, the funds from the subscription's invoices will be transferred to the destination and the ID of the resulting transfers will be found on the resulting charges. This will be unset if you POST an empty value.
    trial_end: Unix timestamp representing the end of the trial period the customer will get before being charged for the first time. This will always overwrite any trials that might apply via a subscribed plan. If set, trial_end will override the default trial period of the plan the customer is being subscribed to. The special value `now` can be provided to end the customer's trial immediately. Can be at most two years from `billing_cycle_anchor`.
    trial_from_plan: Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more.
    trial_settings: Settings related to subscription trials."""
		...


class Customers_Customer_Subscriptions_Subscription_Exposed_Id_Discount(_StripeResourceGroup):
	def delete():
		"""Delete a customer discount"""
		...
	def fetch(*, expand=None):
		"""

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Customers_Customer_Tax_Ids(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List all Customer tax IDs

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, expand=None, type=None, value=None):
		"""Create a Customer tax ID

Parameters:
    expand: Specifies which fields in the response should be expanded.
    type: Type of the tax ID, one of `ad_nrt`, `ae_trn`, `al_tin`, `am_tin`, `ao_tin`, `ar_cuit`, `au_abn`, `au_arn`, `aw_tin`, `az_tin`, `ba_tin`, `bb_tin`, `bd_bin`, `bf_ifu`, `bg_uic`, `bh_vat`, `bj_ifu`, `bo_tin`, `br_cnpj`, `br_cpf`, `bs_tin`, `by_tin`, `ca_bn`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `ca_qst`, `cd_nif`, `ch_uid`, `ch_vat`, `cl_tin`, `cm_niu`, `cn_tin`, `co_nit`, `cr_tin`, `cv_nif`, `de_stn`, `do_rcn`, `ec_ruc`, `eg_tin`, `es_cif`, `et_tin`, `eu_oss_vat`, `eu_vat`, `gb_vat`, `ge_vat`, `gn_nif`, `hk_br`, `hr_oib`, `hu_tin`, `id_npwp`, `il_vat`, `in_gst`, `is_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `ke_pin`, `kg_tin`, `kh_tin`, `kr_brn`, `kz_bin`, `la_tin`, `li_uid`, `li_vat`, `ma_vat`, `md_vat`, `me_pib`, `mk_vat`, `mr_nif`, `mx_rfc`, `my_frp`, `my_itn`, `my_sst`, `ng_tin`, `no_vat`, `no_voec`, `np_pan`, `nz_gst`, `om_vat`, `pe_ruc`, `ph_tin`, `ro_tin`, `rs_pib`, `ru_inn`, `ru_kpp`, `sa_vat`, `sg_gst`, `sg_uen`, `si_tin`, `sn_ninea`, `sr_fin`, `sv_nit`, `th_vat`, `tj_tin`, `tr_tin`, `tw_vat`, `tz_vat`, `ua_vat`, `ug_tin`, `us_ein`, `uy_ruc`, `uz_tin`, `uz_vat`, `ve_rif`, `vn_tin`, `za_vat`, `zm_tin`, or `zw_tin`
    value: Value of the tax ID."""
		...


class Customers_Customer_Tax_Ids_Id(_StripeResourceGroup):
	def delete():
		"""Delete a Customer tax ID"""
		...
	def fetch(*, expand=None):
		"""Retrieve a Customer tax ID

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Disputes(_StripeResourceGroup):
	def fetch(*, charge=None, created=None, ending_before=None, expand=None, limit=None, payment_intent=None, starting_after=None):
		"""List all disputes

Parameters:
    charge: Only return disputes associated to the charge specified by this charge ID.
    created: Only return disputes that were created during the given date interval.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    payment_intent: Only return disputes associated to the PaymentIntent specified by this PaymentIntent ID.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...


class Disputes_Dispute(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a dispute

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, evidence=None, expand=None, metadata=None, submit=None):
		"""Update a dispute

Parameters:
    evidence: Evidence to upload, to respond to a dispute. Updating any field in the hash will submit all fields in the hash for review. The combined character count of all fields is limited to 150,000.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    submit: Whether to immediately submit evidence to the bank. If `false`, evidence is staged on the dispute. Staged evidence is visible in the API and Dashboard, and can be submitted to the bank by making another request with this attribute set to `true` (the default)."""
		...


class Disputes_Dispute_Close(_StripeResourceGroup):
	def create(*, expand=None):
		"""Close a dispute

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Entitlements_Active_Entitlements(_StripeResourceGroup):
	def fetch(*, customer=None, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List all active entitlements

Parameters:
    customer: The ID of the customer.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...


class Entitlements_Active_Entitlements_Id(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve an active entitlement

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Entitlements_Features(_StripeResourceGroup):
	def fetch(*, archived=None, ending_before=None, expand=None, limit=None, lookup_key=None, starting_after=None):
		"""List all features

Parameters:
    archived: If set, filter results to only include features with the given archive status.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    lookup_key: If set, filter results to only include features with the given lookup_key.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, expand=None, lookup_key=None, metadata=None, name=None):
		"""Create a feature

Parameters:
    expand: Specifies which fields in the response should be expanded.
    lookup_key: A unique key you provide as your own system identifier. This may be up to 80 characters.
    metadata: Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    name: The feature's name, for your own purpose, not meant to be displayable to the customer."""
		...


class Entitlements_Features_Id(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a feature

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, active=None, expand=None, metadata=None, name=None):
		"""Updates a feature

Parameters:
    active: Inactive features cannot be attached to new products and will not be returned from the features list endpoint.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    name: The feature's name, for your own purpose, not meant to be displayable to the customer."""
		...


class Ephemeral_Keys(_StripeResourceGroup):
	def create(*, customer=None, expand=None, issuing_card=None, nonce=None, verification_session=None):
		"""Create an ephemeral key

Parameters:
    customer: The ID of the Customer you'd like to modify using the resulting ephemeral key.
    expand: Specifies which fields in the response should be expanded.
    issuing_card: The ID of the Issuing Card you'd like to access using the resulting ephemeral key.
    nonce: A single-use token, created by Stripe.js, used for creating ephemeral keys for Issuing Cards without exchanging sensitive information.
    verification_session: The ID of the Identity VerificationSession you'd like to access using the resulting ephemeral key"""
		...


class Ephemeral_Keys_Key(_StripeResourceGroup):
	def delete(*, expand=None):
		"""Immediately invalidate an ephemeral key

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Events(_StripeResourceGroup):
	def fetch(*, created=None, delivery_success=None, ending_before=None, expand=None, limit=None, starting_after=None, type=None, types=None):
		"""List all events

Parameters:
    created: Only return events that were created during the given date interval.
    delivery_success: Filter events by whether all webhooks were successfully delivered. If false, events which are still pending or have failed all delivery attempts to a webhook endpoint will be returned.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    type: A string containing a specific event name, or group of events using * as a wildcard. The list will be filtered to include only events with a matching event property.
    types: An array of up to 20 strings containing specific event names. The list will be filtered to include only events with a matching event property. You may pass either `type` or `types`, but not both."""
		...


class Events_Id(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve an event

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Exchange_Rates(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List all exchange rates

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is the currency that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with the exchange rate for currency X your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and total number of supported payout currencies, and the default is the max.
    starting_after: A cursor for use in pagination. `starting_after` is the currency that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with the exchange rate for currency X, your subsequent call can include `starting_after=X` in order to fetch the next page of the list."""
		...


class Exchange_Rates_Rate_Id(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve an exchange rate

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class External_Accounts_Id(_StripeResourceGroup):
	def create(*, account_holder_name=None, account_holder_type=None, account_type=None, address_city=None, address_country=None, address_line1=None, address_line2=None, address_state=None, address_zip=None, default_for_currency=None, documents=None, exp_month=None, exp_year=None, expand=None, metadata=None, name=None):
		"""

Parameters:
    account_holder_name: The name of the person or business that owns the bank account.
    account_holder_type: The type of entity that holds the account. This can be either `individual` or `company`.
    account_type: The bank account type. This can only be `checking` or `savings` in most countries. In Japan, this can only be `futsu` or `toza`.
    address_city: City/District/Suburb/Town/Village.
    address_country: Billing address country, if provided when creating card.
    address_line1: Address line 1 (Street address/PO Box/Company name).
    address_line2: Address line 2 (Apartment/Suite/Unit/Building).
    address_state: State/County/Province/Region.
    address_zip: ZIP or postal code.
    default_for_currency: When set to true, this becomes the default external account for its currency.
    documents: Documents that may be submitted to satisfy various informational requests.
    exp_month: Two digit number representing the card’s expiration month.
    exp_year: Four digit number representing the card’s expiration year.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    name: Cardholder name."""
		...


class File_Links(_StripeResourceGroup):
	def fetch(*, created=None, ending_before=None, expand=None, expired=None, file=None, limit=None, starting_after=None):
		"""List all file links

Parameters:
    created: Only return links that were created during the given date interval.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    expired: Filter links by their expiration status. By default, Stripe returns all links.
    file: Only return links for the given file.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, expand=None, expires_at=None, file=None, metadata=None):
		"""Create a file link

Parameters:
    expand: Specifies which fields in the response should be expanded.
    expires_at: The link isn't usable after this future timestamp.
    file: The ID of the file. The file's `purpose` must be one of the following: `business_icon`, `business_logo`, `customer_signature`, `dispute_evidence`, `finance_report_run`, `financial_account_statement`, `identity_document_downloadable`, `issuing_regulatory_reporting`, `pci_document`, `selfie`, `sigma_scheduled_query`, `tax_document_user_upload`, or `terminal_reader_splashscreen`.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."""
		...


class File_Links_Link(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a file link

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, expand=None, expires_at=None, metadata=None):
		"""Update a file link

Parameters:
    expand: Specifies which fields in the response should be expanded.
    expires_at: A future timestamp after which the link will no longer be usable, or `now` to expire the link immediately.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."""
		...


class Files(_StripeResourceGroup):
	def fetch(*, created=None, ending_before=None, expand=None, limit=None, purpose=None, starting_after=None):
		"""List all files

Parameters:
    created: Only return files that were created during the given date interval.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    purpose: Filter queries by the file purpose. If you don't provide a purpose, the queries return unfiltered files.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create():
		"""Create a file"""
		...


class Files_File(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a file

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Financial_Connections_Accounts(_StripeResourceGroup):
	def fetch(*, account_holder=None, ending_before=None, expand=None, limit=None, session=None, starting_after=None):
		"""List Accounts

Parameters:
    account_holder: If present, only return accounts that belong to the specified account holder. `account_holder[customer]` and `account_holder[account]` are mutually exclusive.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    session: If present, only return accounts that were collected as part of the given session.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...


class Financial_Connections_Accounts_Account(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve an Account

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Financial_Connections_Accounts_Account_Disconnect(_StripeResourceGroup):
	def create(*, expand=None):
		"""Disconnect an Account

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Financial_Connections_Accounts_Account_Owners(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, ownership=None, starting_after=None):
		"""List Account Owners

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    ownership: The ID of the ownership object to fetch owners from.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...


class Financial_Connections_Accounts_Account_Refresh(_StripeResourceGroup):
	def create(*, expand=None, features=None):
		"""Refresh Account data

Parameters:
    expand: Specifies which fields in the response should be expanded.
    features: The list of account features that you would like to refresh."""
		...


class Financial_Connections_Accounts_Account_Subscribe(_StripeResourceGroup):
	def create(*, expand=None, features=None):
		"""Subscribe to data refreshes for an Account

Parameters:
    expand: Specifies which fields in the response should be expanded.
    features: The list of account features to which you would like to subscribe."""
		...


class Financial_Connections_Accounts_Account_Unsubscribe(_StripeResourceGroup):
	def create(*, expand=None, features=None):
		"""Unsubscribe from data refreshes for an Account

Parameters:
    expand: Specifies which fields in the response should be expanded.
    features: The list of account features from which you would like to unsubscribe."""
		...


class Financial_Connections_Sessions(_StripeResourceGroup):
	def create(*, account_holder=None, expand=None, filters=None, permissions=None, prefetch=None, return_url=None):
		"""Create a Session

Parameters:
    account_holder: The account holder to link accounts for.
    expand: Specifies which fields in the response should be expanded.
    filters: Filters to restrict the kinds of accounts to collect.
    permissions: List of data features that you would like to request access to.

Possible values are `balances`, `transactions`, `ownership`, and `payment_method`.
    prefetch: List of data features that you would like to retrieve upon account creation.
    return_url: For webview integrations only. Upon completing OAuth login in the native browser, the user will be redirected to this URL to return to your app."""
		...


class Financial_Connections_Sessions_Session(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a Session

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Financial_Connections_Transactions(_StripeResourceGroup):
	def fetch(*, account=None, ending_before=None, expand=None, limit=None, starting_after=None, transacted_at=None, transaction_refresh=None):
		"""List Transactions

Parameters:
    account: The ID of the Financial Connections Account whose transactions will be retrieved.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    transacted_at: A filter on the list based on the object `transacted_at` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with the following options:
    transaction_refresh: A filter on the list based on the object `transaction_refresh` field. The value can be a dictionary with the following options:"""
		...


class Financial_Connections_Transactions_Transaction(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a Transaction

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Forwarding_Requests(_StripeResourceGroup):
	def fetch(*, created=None, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List all ForwardingRequests

Parameters:
    created: Similar to other List endpoints, filters results based on created timestamp. You can pass gt, gte, lt, and lte timestamp values.
    ending_before: A pagination cursor to fetch the previous page of the list. The value must be a ForwardingRequest ID.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A pagination cursor to fetch the next page of the list. The value must be a ForwardingRequest ID."""
		...
	def create(*, expand=None, metadata=None, payment_method=None, replacements=None, request=None, url=None):
		"""Create a ForwardingRequest

Parameters:
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    payment_method: The PaymentMethod to insert into the forwarded request. Forwarding previously consumed PaymentMethods is allowed.
    replacements: The field kinds to be replaced in the forwarded request.
    request: The request body and headers to be sent to the destination endpoint.
    url: The destination URL for the forwarded request. Must be supported by the config."""
		...


class Forwarding_Requests_Id(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a ForwardingRequest

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Identity_Verification_Reports(_StripeResourceGroup):
	def fetch(*, client_reference_id=None, created=None, ending_before=None, expand=None, limit=None, starting_after=None, type=None, verification_session=None):
		"""List VerificationReports

Parameters:
    client_reference_id: A string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.
    created: Only return VerificationReports that were created during the given date interval.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    type: Only return VerificationReports of this type
    verification_session: Only return VerificationReports created by this VerificationSession ID. It is allowed to provide a VerificationIntent ID."""
		...


class Identity_Verification_Reports_Report(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a VerificationReport

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Identity_Verification_Sessions(_StripeResourceGroup):
	def fetch(*, client_reference_id=None, created=None, ending_before=None, expand=None, limit=None, related_customer=None, starting_after=None, status=None):
		"""List VerificationSessions

Parameters:
    client_reference_id: A string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.
    created: Only return VerificationSessions that were created during the given date interval.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    related_customer: 
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    status: Only return VerificationSessions with this status. [Learn more about the lifecycle of sessions](https://stripe.com/docs/identity/how-sessions-work)."""
		...
	def create(*, client_reference_id=None, expand=None, metadata=None, options=None, provided_details=None, related_customer=None, return_url=None, type=None, verification_flow=None):
		"""Create a VerificationSession

Parameters:
    client_reference_id: A string to reference this user. This can be a customer ID, a session ID, or similar, and can be used to reconcile this verification with your internal systems.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    options: A set of options for the session’s verification checks.
    provided_details: Details provided about the user being verified. These details may be shown to the user.
    related_customer: Customer ID
    return_url: The URL that the user will be redirected to upon completing the verification flow.
    type: The type of [verification check](https://stripe.com/docs/identity/verification-checks) to be performed. You must provide a `type` if not passing `verification_flow`.
    verification_flow: The ID of a verification flow from the Dashboard. See https://docs.stripe.com/identity/verification-flows."""
		...


class Identity_Verification_Sessions_Session(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a VerificationSession

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, expand=None, metadata=None, options=None, provided_details=None, type=None):
		"""Update a VerificationSession

Parameters:
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    options: A set of options for the session’s verification checks.
    provided_details: Details provided about the user being verified. These details may be shown to the user.
    type: The type of [verification check](https://stripe.com/docs/identity/verification-checks) to be performed."""
		...


class Identity_Verification_Sessions_Session_Cancel(_StripeResourceGroup):
	def create(*, expand=None):
		"""Cancel a VerificationSession

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Identity_Verification_Sessions_Session_Redact(_StripeResourceGroup):
	def create(*, expand=None):
		"""Redact a VerificationSession

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Invoice_Payments(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, invoice=None, limit=None, payment=None, starting_after=None, status=None):
		"""List all payments for an invoice

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    invoice: The identifier of the invoice whose payments to return.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    payment: The payment details of the invoice payments to return.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    status: The status of the invoice payments to return."""
		...


class Invoice_Payments_Invoice_Payment(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve an InvoicePayment

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Invoice_Rendering_Templates(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None, status=None):
		"""List all invoice rendering templates

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    status: """
		...


class Invoice_Rendering_Templates_Template(_StripeResourceGroup):
	def fetch(*, expand=None, version=None):
		"""Retrieve an invoice rendering template

Parameters:
    expand: Specifies which fields in the response should be expanded.
    version: """
		...


class Invoice_Rendering_Templates_Template_Archive(_StripeResourceGroup):
	def create(*, expand=None):
		"""Archive an invoice rendering template

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Invoice_Rendering_Templates_Template_Unarchive(_StripeResourceGroup):
	def create(*, expand=None):
		"""Unarchive an invoice rendering template

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Invoiceitems(_StripeResourceGroup):
	def fetch(*, created=None, customer=None, ending_before=None, expand=None, invoice=None, limit=None, pending=None, starting_after=None):
		"""List all invoice items

Parameters:
    created: Only return invoice items that were created during the given date interval.
    customer: The identifier of the customer whose invoice items to return. If none is provided, all invoice items will be returned.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    invoice: Only return invoice items belonging to this invoice. If none is provided, all invoice items will be returned. If specifying an invoice, no customer identifier is needed.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    pending: Set to `true` to only show pending invoice items, which are not yet attached to any invoices. Set to `false` to only show invoice items already attached to invoices. If unspecified, no filter is applied.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, amount=None, currency=None, customer=None, description=None, discountable=None, discounts=None, expand=None, invoice=None, metadata=None, period=None, price_data=None, pricing=None, quantity=None, subscription=None, tax_behavior=None, tax_code=None, tax_rates=None, unit_amount_decimal=None):
		"""Create an invoice item

Parameters:
    amount: The integer amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. Passing in a negative `amount` will reduce the `amount_due` on the invoice.
    currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    customer: The ID of the customer who will be billed when this invoice item is billed.
    description: An arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking.
    discountable: Controls whether discounts apply to this invoice item. Defaults to false for prorations or negative invoice items, and true for all other invoice items.
    discounts: The coupons and promotion codes to redeem into discounts for the invoice item or invoice line item.
    expand: Specifies which fields in the response should be expanded.
    invoice: The ID of an existing invoice to add this invoice item to. When left blank, the invoice item will be added to the next upcoming scheduled invoice. This is useful when adding invoice items in response to an invoice.created webhook. You can only add invoice items to draft invoices and there is a maximum of 250 items per invoice.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    period: The period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have [Stripe Revenue Recognition](https://stripe.com/docs/revenue-recognition) enabled, the period will be used to recognize and defer revenue. See the [Revenue Recognition documentation](https://stripe.com/docs/revenue-recognition/methodology/subscriptions-and-invoicing) for details.
    price_data: Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
    pricing: The pricing information for the invoice item.
    quantity: Non-negative integer. The quantity of units for the invoice item.
    subscription: The ID of a subscription to add this invoice item to. When left blank, the invoice item is added to the next upcoming scheduled invoice. When set, scheduled invoices for subscriptions other than the specified subscription will ignore the invoice item. Use this when you want to express that an invoice item has been accrued within the context of a particular subscription.
    tax_behavior: Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
    tax_code: A [tax code](https://stripe.com/docs/tax/tax-categories) ID.
    tax_rates: The tax rates which apply to the invoice item. When set, the `default_tax_rates` on the invoice do not apply to this invoice item.
    unit_amount_decimal: The decimal unit amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. This `unit_amount_decimal` will be multiplied by the quantity to get the full amount. Passing in a negative `unit_amount_decimal` will reduce the `amount_due` on the invoice. Accepts at most 12 decimal places."""
		...


class Invoiceitems_Invoiceitem(_StripeResourceGroup):
	def delete():
		"""Delete an invoice item"""
		...
	def fetch(*, expand=None):
		"""Retrieve an invoice item

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, amount=None, description=None, discountable=None, discounts=None, expand=None, metadata=None, period=None, price_data=None, pricing=None, quantity=None, tax_behavior=None, tax_code=None, tax_rates=None, unit_amount_decimal=None):
		"""Update an invoice item

Parameters:
    amount: The integer amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. If you want to apply a credit to the customer's account, pass a negative amount.
    description: An arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking.
    discountable: Controls whether discounts apply to this invoice item. Defaults to false for prorations or negative invoice items, and true for all other invoice items. Cannot be set to true for prorations.
    discounts: The coupons, promotion codes & existing discounts which apply to the invoice item or invoice line item. Item discounts are applied before invoice discounts. Pass an empty string to remove previously-defined discounts.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    period: The period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have [Stripe Revenue Recognition](https://stripe.com/docs/revenue-recognition) enabled, the period will be used to recognize and defer revenue. See the [Revenue Recognition documentation](https://stripe.com/docs/revenue-recognition/methodology/subscriptions-and-invoicing) for details.
    price_data: Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
    pricing: The pricing information for the invoice item.
    quantity: Non-negative integer. The quantity of units for the invoice item.
    tax_behavior: Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
    tax_code: A [tax code](https://stripe.com/docs/tax/tax-categories) ID.
    tax_rates: The tax rates which apply to the invoice item. When set, the `default_tax_rates` on the invoice do not apply to this invoice item. Pass an empty string to remove previously-defined tax rates.
    unit_amount_decimal: The decimal unit amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. This `unit_amount_decimal` will be multiplied by the quantity to get the full amount. Passing in a negative `unit_amount_decimal` will reduce the `amount_due` on the invoice. Accepts at most 12 decimal places."""
		...


class Invoices(_StripeResourceGroup):
	def fetch(*, collection_method=None, created=None, customer=None, due_date=None, ending_before=None, expand=None, limit=None, starting_after=None, status=None, subscription=None):
		"""List all invoices

Parameters:
    collection_method: The collection method of the invoice to retrieve. Either `charge_automatically` or `send_invoice`.
    created: Only return invoices that were created during the given date interval.
    customer: Only return invoices for the customer specified by this customer ID.
    due_date: 
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    status: The status of the invoice, one of `draft`, `open`, `paid`, `uncollectible`, or `void`. [Learn more](https://stripe.com/docs/billing/invoices/workflow#workflow-overview)
    subscription: Only return invoices for the subscription specified by this subscription ID."""
		...
	def create(*, account_tax_ids=None, application_fee_amount=None, auto_advance=None, automatic_tax=None, automatically_finalizes_at=None, collection_method=None, currency=None, custom_fields=None, customer=None, days_until_due=None, default_payment_method=None, default_source=None, default_tax_rates=None, description=None, discounts=None, due_date=None, effective_at=None, expand=None, footer=None, from_invoice=None, issuer=None, metadata=None, number=None, on_behalf_of=None, payment_settings=None, pending_invoice_items_behavior=None, rendering=None, shipping_cost=None, shipping_details=None, statement_descriptor=None, subscription=None, transfer_data=None):
		"""Create an invoice

Parameters:
    account_tax_ids: The account tax IDs associated with the invoice. Only editable when the invoice is a draft.
    application_fee_amount: A fee in cents (or local equivalent) that will be applied to the invoice and transferred to the application owner's Stripe account. The request must be made with an OAuth key or the Stripe-Account header in order to take an application fee. For more information, see the application fees [documentation](https://stripe.com/docs/billing/invoices/connect#collecting-fees).
    auto_advance: Controls whether Stripe performs [automatic collection](https://stripe.com/docs/invoicing/integration/automatic-advancement-collection) of the invoice. If `false`, the invoice's state doesn't automatically advance without an explicit action.
    automatic_tax: Settings for automatic tax lookup for this invoice.
    automatically_finalizes_at: The time when this invoice should be scheduled to finalize. The invoice will be finalized at this time if it is still in draft state.
    collection_method: Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this invoice using the default source attached to the customer. When sending an invoice, Stripe will email this invoice to the customer with payment instructions. Defaults to `charge_automatically`.
    currency: The currency to create this invoice in. Defaults to that of `customer` if not specified.
    custom_fields: A list of up to 4 custom fields to be displayed on the invoice.
    customer: The ID of the customer who will be billed.
    days_until_due: The number of days from when the invoice is created until it is due. Valid only for invoices where `collection_method=send_invoice`.
    default_payment_method: ID of the default payment method for the invoice. It must belong to the customer associated with the invoice. If not set, defaults to the subscription's default payment method, if any, or to the default payment method in the customer's invoice settings.
    default_source: ID of the default payment source for the invoice. It must belong to the customer associated with the invoice and be in a chargeable state. If not set, defaults to the subscription's default source, if any, or to the customer's default source.
    default_tax_rates: The tax rates that will apply to any line item that does not have `tax_rates` set.
    description: An arbitrary string attached to the object. Often useful for displaying to users. Referenced as 'memo' in the Dashboard.
    discounts: The coupons and promotion codes to redeem into discounts for the invoice. If not specified, inherits the discount from the invoice's customer. Pass an empty string to avoid inheriting any discounts.
    due_date: The date on which payment for this invoice is due. Valid only for invoices where `collection_method=send_invoice`.
    effective_at: The date when this invoice is in effect. Same as `finalized_at` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the invoice PDF and receipt.
    expand: Specifies which fields in the response should be expanded.
    footer: Footer to be displayed on the invoice.
    from_invoice: Revise an existing invoice. The new invoice will be created in `status=draft`. See the [revision documentation](https://stripe.com/docs/invoicing/invoice-revisions) for more details.
    issuer: The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    number: Set the number for this invoice. If no number is present then a number will be assigned automatically when the invoice is finalized. In many markets, regulations require invoices to be unique, sequential and / or gapless. You are responsible for ensuring this is true across all your different invoicing systems in the event that you edit the invoice number using our API. If you use only Stripe for your invoices and do not change invoice numbers, Stripe handles this aspect of compliance for you automatically.
    on_behalf_of: The account (if any) for which the funds of the invoice payment are intended. If set, the invoice will be presented with the branding and support information of the specified account. See the [Invoices with Connect](https://stripe.com/docs/billing/invoices/connect) documentation for details.
    payment_settings: Configuration settings for the PaymentIntent that is generated when the invoice is finalized.
    pending_invoice_items_behavior: How to handle pending invoice items on invoice creation. Defaults to `exclude` if the parameter is omitted.
    rendering: The rendering-related settings that control how the invoice is displayed on customer-facing surfaces such as PDF and Hosted Invoice Page.
    shipping_cost: Settings for the cost of shipping for this invoice.
    shipping_details: Shipping details for the invoice. The Invoice PDF will use the `shipping_details` value if it is set, otherwise the PDF will render the shipping address from the customer.
    statement_descriptor: Extra information about a charge for the customer's credit card statement. It must contain at least one letter. If not specified and this invoice is part of a subscription, the default `statement_descriptor` will be set to the first subscription item's product's `statement_descriptor`.
    subscription: The ID of the subscription to invoice, if any. If set, the created invoice will only include pending invoice items for that subscription. The subscription's billing cycle and regular subscription events won't be affected.
    transfer_data: If specified, the funds from the invoice will be transferred to the destination and the ID of the resulting transfer will be found on the invoice's charge."""
		...


class Invoices_Create_Preview(_StripeResourceGroup):
	def create(*, automatic_tax=None, currency=None, customer=None, customer_details=None, discounts=None, expand=None, invoice_items=None, issuer=None, on_behalf_of=None, preview_mode=None, schedule=None, schedule_details=None, subscription=None, subscription_details=None):
		"""Create a preview invoice

Parameters:
    automatic_tax: Settings for automatic tax lookup for this invoice preview.
    currency: The currency to preview this invoice in. Defaults to that of `customer` if not specified.
    customer: The identifier of the customer whose upcoming invoice you'd like to retrieve. If `automatic_tax` is enabled then one of `customer`, `customer_details`, `subscription`, or `schedule` must be set.
    customer_details: Details about the customer you want to invoice or overrides for an existing customer. If `automatic_tax` is enabled then one of `customer`, `customer_details`, `subscription`, or `schedule` must be set.
    discounts: The coupons to redeem into discounts for the invoice preview. If not specified, inherits the discount from the subscription or customer. This works for both coupons directly applied to an invoice and coupons applied to a subscription. Pass an empty string to avoid inheriting any discounts.
    expand: Specifies which fields in the response should be expanded.
    invoice_items: List of invoice items to add or update in the upcoming invoice preview (up to 250).
    issuer: The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.
    on_behalf_of: The account (if any) for which the funds of the invoice payment are intended. If set, the invoice will be presented with the branding and support information of the specified account. See the [Invoices with Connect](https://stripe.com/docs/billing/invoices/connect) documentation for details.
    preview_mode: Customizes the types of values to include when calculating the invoice. Defaults to `next` if unspecified.
    schedule: The identifier of the schedule whose upcoming invoice you'd like to retrieve. Cannot be used with subscription or subscription fields.
    schedule_details: The schedule creation or modification params to apply as a preview. Cannot be used with `subscription` or `subscription_` prefixed fields.
    subscription: The identifier of the subscription for which you'd like to retrieve the upcoming invoice. If not provided, but a `subscription_details.items` is provided, you will preview creating a subscription with those items. If neither `subscription` nor `subscription_details.items` is provided, you will retrieve the next upcoming invoice from among the customer's subscriptions.
    subscription_details: The subscription creation or modification params to apply as a preview. Cannot be used with `schedule` or `schedule_details` fields."""
		...


class Invoices_Search(_StripeResourceGroup):
	def fetch(*, expand=None, limit=None, page=None, query=None):
		"""Search invoices

Parameters:
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
    query: The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for invoices](https://stripe.com/docs/search#query-fields-for-invoices)."""
		...


class Invoices_Invoice(_StripeResourceGroup):
	def delete():
		"""Delete a draft invoice"""
		...
	def fetch(*, expand=None):
		"""Retrieve an invoice

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, account_tax_ids=None, application_fee_amount=None, auto_advance=None, automatic_tax=None, automatically_finalizes_at=None, collection_method=None, custom_fields=None, days_until_due=None, default_payment_method=None, default_source=None, default_tax_rates=None, description=None, discounts=None, due_date=None, effective_at=None, expand=None, footer=None, issuer=None, metadata=None, number=None, on_behalf_of=None, payment_settings=None, rendering=None, shipping_cost=None, shipping_details=None, statement_descriptor=None, transfer_data=None):
		"""Update an invoice

Parameters:
    account_tax_ids: The account tax IDs associated with the invoice. Only editable when the invoice is a draft.
    application_fee_amount: A fee in cents (or local equivalent) that will be applied to the invoice and transferred to the application owner's Stripe account. The request must be made with an OAuth key or the Stripe-Account header in order to take an application fee. For more information, see the application fees [documentation](https://stripe.com/docs/billing/invoices/connect#collecting-fees).
    auto_advance: Controls whether Stripe performs [automatic collection](https://stripe.com/docs/invoicing/integration/automatic-advancement-collection) of the invoice.
    automatic_tax: Settings for automatic tax lookup for this invoice.
    automatically_finalizes_at: The time when this invoice should be scheduled to finalize. The invoice will be finalized at this time if it is still in draft state. To turn off automatic finalization, set `auto_advance` to false.
    collection_method: Either `charge_automatically` or `send_invoice`. This field can be updated only on `draft` invoices.
    custom_fields: A list of up to 4 custom fields to be displayed on the invoice. If a value for `custom_fields` is specified, the list specified will replace the existing custom field list on this invoice. Pass an empty string to remove previously-defined fields.
    days_until_due: The number of days from which the invoice is created until it is due. Only valid for invoices where `collection_method=send_invoice`. This field can only be updated on `draft` invoices.
    default_payment_method: ID of the default payment method for the invoice. It must belong to the customer associated with the invoice. If not set, defaults to the subscription's default payment method, if any, or to the default payment method in the customer's invoice settings.
    default_source: ID of the default payment source for the invoice. It must belong to the customer associated with the invoice and be in a chargeable state. If not set, defaults to the subscription's default source, if any, or to the customer's default source.
    default_tax_rates: The tax rates that will apply to any line item that does not have `tax_rates` set. Pass an empty string to remove previously-defined tax rates.
    description: An arbitrary string attached to the object. Often useful for displaying to users. Referenced as 'memo' in the Dashboard.
    discounts: The discounts that will apply to the invoice. Pass an empty string to remove previously-defined discounts.
    due_date: The date on which payment for this invoice is due. Only valid for invoices where `collection_method=send_invoice`. This field can only be updated on `draft` invoices.
    effective_at: The date when this invoice is in effect. Same as `finalized_at` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the invoice PDF and receipt.
    expand: Specifies which fields in the response should be expanded.
    footer: Footer to be displayed on the invoice.
    issuer: The connected account that issues the invoice. The invoice is presented with the branding and support information of the specified account.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    number: Set the number for this invoice. If no number is present then a number will be assigned automatically when the invoice is finalized. In many markets, regulations require invoices to be unique, sequential and / or gapless. You are responsible for ensuring this is true across all your different invoicing systems in the event that you edit the invoice number using our API. If you use only Stripe for your invoices and do not change invoice numbers, Stripe handles this aspect of compliance for you automatically.
    on_behalf_of: The account (if any) for which the funds of the invoice payment are intended. If set, the invoice will be presented with the branding and support information of the specified account. See the [Invoices with Connect](https://stripe.com/docs/billing/invoices/connect) documentation for details.
    payment_settings: Configuration settings for the PaymentIntent that is generated when the invoice is finalized.
    rendering: The rendering-related settings that control how the invoice is displayed on customer-facing surfaces such as PDF and Hosted Invoice Page.
    shipping_cost: Settings for the cost of shipping for this invoice.
    shipping_details: Shipping details for the invoice. The Invoice PDF will use the `shipping_details` value if it is set, otherwise the PDF will render the shipping address from the customer.
    statement_descriptor: Extra information about a charge for the customer's credit card statement. It must contain at least one letter. If not specified and this invoice is part of a subscription, the default `statement_descriptor` will be set to the first subscription item's product's `statement_descriptor`.
    transfer_data: If specified, the funds from the invoice will be transferred to the destination and the ID of the resulting transfer will be found on the invoice's charge. This will be unset if you POST an empty value."""
		...


class Invoices_Invoice_Add_Lines(_StripeResourceGroup):
	def create(*, expand=None, invoice_metadata=None, lines=None):
		"""Bulk add invoice line items

Parameters:
    expand: Specifies which fields in the response should be expanded.
    invoice_metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    lines: The line items to add."""
		...


class Invoices_Invoice_Attach_Payment(_StripeResourceGroup):
	def create(*, expand=None, payment_intent=None):
		"""Attach a payment to an Invoice

Parameters:
    expand: Specifies which fields in the response should be expanded.
    payment_intent: The ID of the PaymentIntent to attach to the invoice."""
		...


class Invoices_Invoice_Finalize(_StripeResourceGroup):
	def create(*, auto_advance=None, expand=None):
		"""Finalize an invoice

Parameters:
    auto_advance: Controls whether Stripe performs [automatic collection](https://stripe.com/docs/invoicing/integration/automatic-advancement-collection) of the invoice. If `false`, the invoice's state doesn't automatically advance without an explicit action.
    expand: Specifies which fields in the response should be expanded."""
		...


class Invoices_Invoice_Lines(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None):
		"""Retrieve an invoice's line items

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...


class Invoices_Invoice_Lines_Line_Item_Id(_StripeResourceGroup):
	def create(*, amount=None, description=None, discountable=None, discounts=None, expand=None, metadata=None, period=None, price_data=None, pricing=None, quantity=None, tax_amounts=None, tax_rates=None):
		"""Update an invoice's line item

Parameters:
    amount: The integer amount in cents (or local equivalent) of the charge to be applied to the upcoming invoice. If you want to apply a credit to the customer's account, pass a negative amount.
    description: An arbitrary string which you can attach to the invoice item. The description is displayed in the invoice for easy tracking.
    discountable: Controls whether discounts apply to this line item. Defaults to false for prorations or negative line items, and true for all other line items. Cannot be set to true for prorations.
    discounts: The coupons, promotion codes & existing discounts which apply to the line item. Item discounts are applied before invoice discounts. Pass an empty string to remove previously-defined discounts.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. For [type=subscription](https://stripe.com/docs/api/invoices/line_item#invoice_line_item_object-type) line items, the incoming metadata specified on the request is directly used to set this value, in contrast to [type=invoiceitem](api/invoices/line_item#invoice_line_item_object-type) line items, where any existing metadata on the invoice line is merged with the incoming data.
    period: The period associated with this invoice item. When set to different values, the period will be rendered on the invoice. If you have [Stripe Revenue Recognition](https://stripe.com/docs/revenue-recognition) enabled, the period will be used to recognize and defer revenue. See the [Revenue Recognition documentation](https://stripe.com/docs/revenue-recognition/methodology/subscriptions-and-invoicing) for details.
    price_data: Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
    pricing: The pricing information for the invoice item.
    quantity: Non-negative integer. The quantity of units for the line item.
    tax_amounts: A list of up to 10 tax amounts for this line item. This can be useful if you calculate taxes on your own or use a third-party to calculate them. You cannot set tax amounts if any line item has [tax_rates](https://stripe.com/docs/api/invoices/line_item#invoice_line_item_object-tax_rates) or if the invoice has [default_tax_rates](https://stripe.com/docs/api/invoices/object#invoice_object-default_tax_rates) or uses [automatic tax](https://stripe.com/docs/tax/invoicing). Pass an empty string to remove previously defined tax amounts.
    tax_rates: The tax rates which apply to the line item. When set, the `default_tax_rates` on the invoice do not apply to this line item. Pass an empty string to remove previously-defined tax rates."""
		...


class Invoices_Invoice_Mark_Uncollectible(_StripeResourceGroup):
	def create(*, expand=None):
		"""Mark an invoice as uncollectible

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Invoices_Invoice_Pay(_StripeResourceGroup):
	def create(*, expand=None, forgive=None, mandate=None, off_session=None, paid_out_of_band=None, payment_method=None, source=None):
		"""Pay an invoice

Parameters:
    expand: Specifies which fields in the response should be expanded.
    forgive: In cases where the source used to pay the invoice has insufficient funds, passing `forgive=true` controls whether a charge should be attempted for the full amount available on the source, up to the amount to fully pay the invoice. This effectively forgives the difference between the amount available on the source and the amount due. 

Passing `forgive=false` will fail the charge if the source hasn't been pre-funded with the right amount. An example for this case is with ACH Credit Transfers and wires: if the amount wired is less than the amount due by a small amount, you might want to forgive the difference. Defaults to `false`.
    mandate: ID of the mandate to be used for this invoice. It must correspond to the payment method used to pay the invoice, including the payment_method param or the invoice's default_payment_method or default_source, if set.
    off_session: Indicates if a customer is on or off-session while an invoice payment is attempted. Defaults to `true` (off-session).
    paid_out_of_band: Boolean representing whether an invoice is paid outside of Stripe. This will result in no charge being made. Defaults to `false`.
    payment_method: A PaymentMethod to be charged. The PaymentMethod must be the ID of a PaymentMethod belonging to the customer associated with the invoice being paid.
    source: A payment source to be charged. The source must be the ID of a source belonging to the customer associated with the invoice being paid."""
		...


class Invoices_Invoice_Remove_Lines(_StripeResourceGroup):
	def create(*, expand=None, invoice_metadata=None, lines=None):
		"""Bulk remove invoice line items

Parameters:
    expand: Specifies which fields in the response should be expanded.
    invoice_metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    lines: The line items to remove."""
		...


class Invoices_Invoice_Send(_StripeResourceGroup):
	def create(*, expand=None):
		"""Send an invoice for manual payment

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Invoices_Invoice_Update_Lines(_StripeResourceGroup):
	def create(*, expand=None, invoice_metadata=None, lines=None):
		"""Bulk update invoice line items

Parameters:
    expand: Specifies which fields in the response should be expanded.
    invoice_metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. For [type=subscription](https://stripe.com/docs/api/invoices/line_item#invoice_line_item_object-type) line items, the incoming metadata specified on the request is directly used to set this value, in contrast to [type=invoiceitem](api/invoices/line_item#invoice_line_item_object-type) line items, where any existing metadata on the invoice line is merged with the incoming data.
    lines: The line items to update."""
		...


class Invoices_Invoice_Void(_StripeResourceGroup):
	def create(*, expand=None):
		"""Void an invoice

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Issuing_Authorizations(_StripeResourceGroup):
	def fetch(*, card=None, cardholder=None, created=None, ending_before=None, expand=None, limit=None, starting_after=None, status=None):
		"""List all authorizations

Parameters:
    card: Only return authorizations that belong to the given card.
    cardholder: Only return authorizations that belong to the given cardholder.
    created: Only return authorizations that were created during the given date interval.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    status: Only return authorizations with the given status. One of `pending`, `closed`, or `reversed`."""
		...


class Issuing_Authorizations_Authorization(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve an authorization

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, expand=None, metadata=None):
		"""Update an authorization

Parameters:
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."""
		...


class Issuing_Authorizations_Authorization_Approve(_StripeResourceGroup):
	def create(*, amount=None, expand=None, metadata=None):
		"""Approve an authorization

Parameters:
    amount: If the authorization's `pending_request.is_amount_controllable` property is `true`, you may provide this value to control how much to hold for the authorization. Must be positive (use [`decline`](https://stripe.com/docs/api/issuing/authorizations/decline) to decline an authorization request).
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."""
		...


class Issuing_Authorizations_Authorization_Decline(_StripeResourceGroup):
	def create(*, expand=None, metadata=None):
		"""Decline an authorization

Parameters:
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."""
		...


class Issuing_Cardholders(_StripeResourceGroup):
	def fetch(*, created=None, email=None, ending_before=None, expand=None, limit=None, phone_number=None, starting_after=None, status=None, type=None):
		"""List all cardholders

Parameters:
    created: Only return cardholders that were created during the given date interval.
    email: Only return cardholders that have the given email address.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    phone_number: Only return cardholders that have the given phone number.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    status: Only return cardholders that have the given status. One of `active`, `inactive`, or `blocked`.
    type: Only return cardholders that have the given type. One of `individual` or `company`."""
		...
	def create(*, billing=None, company=None, email=None, expand=None, individual=None, metadata=None, name=None, phone_number=None, preferred_locales=None, spending_controls=None, status=None, type=None):
		"""Create a cardholder

Parameters:
    billing: The cardholder's billing address.
    company: Additional information about a `company` cardholder.
    email: The cardholder's email address.
    expand: Specifies which fields in the response should be expanded.
    individual: Additional information about an `individual` cardholder.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    name: The cardholder's name. This will be printed on cards issued to them. The maximum length of this field is 24 characters. This field cannot contain any special characters or numbers.
    phone_number: The cardholder's phone number. This will be transformed to [E.164](https://en.wikipedia.org/wiki/E.164) if it is not provided in that format already. This is required for all cardholders who will be creating EU cards. See the [3D Secure documentation](https://stripe.com/docs/issuing/3d-secure#when-is-3d-secure-applied) for more details.
    preferred_locales: The cardholder’s preferred locales (languages), ordered by preference. Locales can be `de`, `en`, `es`, `fr`, or `it`.
 This changes the language of the [3D Secure flow](https://stripe.com/docs/issuing/3d-secure) and one-time password messages sent to the cardholder.
    spending_controls: Rules that control spending across this cardholder's cards. Refer to our [documentation](https://stripe.com/docs/issuing/controls/spending-controls) for more details.
    status: Specifies whether to permit authorizations on this cardholder's cards. Defaults to `active`.
    type: One of `individual` or `company`. See [Choose a cardholder type](https://stripe.com/docs/issuing/other/choose-cardholder) for more details."""
		...


class Issuing_Cardholders_Cardholder(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a cardholder

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, billing=None, company=None, email=None, expand=None, individual=None, metadata=None, phone_number=None, preferred_locales=None, spending_controls=None, status=None):
		"""Update a cardholder

Parameters:
    billing: The cardholder's billing address.
    company: Additional information about a `company` cardholder.
    email: The cardholder's email address.
    expand: Specifies which fields in the response should be expanded.
    individual: Additional information about an `individual` cardholder.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    phone_number: The cardholder's phone number. This is required for all cardholders who will be creating EU cards. See the [3D Secure documentation](https://stripe.com/docs/issuing/3d-secure) for more details.
    preferred_locales: The cardholder’s preferred locales (languages), ordered by preference. Locales can be `de`, `en`, `es`, `fr`, or `it`.
 This changes the language of the [3D Secure flow](https://stripe.com/docs/issuing/3d-secure) and one-time password messages sent to the cardholder.
    spending_controls: Rules that control spending across this cardholder's cards. Refer to our [documentation](https://stripe.com/docs/issuing/controls/spending-controls) for more details.
    status: Specifies whether to permit authorizations on this cardholder's cards."""
		...


class Issuing_Cards(_StripeResourceGroup):
	def fetch(*, cardholder=None, created=None, ending_before=None, exp_month=None, exp_year=None, expand=None, last4=None, limit=None, personalization_design=None, starting_after=None, status=None, type=None):
		"""List all cards

Parameters:
    cardholder: Only return cards belonging to the Cardholder with the provided ID.
    created: Only return cards that were issued during the given date interval.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    exp_month: Only return cards that have the given expiration month.
    exp_year: Only return cards that have the given expiration year.
    expand: Specifies which fields in the response should be expanded.
    last4: Only return cards that have the given last four digits.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    personalization_design: 
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    status: Only return cards that have the given status. One of `active`, `inactive`, or `canceled`.
    type: Only return cards that have the given type. One of `virtual` or `physical`."""
		...
	def create(*, cardholder=None, currency=None, expand=None, financial_account=None, metadata=None, personalization_design=None, pin=None, replacement_for=None, replacement_reason=None, second_line=None, shipping=None, spending_controls=None, status=None, type=None):
		"""Create a card

Parameters:
    cardholder: The [Cardholder](https://stripe.com/docs/api#issuing_cardholder_object) object with which the card will be associated.
    currency: The currency for the card.
    expand: Specifies which fields in the response should be expanded.
    financial_account: The new financial account ID the card will be associated with. This field allows a card to be reassigned to a different financial account.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    personalization_design: The personalization design object belonging to this card.
    pin: The desired PIN for this card.
    replacement_for: The card this is meant to be a replacement for (if any).
    replacement_reason: If `replacement_for` is specified, this should indicate why that card is being replaced.
    second_line: The second line to print on the card. Max length: 24 characters.
    shipping: The address where the card will be shipped.
    spending_controls: Rules that control spending for this card. Refer to our [documentation](https://stripe.com/docs/issuing/controls/spending-controls) for more details.
    status: Whether authorizations can be approved on this card. May be blocked from activating cards depending on past-due Cardholder requirements. Defaults to `inactive`.
    type: The type of card to issue. Possible values are `physical` or `virtual`."""
		...


class Issuing_Cards_Card(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a card

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, cancellation_reason=None, expand=None, metadata=None, personalization_design=None, pin=None, shipping=None, spending_controls=None, status=None):
		"""Update a card

Parameters:
    cancellation_reason: Reason why the `status` of this card is `canceled`.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    personalization_design: 
    pin: The desired new PIN for this card.
    shipping: Updated shipping information for the card.
    spending_controls: Rules that control spending for this card. Refer to our [documentation](https://stripe.com/docs/issuing/controls/spending-controls) for more details.
    status: Dictates whether authorizations can be approved on this card. May be blocked from activating cards depending on past-due Cardholder requirements. Defaults to `inactive`. If this card is being canceled because it was lost or stolen, this information should be provided as `cancellation_reason`."""
		...


class Issuing_Disputes(_StripeResourceGroup):
	def fetch(*, created=None, ending_before=None, expand=None, limit=None, starting_after=None, status=None, transaction=None):
		"""List all disputes

Parameters:
    created: Only return Issuing disputes that were created during the given date interval.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    status: Select Issuing disputes with the given status.
    transaction: Select the Issuing dispute for the given transaction."""
		...
	def create(*, amount=None, evidence=None, expand=None, metadata=None, transaction=None, treasury=None):
		"""Create a dispute

Parameters:
    amount: The dispute amount in the card's currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal). If not set, defaults to the full transaction amount.
    evidence: Evidence provided for the dispute.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    transaction: The ID of the issuing transaction to create a dispute for. For transaction on Treasury FinancialAccounts, use `treasury.received_debit`.
    treasury: Params for disputes related to Treasury FinancialAccounts"""
		...


class Issuing_Disputes_Dispute(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a dispute

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, amount=None, evidence=None, expand=None, metadata=None):
		"""Update a dispute

Parameters:
    amount: The dispute amount in the card's currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    evidence: Evidence provided for the dispute.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."""
		...


class Issuing_Disputes_Dispute_Submit(_StripeResourceGroup):
	def create(*, expand=None, metadata=None):
		"""Submit a dispute

Parameters:
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."""
		...


class Issuing_Personalization_Designs(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, lookup_keys=None, preferences=None, starting_after=None, status=None):
		"""List all personalization designs

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    lookup_keys: Only return personalization designs with the given lookup keys.
    preferences: Only return personalization designs with the given preferences.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    status: Only return personalization designs with the given status."""
		...
	def create(*, card_logo=None, carrier_text=None, expand=None, lookup_key=None, metadata=None, name=None, physical_bundle=None, preferences=None, transfer_lookup_key=None):
		"""Create a personalization design

Parameters:
    card_logo: The file for the card logo, for use with physical bundles that support card logos. Must have a `purpose` value of `issuing_logo`.
    carrier_text: Hash containing carrier text, for use with physical bundles that support carrier text.
    expand: Specifies which fields in the response should be expanded.
    lookup_key: A lookup key used to retrieve personalization designs dynamically from a static string. This may be up to 200 characters.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    name: Friendly display name.
    physical_bundle: The physical bundle object belonging to this personalization design.
    preferences: Information on whether this personalization design is used to create cards when one is not specified.
    transfer_lookup_key: If set to true, will atomically remove the lookup key from the existing personalization design, and assign it to this personalization design."""
		...


class Issuing_Personalization_Designs_Personalization_Design(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a personalization design

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, card_logo=None, carrier_text=None, expand=None, lookup_key=None, metadata=None, name=None, physical_bundle=None, preferences=None, transfer_lookup_key=None):
		"""Update a personalization design

Parameters:
    card_logo: The file for the card logo, for use with physical bundles that support card logos. Must have a `purpose` value of `issuing_logo`.
    carrier_text: Hash containing carrier text, for use with physical bundles that support carrier text.
    expand: Specifies which fields in the response should be expanded.
    lookup_key: A lookup key used to retrieve personalization designs dynamically from a static string. This may be up to 200 characters.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    name: Friendly display name. Providing an empty string will set the field to null.
    physical_bundle: The physical bundle object belonging to this personalization design.
    preferences: Information on whether this personalization design is used to create cards when one is not specified.
    transfer_lookup_key: If set to true, will atomically remove the lookup key from the existing personalization design, and assign it to this personalization design."""
		...


class Issuing_Physical_Bundles(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None, status=None, type=None):
		"""List all physical bundles

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    status: Only return physical bundles with the given status.
    type: Only return physical bundles with the given type."""
		...


class Issuing_Physical_Bundles_Physical_Bundle(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a physical bundle

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Issuing_Settlements_Settlement(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a settlement

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, expand=None, metadata=None):
		"""Update a settlement

Parameters:
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."""
		...


class Issuing_Tokens(_StripeResourceGroup):
	def fetch(*, card=None, created=None, ending_before=None, expand=None, limit=None, starting_after=None, status=None):
		"""List all issuing tokens for card

Parameters:
    card: The Issuing card identifier to list tokens for.
    created: Only return Issuing tokens that were created during the given date interval.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    status: Select Issuing tokens with the given status."""
		...


class Issuing_Tokens_Token(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve an issuing token

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, expand=None, status=None):
		"""Update a token status

Parameters:
    expand: Specifies which fields in the response should be expanded.
    status: Specifies which status the token should be updated to."""
		...


class Issuing_Transactions(_StripeResourceGroup):
	def fetch(*, card=None, cardholder=None, created=None, ending_before=None, expand=None, limit=None, starting_after=None, type=None):
		"""List all transactions

Parameters:
    card: Only return transactions that belong to the given card.
    cardholder: Only return transactions that belong to the given cardholder.
    created: Only return transactions that were created during the given date interval.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    type: Only return transactions that have the given type. One of `capture` or `refund`."""
		...


class Issuing_Transactions_Transaction(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a transaction

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, expand=None, metadata=None):
		"""Update a transaction

Parameters:
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."""
		...


class Link_Account_Sessions(_StripeResourceGroup):
	def create(*, account_holder=None, expand=None, filters=None, permissions=None, prefetch=None, return_url=None):
		"""Create a Session

Parameters:
    account_holder: The account holder to link accounts for.
    expand: Specifies which fields in the response should be expanded.
    filters: Filters to restrict the kinds of accounts to collect.
    permissions: List of data features that you would like to request access to.

Possible values are `balances`, `transactions`, `ownership`, and `payment_method`.
    prefetch: List of data features that you would like to retrieve upon account creation.
    return_url: For webview integrations only. Upon completing OAuth login in the native browser, the user will be redirected to this URL to return to your app."""
		...


class Link_Account_Sessions_Session(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a Session

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Linked_Accounts(_StripeResourceGroup):
	def fetch(*, account_holder=None, ending_before=None, expand=None, limit=None, session=None, starting_after=None):
		"""List Accounts

Parameters:
    account_holder: If present, only return accounts that belong to the specified account holder. `account_holder[customer]` and `account_holder[account]` are mutually exclusive.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    session: If present, only return accounts that were collected as part of the given session.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...


class Linked_Accounts_Account(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve an Account

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Linked_Accounts_Account_Disconnect(_StripeResourceGroup):
	def create(*, expand=None):
		"""Disconnect an Account

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Linked_Accounts_Account_Owners(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, ownership=None, starting_after=None):
		"""List Account Owners

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    ownership: The ID of the ownership object to fetch owners from.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...


class Linked_Accounts_Account_Refresh(_StripeResourceGroup):
	def create(*, expand=None, features=None):
		"""Refresh Account data

Parameters:
    expand: Specifies which fields in the response should be expanded.
    features: The list of account features that you would like to refresh."""
		...


class Mandates_Mandate(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a Mandate

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Payment_Intents(_StripeResourceGroup):
	def fetch(*, created=None, customer=None, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List all PaymentIntents

Parameters:
    created: A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp or a dictionary with a number of different query options.
    customer: Only return PaymentIntents for the customer that this customer ID specifies.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, amount=None, application_fee_amount=None, automatic_payment_methods=None, capture_method=None, confirm=None, confirmation_method=None, confirmation_token=None, currency=None, customer=None, description=None, error_on_requires_action=None, expand=None, mandate=None, mandate_data=None, metadata=None, off_session=None, on_behalf_of=None, payment_method=None, payment_method_configuration=None, payment_method_data=None, payment_method_options=None, payment_method_types=None, radar_options=None, receipt_email=None, return_url=None, setup_future_usage=None, shipping=None, statement_descriptor=None, statement_descriptor_suffix=None, transfer_data=None, transfer_group=None, use_stripe_sdk=None):
		"""Create a PaymentIntent

Parameters:
    amount: Amount intended to be collected by this PaymentIntent. A positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).
    application_fee_amount: The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total amount captured. For more information, see the PaymentIntents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
    automatic_payment_methods: When you enable this parameter, this PaymentIntent accepts payment methods that you enable in the Dashboard and that are compatible with this PaymentIntent's other parameters.
    capture_method: Controls when the funds will be captured from the customer's account.
    confirm: Set to `true` to attempt to [confirm this PaymentIntent](https://stripe.com/docs/api/payment_intents/confirm) immediately. This parameter defaults to `false`. When creating and confirming a PaymentIntent at the same time, you can also provide the parameters available in the [Confirm API](https://stripe.com/docs/api/payment_intents/confirm).
    confirmation_method: Describes whether we can confirm this PaymentIntent automatically, or if it requires customer action to confirm the payment.
    confirmation_token: ID of the ConfirmationToken used to confirm this PaymentIntent.

If the provided ConfirmationToken contains properties that are also being provided in this request, such as `payment_method`, then the values in this request will take precedence.
    currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    customer: ID of the Customer this PaymentIntent belongs to, if one exists.

Payment methods attached to other Customers cannot be used with this PaymentIntent.

If [setup_future_usage](https://stripe.com/docs/api#payment_intent_object-setup_future_usage) is set and this PaymentIntent's payment method is not `card_present`, then the payment method attaches to the Customer after the PaymentIntent has been confirmed and any required actions from the user are complete. If the payment method is `card_present` and isn't a digital wallet, then a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card is created and attached to the Customer instead.
    description: An arbitrary string attached to the object. Often useful for displaying to users.
    error_on_requires_action: Set to `true` to fail the payment attempt if the PaymentIntent transitions into `requires_action`. Use this parameter for simpler integrations that don't handle customer actions, such as [saving cards without authentication](https://stripe.com/docs/payments/save-card-without-authentication). This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm).
    expand: Specifies which fields in the response should be expanded.
    mandate: ID of the mandate that's used for this payment. This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm).
    mandate_data: This hash contains details about the Mandate to create. This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm).
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    off_session: Set to `true` to indicate that the customer isn't in your checkout flow during this payment attempt and can't authenticate. Use this parameter in scenarios where you collect card details and [charge them later](https://stripe.com/docs/payments/cards/charging-saved-cards). This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm).
    on_behalf_of: The Stripe account ID that these funds are intended for. Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
    payment_method: ID of the payment method (a PaymentMethod, Card, or [compatible Source](https://stripe.com/docs/payments/payment-methods/transitioning#compatibility) object) to attach to this PaymentIntent.

If you omit this parameter with `confirm=true`, `customer.default_source` attaches as this PaymentIntent's payment instrument to improve migration for users of the Charges API. We recommend that you explicitly provide the `payment_method` moving forward.
If the payment method is attached to a Customer, you must also provide the ID of that Customer as the [customer](https://stripe.com/docs/api#create_payment_intent-customer) parameter of this PaymentIntent.
    payment_method_configuration: The ID of the [payment method configuration](https://stripe.com/docs/api/payment_method_configurations) to use with this PaymentIntent.
    payment_method_data: If provided, this hash will be used to create a PaymentMethod. The new PaymentMethod will appear
in the [payment_method](https://stripe.com/docs/api/payment_intents/object#payment_intent_object-payment_method)
property on the PaymentIntent.
    payment_method_options: Payment method-specific configuration for this PaymentIntent.
    payment_method_types: The list of payment method types (for example, a card) that this PaymentIntent can use. If you don't provide this, Stripe will dynamically show relevant payment methods from your [payment method settings](https://dashboard.stripe.com/settings/payment_methods).
    radar_options: Options to configure Radar. Learn more about [Radar Sessions](https://stripe.com/docs/radar/radar-session).
    receipt_email: Email address to send the receipt to. If you specify `receipt_email` for a payment in live mode, you send a receipt regardless of your [email settings](https://dashboard.stripe.com/account/emails).
    return_url: The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method's app or site. If you'd prefer to redirect to a mobile application, you can alternatively supply an application URI scheme. This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-confirm).
    setup_future_usage: Indicates that you intend to make future payments with this PaymentIntent's payment method.

If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](/strong-customer-authentication).
    shipping: Shipping information for this PaymentIntent.
    statement_descriptor: Text that appears on the customer's statement as the statement descriptor for a non-card charge. This value overrides the account's default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).

Setting this value for a card charge returns an error. For card charges, set the [statement_descriptor_suffix](https://docs.stripe.com/get-started/account/statement-descriptors#dynamic) instead.
    statement_descriptor_suffix: Provides information about a card charge. Concatenated to the account's [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors#static) to form the complete statement descriptor that appears on the customer's statement.
    transfer_data: The parameters that you can use to automatically create a Transfer.
Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
    transfer_group: A string that identifies the resulting payment as part of a group. Learn more about the [use case for connected accounts](https://stripe.com/docs/connect/separate-charges-and-transfers).
    use_stripe_sdk: Set to `true` when confirming server-side and using Stripe.js, iOS, or Android client-side SDKs to handle the next actions."""
		...


class Payment_Intents_Search(_StripeResourceGroup):
	def fetch(*, expand=None, limit=None, page=None, query=None):
		"""Search PaymentIntents

Parameters:
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
    query: The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for payment intents](https://stripe.com/docs/search#query-fields-for-payment-intents)."""
		...


class Payment_Intents_Intent(_StripeResourceGroup):
	def fetch(*, client_secret=None, expand=None):
		"""Retrieve a PaymentIntent

Parameters:
    client_secret: The client secret of the PaymentIntent. We require it if you use a publishable key to retrieve the source.
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, amount=None, application_fee_amount=None, capture_method=None, currency=None, customer=None, description=None, expand=None, metadata=None, payment_method=None, payment_method_configuration=None, payment_method_data=None, payment_method_options=None, payment_method_types=None, receipt_email=None, setup_future_usage=None, shipping=None, statement_descriptor=None, statement_descriptor_suffix=None, transfer_data=None, transfer_group=None):
		"""Update a PaymentIntent

Parameters:
    amount: Amount intended to be collected by this PaymentIntent. A positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).
    application_fee_amount: The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total amount captured. For more information, see the PaymentIntents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
    capture_method: Controls when the funds will be captured from the customer's account.
    currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    customer: ID of the Customer this PaymentIntent belongs to, if one exists.

Payment methods attached to other Customers cannot be used with this PaymentIntent.

If [setup_future_usage](https://stripe.com/docs/api#payment_intent_object-setup_future_usage) is set and this PaymentIntent's payment method is not `card_present`, then the payment method attaches to the Customer after the PaymentIntent has been confirmed and any required actions from the user are complete. If the payment method is `card_present` and isn't a digital wallet, then a [generated_card](https://docs.stripe.com/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card is created and attached to the Customer instead.
    description: An arbitrary string attached to the object. Often useful for displaying to users.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    payment_method: ID of the payment method (a PaymentMethod, Card, or [compatible Source](https://stripe.com/docs/payments/payment-methods/transitioning#compatibility) object) to attach to this PaymentIntent. To unset this field to null, pass in an empty string.
    payment_method_configuration: The ID of the [payment method configuration](https://stripe.com/docs/api/payment_method_configurations) to use with this PaymentIntent.
    payment_method_data: If provided, this hash will be used to create a PaymentMethod. The new PaymentMethod will appear
in the [payment_method](https://stripe.com/docs/api/payment_intents/object#payment_intent_object-payment_method)
property on the PaymentIntent.
    payment_method_options: Payment-method-specific configuration for this PaymentIntent.
    payment_method_types: The list of payment method types (for example, card) that this PaymentIntent can use. Use `automatic_payment_methods` to manage payment methods from the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods).
    receipt_email: Email address that the receipt for the resulting payment will be sent to. If `receipt_email` is specified for a payment in live mode, a receipt will be sent regardless of your [email settings](https://dashboard.stripe.com/account/emails).
    setup_future_usage: Indicates that you intend to make future payments with this PaymentIntent's payment method.

If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](/strong-customer-authentication).

If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    shipping: Shipping information for this PaymentIntent.
    statement_descriptor: Text that appears on the customer's statement as the statement descriptor for a non-card charge. This value overrides the account's default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).

Setting this value for a card charge returns an error. For card charges, set the [statement_descriptor_suffix](https://docs.stripe.com/get-started/account/statement-descriptors#dynamic) instead.
    statement_descriptor_suffix: Provides information about a card charge. Concatenated to the account's [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors#static) to form the complete statement descriptor that appears on the customer's statement.
    transfer_data: Use this parameter to automatically create a Transfer when the payment succeeds. Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
    transfer_group: A string that identifies the resulting payment as part of a group. You can only provide `transfer_group` if it hasn't been set. Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts)."""
		...


class Payment_Intents_Intent_Apply_Customer_Balance(_StripeResourceGroup):
	def create(*, amount=None, currency=None, expand=None):
		"""Reconcile a customer_balance PaymentIntent

Parameters:
    amount: Amount that you intend to apply to this PaymentIntent from the customer’s cash balance. If the PaymentIntent was created by an Invoice, the full amount of the PaymentIntent is applied regardless of this parameter.

A positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (for example, 100 cents to charge 1 USD or 100 to charge 100 JPY, a zero-decimal currency). The maximum amount is the amount of the PaymentIntent.

When you omit the amount, it defaults to the remaining amount requested on the PaymentIntent.
    currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    expand: Specifies which fields in the response should be expanded."""
		...


class Payment_Intents_Intent_Cancel(_StripeResourceGroup):
	def create(*, cancellation_reason=None, expand=None):
		"""Cancel a PaymentIntent

Parameters:
    cancellation_reason: Reason for canceling this PaymentIntent. Possible values are: `duplicate`, `fraudulent`, `requested_by_customer`, or `abandoned`
    expand: Specifies which fields in the response should be expanded."""
		...


class Payment_Intents_Intent_Capture(_StripeResourceGroup):
	def create(*, amount_to_capture=None, application_fee_amount=None, expand=None, final_capture=None, metadata=None, statement_descriptor=None, statement_descriptor_suffix=None, transfer_data=None):
		"""Capture a PaymentIntent

Parameters:
    amount_to_capture: The amount to capture from the PaymentIntent, which must be less than or equal to the original amount. Defaults to the full `amount_capturable` if it's not provided.
    application_fee_amount: The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total amount captured. For more information, see the PaymentIntents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
    expand: Specifies which fields in the response should be expanded.
    final_capture: Defaults to `true`. When capturing a PaymentIntent, setting `final_capture` to `false` notifies Stripe to not release the remaining uncaptured funds to make sure that they're captured in future requests. You can only use this setting when [multicapture](https://stripe.com/docs/payments/multicapture) is available for PaymentIntents.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    statement_descriptor: Text that appears on the customer's statement as the statement descriptor for a non-card charge. This value overrides the account's default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).

Setting this value for a card charge returns an error. For card charges, set the [statement_descriptor_suffix](https://docs.stripe.com/get-started/account/statement-descriptors#dynamic) instead.
    statement_descriptor_suffix: Provides information about a card charge. Concatenated to the account's [statement descriptor prefix](https://docs.stripe.com/get-started/account/statement-descriptors#static) to form the complete statement descriptor that appears on the customer's statement.
    transfer_data: The parameters that you can use to automatically create a transfer after the payment
is captured. Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts)."""
		...


class Payment_Intents_Intent_Confirm(_StripeResourceGroup):
	def create(*, capture_method=None, client_secret=None, confirmation_token=None, error_on_requires_action=None, expand=None, mandate=None, mandate_data=None, off_session=None, payment_method=None, payment_method_data=None, payment_method_options=None, payment_method_types=None, radar_options=None, receipt_email=None, return_url=None, setup_future_usage=None, shipping=None, use_stripe_sdk=None):
		"""Confirm a PaymentIntent

Parameters:
    capture_method: Controls when the funds will be captured from the customer's account.
    client_secret: The client secret of the PaymentIntent.
    confirmation_token: ID of the ConfirmationToken used to confirm this PaymentIntent.

If the provided ConfirmationToken contains properties that are also being provided in this request, such as `payment_method`, then the values in this request will take precedence.
    error_on_requires_action: Set to `true` to fail the payment attempt if the PaymentIntent transitions into `requires_action`. This parameter is intended for simpler integrations that do not handle customer actions, like [saving cards without authentication](https://stripe.com/docs/payments/save-card-without-authentication).
    expand: Specifies which fields in the response should be expanded.
    mandate: ID of the mandate that's used for this payment.
    mandate_data: 
    off_session: Set to `true` to indicate that the customer isn't in your checkout flow during this payment attempt and can't authenticate. Use this parameter in scenarios where you collect card details and [charge them later](https://stripe.com/docs/payments/cards/charging-saved-cards).
    payment_method: ID of the payment method (a PaymentMethod, Card, or [compatible Source](https://stripe.com/docs/payments/payment-methods/transitioning#compatibility) object) to attach to this PaymentIntent.
If the payment method is attached to a Customer, it must match the [customer](https://stripe.com/docs/api#create_payment_intent-customer) that is set on this PaymentIntent.
    payment_method_data: If provided, this hash will be used to create a PaymentMethod. The new PaymentMethod will appear
in the [payment_method](https://stripe.com/docs/api/payment_intents/object#payment_intent_object-payment_method)
property on the PaymentIntent.
    payment_method_options: Payment method-specific configuration for this PaymentIntent.
    payment_method_types: The list of payment method types (for example, a card) that this PaymentIntent can use. Use `automatic_payment_methods` to manage payment methods from the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods).
    radar_options: Options to configure Radar. Learn more about [Radar Sessions](https://stripe.com/docs/radar/radar-session).
    receipt_email: Email address that the receipt for the resulting payment will be sent to. If `receipt_email` is specified for a payment in live mode, a receipt will be sent regardless of your [email settings](https://dashboard.stripe.com/account/emails).
    return_url: The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method's app or site.
If you'd prefer to redirect to a mobile application, you can alternatively supply an application URI scheme.
This parameter is only used for cards and other redirect-based payment methods.
    setup_future_usage: Indicates that you intend to make future payments with this PaymentIntent's payment method.

If you provide a Customer with the PaymentIntent, you can use this parameter to [attach the payment method](/payments/save-during-payment) to the Customer after the PaymentIntent is confirmed and the customer completes any required actions. If you don't provide a Customer, you can still [attach](/api/payment_methods/attach) the payment method to a Customer after the transaction completes.

If the payment method is `card_present` and isn't a digital wallet, Stripe creates and attaches a [generated_card](/api/charges/object#charge_object-payment_method_details-card_present-generated_card) payment method representing the card to the Customer instead.

When processing card payments, Stripe uses `setup_future_usage` to help you comply with regional legislation and network rules, such as [SCA](/strong-customer-authentication).

If you've already set `setup_future_usage` and you're performing a request using a publishable key, you can only update the value from `on_session` to `off_session`.
    shipping: Shipping information for this PaymentIntent.
    use_stripe_sdk: Set to `true` when confirming server-side and using Stripe.js, iOS, or Android client-side SDKs to handle the next actions."""
		...


class Payment_Intents_Intent_Increment_Authorization(_StripeResourceGroup):
	def create(*, amount=None, application_fee_amount=None, description=None, expand=None, metadata=None, statement_descriptor=None, transfer_data=None):
		"""Increment an authorization

Parameters:
    amount: The updated total amount that you intend to collect from the cardholder. This amount must be greater than the currently authorized amount.
    application_fee_amount: The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. The amount of the application fee collected will be capped at the total amount captured. For more information, see the PaymentIntents [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts).
    description: An arbitrary string attached to the object. Often useful for displaying to users.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    statement_descriptor: Text that appears on the customer's statement as the statement descriptor for a non-card or card charge. This value overrides the account's default statement descriptor. For information about requirements, including the 22-character limit, see [the Statement Descriptor docs](https://docs.stripe.com/get-started/account/statement-descriptors).
    transfer_data: The parameters used to automatically create a transfer after the payment is captured.
Learn more about the [use case for connected accounts](https://stripe.com/docs/payments/connected-accounts)."""
		...


class Payment_Intents_Intent_Verify_Microdeposits(_StripeResourceGroup):
	def create(*, amounts=None, client_secret=None, descriptor_code=None, expand=None):
		"""Verify microdeposits on a PaymentIntent

Parameters:
    amounts: Two positive integers, in *cents*, equal to the values of the microdeposits sent to the bank account.
    client_secret: The client secret of the PaymentIntent.
    descriptor_code: A six-character code starting with SM present in the microdeposit sent to the bank account.
    expand: Specifies which fields in the response should be expanded."""
		...


class Payment_Links(_StripeResourceGroup):
	def fetch(*, active=None, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List all payment links

Parameters:
    active: Only return payment links that are active or inactive (e.g., pass `false` to list all inactive payment links).
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, after_completion=None, allow_promotion_codes=None, application_fee_amount=None, application_fee_percent=None, automatic_tax=None, billing_address_collection=None, consent_collection=None, currency=None, custom_fields=None, custom_text=None, customer_creation=None, expand=None, inactive_message=None, invoice_creation=None, line_items=None, metadata=None, on_behalf_of=None, optional_items=None, payment_intent_data=None, payment_method_collection=None, payment_method_types=None, phone_number_collection=None, restrictions=None, shipping_address_collection=None, shipping_options=None, submit_type=None, subscription_data=None, tax_id_collection=None, transfer_data=None):
		"""Create a payment link

Parameters:
    after_completion: Behavior after the purchase is complete.
    allow_promotion_codes: Enables user redeemable promotion codes.
    application_fee_amount: The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. Can only be applied when there are no line items with recurring prices.
    application_fee_percent: A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. There must be at least 1 line item with a recurring price to use this field.
    automatic_tax: Configuration for automatic tax collection.
    billing_address_collection: Configuration for collecting the customer's billing address. Defaults to `auto`.
    consent_collection: Configure fields to gather active consent from customers.
    currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies) and supported by each line item's price.
    custom_fields: Collect additional information from your customer using custom fields. Up to 3 fields are supported.
    custom_text: Display additional text for your customers using custom text.
    customer_creation: Configures whether [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link create a [Customer](https://stripe.com/docs/api/customers).
    expand: Specifies which fields in the response should be expanded.
    inactive_message: The custom message to be displayed to a customer when a payment link is no longer active.
    invoice_creation: Generate a post-purchase Invoice for one-time payments.
    line_items: The line items representing what is being sold. Each line item represents an item being sold. Up to 20 line items are supported.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. Metadata associated with this Payment Link will automatically be copied to [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link.
    on_behalf_of: The account on behalf of which to charge.
    optional_items: A list of optional items the customer can add to their order at checkout. Use this parameter to pass one-time or recurring [Prices](https://stripe.com/docs/api/prices).
There is a maximum of 10 optional items allowed on a payment link, and the existing limits on the number of line items allowed on a payment link apply to the combined number of line items and optional items.
There is a maximum of 20 combined line items and optional items.
    payment_intent_data: A subset of parameters to be passed to PaymentIntent creation for Checkout Sessions in `payment` mode.
    payment_method_collection: Specify whether Checkout should collect a payment method. When set to `if_required`, Checkout will not collect a payment method when the total due for the session is 0.This may occur if the Checkout Session includes a free trial or a discount.

Can only be set in `subscription` mode. Defaults to `always`.

If you'd like information on how to collect a payment method outside of Checkout, read the guide on [configuring subscriptions with a free trial](https://stripe.com/docs/payments/checkout/free-trials).
    payment_method_types: The list of payment method types that customers can use. If no value is passed, Stripe will dynamically show relevant payment methods from your [payment method settings](https://dashboard.stripe.com/settings/payment_methods) (20+ payment methods [supported](https://stripe.com/docs/payments/payment-methods/integration-options#payment-method-product-support)).
    phone_number_collection: Controls phone number collection settings during checkout.

We recommend that you review your privacy policy and check with your legal contacts.
    restrictions: Settings that restrict the usage of a payment link.
    shipping_address_collection: Configuration for collecting the customer's shipping address.
    shipping_options: The shipping rate options to apply to [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link.
    submit_type: Describes the type of transaction being performed in order to customize relevant text on the page, such as the submit button. Changing this value will also affect the hostname in the [url](https://stripe.com/docs/api/payment_links/payment_links/object#url) property (example: `donate.stripe.com`).
    subscription_data: When creating a subscription, the specified configuration data will be used. There must be at least one line item with a recurring price to use `subscription_data`.
    tax_id_collection: Controls tax ID collection during checkout.
    transfer_data: The account (if any) the payments will be attributed to for tax reporting, and where funds from each payment will be transferred to."""
		...


class Payment_Links_Payment_Link(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve payment link

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, active=None, after_completion=None, allow_promotion_codes=None, automatic_tax=None, billing_address_collection=None, custom_fields=None, custom_text=None, customer_creation=None, expand=None, inactive_message=None, invoice_creation=None, line_items=None, metadata=None, payment_intent_data=None, payment_method_collection=None, payment_method_types=None, phone_number_collection=None, restrictions=None, shipping_address_collection=None, submit_type=None, subscription_data=None, tax_id_collection=None):
		"""Update a payment link

Parameters:
    active: Whether the payment link's `url` is active. If `false`, customers visiting the URL will be shown a page saying that the link has been deactivated.
    after_completion: Behavior after the purchase is complete.
    allow_promotion_codes: Enables user redeemable promotion codes.
    automatic_tax: Configuration for automatic tax collection.
    billing_address_collection: Configuration for collecting the customer's billing address. Defaults to `auto`.
    custom_fields: Collect additional information from your customer using custom fields. Up to 3 fields are supported.
    custom_text: Display additional text for your customers using custom text.
    customer_creation: Configures whether [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link create a [Customer](https://stripe.com/docs/api/customers).
    expand: Specifies which fields in the response should be expanded.
    inactive_message: The custom message to be displayed to a customer when a payment link is no longer active.
    invoice_creation: Generate a post-purchase Invoice for one-time payments.
    line_items: The line items representing what is being sold. Each line item represents an item being sold. Up to 20 line items are supported.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. Metadata associated with this Payment Link will automatically be copied to [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link.
    payment_intent_data: A subset of parameters to be passed to PaymentIntent creation for Checkout Sessions in `payment` mode.
    payment_method_collection: Specify whether Checkout should collect a payment method. When set to `if_required`, Checkout will not collect a payment method when the total due for the session is 0.This may occur if the Checkout Session includes a free trial or a discount.

Can only be set in `subscription` mode. Defaults to `always`.

If you'd like information on how to collect a payment method outside of Checkout, read the guide on [configuring subscriptions with a free trial](https://stripe.com/docs/payments/checkout/free-trials).
    payment_method_types: The list of payment method types that customers can use. Pass an empty string to enable dynamic payment methods that use your [payment method settings](https://dashboard.stripe.com/settings/payment_methods).
    phone_number_collection: Controls phone number collection settings during checkout.

We recommend that you review your privacy policy and check with your legal contacts.
    restrictions: Settings that restrict the usage of a payment link.
    shipping_address_collection: Configuration for collecting the customer's shipping address.
    submit_type: Describes the type of transaction being performed in order to customize relevant text on the page, such as the submit button. Changing this value will also affect the hostname in the [url](https://stripe.com/docs/api/payment_links/payment_links/object#url) property (example: `donate.stripe.com`).
    subscription_data: When creating a subscription, the specified configuration data will be used. There must be at least one line item with a recurring price to use `subscription_data`.
    tax_id_collection: Controls tax ID collection during checkout."""
		...


class Payment_Links_Payment_Link_Line_Items(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None):
		"""Retrieve a payment link's line items

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...


class Payment_Method_Configurations(_StripeResourceGroup):
	def fetch(*, application=None, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List payment method configurations

Parameters:
    application: The Connect application to filter by.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, acss_debit=None, affirm=None, afterpay_clearpay=None, alipay=None, alma=None, amazon_pay=None, apple_pay=None, apple_pay_later=None, au_becs_debit=None, bacs_debit=None, bancontact=None, billie=None, blik=None, boleto=None, card=None, cartes_bancaires=None, cashapp=None, customer_balance=None, eps=None, expand=None, fpx=None, giropay=None, google_pay=None, grabpay=None, ideal=None, jcb=None, kakao_pay=None, klarna=None, konbini=None, kr_card=None, link=None, mobilepay=None, multibanco=None, name=None, naver_pay=None, nz_bank_account=None, oxxo=None, p24=None, parent=None, pay_by_bank=None, payco=None, paynow=None, paypal=None, pix=None, promptpay=None, revolut_pay=None, samsung_pay=None, satispay=None, sepa_debit=None, sofort=None, swish=None, twint=None, us_bank_account=None, wechat_pay=None, zip=None):
		"""Create a payment method configuration

Parameters:
    acss_debit: Canadian pre-authorized debit payments, check this [page](https://stripe.com/docs/payments/acss-debit) for more details like country availability.
    affirm: [Affirm](https://www.affirm.com/) gives your customers a way to split purchases over a series of payments. Depending on the purchase, they can pay with four interest-free payments (Split Pay) or pay over a longer term (Installments), which might include interest. Check this [page](https://stripe.com/docs/payments/affirm) for more details like country availability.
    afterpay_clearpay: Afterpay gives your customers a way to pay for purchases in installments, check this [page](https://stripe.com/docs/payments/afterpay-clearpay) for more details like country availability. Afterpay is particularly popular among businesses selling fashion, beauty, and sports products.
    alipay: Alipay is a digital wallet in China that has more than a billion active users worldwide. Alipay users can pay on the web or on a mobile device using login credentials or their Alipay app. Alipay has a low dispute rate and reduces fraud by authenticating payments using the customer's login credentials. Check this [page](https://stripe.com/docs/payments/alipay) for more details.
    alma: Alma is a Buy Now, Pay Later payment method that offers customers the ability to pay in 2, 3, or 4 installments.
    amazon_pay: Amazon Pay is a wallet payment method that lets your customers check out the same way as on Amazon.
    apple_pay: Stripe users can accept [Apple Pay](https://stripe.com/payments/apple-pay) in iOS applications in iOS 9 and later, and on the web in Safari starting with iOS 10 or macOS Sierra. There are no additional fees to process Apple Pay payments, and the [pricing](https://stripe.com/pricing) is the same as other card transactions. Check this [page](https://stripe.com/docs/apple-pay) for more details.
    apple_pay_later: Apple Pay Later, a payment method for customers to buy now and pay later, gives your customers a way to split purchases into four installments across six weeks.
    au_becs_debit: Stripe users in Australia can accept Bulk Electronic Clearing System (BECS) direct debit payments from customers with an Australian bank account. Check this [page](https://stripe.com/docs/payments/au-becs-debit) for more details.
    bacs_debit: Stripe users in the UK can accept Bacs Direct Debit payments from customers with a UK bank account, check this [page](https://stripe.com/docs/payments/payment-methods/bacs-debit) for more details.
    bancontact: Bancontact is the most popular online payment method in Belgium, with over 15 million cards in circulation. [Customers](https://stripe.com/docs/api/customers) use a Bancontact card or mobile app linked to a Belgian bank account to make online payments that are secure, guaranteed, and confirmed immediately. Check this [page](https://stripe.com/docs/payments/bancontact) for more details.
    billie: Billie is a [single-use](https://docs.stripe.com/payments/payment-methods#usage) payment method that offers businesses Pay by Invoice where they offer payment terms ranging from 7-120 days. Customers are redirected from your website or app, authorize the payment with Billie, then return to your website or app. You get [immediate notification](/payments/payment-methods#payment-notification) of whether the payment succeeded or failed.
    blik: BLIK is a [single use](https://stripe.com/docs/payments/payment-methods#usage) payment method that requires customers to authenticate their payments. When customers want to pay online using BLIK, they request a six-digit code from their banking application and enter it into the payment collection form. Check this [page](https://stripe.com/docs/payments/blik) for more details.
    boleto: Boleto is an official (regulated by the Central Bank of Brazil) payment method in Brazil. Check this [page](https://stripe.com/docs/payments/boleto) for more details.
    card: Cards are a popular way for consumers and businesses to pay online or in person. Stripe supports global and local card networks.
    cartes_bancaires: Cartes Bancaires is France's local card network. More than 95% of these cards are co-branded with either Visa or Mastercard, meaning you can process these cards over either Cartes Bancaires or the Visa or Mastercard networks. Check this [page](https://stripe.com/docs/payments/cartes-bancaires) for more details.
    cashapp: Cash App is a popular consumer app in the US that allows customers to bank, invest, send, and receive money using their digital wallet. Check this [page](https://stripe.com/docs/payments/cash-app-pay) for more details.
    customer_balance: Uses a customer’s [cash balance](https://stripe.com/docs/payments/customer-balance) for the payment. The cash balance can be funded via a bank transfer. Check this [page](https://stripe.com/docs/payments/bank-transfers) for more details.
    eps: EPS is an Austria-based payment method that allows customers to complete transactions online using their bank credentials. EPS is supported by all Austrian banks and is accepted by over 80% of Austrian online retailers. Check this [page](https://stripe.com/docs/payments/eps) for more details.
    expand: Specifies which fields in the response should be expanded.
    fpx: Financial Process Exchange (FPX) is a Malaysia-based payment method that allows customers to complete transactions online using their bank credentials. Bank Negara Malaysia (BNM), the Central Bank of Malaysia, and eleven other major Malaysian financial institutions are members of the PayNet Group, which owns and operates FPX. It is one of the most popular online payment methods in Malaysia, with nearly 90 million transactions in 2018 according to BNM. Check this [page](https://stripe.com/docs/payments/fpx) for more details.
    giropay: giropay is a German payment method based on online banking, introduced in 2006. It allows customers to complete transactions online using their online banking environment, with funds debited from their bank account. Depending on their bank, customers confirm payments on giropay using a second factor of authentication or a PIN. giropay accounts for 10% of online checkouts in Germany. Check this [page](https://stripe.com/docs/payments/giropay) for more details.
    google_pay: Google Pay allows customers to make payments in your app or website using any credit or debit card saved to their Google Account, including those from Google Play, YouTube, Chrome, or an Android device. Use the Google Pay API to request any credit or debit card stored in your customer's Google account. Check this [page](https://stripe.com/docs/google-pay) for more details.
    grabpay: GrabPay is a payment method developed by [Grab](https://www.grab.com/sg/consumer/finance/pay/). GrabPay is a digital wallet - customers maintain a balance in their wallets that they pay out with. Check this [page](https://stripe.com/docs/payments/grabpay) for more details.
    ideal: iDEAL is a Netherlands-based payment method that allows customers to complete transactions online using their bank credentials. All major Dutch banks are members of Currence, the scheme that operates iDEAL, making it the most popular online payment method in the Netherlands with a share of online transactions close to 55%. Check this [page](https://stripe.com/docs/payments/ideal) for more details.
    jcb: JCB is a credit card company based in Japan. JCB is currently available in Japan to businesses approved by JCB, and available to all businesses in Australia, Canada, Hong Kong, Japan, New Zealand, Singapore, Switzerland, United Kingdom, United States, and all countries in the European Economic Area except Iceland. Check this [page](https://support.stripe.com/questions/accepting-japan-credit-bureau-%28jcb%29-payments) for more details.
    kakao_pay: Kakao Pay is a popular local wallet available in South Korea.
    klarna: Klarna gives customers a range of [payment options](https://stripe.com/docs/payments/klarna#payment-options) during checkout. Available payment options vary depending on the customer's billing address and the transaction amount. These payment options make it convenient for customers to purchase items in all price ranges. Check this [page](https://stripe.com/docs/payments/klarna) for more details.
    konbini: Konbini allows customers in Japan to pay for bills and online purchases at convenience stores with cash. Check this [page](https://stripe.com/docs/payments/konbini) for more details.
    kr_card: Korean cards let users pay using locally issued cards from South Korea.
    link: [Link](https://stripe.com/docs/payments/link) is a payment method network. With Link, users save their payment details once, then reuse that information to pay with one click for any business on the network.
    mobilepay: MobilePay is a [single-use](https://stripe.com/docs/payments/payment-methods#usage) card wallet payment method used in Denmark and Finland. It allows customers to [authenticate and approve](https://stripe.com/docs/payments/payment-methods#customer-actions) payments using the MobilePay app. Check this [page](https://stripe.com/docs/payments/mobilepay) for more details.
    multibanco: Stripe users in Europe and the United States can accept Multibanco payments from customers in Portugal using [Sources](https://stripe.com/docs/sources)—a single integration path for creating payments using any supported method.
    name: Configuration name.
    naver_pay: Naver Pay is a popular local wallet available in South Korea.
    nz_bank_account: Stripe users in New Zealand can accept Bulk Electronic Clearing System (BECS) direct debit payments from customers with a New Zeland bank account. Check this [page](https://stripe.com/docs/payments/nz-bank-account) for more details.
    oxxo: OXXO is a Mexican chain of convenience stores with thousands of locations across Latin America and represents nearly 20% of online transactions in Mexico. OXXO allows customers to pay bills and online purchases in-store with cash. Check this [page](https://stripe.com/docs/payments/oxxo) for more details.
    p24: Przelewy24 is a Poland-based payment method aggregator that allows customers to complete transactions online using bank transfers and other methods. Bank transfers account for 30% of online payments in Poland and Przelewy24 provides a way for customers to pay with over 165 banks. Check this [page](https://stripe.com/docs/payments/p24) for more details.
    parent: Configuration's parent configuration. Specify to create a child configuration.
    pay_by_bank: Pay by bank is a redirect payment method backed by bank transfers. A customer is redirected to their bank to authorize a bank transfer for a given amount. This removes a lot of the error risks inherent in waiting for the customer to initiate a transfer themselves, and is less expensive than card payments.
    payco: PAYCO is a [single-use](https://docs.stripe.com/payments/payment-methods#usage local wallet available in South Korea.
    paynow: PayNow is a Singapore-based payment method that allows customers to make a payment using their preferred app from participating banks and participating non-bank financial institutions. Check this [page](https://stripe.com/docs/payments/paynow) for more details.
    paypal: PayPal, a digital wallet popular with customers in Europe, allows your customers worldwide to pay using their PayPal account. Check this [page](https://stripe.com/docs/payments/paypal) for more details.
    pix: Pix is a payment method popular in Brazil. When paying with Pix, customers authenticate and approve payments by scanning a QR code in their preferred banking app. Check this [page](https://docs.stripe.com/payments/pix) for more details.
    promptpay: PromptPay is a Thailand-based payment method that allows customers to make a payment using their preferred app from participating banks. Check this [page](https://stripe.com/docs/payments/promptpay) for more details.
    revolut_pay: Revolut Pay, developed by Revolut, a global finance app, is a digital wallet payment method. Revolut Pay uses the customer’s stored balance or cards to fund the payment, and offers the option for non-Revolut customers to save their details after their first purchase.
    samsung_pay: Samsung Pay is a [single-use](https://docs.stripe.com/payments/payment-methods#usage local wallet available in South Korea.
    satispay: Satispay is a [single-use](https://docs.stripe.com/payments/payment-methods#usage) payment method where customers are required to [authenticate](/payments/payment-methods#customer-actions) their payment. Customers pay by being redirected from your website or app, authorizing the payment with Satispay, then returning to your website or app. You get [immediate notification](/payments/payment-methods#payment-notification) of whether the payment succeeded or failed.
    sepa_debit: The [Single Euro Payments Area (SEPA)](https://en.wikipedia.org/wiki/Single_Euro_Payments_Area) is an initiative of the European Union to simplify payments within and across member countries. SEPA established and enforced banking standards to allow for the direct debiting of every EUR-denominated bank account within the SEPA region, check this [page](https://stripe.com/docs/payments/sepa-debit) for more details.
    sofort: Stripe users in Europe and the United States can use the [Payment Intents API](https://stripe.com/docs/payments/payment-intents)—a single integration path for creating payments using any supported method—to accept [Sofort](https://www.sofort.com/) payments from customers. Check this [page](https://stripe.com/docs/payments/sofort) for more details.
    swish: Swish is a [real-time](https://stripe.com/docs/payments/real-time) payment method popular in Sweden. It allows customers to [authenticate and approve](https://stripe.com/docs/payments/payment-methods#customer-actions) payments using the Swish mobile app and the Swedish BankID mobile app. Check this [page](https://stripe.com/docs/payments/swish) for more details.
    twint: Twint is a payment method popular in Switzerland. It allows customers to pay using their mobile phone. Check this [page](https://docs.stripe.com/payments/twint) for more details.
    us_bank_account: Stripe users in the United States can accept ACH direct debit payments from customers with a US bank account using the Automated Clearing House (ACH) payments system operated by Nacha. Check this [page](https://stripe.com/docs/payments/ach-direct-debit) for more details.
    wechat_pay: WeChat, owned by Tencent, is China's leading mobile app with over 1 billion monthly active users. Chinese consumers can use WeChat Pay to pay for goods and services inside of businesses' apps and websites. WeChat Pay users buy most frequently in gaming, e-commerce, travel, online education, and food/nutrition. Check this [page](https://stripe.com/docs/payments/wechat-pay) for more details.
    zip: Zip gives your customers a way to split purchases over a series of payments. Check this [page](https://stripe.com/docs/payments/zip) for more details like country availability."""
		...


class Payment_Method_Configurations_Configuration(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve payment method configuration

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, acss_debit=None, active=None, affirm=None, afterpay_clearpay=None, alipay=None, alma=None, amazon_pay=None, apple_pay=None, apple_pay_later=None, au_becs_debit=None, bacs_debit=None, bancontact=None, billie=None, blik=None, boleto=None, card=None, cartes_bancaires=None, cashapp=None, customer_balance=None, eps=None, expand=None, fpx=None, giropay=None, google_pay=None, grabpay=None, ideal=None, jcb=None, kakao_pay=None, klarna=None, konbini=None, kr_card=None, link=None, mobilepay=None, multibanco=None, name=None, naver_pay=None, nz_bank_account=None, oxxo=None, p24=None, pay_by_bank=None, payco=None, paynow=None, paypal=None, pix=None, promptpay=None, revolut_pay=None, samsung_pay=None, satispay=None, sepa_debit=None, sofort=None, swish=None, twint=None, us_bank_account=None, wechat_pay=None, zip=None):
		"""Update payment method configuration

Parameters:
    acss_debit: Canadian pre-authorized debit payments, check this [page](https://stripe.com/docs/payments/acss-debit) for more details like country availability.
    active: Whether the configuration can be used for new payments.
    affirm: [Affirm](https://www.affirm.com/) gives your customers a way to split purchases over a series of payments. Depending on the purchase, they can pay with four interest-free payments (Split Pay) or pay over a longer term (Installments), which might include interest. Check this [page](https://stripe.com/docs/payments/affirm) for more details like country availability.
    afterpay_clearpay: Afterpay gives your customers a way to pay for purchases in installments, check this [page](https://stripe.com/docs/payments/afterpay-clearpay) for more details like country availability. Afterpay is particularly popular among businesses selling fashion, beauty, and sports products.
    alipay: Alipay is a digital wallet in China that has more than a billion active users worldwide. Alipay users can pay on the web or on a mobile device using login credentials or their Alipay app. Alipay has a low dispute rate and reduces fraud by authenticating payments using the customer's login credentials. Check this [page](https://stripe.com/docs/payments/alipay) for more details.
    alma: Alma is a Buy Now, Pay Later payment method that offers customers the ability to pay in 2, 3, or 4 installments.
    amazon_pay: Amazon Pay is a wallet payment method that lets your customers check out the same way as on Amazon.
    apple_pay: Stripe users can accept [Apple Pay](https://stripe.com/payments/apple-pay) in iOS applications in iOS 9 and later, and on the web in Safari starting with iOS 10 or macOS Sierra. There are no additional fees to process Apple Pay payments, and the [pricing](https://stripe.com/pricing) is the same as other card transactions. Check this [page](https://stripe.com/docs/apple-pay) for more details.
    apple_pay_later: Apple Pay Later, a payment method for customers to buy now and pay later, gives your customers a way to split purchases into four installments across six weeks.
    au_becs_debit: Stripe users in Australia can accept Bulk Electronic Clearing System (BECS) direct debit payments from customers with an Australian bank account. Check this [page](https://stripe.com/docs/payments/au-becs-debit) for more details.
    bacs_debit: Stripe users in the UK can accept Bacs Direct Debit payments from customers with a UK bank account, check this [page](https://stripe.com/docs/payments/payment-methods/bacs-debit) for more details.
    bancontact: Bancontact is the most popular online payment method in Belgium, with over 15 million cards in circulation. [Customers](https://stripe.com/docs/api/customers) use a Bancontact card or mobile app linked to a Belgian bank account to make online payments that are secure, guaranteed, and confirmed immediately. Check this [page](https://stripe.com/docs/payments/bancontact) for more details.
    billie: Billie is a [single-use](https://docs.stripe.com/payments/payment-methods#usage) payment method that offers businesses Pay by Invoice where they offer payment terms ranging from 7-120 days. Customers are redirected from your website or app, authorize the payment with Billie, then return to your website or app. You get [immediate notification](/payments/payment-methods#payment-notification) of whether the payment succeeded or failed.
    blik: BLIK is a [single use](https://stripe.com/docs/payments/payment-methods#usage) payment method that requires customers to authenticate their payments. When customers want to pay online using BLIK, they request a six-digit code from their banking application and enter it into the payment collection form. Check this [page](https://stripe.com/docs/payments/blik) for more details.
    boleto: Boleto is an official (regulated by the Central Bank of Brazil) payment method in Brazil. Check this [page](https://stripe.com/docs/payments/boleto) for more details.
    card: Cards are a popular way for consumers and businesses to pay online or in person. Stripe supports global and local card networks.
    cartes_bancaires: Cartes Bancaires is France's local card network. More than 95% of these cards are co-branded with either Visa or Mastercard, meaning you can process these cards over either Cartes Bancaires or the Visa or Mastercard networks. Check this [page](https://stripe.com/docs/payments/cartes-bancaires) for more details.
    cashapp: Cash App is a popular consumer app in the US that allows customers to bank, invest, send, and receive money using their digital wallet. Check this [page](https://stripe.com/docs/payments/cash-app-pay) for more details.
    customer_balance: Uses a customer’s [cash balance](https://stripe.com/docs/payments/customer-balance) for the payment. The cash balance can be funded via a bank transfer. Check this [page](https://stripe.com/docs/payments/bank-transfers) for more details.
    eps: EPS is an Austria-based payment method that allows customers to complete transactions online using their bank credentials. EPS is supported by all Austrian banks and is accepted by over 80% of Austrian online retailers. Check this [page](https://stripe.com/docs/payments/eps) for more details.
    expand: Specifies which fields in the response should be expanded.
    fpx: Financial Process Exchange (FPX) is a Malaysia-based payment method that allows customers to complete transactions online using their bank credentials. Bank Negara Malaysia (BNM), the Central Bank of Malaysia, and eleven other major Malaysian financial institutions are members of the PayNet Group, which owns and operates FPX. It is one of the most popular online payment methods in Malaysia, with nearly 90 million transactions in 2018 according to BNM. Check this [page](https://stripe.com/docs/payments/fpx) for more details.
    giropay: giropay is a German payment method based on online banking, introduced in 2006. It allows customers to complete transactions online using their online banking environment, with funds debited from their bank account. Depending on their bank, customers confirm payments on giropay using a second factor of authentication or a PIN. giropay accounts for 10% of online checkouts in Germany. Check this [page](https://stripe.com/docs/payments/giropay) for more details.
    google_pay: Google Pay allows customers to make payments in your app or website using any credit or debit card saved to their Google Account, including those from Google Play, YouTube, Chrome, or an Android device. Use the Google Pay API to request any credit or debit card stored in your customer's Google account. Check this [page](https://stripe.com/docs/google-pay) for more details.
    grabpay: GrabPay is a payment method developed by [Grab](https://www.grab.com/sg/consumer/finance/pay/). GrabPay is a digital wallet - customers maintain a balance in their wallets that they pay out with. Check this [page](https://stripe.com/docs/payments/grabpay) for more details.
    ideal: iDEAL is a Netherlands-based payment method that allows customers to complete transactions online using their bank credentials. All major Dutch banks are members of Currence, the scheme that operates iDEAL, making it the most popular online payment method in the Netherlands with a share of online transactions close to 55%. Check this [page](https://stripe.com/docs/payments/ideal) for more details.
    jcb: JCB is a credit card company based in Japan. JCB is currently available in Japan to businesses approved by JCB, and available to all businesses in Australia, Canada, Hong Kong, Japan, New Zealand, Singapore, Switzerland, United Kingdom, United States, and all countries in the European Economic Area except Iceland. Check this [page](https://support.stripe.com/questions/accepting-japan-credit-bureau-%28jcb%29-payments) for more details.
    kakao_pay: Kakao Pay is a popular local wallet available in South Korea.
    klarna: Klarna gives customers a range of [payment options](https://stripe.com/docs/payments/klarna#payment-options) during checkout. Available payment options vary depending on the customer's billing address and the transaction amount. These payment options make it convenient for customers to purchase items in all price ranges. Check this [page](https://stripe.com/docs/payments/klarna) for more details.
    konbini: Konbini allows customers in Japan to pay for bills and online purchases at convenience stores with cash. Check this [page](https://stripe.com/docs/payments/konbini) for more details.
    kr_card: Korean cards let users pay using locally issued cards from South Korea.
    link: [Link](https://stripe.com/docs/payments/link) is a payment method network. With Link, users save their payment details once, then reuse that information to pay with one click for any business on the network.
    mobilepay: MobilePay is a [single-use](https://stripe.com/docs/payments/payment-methods#usage) card wallet payment method used in Denmark and Finland. It allows customers to [authenticate and approve](https://stripe.com/docs/payments/payment-methods#customer-actions) payments using the MobilePay app. Check this [page](https://stripe.com/docs/payments/mobilepay) for more details.
    multibanco: Stripe users in Europe and the United States can accept Multibanco payments from customers in Portugal using [Sources](https://stripe.com/docs/sources)—a single integration path for creating payments using any supported method.
    name: Configuration name.
    naver_pay: Naver Pay is a popular local wallet available in South Korea.
    nz_bank_account: Stripe users in New Zealand can accept Bulk Electronic Clearing System (BECS) direct debit payments from customers with a New Zeland bank account. Check this [page](https://stripe.com/docs/payments/nz-bank-account) for more details.
    oxxo: OXXO is a Mexican chain of convenience stores with thousands of locations across Latin America and represents nearly 20% of online transactions in Mexico. OXXO allows customers to pay bills and online purchases in-store with cash. Check this [page](https://stripe.com/docs/payments/oxxo) for more details.
    p24: Przelewy24 is a Poland-based payment method aggregator that allows customers to complete transactions online using bank transfers and other methods. Bank transfers account for 30% of online payments in Poland and Przelewy24 provides a way for customers to pay with over 165 banks. Check this [page](https://stripe.com/docs/payments/p24) for more details.
    pay_by_bank: Pay by bank is a redirect payment method backed by bank transfers. A customer is redirected to their bank to authorize a bank transfer for a given amount. This removes a lot of the error risks inherent in waiting for the customer to initiate a transfer themselves, and is less expensive than card payments.
    payco: PAYCO is a [single-use](https://docs.stripe.com/payments/payment-methods#usage local wallet available in South Korea.
    paynow: PayNow is a Singapore-based payment method that allows customers to make a payment using their preferred app from participating banks and participating non-bank financial institutions. Check this [page](https://stripe.com/docs/payments/paynow) for more details.
    paypal: PayPal, a digital wallet popular with customers in Europe, allows your customers worldwide to pay using their PayPal account. Check this [page](https://stripe.com/docs/payments/paypal) for more details.
    pix: Pix is a payment method popular in Brazil. When paying with Pix, customers authenticate and approve payments by scanning a QR code in their preferred banking app. Check this [page](https://docs.stripe.com/payments/pix) for more details.
    promptpay: PromptPay is a Thailand-based payment method that allows customers to make a payment using their preferred app from participating banks. Check this [page](https://stripe.com/docs/payments/promptpay) for more details.
    revolut_pay: Revolut Pay, developed by Revolut, a global finance app, is a digital wallet payment method. Revolut Pay uses the customer’s stored balance or cards to fund the payment, and offers the option for non-Revolut customers to save their details after their first purchase.
    samsung_pay: Samsung Pay is a [single-use](https://docs.stripe.com/payments/payment-methods#usage local wallet available in South Korea.
    satispay: Satispay is a [single-use](https://docs.stripe.com/payments/payment-methods#usage) payment method where customers are required to [authenticate](/payments/payment-methods#customer-actions) their payment. Customers pay by being redirected from your website or app, authorizing the payment with Satispay, then returning to your website or app. You get [immediate notification](/payments/payment-methods#payment-notification) of whether the payment succeeded or failed.
    sepa_debit: The [Single Euro Payments Area (SEPA)](https://en.wikipedia.org/wiki/Single_Euro_Payments_Area) is an initiative of the European Union to simplify payments within and across member countries. SEPA established and enforced banking standards to allow for the direct debiting of every EUR-denominated bank account within the SEPA region, check this [page](https://stripe.com/docs/payments/sepa-debit) for more details.
    sofort: Stripe users in Europe and the United States can use the [Payment Intents API](https://stripe.com/docs/payments/payment-intents)—a single integration path for creating payments using any supported method—to accept [Sofort](https://www.sofort.com/) payments from customers. Check this [page](https://stripe.com/docs/payments/sofort) for more details.
    swish: Swish is a [real-time](https://stripe.com/docs/payments/real-time) payment method popular in Sweden. It allows customers to [authenticate and approve](https://stripe.com/docs/payments/payment-methods#customer-actions) payments using the Swish mobile app and the Swedish BankID mobile app. Check this [page](https://stripe.com/docs/payments/swish) for more details.
    twint: Twint is a payment method popular in Switzerland. It allows customers to pay using their mobile phone. Check this [page](https://docs.stripe.com/payments/twint) for more details.
    us_bank_account: Stripe users in the United States can accept ACH direct debit payments from customers with a US bank account using the Automated Clearing House (ACH) payments system operated by Nacha. Check this [page](https://stripe.com/docs/payments/ach-direct-debit) for more details.
    wechat_pay: WeChat, owned by Tencent, is China's leading mobile app with over 1 billion monthly active users. Chinese consumers can use WeChat Pay to pay for goods and services inside of businesses' apps and websites. WeChat Pay users buy most frequently in gaming, e-commerce, travel, online education, and food/nutrition. Check this [page](https://stripe.com/docs/payments/wechat-pay) for more details.
    zip: Zip gives your customers a way to split purchases over a series of payments. Check this [page](https://stripe.com/docs/payments/zip) for more details like country availability."""
		...


class Payment_Method_Domains(_StripeResourceGroup):
	def fetch(*, domain_name=None, enabled=None, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List payment method domains

Parameters:
    domain_name: The domain name that this payment method domain object represents.
    enabled: Whether this payment method domain is enabled. If the domain is not enabled, payment methods will not appear in Elements or Embedded Checkout
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, domain_name=None, enabled=None, expand=None):
		"""Create a payment method domain

Parameters:
    domain_name: The domain name that this payment method domain object represents.
    enabled: Whether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements or Embedded Checkout.
    expand: Specifies which fields in the response should be expanded."""
		...


class Payment_Method_Domains_Payment_Method_Domain(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a payment method domain

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, enabled=None, expand=None):
		"""Update a payment method domain

Parameters:
    enabled: Whether this payment method domain is enabled. If the domain is not enabled, payment methods that require a payment method domain will not appear in Elements or Embedded Checkout.
    expand: Specifies which fields in the response should be expanded."""
		...


class Payment_Method_Domains_Payment_Method_Domain_Validate(_StripeResourceGroup):
	def create(*, expand=None):
		"""Validate an existing payment method domain

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Payment_Methods(_StripeResourceGroup):
	def fetch(*, customer=None, ending_before=None, expand=None, limit=None, starting_after=None, type=None):
		"""List PaymentMethods

Parameters:
    customer: The ID of the customer whose PaymentMethods will be retrieved.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    type: An optional filter on the list, based on the object `type` field. Without the filter, the list includes all current and future payment method types. If your integration expects only one type of payment method in the response, make sure to provide a type value in the request."""
		...
	def create(*, acss_debit=None, affirm=None, afterpay_clearpay=None, alipay=None, allow_redisplay=None, alma=None, amazon_pay=None, au_becs_debit=None, bacs_debit=None, bancontact=None, billie=None, billing_details=None, blik=None, boleto=None, card=None, cashapp=None, customer=None, customer_balance=None, eps=None, expand=None, fpx=None, giropay=None, grabpay=None, ideal=None, interac_present=None, kakao_pay=None, klarna=None, konbini=None, kr_card=None, link=None, metadata=None, mobilepay=None, multibanco=None, naver_pay=None, nz_bank_account=None, oxxo=None, p24=None, pay_by_bank=None, payco=None, payment_method=None, paynow=None, paypal=None, pix=None, promptpay=None, radar_options=None, revolut_pay=None, samsung_pay=None, satispay=None, sepa_debit=None, sofort=None, swish=None, twint=None, type=None, us_bank_account=None, wechat_pay=None, zip=None):
		"""Shares a PaymentMethod

Parameters:
    acss_debit: If this is an `acss_debit` PaymentMethod, this hash contains details about the ACSS Debit payment method.
    affirm: If this is an `affirm` PaymentMethod, this hash contains details about the Affirm payment method.
    afterpay_clearpay: If this is an `AfterpayClearpay` PaymentMethod, this hash contains details about the AfterpayClearpay payment method.
    alipay: If this is an `Alipay` PaymentMethod, this hash contains details about the Alipay payment method.
    allow_redisplay: This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to `unspecified`.
    alma: If this is a Alma PaymentMethod, this hash contains details about the Alma payment method.
    amazon_pay: If this is a AmazonPay PaymentMethod, this hash contains details about the AmazonPay payment method.
    au_becs_debit: If this is an `au_becs_debit` PaymentMethod, this hash contains details about the bank account.
    bacs_debit: If this is a `bacs_debit` PaymentMethod, this hash contains details about the Bacs Direct Debit bank account.
    bancontact: If this is a `bancontact` PaymentMethod, this hash contains details about the Bancontact payment method.
    billie: If this is a `billie` PaymentMethod, this hash contains details about the Billie payment method.
    billing_details: Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.
    blik: If this is a `blik` PaymentMethod, this hash contains details about the BLIK payment method.
    boleto: If this is a `boleto` PaymentMethod, this hash contains details about the Boleto payment method.
    card: If this is a `card` PaymentMethod, this hash contains the user's card details. For backwards compatibility, you can alternatively provide a Stripe token (e.g., for Apple Pay, Amex Express Checkout, or legacy Checkout) into the card hash with format `card: {token: "tok_visa"}`. When providing a card number, you must meet the requirements for [PCI compliance](https://stripe.com/docs/security#validating-pci-compliance). We strongly recommend using Stripe.js instead of interacting with this API directly.
    cashapp: If this is a `cashapp` PaymentMethod, this hash contains details about the Cash App Pay payment method.
    customer: The `Customer` to whom the original PaymentMethod is attached.
    customer_balance: If this is a `customer_balance` PaymentMethod, this hash contains details about the CustomerBalance payment method.
    eps: If this is an `eps` PaymentMethod, this hash contains details about the EPS payment method.
    expand: Specifies which fields in the response should be expanded.
    fpx: If this is an `fpx` PaymentMethod, this hash contains details about the FPX payment method.
    giropay: If this is a `giropay` PaymentMethod, this hash contains details about the Giropay payment method.
    grabpay: If this is a `grabpay` PaymentMethod, this hash contains details about the GrabPay payment method.
    ideal: If this is an `ideal` PaymentMethod, this hash contains details about the iDEAL payment method.
    interac_present: If this is an `interac_present` PaymentMethod, this hash contains details about the Interac Present payment method.
    kakao_pay: If this is a `kakao_pay` PaymentMethod, this hash contains details about the Kakao Pay payment method.
    klarna: If this is a `klarna` PaymentMethod, this hash contains details about the Klarna payment method.
    konbini: If this is a `konbini` PaymentMethod, this hash contains details about the Konbini payment method.
    kr_card: If this is a `kr_card` PaymentMethod, this hash contains details about the Korean Card payment method.
    link: If this is an `Link` PaymentMethod, this hash contains details about the Link payment method.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    mobilepay: If this is a `mobilepay` PaymentMethod, this hash contains details about the MobilePay payment method.
    multibanco: If this is a `multibanco` PaymentMethod, this hash contains details about the Multibanco payment method.
    naver_pay: If this is a `naver_pay` PaymentMethod, this hash contains details about the Naver Pay payment method.
    nz_bank_account: If this is an nz_bank_account PaymentMethod, this hash contains details about the nz_bank_account payment method.
    oxxo: If this is an `oxxo` PaymentMethod, this hash contains details about the OXXO payment method.
    p24: If this is a `p24` PaymentMethod, this hash contains details about the P24 payment method.
    pay_by_bank: If this is a `pay_by_bank` PaymentMethod, this hash contains details about the PayByBank payment method.
    payco: If this is a `payco` PaymentMethod, this hash contains details about the PAYCO payment method.
    payment_method: The PaymentMethod to share.
    paynow: If this is a `paynow` PaymentMethod, this hash contains details about the PayNow payment method.
    paypal: If this is a `paypal` PaymentMethod, this hash contains details about the PayPal payment method.
    pix: If this is a `pix` PaymentMethod, this hash contains details about the Pix payment method.
    promptpay: If this is a `promptpay` PaymentMethod, this hash contains details about the PromptPay payment method.
    radar_options: Options to configure Radar. See [Radar Session](https://stripe.com/docs/radar/radar-session) for more information.
    revolut_pay: If this is a `revolut_pay` PaymentMethod, this hash contains details about the Revolut Pay payment method.
    samsung_pay: If this is a `samsung_pay` PaymentMethod, this hash contains details about the SamsungPay payment method.
    satispay: If this is a `satispay` PaymentMethod, this hash contains details about the Satispay payment method.
    sepa_debit: If this is a `sepa_debit` PaymentMethod, this hash contains details about the SEPA debit bank account.
    sofort: If this is a `sofort` PaymentMethod, this hash contains details about the SOFORT payment method.
    swish: If this is a `swish` PaymentMethod, this hash contains details about the Swish payment method.
    twint: If this is a TWINT PaymentMethod, this hash contains details about the TWINT payment method.
    type: The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.
    us_bank_account: If this is an `us_bank_account` PaymentMethod, this hash contains details about the US bank account payment method.
    wechat_pay: If this is an `wechat_pay` PaymentMethod, this hash contains details about the wechat_pay payment method.
    zip: If this is a `zip` PaymentMethod, this hash contains details about the Zip payment method."""
		...


class Payment_Methods_Payment_Method(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a PaymentMethod

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, allow_redisplay=None, billing_details=None, card=None, expand=None, link=None, metadata=None, pay_by_bank=None, us_bank_account=None):
		"""Update a PaymentMethod

Parameters:
    allow_redisplay: This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to `unspecified`.
    billing_details: Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.
    card: If this is a `card` PaymentMethod, this hash contains the user's card details.
    expand: Specifies which fields in the response should be expanded.
    link: If this is an `Link` PaymentMethod, this hash contains details about the Link payment method.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    pay_by_bank: If this is a `pay_by_bank` PaymentMethod, this hash contains details about the PayByBank payment method.
    us_bank_account: If this is an `us_bank_account` PaymentMethod, this hash contains details about the US bank account payment method."""
		...


class Payment_Methods_Payment_Method_Attach(_StripeResourceGroup):
	def create(*, customer=None, expand=None):
		"""Attach a PaymentMethod to a Customer

Parameters:
    customer: The ID of the customer to which to attach the PaymentMethod.
    expand: Specifies which fields in the response should be expanded."""
		...


class Payment_Methods_Payment_Method_Detach(_StripeResourceGroup):
	def create(*, expand=None):
		"""Detach a PaymentMethod from a Customer

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Payouts(_StripeResourceGroup):
	def fetch(*, arrival_date=None, created=None, destination=None, ending_before=None, expand=None, limit=None, starting_after=None, status=None):
		"""List all payouts

Parameters:
    arrival_date: Only return payouts that are expected to arrive during the given date interval.
    created: Only return payouts that were created during the given date interval.
    destination: The ID of an external account - only return payouts sent to this external account.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    status: Only return payouts that have the given status: `pending`, `paid`, `failed`, or `canceled`."""
		...
	def create(*, amount=None, currency=None, description=None, destination=None, expand=None, metadata=None, method=None, source_type=None, statement_descriptor=None):
		"""Create a payout

Parameters:
    amount: A positive integer in cents representing how much to payout.
    currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    description: An arbitrary string attached to the object. Often useful for displaying to users.
    destination: The ID of a bank account or a card to send the payout to. If you don't provide a destination, we use the default external account for the specified currency.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    method: The method used to send this payout, which is `standard` or `instant`. We support `instant` for payouts to debit cards and bank accounts in certain countries. Learn more about [bank support for Instant Payouts](https://stripe.com/docs/payouts/instant-payouts-banks).
    source_type: The balance type of your Stripe balance to draw this payout from. Balances for different payment sources are kept separately. You can find the amounts with the Balances API. One of `bank_account`, `card`, or `fpx`.
    statement_descriptor: A string that displays on the recipient's bank or card statement (up to 22 characters). A `statement_descriptor` that's longer than 22 characters return an error. Most banks truncate this information and display it inconsistently. Some banks might not display it at all."""
		...


class Payouts_Payout(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a payout

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, expand=None, metadata=None):
		"""Update a payout

Parameters:
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."""
		...


class Payouts_Payout_Cancel(_StripeResourceGroup):
	def create(*, expand=None):
		"""Cancel a payout

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Payouts_Payout_Reverse(_StripeResourceGroup):
	def create(*, expand=None, metadata=None):
		"""Reverse a payout

Parameters:
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."""
		...


class Plans(_StripeResourceGroup):
	def fetch(*, active=None, created=None, ending_before=None, expand=None, limit=None, product=None, starting_after=None):
		"""List all plans

Parameters:
    active: Only return plans that are active or inactive (e.g., pass `false` to list all inactive plans).
    created: A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    product: Only return plans for the given product.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, active=None, amount=None, amount_decimal=None, billing_scheme=None, currency=None, expand=None, id=None, interval=None, interval_count=None, metadata=None, meter=None, nickname=None, product=None, tiers=None, tiers_mode=None, transform_usage=None, trial_period_days=None, usage_type=None):
		"""Create a plan

Parameters:
    active: Whether the plan is currently available for new subscriptions. Defaults to `true`.
    amount: A positive integer in cents (or local equivalent) (or 0 for a free plan) representing how much to charge on a recurring basis.
    amount_decimal: Same as `amount`, but accepts a decimal value with at most 12 decimal places. Only one of `amount` and `amount_decimal` can be set.
    billing_scheme: Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `amount`) will be charged per unit in `quantity` (for plans with `usage_type=licensed`), or per unit of total usage (for plans with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes.
    currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    expand: Specifies which fields in the response should be expanded.
    id: An identifier randomly generated by Stripe. Used to identify this plan when subscribing a customer. You can optionally override this ID, but the ID must be unique across all plans in your Stripe account. You can, however, use the same plan ID in both live and test modes.
    interval: Specifies billing frequency. Either `day`, `week`, `month` or `year`.
    interval_count: The number of intervals between subscription billings. For example, `interval=month` and `interval_count=3` bills every 3 months. Maximum of three years interval allowed (3 years, 36 months, or 156 weeks).
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    meter: The meter tracking the usage of a metered price
    nickname: A brief description of the plan, hidden from customers.
    product: 
    tiers: Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.
    tiers_mode: Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price, in `graduated` tiering pricing can successively change as the quantity grows.
    transform_usage: Apply a transformation to the reported usage or set quantity before computing the billed price. Cannot be combined with `tiers`.
    trial_period_days: Default number of trial days when subscribing a customer to this plan using [`trial_from_plan=true`](https://stripe.com/docs/api#create_subscription-trial_from_plan).
    usage_type: Configures how the quantity per period should be determined. Can be either `metered` or `licensed`. `licensed` automatically bills the `quantity` set when adding it to a subscription. `metered` aggregates the total usage based on usage records. Defaults to `licensed`."""
		...


class Plans_Plan(_StripeResourceGroup):
	def delete():
		"""Delete a plan"""
		...
	def fetch(*, expand=None):
		"""Retrieve a plan

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, active=None, expand=None, metadata=None, nickname=None, product=None, trial_period_days=None):
		"""Update a plan

Parameters:
    active: Whether the plan is currently available for new subscriptions.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    nickname: A brief description of the plan, hidden from customers.
    product: The product the plan belongs to. This cannot be changed once it has been used in a subscription or subscription schedule.
    trial_period_days: Default number of trial days when subscribing a customer to this plan using [`trial_from_plan=true`](https://stripe.com/docs/api#create_subscription-trial_from_plan)."""
		...


class Prices(_StripeResourceGroup):
	def fetch(*, active=None, created=None, currency=None, ending_before=None, expand=None, limit=None, lookup_keys=None, product=None, recurring=None, starting_after=None, type=None):
		"""List all prices

Parameters:
    active: Only return prices that are active or inactive (e.g., pass `false` to list all inactive prices).
    created: A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.
    currency: Only return prices for the given currency.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    lookup_keys: Only return the price with these lookup_keys, if any exist. You can specify up to 10 lookup_keys.
    product: Only return prices for the given product.
    recurring: Only return prices with these recurring fields.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    type: Only return prices of type `recurring` or `one_time`."""
		...
	def create(*, active=None, billing_scheme=None, currency=None, currency_options=None, custom_unit_amount=None, expand=None, lookup_key=None, metadata=None, nickname=None, product=None, product_data=None, recurring=None, tax_behavior=None, tiers=None, tiers_mode=None, transfer_lookup_key=None, transform_quantity=None, unit_amount=None, unit_amount_decimal=None):
		"""Create a price

Parameters:
    active: Whether the price can be used for new purchases. Defaults to `true`.
    billing_scheme: Describes how to compute the price per period. Either `per_unit` or `tiered`. `per_unit` indicates that the fixed amount (specified in `unit_amount` or `unit_amount_decimal`) will be charged per unit in `quantity` (for prices with `usage_type=licensed`), or per unit of total usage (for prices with `usage_type=metered`). `tiered` indicates that the unit pricing will be computed using a tiering strategy as defined using the `tiers` and `tiers_mode` attributes.
    currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    currency_options: Prices defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
    custom_unit_amount: When set, provides configuration for the amount to be adjusted by the customer during Checkout Sessions and Payment Links.
    expand: Specifies which fields in the response should be expanded.
    lookup_key: A lookup key used to retrieve prices dynamically from a static string. This may be up to 200 characters.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    nickname: A brief description of the price, hidden from customers.
    product: The ID of the [Product](https://docs.stripe.com/api/products) that this [Price](https://docs.stripe.com/api/prices) will belong to.
    product_data: These fields can be used to create a new product that this price will belong to.
    recurring: The recurring components of a price such as `interval` and `usage_type`.
    tax_behavior: Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
    tiers: Each element represents a pricing tier. This parameter requires `billing_scheme` to be set to `tiered`. See also the documentation for `billing_scheme`.
    tiers_mode: Defines if the tiering price should be `graduated` or `volume` based. In `volume`-based tiering, the maximum quantity within a period determines the per unit price, in `graduated` tiering pricing can successively change as the quantity grows.
    transfer_lookup_key: If set to true, will atomically remove the lookup key from the existing price, and assign it to this price.
    transform_quantity: Apply a transformation to the reported usage or set quantity before computing the billed price. Cannot be combined with `tiers`.
    unit_amount: A positive integer in cents (or local equivalent) (or 0 for a free price) representing how much to charge. One of `unit_amount`, `unit_amount_decimal`, or `custom_unit_amount` is required, unless `billing_scheme=tiered`.
    unit_amount_decimal: Same as `unit_amount`, but accepts a decimal value in cents (or local equivalent) with at most 12 decimal places. Only one of `unit_amount` and `unit_amount_decimal` can be set."""
		...


class Prices_Search(_StripeResourceGroup):
	def fetch(*, expand=None, limit=None, page=None, query=None):
		"""Search prices

Parameters:
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
    query: The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for prices](https://stripe.com/docs/search#query-fields-for-prices)."""
		...


class Prices_Price(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a price

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, active=None, currency_options=None, expand=None, lookup_key=None, metadata=None, nickname=None, tax_behavior=None, transfer_lookup_key=None):
		"""Update a price

Parameters:
    active: Whether the price can be used for new purchases. Defaults to `true`.
    currency_options: Prices defined in each available currency option. Each key must be a three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html) and a [supported currency](https://stripe.com/docs/currencies).
    expand: Specifies which fields in the response should be expanded.
    lookup_key: A lookup key used to retrieve prices dynamically from a static string. This may be up to 200 characters.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    nickname: A brief description of the price, hidden from customers.
    tax_behavior: Only required if a [default tax behavior](https://stripe.com/docs/tax/products-prices-tax-categories-tax-behavior#setting-a-default-tax-behavior-(recommended)) was not provided in the Stripe Tax settings. Specifies whether the price is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`. Once specified as either `inclusive` or `exclusive`, it cannot be changed.
    transfer_lookup_key: If set to true, will atomically remove the lookup key from the existing price, and assign it to this price."""
		...


class Products(_StripeResourceGroup):
	def fetch(*, active=None, created=None, ending_before=None, expand=None, ids=None, limit=None, shippable=None, starting_after=None, url=None):
		"""List all products

Parameters:
    active: Only return products that are active or inactive (e.g., pass `false` to list all inactive products).
    created: Only return products that were created during the given date interval.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    ids: Only return products with the given IDs. Cannot be used with [starting_after](https://stripe.com/docs/api#list_products-starting_after) or [ending_before](https://stripe.com/docs/api#list_products-ending_before).
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    shippable: Only return products that can be shipped (i.e., physical, not digital products).
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    url: Only return products with the given url."""
		...
	def create(*, active=None, default_price_data=None, description=None, expand=None, id=None, images=None, marketing_features=None, metadata=None, name=None, package_dimensions=None, shippable=None, statement_descriptor=None, tax_code=None, unit_label=None, url=None):
		"""Create a product

Parameters:
    active: Whether the product is currently available for purchase. Defaults to `true`.
    default_price_data: Data used to generate a new [Price](https://stripe.com/docs/api/prices) object. This Price will be set as the default price for this product.
    description: The product's description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.
    expand: Specifies which fields in the response should be expanded.
    id: An identifier will be randomly generated by Stripe. You can optionally override this ID, but the ID must be unique across all products in your Stripe account.
    images: A list of up to 8 URLs of images for this product, meant to be displayable to the customer.
    marketing_features: A list of up to 15 marketing features for this product. These are displayed in [pricing tables](https://stripe.com/docs/payments/checkout/pricing-table).
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    name: The product's name, meant to be displayable to the customer.
    package_dimensions: The dimensions of this product for shipping purposes.
    shippable: Whether this product is shipped (i.e., physical goods).
    statement_descriptor: An arbitrary string to be displayed on your customer's credit card or bank statement. While most banks display this information consistently, some may display it incorrectly or not at all.

This may be up to 22 characters. The statement description may not include `<`, `>`, `\`, `"`, `'` characters, and will appear on your customer's statement in capital letters. Non-ASCII characters are automatically stripped.
 It must contain at least one letter. Only used for subscription payments.
    tax_code: A [tax code](https://stripe.com/docs/tax/tax-categories) ID.
    unit_label: A label that represents units of this product. When set, this will be included in customers' receipts, invoices, Checkout, and the customer portal.
    url: A URL of a publicly-accessible webpage for this product."""
		...


class Products_Search(_StripeResourceGroup):
	def fetch(*, expand=None, limit=None, page=None, query=None):
		"""Search products

Parameters:
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
    query: The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for products](https://stripe.com/docs/search#query-fields-for-products)."""
		...


class Products_Id(_StripeResourceGroup):
	def delete():
		"""Delete a product"""
		...
	def fetch(*, expand=None):
		"""Retrieve a product

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, active=None, default_price=None, description=None, expand=None, images=None, marketing_features=None, metadata=None, name=None, package_dimensions=None, shippable=None, statement_descriptor=None, tax_code=None, unit_label=None, url=None):
		"""Update a product

Parameters:
    active: Whether the product is available for purchase.
    default_price: The ID of the [Price](https://stripe.com/docs/api/prices) object that is the default price for this product.
    description: The product's description, meant to be displayable to the customer. Use this field to optionally store a long form explanation of the product being sold for your own rendering purposes.
    expand: Specifies which fields in the response should be expanded.
    images: A list of up to 8 URLs of images for this product, meant to be displayable to the customer.
    marketing_features: A list of up to 15 marketing features for this product. These are displayed in [pricing tables](https://stripe.com/docs/payments/checkout/pricing-table).
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    name: The product's name, meant to be displayable to the customer.
    package_dimensions: The dimensions of this product for shipping purposes.
    shippable: Whether this product is shipped (i.e., physical goods).
    statement_descriptor: An arbitrary string to be displayed on your customer's credit card or bank statement. While most banks display this information consistently, some may display it incorrectly or not at all.

This may be up to 22 characters. The statement description may not include `<`, `>`, `\`, `"`, `'` characters, and will appear on your customer's statement in capital letters. Non-ASCII characters are automatically stripped.
 It must contain at least one letter. May only be set if `type=service`. Only used for subscription payments.
    tax_code: A [tax code](https://stripe.com/docs/tax/tax-categories) ID.
    unit_label: A label that represents units of this product. When set, this will be included in customers' receipts, invoices, Checkout, and the customer portal. May only be set if `type=service`.
    url: A URL of a publicly-accessible webpage for this product."""
		...


class Products_Product_Features(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List all features attached to a product

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, entitlement_feature=None, expand=None):
		"""Attach a feature to a product

Parameters:
    entitlement_feature: The ID of the [Feature](https://stripe.com/docs/api/entitlements/feature) object attached to this product.
    expand: Specifies which fields in the response should be expanded."""
		...


class Products_Product_Features_Id(_StripeResourceGroup):
	def delete():
		"""Remove a feature from a product"""
		...
	def fetch(*, expand=None):
		"""Retrieve a product_feature

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Promotion_Codes(_StripeResourceGroup):
	def fetch(*, active=None, code=None, coupon=None, created=None, customer=None, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List all promotion codes

Parameters:
    active: Filter promotion codes by whether they are active.
    code: Only return promotion codes that have this case-insensitive code.
    coupon: Only return promotion codes for this coupon.
    created: A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.
    customer: Only return promotion codes that are restricted to this customer.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, active=None, code=None, coupon=None, customer=None, expand=None, expires_at=None, max_redemptions=None, metadata=None, restrictions=None):
		"""Create a promotion code

Parameters:
    active: Whether the promotion code is currently active.
    code: The customer-facing code. Regardless of case, this code must be unique across all active promotion codes for a specific customer. Valid characters are lower case letters (a-z), upper case letters (A-Z), and digits (0-9).

If left blank, we will generate one automatically.
    coupon: The coupon for this promotion code.
    customer: The customer that this promotion code can be used by. If not set, the promotion code can be used by all customers.
    expand: Specifies which fields in the response should be expanded.
    expires_at: The timestamp at which this promotion code will expire. If the coupon has specified a `redeems_by`, then this value cannot be after the coupon's `redeems_by`.
    max_redemptions: A positive integer specifying the number of times the promotion code can be redeemed. If the coupon has specified a `max_redemptions`, then this value cannot be greater than the coupon's `max_redemptions`.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    restrictions: Settings that restrict the redemption of the promotion code."""
		...


class Promotion_Codes_Promotion_Code(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a promotion code

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, active=None, expand=None, metadata=None, restrictions=None):
		"""Update a promotion code

Parameters:
    active: Whether the promotion code is currently active. A promotion code can only be reactivated when the coupon is still valid and the promotion code is otherwise redeemable.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    restrictions: Settings that restrict the redemption of the promotion code."""
		...


class Quotes(_StripeResourceGroup):
	def fetch(*, customer=None, ending_before=None, expand=None, limit=None, starting_after=None, status=None, test_clock=None):
		"""List all quotes

Parameters:
    customer: The ID of the customer whose quotes will be retrieved.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    status: The status of the quote.
    test_clock: Provides a list of quotes that are associated with the specified test clock. The response will not include quotes with test clocks if this and the customer parameter is not set."""
		...
	def create(*, application_fee_amount=None, application_fee_percent=None, automatic_tax=None, collection_method=None, customer=None, default_tax_rates=None, description=None, discounts=None, expand=None, expires_at=None, footer=None, from_quote=None, header=None, invoice_settings=None, line_items=None, metadata=None, on_behalf_of=None, subscription_data=None, test_clock=None, transfer_data=None):
		"""Create a quote

Parameters:
    application_fee_amount: The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. There cannot be any line items with recurring prices when using this field.
    application_fee_percent: A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. There must be at least 1 line item with a recurring price to use this field.
    automatic_tax: Settings for automatic tax lookup for this quote and resulting invoices and subscriptions.
    collection_method: Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay invoices at the end of the subscription cycle or at invoice finalization using the default payment method attached to the subscription or customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`.
    customer: The customer for which this quote belongs to. A customer is required before finalizing the quote. Once specified, it cannot be changed.
    default_tax_rates: The tax rates that will apply to any line item that does not have `tax_rates` set.
    description: A description that will be displayed on the quote PDF. If no value is passed, the default description configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used.
    discounts: The discounts applied to the quote.
    expand: Specifies which fields in the response should be expanded.
    expires_at: A future timestamp on which the quote will be canceled if in `open` or `draft` status. Measured in seconds since the Unix epoch. If no value is passed, the default expiration date configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used.
    footer: A footer that will be displayed on the quote PDF. If no value is passed, the default footer configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used.
    from_quote: Clone an existing quote. The new quote will be created in `status=draft`. When using this parameter, you cannot specify any other parameters except for `expires_at`.
    header: A header that will be displayed on the quote PDF. If no value is passed, the default header configured in your [quote template settings](https://dashboard.stripe.com/settings/billing/quote) will be used.
    invoice_settings: All invoices will be billed using the specified settings.
    line_items: A list of line items the customer is being quoted for. Each line item includes information about the product, the quantity, and the resulting cost.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    on_behalf_of: The account on behalf of which to charge.
    subscription_data: When creating a subscription or subscription schedule, the specified configuration data will be used. There must be at least one line item with a recurring price for a subscription or subscription schedule to be created. A subscription schedule is created if `subscription_data[effective_date]` is present and in the future, otherwise a subscription is created.
    test_clock: ID of the test clock to attach to the quote.
    transfer_data: The data with which to automatically create a Transfer for each of the invoices."""
		...


class Quotes_Quote(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a quote

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, application_fee_amount=None, application_fee_percent=None, automatic_tax=None, collection_method=None, customer=None, default_tax_rates=None, description=None, discounts=None, expand=None, expires_at=None, footer=None, header=None, invoice_settings=None, line_items=None, metadata=None, on_behalf_of=None, subscription_data=None, transfer_data=None):
		"""Update a quote

Parameters:
    application_fee_amount: The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. There cannot be any line items with recurring prices when using this field.
    application_fee_percent: A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. There must be at least 1 line item with a recurring price to use this field.
    automatic_tax: Settings for automatic tax lookup for this quote and resulting invoices and subscriptions.
    collection_method: Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay invoices at the end of the subscription cycle or at invoice finalization using the default payment method attached to the subscription or customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`.
    customer: The customer for which this quote belongs to. A customer is required before finalizing the quote. Once specified, it cannot be changed.
    default_tax_rates: The tax rates that will apply to any line item that does not have `tax_rates` set.
    description: A description that will be displayed on the quote PDF.
    discounts: The discounts applied to the quote.
    expand: Specifies which fields in the response should be expanded.
    expires_at: A future timestamp on which the quote will be canceled if in `open` or `draft` status. Measured in seconds since the Unix epoch.
    footer: A footer that will be displayed on the quote PDF.
    header: A header that will be displayed on the quote PDF.
    invoice_settings: All invoices will be billed using the specified settings.
    line_items: A list of line items the customer is being quoted for. Each line item includes information about the product, the quantity, and the resulting cost.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    on_behalf_of: The account on behalf of which to charge.
    subscription_data: When creating a subscription or subscription schedule, the specified configuration data will be used. There must be at least one line item with a recurring price for a subscription or subscription schedule to be created. A subscription schedule is created if `subscription_data[effective_date]` is present and in the future, otherwise a subscription is created.
    transfer_data: The data with which to automatically create a Transfer for each of the invoices."""
		...


class Quotes_Quote_Accept(_StripeResourceGroup):
	def create(*, expand=None):
		"""Accept a quote

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Quotes_Quote_Cancel(_StripeResourceGroup):
	def create(*, expand=None):
		"""Cancel a quote

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Quotes_Quote_Computed_Upfront_Line_Items(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None):
		"""Retrieve a quote's upfront line items

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...


class Quotes_Quote_Finalize(_StripeResourceGroup):
	def create(*, expand=None, expires_at=None):
		"""Finalize a quote

Parameters:
    expand: Specifies which fields in the response should be expanded.
    expires_at: A future timestamp on which the quote will be canceled if in `open` or `draft` status. Measured in seconds since the Unix epoch."""
		...


class Quotes_Quote_Line_Items(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None):
		"""Retrieve a quote's line items

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...


class Quotes_Quote_Pdf(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Download quote PDF

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Radar_Early_Fraud_Warnings(_StripeResourceGroup):
	def fetch(*, charge=None, created=None, ending_before=None, expand=None, limit=None, payment_intent=None, starting_after=None):
		"""List all early fraud warnings

Parameters:
    charge: Only return early fraud warnings for the charge specified by this charge ID.
    created: Only return early fraud warnings that were created during the given date interval.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    payment_intent: Only return early fraud warnings for charges that were created by the PaymentIntent specified by this PaymentIntent ID.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...


class Radar_Early_Fraud_Warnings_Early_Fraud_Warning(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve an early fraud warning

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Radar_Value_List_Items(_StripeResourceGroup):
	def fetch(*, created=None, ending_before=None, expand=None, limit=None, starting_after=None, value=None, value_list=None):
		"""List all value list items

Parameters:
    created: Only return items that were created during the given date interval.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    value: Return items belonging to the parent list whose value matches the specified value (using an "is like" match).
    value_list: Identifier for the parent value list this item belongs to."""
		...
	def create(*, expand=None, value=None, value_list=None):
		"""Create a value list item

Parameters:
    expand: Specifies which fields in the response should be expanded.
    value: The value of the item (whose type must match the type of the parent value list).
    value_list: The identifier of the value list which the created item will be added to."""
		...


class Radar_Value_List_Items_Item(_StripeResourceGroup):
	def delete():
		"""Delete a value list item"""
		...
	def fetch(*, expand=None):
		"""Retrieve a value list item

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Radar_Value_Lists(_StripeResourceGroup):
	def fetch(*, alias=None, contains=None, created=None, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List all value lists

Parameters:
    alias: The alias used to reference the value list when writing rules.
    contains: A value contained within a value list - returns all value lists containing this value.
    created: Only return value lists that were created during the given date interval.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, alias=None, expand=None, item_type=None, metadata=None, name=None):
		"""Create a value list

Parameters:
    alias: The name of the value list for use in rules.
    expand: Specifies which fields in the response should be expanded.
    item_type: Type of the items in the value list. One of `card_fingerprint`, `us_bank_account_fingerprint`, `sepa_debit_fingerprint`, `card_bin`, `email`, `ip_address`, `country`, `string`, `case_sensitive_string`, or `customer_id`. Use `string` if the item type is unknown or mixed.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    name: The human-readable name of the value list."""
		...


class Radar_Value_Lists_Value_List(_StripeResourceGroup):
	def delete():
		"""Delete a value list"""
		...
	def fetch(*, expand=None):
		"""Retrieve a value list

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, alias=None, expand=None, metadata=None, name=None):
		"""Update a value list

Parameters:
    alias: The name of the value list for use in rules.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    name: The human-readable name of the value list."""
		...


class Refunds(_StripeResourceGroup):
	def fetch(*, charge=None, created=None, ending_before=None, expand=None, limit=None, payment_intent=None, starting_after=None):
		"""List all refunds

Parameters:
    charge: Only return refunds for the charge specified by this charge ID.
    created: Only return refunds that were created during the given date interval.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    payment_intent: Only return refunds for the PaymentIntent specified by this ID.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, amount=None, charge=None, currency=None, customer=None, expand=None, instructions_email=None, metadata=None, origin=None, payment_intent=None, reason=None, refund_application_fee=None, reverse_transfer=None):
		"""Create customer balance refund

Parameters:
    amount: 
    charge: The identifier of the charge to refund.
    currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    customer: Customer whose customer balance to refund from.
    expand: Specifies which fields in the response should be expanded.
    instructions_email: For payment methods without native refund support (e.g., Konbini, PromptPay), use this email from the customer to receive refund instructions.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    origin: Origin of the refund
    payment_intent: The identifier of the PaymentIntent to refund.
    reason: String indicating the reason for the refund. If set, possible values are `duplicate`, `fraudulent`, and `requested_by_customer`. If you believe the charge to be fraudulent, specifying `fraudulent` as the reason will add the associated card and email to your [block lists](https://stripe.com/docs/radar/lists), and will also help us improve our fraud detection algorithms.
    refund_application_fee: Boolean indicating whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded. An application fee can be refunded only by the application that created the charge.
    reverse_transfer: Boolean indicating whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount).<br><br>A transfer can be reversed only by the application that created the charge."""
		...


class Refunds_Refund(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a refund

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, expand=None, metadata=None):
		"""Update a refund

Parameters:
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."""
		...


class Refunds_Refund_Cancel(_StripeResourceGroup):
	def create(*, expand=None):
		"""Cancel a refund

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Reporting_Report_Runs(_StripeResourceGroup):
	def fetch(*, created=None, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List all Report Runs

Parameters:
    created: Only return Report Runs that were created during the given date interval.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, expand=None, parameters=None, report_type=None):
		"""Create a Report Run

Parameters:
    expand: Specifies which fields in the response should be expanded.
    parameters: Parameters specifying how the report should be run. Different Report Types have different required and optional parameters, listed in the [API Access to Reports](https://stripe.com/docs/reporting/statements/api) documentation.
    report_type: The ID of the [report type](https://stripe.com/docs/reporting/statements/api#report-types) to run, such as `"balance.summary.1"`."""
		...


class Reporting_Report_Runs_Report_Run(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a Report Run

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Reporting_Report_Types(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""List all Report Types

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Reporting_Report_Types_Report_Type(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a Report Type

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Reviews(_StripeResourceGroup):
	def fetch(*, created=None, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List all open reviews

Parameters:
    created: Only return reviews that were created during the given date interval.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...


class Reviews_Review(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a review

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Reviews_Review_Approve(_StripeResourceGroup):
	def create(*, expand=None):
		"""Approve a review

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Setup_Attempts(_StripeResourceGroup):
	def fetch(*, created=None, ending_before=None, expand=None, limit=None, setup_intent=None, starting_after=None):
		"""List all SetupAttempts

Parameters:
    created: A filter on the list, based on the object `created` field. The value
can be a string with an integer Unix timestamp or a
dictionary with a number of different query options.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    setup_intent: Only return SetupAttempts created by the SetupIntent specified by
this ID.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...


class Setup_Intents(_StripeResourceGroup):
	def fetch(*, attach_to_self=None, created=None, customer=None, ending_before=None, expand=None, limit=None, payment_method=None, starting_after=None):
		"""List all SetupIntents

Parameters:
    attach_to_self: If present, the SetupIntent's payment method will be attached to the in-context Stripe Account.

It can only be used for this Stripe Account’s own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer.
    created: A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.
    customer: Only return SetupIntents for the customer specified by this customer ID.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    payment_method: Only return SetupIntents that associate with the specified payment method.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, attach_to_self=None, automatic_payment_methods=None, confirm=None, confirmation_token=None, customer=None, description=None, expand=None, flow_directions=None, mandate_data=None, metadata=None, on_behalf_of=None, payment_method=None, payment_method_configuration=None, payment_method_data=None, payment_method_options=None, payment_method_types=None, return_url=None, single_use=None, usage=None, use_stripe_sdk=None):
		"""Create a SetupIntent

Parameters:
    attach_to_self: If present, the SetupIntent's payment method will be attached to the in-context Stripe Account.

It can only be used for this Stripe Account’s own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer.
    automatic_payment_methods: When you enable this parameter, this SetupIntent accepts payment methods that you enable in the Dashboard and that are compatible with its other parameters.
    confirm: Set to `true` to attempt to confirm this SetupIntent immediately. This parameter defaults to `false`. If a card is the attached payment method, you can provide a `return_url` in case further authentication is necessary.
    confirmation_token: ID of the ConfirmationToken used to confirm this SetupIntent.

If the provided ConfirmationToken contains properties that are also being provided in this request, such as `payment_method`, then the values in this request will take precedence.
    customer: ID of the Customer this SetupIntent belongs to, if one exists.

If present, the SetupIntent's payment method will be attached to the Customer on successful setup. Payment methods attached to other Customers cannot be used with this SetupIntent.
    description: An arbitrary string attached to the object. Often useful for displaying to users.
    expand: Specifies which fields in the response should be expanded.
    flow_directions: Indicates the directions of money movement for which this payment method is intended to be used.

Include `inbound` if you intend to use the payment method as the origin to pull funds from. Include `outbound` if you intend to use the payment method as the destination to send funds to. You can include both if you intend to use the payment method for both purposes.
    mandate_data: This hash contains details about the mandate to create. This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/setup_intents/create#create_setup_intent-confirm).
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    on_behalf_of: The Stripe account ID created for this SetupIntent.
    payment_method: ID of the payment method (a PaymentMethod, Card, or saved Source object) to attach to this SetupIntent.
    payment_method_configuration: The ID of the [payment method configuration](https://stripe.com/docs/api/payment_method_configurations) to use with this SetupIntent.
    payment_method_data: When included, this hash creates a PaymentMethod that is set as the [`payment_method`](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-payment_method)
value in the SetupIntent.
    payment_method_options: Payment method-specific configuration for this SetupIntent.
    payment_method_types: The list of payment method types (for example, card) that this SetupIntent can use. If you don't provide this, Stripe will dynamically show relevant payment methods from your [payment method settings](https://dashboard.stripe.com/settings/payment_methods).
    return_url: The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method's app or site. To redirect to a mobile application, you can alternatively supply an application URI scheme. This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/setup_intents/create#create_setup_intent-confirm).
    single_use: If you populate this hash, this SetupIntent generates a `single_use` mandate after successful completion.

Single-use mandates are only valid for the following payment methods: `acss_debit`, `alipay`, `au_becs_debit`, `bacs_debit`, `bancontact`, `boleto`, `ideal`, `link`, `sepa_debit`, and `us_bank_account`.
    usage: Indicates how the payment method is intended to be used in the future. If not provided, this value defaults to `off_session`.
    use_stripe_sdk: Set to `true` when confirming server-side and using Stripe.js, iOS, or Android client-side SDKs to handle the next actions."""
		...


class Setup_Intents_Intent(_StripeResourceGroup):
	def fetch(*, client_secret=None, expand=None):
		"""Retrieve a SetupIntent

Parameters:
    client_secret: The client secret of the SetupIntent. We require this string if you use a publishable key to retrieve the SetupIntent.
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, attach_to_self=None, customer=None, description=None, expand=None, flow_directions=None, metadata=None, payment_method=None, payment_method_configuration=None, payment_method_data=None, payment_method_options=None, payment_method_types=None):
		"""Update a SetupIntent

Parameters:
    attach_to_self: If present, the SetupIntent's payment method will be attached to the in-context Stripe Account.

It can only be used for this Stripe Account’s own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer.
    customer: ID of the Customer this SetupIntent belongs to, if one exists.

If present, the SetupIntent's payment method will be attached to the Customer on successful setup. Payment methods attached to other Customers cannot be used with this SetupIntent.
    description: An arbitrary string attached to the object. Often useful for displaying to users.
    expand: Specifies which fields in the response should be expanded.
    flow_directions: Indicates the directions of money movement for which this payment method is intended to be used.

Include `inbound` if you intend to use the payment method as the origin to pull funds from. Include `outbound` if you intend to use the payment method as the destination to send funds to. You can include both if you intend to use the payment method for both purposes.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    payment_method: ID of the payment method (a PaymentMethod, Card, or saved Source object) to attach to this SetupIntent. To unset this field to null, pass in an empty string.
    payment_method_configuration: The ID of the [payment method configuration](https://stripe.com/docs/api/payment_method_configurations) to use with this SetupIntent.
    payment_method_data: When included, this hash creates a PaymentMethod that is set as the [`payment_method`](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-payment_method)
value in the SetupIntent.
    payment_method_options: Payment method-specific configuration for this SetupIntent.
    payment_method_types: The list of payment method types (for example, card) that this SetupIntent can set up. If you don't provide this, Stripe will dynamically show relevant payment methods from your [payment method settings](https://dashboard.stripe.com/settings/payment_methods)."""
		...


class Setup_Intents_Intent_Cancel(_StripeResourceGroup):
	def create(*, cancellation_reason=None, expand=None):
		"""Cancel a SetupIntent

Parameters:
    cancellation_reason: Reason for canceling this SetupIntent. Possible values are: `abandoned`, `requested_by_customer`, or `duplicate`
    expand: Specifies which fields in the response should be expanded."""
		...


class Setup_Intents_Intent_Confirm(_StripeResourceGroup):
	def create(*, client_secret=None, confirmation_token=None, expand=None, mandate_data=None, payment_method=None, payment_method_data=None, payment_method_options=None, return_url=None, use_stripe_sdk=None):
		"""Confirm a SetupIntent

Parameters:
    client_secret: The client secret of the SetupIntent.
    confirmation_token: ID of the ConfirmationToken used to confirm this SetupIntent.

If the provided ConfirmationToken contains properties that are also being provided in this request, such as `payment_method`, then the values in this request will take precedence.
    expand: Specifies which fields in the response should be expanded.
    mandate_data: 
    payment_method: ID of the payment method (a PaymentMethod, Card, or saved Source object) to attach to this SetupIntent.
    payment_method_data: When included, this hash creates a PaymentMethod that is set as the [`payment_method`](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-payment_method)
value in the SetupIntent.
    payment_method_options: Payment method-specific configuration for this SetupIntent.
    return_url: The URL to redirect your customer back to after they authenticate on the payment method's app or site.
If you'd prefer to redirect to a mobile application, you can alternatively supply an application URI scheme.
This parameter is only used for cards and other redirect-based payment methods.
    use_stripe_sdk: Set to `true` when confirming server-side and using Stripe.js, iOS, or Android client-side SDKs to handle the next actions."""
		...


class Setup_Intents_Intent_Verify_Microdeposits(_StripeResourceGroup):
	def create(*, amounts=None, client_secret=None, descriptor_code=None, expand=None):
		"""Verify microdeposits on a SetupIntent

Parameters:
    amounts: Two positive integers, in *cents*, equal to the values of the microdeposits sent to the bank account.
    client_secret: The client secret of the SetupIntent.
    descriptor_code: A six-character code starting with SM present in the microdeposit sent to the bank account.
    expand: Specifies which fields in the response should be expanded."""
		...


class Shipping_Rates(_StripeResourceGroup):
	def fetch(*, active=None, created=None, currency=None, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List all shipping rates

Parameters:
    active: Only return shipping rates that are active or inactive.
    created: A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.
    currency: Only return shipping rates for the given currency.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, delivery_estimate=None, display_name=None, expand=None, fixed_amount=None, metadata=None, tax_behavior=None, tax_code=None, type=None):
		"""Create a shipping rate

Parameters:
    delivery_estimate: The estimated range for how long shipping will take, meant to be displayable to the customer. This will appear on CheckoutSessions.
    display_name: The name of the shipping rate, meant to be displayable to the customer. This will appear on CheckoutSessions.
    expand: Specifies which fields in the response should be expanded.
    fixed_amount: Describes a fixed amount to charge for shipping. Must be present if type is `fixed_amount`.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    tax_behavior: Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`.
    tax_code: A [tax code](https://stripe.com/docs/tax/tax-categories) ID. The Shipping tax code is `txcd_92010001`.
    type: The type of calculation to use on the shipping rate."""
		...


class Shipping_Rates_Shipping_Rate_Token(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a shipping rate

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, active=None, expand=None, fixed_amount=None, metadata=None, tax_behavior=None):
		"""Update a shipping rate

Parameters:
    active: Whether the shipping rate can be used for new purchases. Defaults to `true`.
    expand: Specifies which fields in the response should be expanded.
    fixed_amount: Describes a fixed amount to charge for shipping. Must be present if type is `fixed_amount`.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    tax_behavior: Specifies whether the rate is considered inclusive of taxes or exclusive of taxes. One of `inclusive`, `exclusive`, or `unspecified`."""
		...


class Sigma_Saved_Queries_Id(_StripeResourceGroup):
	def create(*, expand=None, name=None, sql=None):
		"""Update an existing Sigma Query

Parameters:
    expand: Specifies which fields in the response should be expanded.
    name: The name of the query to update.
    sql: The sql statement to update the specified query statement with. This should be a valid Trino SQL statement that can be run in Sigma."""
		...


class Sigma_Scheduled_Query_Runs(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List all scheduled query runs

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...


class Sigma_Scheduled_Query_Runs_Scheduled_Query_Run(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a scheduled query run

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Sources(_StripeResourceGroup):
	def create(*, amount=None, currency=None, customer=None, expand=None, flow=None, mandate=None, metadata=None, original_source=None, owner=None, receiver=None, redirect=None, source_order=None, statement_descriptor=None, token=None, type=None, usage=None):
		"""Shares a source

Parameters:
    amount: Amount associated with the source. This is the amount for which the source will be chargeable once ready. Required for `single_use` sources. Not supported for `receiver` type sources, where charge amount may not be specified until funds land.
    currency: Three-letter [ISO code for the currency](https://stripe.com/docs/currencies) associated with the source. This is the currency for which the source will be chargeable once ready.
    customer: The `Customer` to whom the original source is attached to. Must be set when the original source is not a `Source` (e.g., `Card`).
    expand: Specifies which fields in the response should be expanded.
    flow: The authentication `flow` of the source to create. `flow` is one of `redirect`, `receiver`, `code_verification`, `none`. It is generally inferred unless a type supports multiple flows.
    mandate: Information about a mandate possibility attached to a source object (generally for bank debits) as well as its acceptance status.
    metadata: 
    original_source: The source to share.
    owner: Information about the owner of the payment instrument that may be used or required by particular source types.
    receiver: Optional parameters for the receiver flow. Can be set only if the source is a receiver (`flow` is `receiver`).
    redirect: Parameters required for the redirect flow. Required if the source is authenticated by a redirect (`flow` is `redirect`).
    source_order: Information about the items and shipping associated with the source. Required for transactional credit (for example Klarna) sources before you can charge it.
    statement_descriptor: An arbitrary string to be displayed on your customer's statement. As an example, if your website is `RunClub` and the item you're charging for is a race ticket, you may want to specify a `statement_descriptor` of `RunClub 5K race ticket.` While many payment types will display this information, some may not display it at all.
    token: An optional token used to create the source. When passed, token properties will override source parameters.
    type: The `type` of the source to create. Required unless `customer` and `original_source` are specified (see the [Cloning card Sources](https://stripe.com/docs/sources/connect#cloning-card-sources) guide)
    usage: """
		...


class Sources_Source(_StripeResourceGroup):
	def fetch(*, client_secret=None, expand=None):
		"""Retrieve a source

Parameters:
    client_secret: The client secret of the source. Required if a publishable key is used to retrieve the source.
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, amount=None, expand=None, mandate=None, metadata=None, owner=None, source_order=None):
		"""Update a source

Parameters:
    amount: Amount associated with the source.
    expand: Specifies which fields in the response should be expanded.
    mandate: Information about a mandate possibility attached to a source object (generally for bank debits) as well as its acceptance status.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    owner: Information about the owner of the payment instrument that may be used or required by particular source types.
    source_order: Information about the items and shipping associated with the source. Required for transactional credit (for example Klarna) sources before you can charge it."""
		...


class Sources_Source_Mandate_Notifications_Mandate_Notification(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a Source MandateNotification

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Sources_Source_Source_Transactions(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None):
		"""

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...


class Sources_Source_Source_Transactions_Source_Transaction(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a source transaction

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Sources_Source_Verify(_StripeResourceGroup):
	def create(*, expand=None, values=None):
		"""

Parameters:
    expand: Specifies which fields in the response should be expanded.
    values: The values needed to verify the source."""
		...


class Subscription_Items(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None, subscription=None):
		"""List all subscription items

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    subscription: The ID of the subscription whose items will be retrieved."""
		...
	def create(*, billing_thresholds=None, discounts=None, expand=None, metadata=None, payment_behavior=None, price=None, price_data=None, proration_behavior=None, proration_date=None, quantity=None, subscription=None, tax_rates=None):
		"""Create a subscription item

Parameters:
    billing_thresholds: Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. Pass an empty string to remove previously-defined thresholds.
    discounts: The coupons to redeem into discounts for the subscription item.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    payment_behavior: Use `allow_incomplete` to transition the subscription to `status=past_due` if a payment is required but cannot be paid. This allows you to manage scenarios where additional user actions are needed to pay a subscription's invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication) for Billing to learn more. This is the default behavior.

Use `default_incomplete` to transition the subscription to `status=past_due` when payment is required and await explicit confirmation of the invoice's payment intent. This allows simpler management of scenarios where additional user actions are needed to pay a subscription’s invoice. Such as failed payments, [SCA regulation](https://stripe.com/docs/billing/migration/strong-customer-authentication), or collecting a mandate for a bank debit payment method.

Use `pending_if_incomplete` to update the subscription using [pending updates](https://stripe.com/docs/billing/subscriptions/pending-updates). When you use `pending_if_incomplete` you can only pass the parameters [supported by pending updates](https://stripe.com/docs/billing/pending-updates-reference#supported-attributes).

Use `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription's invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not update the subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://stripe.com/docs/upgrades#2019-03-14) to learn more.
    price: The ID of the price object.
    price_data: Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline.
    proration_behavior: Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`.
    proration_date: If set, the proration will be calculated as though the subscription was updated at the given time. This can be used to apply the same proration that was previewed with the [upcoming invoice](https://stripe.com/docs/api#retrieve_customer_invoice) endpoint.
    quantity: The quantity you'd like to apply to the subscription item you're creating.
    subscription: The identifier of the subscription to modify.
    tax_rates: A list of [Tax Rate](https://stripe.com/docs/api/tax_rates) ids. These Tax Rates will override the [`default_tax_rates`](https://stripe.com/docs/api/subscriptions/create#create_subscription-default_tax_rates) on the Subscription. When updating, pass an empty string to remove previously-defined tax rates."""
		...


class Subscription_Items_Item(_StripeResourceGroup):
	def delete(*, clear_usage=None, proration_behavior=None, proration_date=None):
		"""Delete a subscription item

Parameters:
    clear_usage: Delete all usage for the given subscription item. Allowed only when the current plan's `usage_type` is `metered`.
    proration_behavior: Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`.
    proration_date: If set, the proration will be calculated as though the subscription was updated at the given time. This can be used to apply the same proration that was previewed with the [upcoming invoice](https://stripe.com/docs/api#retrieve_customer_invoice) endpoint."""
		...
	def fetch(*, expand=None):
		"""Retrieve a subscription item

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, billing_thresholds=None, discounts=None, expand=None, metadata=None, off_session=None, payment_behavior=None, price=None, price_data=None, proration_behavior=None, proration_date=None, quantity=None, tax_rates=None):
		"""Update a subscription item

Parameters:
    billing_thresholds: Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. Pass an empty string to remove previously-defined thresholds.
    discounts: The coupons to redeem into discounts for the subscription item.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    off_session: Indicates if a customer is on or off-session while an invoice payment is attempted. Defaults to `false` (on-session).
    payment_behavior: Use `allow_incomplete` to transition the subscription to `status=past_due` if a payment is required but cannot be paid. This allows you to manage scenarios where additional user actions are needed to pay a subscription's invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication) for Billing to learn more. This is the default behavior.

Use `default_incomplete` to transition the subscription to `status=past_due` when payment is required and await explicit confirmation of the invoice's payment intent. This allows simpler management of scenarios where additional user actions are needed to pay a subscription’s invoice. Such as failed payments, [SCA regulation](https://stripe.com/docs/billing/migration/strong-customer-authentication), or collecting a mandate for a bank debit payment method.

Use `pending_if_incomplete` to update the subscription using [pending updates](https://stripe.com/docs/billing/subscriptions/pending-updates). When you use `pending_if_incomplete` you can only pass the parameters [supported by pending updates](https://stripe.com/docs/billing/pending-updates-reference#supported-attributes).

Use `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription's invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not update the subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://stripe.com/docs/upgrades#2019-03-14) to learn more.
    price: The ID of the price object. One of `price` or `price_data` is required. When changing a subscription item's price, `quantity` is set to 1 unless a `quantity` parameter is provided.
    price_data: Data used to generate a new [Price](https://stripe.com/docs/api/prices) object inline. One of `price` or `price_data` is required.
    proration_behavior: Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`.
    proration_date: If set, the proration will be calculated as though the subscription was updated at the given time. This can be used to apply the same proration that was previewed with the [upcoming invoice](https://stripe.com/docs/api#retrieve_customer_invoice) endpoint.
    quantity: The quantity you'd like to apply to the subscription item you're creating.
    tax_rates: A list of [Tax Rate](https://stripe.com/docs/api/tax_rates) ids. These Tax Rates will override the [`default_tax_rates`](https://stripe.com/docs/api/subscriptions/create#create_subscription-default_tax_rates) on the Subscription. When updating, pass an empty string to remove previously-defined tax rates."""
		...


class Subscription_Schedules(_StripeResourceGroup):
	def fetch(*, canceled_at=None, completed_at=None, created=None, customer=None, ending_before=None, expand=None, limit=None, released_at=None, scheduled=None, starting_after=None):
		"""List all schedules

Parameters:
    canceled_at: Only return subscription schedules that were created canceled the given date interval.
    completed_at: Only return subscription schedules that completed during the given date interval.
    created: Only return subscription schedules that were created during the given date interval.
    customer: Only return subscription schedules for the given customer.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    released_at: Only return subscription schedules that were released during the given date interval.
    scheduled: Only return subscription schedules that have not started yet.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, customer=None, default_settings=None, end_behavior=None, expand=None, from_subscription=None, metadata=None, phases=None, start_date=None):
		"""Create a schedule

Parameters:
    customer: The identifier of the customer to create the subscription schedule for.
    default_settings: Object representing the subscription schedule's default settings.
    end_behavior: Behavior of the subscription schedule and underlying subscription when it ends. Possible values are `release` or `cancel` with the default being `release`. `release` will end the subscription schedule and keep the underlying subscription running. `cancel` will end the subscription schedule and cancel the underlying subscription.
    expand: Specifies which fields in the response should be expanded.
    from_subscription: Migrate an existing subscription to be managed by a subscription schedule. If this parameter is set, a subscription schedule will be created using the subscription's item(s), set to auto-renew using the subscription's interval. When using this parameter, other parameters (such as phase values) cannot be set. To create a subscription schedule with other modifications, we recommend making two separate API calls.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    phases: List representing phases of the subscription schedule. Each phase can be customized to have different durations, plans, and coupons. If there are multiple phases, the `end_date` of one phase will always equal the `start_date` of the next phase.
    start_date: When the subscription schedule starts. We recommend using `now` so that it starts the subscription immediately. You can also use a Unix timestamp to backdate the subscription so that it starts on a past date, or set a future date for the subscription to start on."""
		...


class Subscription_Schedules_Schedule(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a schedule

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, default_settings=None, end_behavior=None, expand=None, metadata=None, phases=None, proration_behavior=None):
		"""Update a schedule

Parameters:
    default_settings: Object representing the subscription schedule's default settings.
    end_behavior: Behavior of the subscription schedule and underlying subscription when it ends. Possible values are `release` or `cancel` with the default being `release`. `release` will end the subscription schedule and keep the underlying subscription running. `cancel` will end the subscription schedule and cancel the underlying subscription.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    phases: List representing phases of the subscription schedule. Each phase can be customized to have different durations, plans, and coupons. If there are multiple phases, the `end_date` of one phase will always equal the `start_date` of the next phase. Note that past phases can be omitted.
    proration_behavior: If the update changes the billing configuration (item price, quantity, etc.) of the current phase, indicates how prorations from this change should be handled. The default value is `create_prorations`."""
		...


class Subscription_Schedules_Schedule_Cancel(_StripeResourceGroup):
	def create(*, expand=None, invoice_now=None, prorate=None):
		"""Cancel a schedule

Parameters:
    expand: Specifies which fields in the response should be expanded.
    invoice_now: If the subscription schedule is `active`, indicates if a final invoice will be generated that contains any un-invoiced metered usage and new/pending proration invoice items. Defaults to `true`.
    prorate: If the subscription schedule is `active`, indicates if the cancellation should be prorated. Defaults to `true`."""
		...


class Subscription_Schedules_Schedule_Release(_StripeResourceGroup):
	def create(*, expand=None, preserve_cancel_date=None):
		"""Release a schedule

Parameters:
    expand: Specifies which fields in the response should be expanded.
    preserve_cancel_date: Keep any cancellation on the subscription that the schedule has set"""
		...


class Subscriptions(_StripeResourceGroup):
	def fetch(*, automatic_tax=None, collection_method=None, created=None, current_period_end=None, current_period_start=None, customer=None, ending_before=None, expand=None, limit=None, price=None, starting_after=None, status=None, test_clock=None):
		"""List subscriptions

Parameters:
    automatic_tax: Filter subscriptions by their automatic tax settings.
    collection_method: The collection method of the subscriptions to retrieve. Either `charge_automatically` or `send_invoice`.
    created: Only return subscriptions that were created during the given date interval.
    current_period_end: Only return subscriptions whose current_period_end falls within the given date interval.
    current_period_start: Only return subscriptions whose current_period_start falls within the given date interval.
    customer: The ID of the customer whose subscriptions will be retrieved.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    price: Filter for subscriptions that contain this recurring price ID.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    status: The status of the subscriptions to retrieve. Passing in a value of `canceled` will return all canceled subscriptions, including those belonging to deleted customers. Pass `ended` to find subscriptions that are canceled and subscriptions that are expired due to [incomplete payment](https://stripe.com/docs/billing/subscriptions/overview#subscription-statuses). Passing in a value of `all` will return subscriptions of all statuses. If no value is supplied, all subscriptions that have not been canceled are returned.
    test_clock: Filter for subscriptions that are associated with the specified test clock. The response will not include subscriptions with test clocks if this and the customer parameter is not set."""
		...
	def create(*, add_invoice_items=None, application_fee_percent=None, automatic_tax=None, backdate_start_date=None, billing_cycle_anchor=None, billing_cycle_anchor_config=None, billing_thresholds=None, cancel_at=None, cancel_at_period_end=None, collection_method=None, currency=None, customer=None, days_until_due=None, default_payment_method=None, default_source=None, default_tax_rates=None, description=None, discounts=None, expand=None, invoice_settings=None, items=None, metadata=None, off_session=None, on_behalf_of=None, payment_behavior=None, payment_settings=None, pending_invoice_item_interval=None, proration_behavior=None, transfer_data=None, trial_end=None, trial_from_plan=None, trial_period_days=None, trial_settings=None):
		"""Create a subscription

Parameters:
    add_invoice_items: A list of prices and quantities that will generate invoice items appended to the next invoice for this subscription. You may pass up to 20 items.
    application_fee_percent: A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions).
    automatic_tax: Automatic tax settings for this subscription. We recommend you only include this parameter when the existing value is being changed.
    backdate_start_date: For new subscriptions, a past timestamp to backdate the subscription's start date to. If set, the first invoice will contain a proration for the timespan between the start date and the current time. Can be combined with trials and the billing cycle anchor.
    billing_cycle_anchor: A future timestamp in UTC format to anchor the subscription's [billing cycle](https://stripe.com/docs/subscriptions/billing-cycle). The anchor is the reference point that aligns future billing cycle dates. It sets the day of week for `week` intervals, the day of month for `month` and `year` intervals, and the month of year for `year` intervals.
    billing_cycle_anchor_config: Mutually exclusive with billing_cycle_anchor and only valid with monthly and yearly price intervals. When provided, the billing_cycle_anchor is set to the next occurence of the day_of_month at the hour, minute, and second UTC.
    billing_thresholds: Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. When updating, pass an empty string to remove previously-defined thresholds.
    cancel_at: A timestamp at which the subscription should cancel. If set to a date before the current period ends, this will cause a proration if prorations have been enabled using `proration_behavior`. If set during a future period, this will always cause a proration for that period.
    cancel_at_period_end: Indicate whether this subscription should cancel at the end of the current period (`current_period_end`). Defaults to `false`. This param will be removed in a future API version. Please use `cancel_at` instead.
    collection_method: Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`.
    currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    customer: The identifier of the customer to subscribe.
    days_until_due: Number of days a customer has to pay invoices generated by this subscription. Valid only for subscriptions where `collection_method` is set to `send_invoice`.
    default_payment_method: ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over `default_source`. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source).
    default_source: ID of the default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If `default_payment_method` is also set, `default_payment_method` will take precedence. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source).
    default_tax_rates: The tax rates that will apply to any subscription item that does not have `tax_rates` set. Invoices created will have their `default_tax_rates` populated from the subscription.
    description: The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
    discounts: The coupons to redeem into discounts for the subscription. If not specified or empty, inherits the discount from the subscription's customer.
    expand: Specifies which fields in the response should be expanded.
    invoice_settings: All invoices will be billed using the specified settings.
    items: A list of up to 20 subscription items, each with an attached price.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    off_session: Indicates if a customer is on or off-session while an invoice payment is attempted. Defaults to `false` (on-session).
    on_behalf_of: The account on behalf of which to charge, for each of the subscription's invoices.
    payment_behavior: Only applies to subscriptions with `collection_method=charge_automatically`.

Use `allow_incomplete` to create Subscriptions with `status=incomplete` if the first invoice can't be paid. Creating Subscriptions with this status allows you to manage scenarios where additional customer actions are needed to pay a subscription's invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication) for Billing to learn more. This is the default behavior.

Use `default_incomplete` to create Subscriptions with `status=incomplete` when the first invoice requires payment, otherwise start as active. Subscriptions transition to `status=active` when successfully confirming the PaymentIntent on the first invoice. This allows simpler management of scenarios where additional customer actions are needed to pay a subscription’s invoice, such as failed payments, [SCA regulation](https://stripe.com/docs/billing/migration/strong-customer-authentication), or collecting a mandate for a bank debit payment method. If the PaymentIntent is not confirmed within 23 hours Subscriptions transition to `status=incomplete_expired`, which is a terminal state.

Use `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription's first invoice can't be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further customer action is needed, this parameter doesn't create a Subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://stripe.com/docs/upgrades#2019-03-14) to learn more.

`pending_if_incomplete` is only used with updates and cannot be passed when creating a Subscription.

Subscriptions with `collection_method=send_invoice` are automatically activated regardless of the first Invoice status.
    payment_settings: Payment settings to pass to invoices created by the subscription.
    pending_invoice_item_interval: Specifies an interval for how often to bill for any pending invoice items. It is analogous to calling [Create an invoice](https://stripe.com/docs/api#create_invoice) for the given subscription at the specified interval.
    proration_behavior: Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) resulting from the `billing_cycle_anchor`. If no value is passed, the default is `create_prorations`.
    transfer_data: If specified, the funds from the subscription's invoices will be transferred to the destination and the ID of the resulting transfers will be found on the resulting charges.
    trial_end: Unix timestamp representing the end of the trial period the customer will get before being charged for the first time. If set, trial_end will override the default trial period of the plan the customer is being subscribed to. The special value `now` can be provided to end the customer's trial immediately. Can be at most two years from `billing_cycle_anchor`. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more.
    trial_from_plan: Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more.
    trial_period_days: Integer representing the number of trial period days before the customer is charged for the first time. This will always overwrite any trials that might apply via a subscribed plan. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more.
    trial_settings: Settings related to subscription trials."""
		...


class Subscriptions_Search(_StripeResourceGroup):
	def fetch(*, expand=None, limit=None, page=None, query=None):
		"""Search subscriptions

Parameters:
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    page: A cursor for pagination across multiple pages of results. Don't include this parameter on the first call. Use the next_page value returned in a previous response to request subsequent results.
    query: The search query string. See [search query language](https://stripe.com/docs/search#search-query-language) and the list of supported [query fields for subscriptions](https://stripe.com/docs/search#query-fields-for-subscriptions)."""
		...


class Subscriptions_Subscription_Exposed_Id(_StripeResourceGroup):
	def delete(*, cancellation_details=None, expand=None, invoice_now=None, prorate=None):
		"""Cancel a subscription

Parameters:
    cancellation_details: Details about why this subscription was cancelled
    expand: Specifies which fields in the response should be expanded.
    invoice_now: Will generate a final invoice that invoices for any un-invoiced metered usage and new/pending proration invoice items. Defaults to `false`.
    prorate: Will generate a proration invoice item that credits remaining unused time until the subscription period end. Defaults to `false`."""
		...
	def fetch(*, expand=None):
		"""Retrieve a subscription

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, add_invoice_items=None, application_fee_percent=None, automatic_tax=None, billing_cycle_anchor=None, billing_thresholds=None, cancel_at=None, cancel_at_period_end=None, cancellation_details=None, collection_method=None, days_until_due=None, default_payment_method=None, default_source=None, default_tax_rates=None, description=None, discounts=None, expand=None, invoice_settings=None, items=None, metadata=None, off_session=None, on_behalf_of=None, pause_collection=None, payment_behavior=None, payment_settings=None, pending_invoice_item_interval=None, proration_behavior=None, proration_date=None, transfer_data=None, trial_end=None, trial_from_plan=None, trial_settings=None):
		"""Update a subscription

Parameters:
    add_invoice_items: A list of prices and quantities that will generate invoice items appended to the next invoice for this subscription. You may pass up to 20 items.
    application_fee_percent: A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. The request must be made by a platform account on a connected account in order to set an application fee percentage. For more information, see the application fees [documentation](https://stripe.com/docs/connect/subscriptions#collecting-fees-on-subscriptions).
    automatic_tax: Automatic tax settings for this subscription. We recommend you only include this parameter when the existing value is being changed.
    billing_cycle_anchor: Either `now` or `unchanged`. Setting the value to `now` resets the subscription's billing cycle anchor to the current time (in UTC). For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle).
    billing_thresholds: Define thresholds at which an invoice will be sent, and the subscription advanced to a new billing period. When updating, pass an empty string to remove previously-defined thresholds.
    cancel_at: A timestamp at which the subscription should cancel. If set to a date before the current period ends, this will cause a proration if prorations have been enabled using `proration_behavior`. If set during a future period, this will always cause a proration for that period.
    cancel_at_period_end: Indicate whether this subscription should cancel at the end of the current period (`current_period_end`). Defaults to `false`. This param will be removed in a future API version. Please use `cancel_at` instead.
    cancellation_details: Details about why this subscription was cancelled
    collection_method: Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this subscription at the end of the cycle using the default source attached to the customer. When sending an invoice, Stripe will email your customer an invoice with payment instructions and mark the subscription as `active`. Defaults to `charge_automatically`.
    days_until_due: Number of days a customer has to pay invoices generated by this subscription. Valid only for subscriptions where `collection_method` is set to `send_invoice`.
    default_payment_method: ID of the default payment method for the subscription. It must belong to the customer associated with the subscription. This takes precedence over `default_source`. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source).
    default_source: ID of the default payment source for the subscription. It must belong to the customer associated with the subscription and be in a chargeable state. If `default_payment_method` is also set, `default_payment_method` will take precedence. If neither are set, invoices will use the customer's [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/object#customer_object-invoice_settings-default_payment_method) or [default_source](https://stripe.com/docs/api/customers/object#customer_object-default_source).
    default_tax_rates: The tax rates that will apply to any subscription item that does not have `tax_rates` set. Invoices created will have their `default_tax_rates` populated from the subscription. Pass an empty string to remove previously-defined tax rates.
    description: The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
    discounts: The coupons to redeem into discounts for the subscription. If not specified or empty, inherits the discount from the subscription's customer.
    expand: Specifies which fields in the response should be expanded.
    invoice_settings: All invoices will be billed using the specified settings.
    items: A list of up to 20 subscription items, each with an attached price.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    off_session: Indicates if a customer is on or off-session while an invoice payment is attempted. Defaults to `false` (on-session).
    on_behalf_of: The account on behalf of which to charge, for each of the subscription's invoices.
    pause_collection: If specified, payment collection for this subscription will be paused. Note that the subscription status will be unchanged and will not be updated to `paused`. Learn more about [pausing collection](https://stripe.com/docs/billing/subscriptions/pause-payment).
    payment_behavior: Use `allow_incomplete` to transition the subscription to `status=past_due` if a payment is required but cannot be paid. This allows you to manage scenarios where additional user actions are needed to pay a subscription's invoice. For example, SCA regulation may require 3DS authentication to complete payment. See the [SCA Migration Guide](https://stripe.com/docs/billing/migration/strong-customer-authentication) for Billing to learn more. This is the default behavior.

Use `default_incomplete` to transition the subscription to `status=past_due` when payment is required and await explicit confirmation of the invoice's payment intent. This allows simpler management of scenarios where additional user actions are needed to pay a subscription’s invoice. Such as failed payments, [SCA regulation](https://stripe.com/docs/billing/migration/strong-customer-authentication), or collecting a mandate for a bank debit payment method.

Use `pending_if_incomplete` to update the subscription using [pending updates](https://stripe.com/docs/billing/subscriptions/pending-updates). When you use `pending_if_incomplete` you can only pass the parameters [supported by pending updates](https://stripe.com/docs/billing/pending-updates-reference#supported-attributes).

Use `error_if_incomplete` if you want Stripe to return an HTTP 402 status code if a subscription's invoice cannot be paid. For example, if a payment method requires 3DS authentication due to SCA regulation and further user action is needed, this parameter does not update the subscription and returns an error instead. This was the default behavior for API versions prior to 2019-03-14. See the [changelog](https://stripe.com/docs/upgrades#2019-03-14) to learn more.
    payment_settings: Payment settings to pass to invoices created by the subscription.
    pending_invoice_item_interval: Specifies an interval for how often to bill for any pending invoice items. It is analogous to calling [Create an invoice](https://stripe.com/docs/api#create_invoice) for the given subscription at the specified interval.
    proration_behavior: Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) when the billing cycle changes (e.g., when switching plans, resetting `billing_cycle_anchor=now`, or starting a trial), or if an item's `quantity` changes. The default value is `create_prorations`.
    proration_date: If set, prorations will be calculated as though the subscription was updated at the given time. This can be used to apply exactly the same prorations that were previewed with the [create preview](https://stripe.com/docs/api/invoices/create_preview) endpoint. `proration_date` can also be used to implement custom proration logic, such as prorating by day instead of by second, by providing the time that you wish to use for proration calculations.
    transfer_data: If specified, the funds from the subscription's invoices will be transferred to the destination and the ID of the resulting transfers will be found on the resulting charges. This will be unset if you POST an empty value.
    trial_end: Unix timestamp representing the end of the trial period the customer will get before being charged for the first time. This will always overwrite any trials that might apply via a subscribed plan. If set, `trial_end` will override the default trial period of the plan the customer is being subscribed to. The `billing_cycle_anchor` will be updated to the `trial_end` value. The special value `now` can be provided to end the customer's trial immediately. Can be at most two years from `billing_cycle_anchor`.
    trial_from_plan: Indicates if a plan's `trial_period_days` should be applied to the subscription. Setting `trial_end` per subscription is preferred, and this defaults to `false`. Setting this flag to `true` together with `trial_end` is not allowed. See [Using trial periods on subscriptions](https://stripe.com/docs/billing/subscriptions/trials) to learn more.
    trial_settings: Settings related to subscription trials."""
		...


class Subscriptions_Subscription_Exposed_Id_Discount(_StripeResourceGroup):
	def delete():
		"""Delete a subscription discount"""
		...


class Subscriptions_Subscription_Resume(_StripeResourceGroup):
	def create(*, billing_cycle_anchor=None, expand=None, proration_behavior=None, proration_date=None):
		"""Resume a subscription

Parameters:
    billing_cycle_anchor: The billing cycle anchor that applies when the subscription is resumed. Either `now` or `unchanged`. The default is `now`. For more information, see the billing cycle [documentation](https://stripe.com/docs/billing/subscriptions/billing-cycle).
    expand: Specifies which fields in the response should be expanded.
    proration_behavior: Determines how to handle [prorations](https://stripe.com/docs/billing/subscriptions/prorations) resulting from the `billing_cycle_anchor` being `unchanged`. When the `billing_cycle_anchor` is set to `now` (default value), no prorations are generated. If no value is passed, the default is `create_prorations`.
    proration_date: If set, prorations will be calculated as though the subscription was resumed at the given time. This can be used to apply exactly the same prorations that were previewed with the [create preview](https://stripe.com/docs/api/invoices/create_preview) endpoint."""
		...


class Tax_Calculations(_StripeResourceGroup):
	def create(*, currency=None, customer=None, customer_details=None, expand=None, line_items=None, ship_from_details=None, shipping_cost=None, tax_date=None):
		"""Create a Tax Calculation

Parameters:
    currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    customer: The ID of an existing customer to use for this calculation. If provided, the customer's address and tax IDs are copied to `customer_details`.
    customer_details: Details about the customer, including address and tax IDs.
    expand: Specifies which fields in the response should be expanded.
    line_items: A list of items the customer is purchasing.
    ship_from_details: Details about the address from which the goods are being shipped.
    shipping_cost: Shipping cost details to be used for the calculation.
    tax_date: Timestamp of date at which the tax rules and rates in effect applies for the calculation. Measured in seconds since the Unix epoch. Can be up to 48 hours in the past, and up to 48 hours in the future."""
		...


class Tax_Calculations_Calculation(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a Tax Calculation

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Tax_Calculations_Calculation_Line_Items(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None):
		"""Retrieve a calculation's line items

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...


class Tax_Registrations(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None, status=None):
		"""List registrations

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    status: The status of the Tax Registration."""
		...
	def create(*, active_from=None, country=None, country_options=None, expand=None, expires_at=None):
		"""Create a registration

Parameters:
    active_from: Time at which the Tax Registration becomes active. It can be either `now` to indicate the current time, or a future timestamp measured in seconds since the Unix epoch.
    country: Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    country_options: Specific options for a registration in the specified `country`.
    expand: Specifies which fields in the response should be expanded.
    expires_at: If set, the Tax Registration stops being active at this time. If not set, the Tax Registration will be active indefinitely. Timestamp measured in seconds since the Unix epoch."""
		...


class Tax_Registrations_Id(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a registration

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, active_from=None, expand=None, expires_at=None):
		"""Update a registration

Parameters:
    active_from: Time at which the registration becomes active. It can be either `now` to indicate the current time, or a timestamp measured in seconds since the Unix epoch.
    expand: Specifies which fields in the response should be expanded.
    expires_at: If set, the registration stops being active at this time. If not set, the registration will be active indefinitely. It can be either `now` to indicate the current time, or a timestamp measured in seconds since the Unix epoch."""
		...


class Tax_Settings(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve settings

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, defaults=None, expand=None, head_office=None):
		"""Update settings

Parameters:
    defaults: Default configuration to be used on Stripe Tax calculations.
    expand: Specifies which fields in the response should be expanded.
    head_office: The place where your business is located."""
		...


class Tax_Transactions_Create_From_Calculation(_StripeResourceGroup):
	def create(*, calculation=None, expand=None, metadata=None, posted_at=None, reference=None):
		"""Create a transaction from a calculation

Parameters:
    calculation: Tax Calculation ID to be used as input when creating the transaction.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    posted_at: The Unix timestamp representing when the tax liability is assumed or reduced, which determines the liability posting period and handling in tax liability reports. The timestamp must fall within the `tax_date` and the current time, unless the `tax_date` is scheduled in advance. Defaults to the current time.
    reference: A custom order or sale identifier, such as 'myOrder_123'. Must be unique across all transactions, including reversals."""
		...


class Tax_Transactions_Create_Reversal(_StripeResourceGroup):
	def create(*, expand=None, flat_amount=None, line_items=None, metadata=None, mode=None, original_transaction=None, reference=None, shipping_cost=None):
		"""Create a reversal transaction

Parameters:
    expand: Specifies which fields in the response should be expanded.
    flat_amount: A flat amount to reverse across the entire transaction, in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) in negative. This value represents the total amount to refund from the transaction, including taxes.
    line_items: The line item amounts to reverse.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    mode: If `partial`, the provided line item or shipping cost amounts are reversed. If `full`, the original transaction is fully reversed.
    original_transaction: The ID of the Transaction to partially or fully reverse.
    reference: A custom identifier for this reversal, such as `myOrder_123-refund_1`, which must be unique across all transactions. The reference helps identify this reversal transaction in exported [tax reports](https://stripe.com/docs/tax/reports).
    shipping_cost: The shipping cost to reverse."""
		...


class Tax_Transactions_Transaction(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a transaction

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Tax_Transactions_Transaction_Line_Items(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None):
		"""Retrieve a transaction's line items

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...


class Tax_Codes(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List all tax codes

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...


class Tax_Codes_Id(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a tax code

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Tax_Ids(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, owner=None, starting_after=None):
		"""List all tax IDs

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    owner: The account or customer the tax ID belongs to. Defaults to `owner[type]=self`.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, expand=None, owner=None, type=None, value=None):
		"""Create a tax ID

Parameters:
    expand: Specifies which fields in the response should be expanded.
    owner: The account or customer the tax ID belongs to. Defaults to `owner[type]=self`.
    type: Type of the tax ID, one of `ad_nrt`, `ae_trn`, `al_tin`, `am_tin`, `ao_tin`, `ar_cuit`, `au_abn`, `au_arn`, `aw_tin`, `az_tin`, `ba_tin`, `bb_tin`, `bd_bin`, `bf_ifu`, `bg_uic`, `bh_vat`, `bj_ifu`, `bo_tin`, `br_cnpj`, `br_cpf`, `bs_tin`, `by_tin`, `ca_bn`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `ca_qst`, `cd_nif`, `ch_uid`, `ch_vat`, `cl_tin`, `cm_niu`, `cn_tin`, `co_nit`, `cr_tin`, `cv_nif`, `de_stn`, `do_rcn`, `ec_ruc`, `eg_tin`, `es_cif`, `et_tin`, `eu_oss_vat`, `eu_vat`, `gb_vat`, `ge_vat`, `gn_nif`, `hk_br`, `hr_oib`, `hu_tin`, `id_npwp`, `il_vat`, `in_gst`, `is_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `ke_pin`, `kg_tin`, `kh_tin`, `kr_brn`, `kz_bin`, `la_tin`, `li_uid`, `li_vat`, `ma_vat`, `md_vat`, `me_pib`, `mk_vat`, `mr_nif`, `mx_rfc`, `my_frp`, `my_itn`, `my_sst`, `ng_tin`, `no_vat`, `no_voec`, `np_pan`, `nz_gst`, `om_vat`, `pe_ruc`, `ph_tin`, `ro_tin`, `rs_pib`, `ru_inn`, `ru_kpp`, `sa_vat`, `sg_gst`, `sg_uen`, `si_tin`, `sn_ninea`, `sr_fin`, `sv_nit`, `th_vat`, `tj_tin`, `tr_tin`, `tw_vat`, `tz_vat`, `ua_vat`, `ug_tin`, `us_ein`, `uy_ruc`, `uz_tin`, `uz_vat`, `ve_rif`, `vn_tin`, `za_vat`, `zm_tin`, or `zw_tin`
    value: Value of the tax ID."""
		...


class Tax_Ids_Id(_StripeResourceGroup):
	def delete():
		"""Delete a tax ID"""
		...
	def fetch(*, expand=None):
		"""Retrieve a tax ID

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Tax_Rates(_StripeResourceGroup):
	def fetch(*, active=None, created=None, ending_before=None, expand=None, inclusive=None, limit=None, starting_after=None):
		"""List all tax rates

Parameters:
    active: Optional flag to filter by tax rates that are either active or inactive (archived).
    created: Optional range for filtering created date.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    inclusive: Optional flag to filter by tax rates that are inclusive (or those that are not inclusive).
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, active=None, country=None, description=None, display_name=None, expand=None, inclusive=None, jurisdiction=None, metadata=None, percentage=None, state=None, tax_type=None):
		"""Create a tax rate

Parameters:
    active: Flag determining whether the tax rate is active or inactive (archived). Inactive tax rates cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.
    country: Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    description: An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.
    display_name: The display name of the tax rate, which will be shown to users.
    expand: Specifies which fields in the response should be expanded.
    inclusive: This specifies if the tax rate is inclusive or exclusive.
    jurisdiction: The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    percentage: This represents the tax rate percent out of 100.
    state: [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, "NY" for New York, United States.
    tax_type: The high-level tax type, such as `vat` or `sales_tax`."""
		...


class Tax_Rates_Tax_Rate(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a tax rate

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, active=None, country=None, description=None, display_name=None, expand=None, jurisdiction=None, metadata=None, state=None, tax_type=None):
		"""Update a tax rate

Parameters:
    active: Flag determining whether the tax rate is active or inactive (archived). Inactive tax rates cannot be used with new applications or Checkout Sessions, but will still work for subscriptions and invoices that already have it set.
    country: Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    description: An arbitrary string attached to the tax rate for your internal use only. It will not be visible to your customers.
    display_name: The display name of the tax rate, which will be shown to users.
    expand: Specifies which fields in the response should be expanded.
    jurisdiction: The jurisdiction for the tax rate. You can use this label field for tax reporting purposes. It also appears on your customer’s invoice.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    state: [ISO 3166-2 subdivision code](https://en.wikipedia.org/wiki/ISO_3166-2), without country prefix. For example, "NY" for New York, United States.
    tax_type: The high-level tax type, such as `vat` or `sales_tax`."""
		...


class Terminal_Configurations(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, is_account_default=None, limit=None, starting_after=None):
		"""List all Configurations

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    is_account_default: if present, only return the account default or non-default configurations.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, bbpos_wisepos_e=None, expand=None, name=None, offline=None, reboot_window=None, stripe_s700=None, tipping=None, verifone_p400=None, wifi=None):
		"""Create a Configuration

Parameters:
    bbpos_wisepos_e: An object containing device type specific settings for BBPOS WisePOS E readers
    expand: Specifies which fields in the response should be expanded.
    name: Name of the configuration
    offline: Configurations for collecting transactions offline.
    reboot_window: Reboot time settings for readers that support customized reboot time configuration.
    stripe_s700: An object containing device type specific settings for Stripe S700 readers
    tipping: Tipping configurations for readers supporting on-reader tips
    verifone_p400: An object containing device type specific settings for Verifone P400 readers
    wifi: Configurations for connecting to a WiFi network."""
		...


class Terminal_Configurations_Configuration(_StripeResourceGroup):
	def delete():
		"""Delete a Configuration"""
		...
	def fetch(*, expand=None):
		"""Retrieve a Configuration

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, bbpos_wisepos_e=None, expand=None, name=None, offline=None, reboot_window=None, stripe_s700=None, tipping=None, verifone_p400=None, wifi=None):
		"""Update a Configuration

Parameters:
    bbpos_wisepos_e: An object containing device type specific settings for BBPOS WisePOS E readers
    expand: Specifies which fields in the response should be expanded.
    name: Name of the configuration
    offline: Configurations for collecting transactions offline.
    reboot_window: Reboot time settings for readers that support customized reboot time configuration.
    stripe_s700: An object containing device type specific settings for Stripe S700 readers
    tipping: Tipping configurations for readers supporting on-reader tips
    verifone_p400: An object containing device type specific settings for Verifone P400 readers
    wifi: Configurations for connecting to a WiFi network."""
		...


class Terminal_Connection_Tokens(_StripeResourceGroup):
	def create(*, expand=None, location=None):
		"""Create a Connection Token

Parameters:
    expand: Specifies which fields in the response should be expanded.
    location: The id of the location that this connection token is scoped to. If specified the connection token will only be usable with readers assigned to that location, otherwise the connection token will be usable with all readers. Note that location scoping only applies to internet-connected readers. For more details, see [the docs on scoping connection tokens](https://docs.stripe.com/terminal/fleet/locations-and-zones?dashboard-or-api=api#connection-tokens)."""
		...


class Terminal_Locations(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List all Locations

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, address=None, configuration_overrides=None, display_name=None, expand=None, metadata=None):
		"""Create a Location

Parameters:
    address: The full address of the location.
    configuration_overrides: The ID of a configuration that will be used to customize all readers in this location.
    display_name: A name for the location. Maximum length is 1000 characters.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."""
		...


class Terminal_Locations_Location(_StripeResourceGroup):
	def delete():
		"""Delete a Location"""
		...
	def fetch(*, expand=None):
		"""Retrieve a Location

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, address=None, configuration_overrides=None, display_name=None, expand=None, metadata=None):
		"""Update a Location

Parameters:
    address: The full address of the location. You can't change the location's `country`. If you need to modify the `country` field, create a new `Location` object and re-register any existing readers to that location.
    configuration_overrides: The ID of a configuration that will be used to customize all readers in this location.
    display_name: A name for the location.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."""
		...


class Terminal_Readers(_StripeResourceGroup):
	def fetch(*, device_type=None, ending_before=None, expand=None, limit=None, location=None, serial_number=None, starting_after=None, status=None):
		"""List all Readers

Parameters:
    device_type: Filters readers by device type
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    location: A location ID to filter the response list to only readers at the specific location
    serial_number: Filters readers by serial number
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    status: A status filter to filter readers to only offline or online readers"""
		...
	def create(*, expand=None, label=None, location=None, metadata=None, registration_code=None):
		"""Create a Reader

Parameters:
    expand: Specifies which fields in the response should be expanded.
    label: Custom label given to the reader for easier identification. If no label is specified, the registration code will be used.
    location: The location to assign the reader to.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    registration_code: A code generated by the reader used for registering to an account."""
		...


class Terminal_Readers_Reader(_StripeResourceGroup):
	def delete():
		"""Delete a Reader"""
		...
	def fetch(*, expand=None):
		"""Retrieve a Reader

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, expand=None, label=None, metadata=None):
		"""Update a Reader

Parameters:
    expand: Specifies which fields in the response should be expanded.
    label: The new label of the reader.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."""
		...


class Terminal_Readers_Reader_Cancel_Action(_StripeResourceGroup):
	def create(*, expand=None):
		"""Cancel the current reader action

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Terminal_Readers_Reader_Collect_Inputs(_StripeResourceGroup):
	def create(*, expand=None, inputs=None, metadata=None):
		"""Collect inputs using a Reader

Parameters:
    expand: Specifies which fields in the response should be expanded.
    inputs: List of inputs to be collected using the Reader
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."""
		...


class Terminal_Readers_Reader_Process_Payment_Intent(_StripeResourceGroup):
	def create(*, expand=None, payment_intent=None, process_config=None):
		"""Hand-off a PaymentIntent to a Reader

Parameters:
    expand: Specifies which fields in the response should be expanded.
    payment_intent: PaymentIntent ID
    process_config: Configuration overrides"""
		...


class Terminal_Readers_Reader_Process_Setup_Intent(_StripeResourceGroup):
	def create(*, allow_redisplay=None, expand=None, process_config=None, setup_intent=None):
		"""Hand-off a SetupIntent to a Reader

Parameters:
    allow_redisplay: This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow.
    expand: Specifies which fields in the response should be expanded.
    process_config: Configuration overrides
    setup_intent: SetupIntent ID"""
		...


class Terminal_Readers_Reader_Refund_Payment(_StripeResourceGroup):
	def create(*, amount=None, charge=None, expand=None, metadata=None, payment_intent=None, refund_application_fee=None, refund_payment_config=None, reverse_transfer=None):
		"""Refund a Charge or a PaymentIntent in-person

Parameters:
    amount: A positive integer in __cents__ representing how much of this charge to refund.
    charge: ID of the Charge to refund.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    payment_intent: ID of the PaymentIntent to refund.
    refund_application_fee: Boolean indicating whether the application fee should be refunded when refunding this charge. If a full charge refund is given, the full application fee will be refunded. Otherwise, the application fee will be refunded in an amount proportional to the amount of the charge refunded. An application fee can be refunded only by the application that created the charge.
    refund_payment_config: Configuration overrides
    reverse_transfer: Boolean indicating whether the transfer should be reversed when refunding this charge. The transfer will be reversed proportionally to the amount being refunded (either the entire or partial amount). A transfer can be reversed only by the application that created the charge."""
		...


class Terminal_Readers_Reader_Set_Reader_Display(_StripeResourceGroup):
	def create(*, cart=None, expand=None, type=None):
		"""Set reader display

Parameters:
    cart: Cart
    expand: Specifies which fields in the response should be expanded.
    type: Type"""
		...


class Test_Helpers_Confirmation_Tokens(_StripeResourceGroup):
	def create(*, expand=None, payment_method=None, payment_method_data=None, payment_method_options=None, return_url=None, setup_future_usage=None, shipping=None):
		"""Create a test Confirmation Token

Parameters:
    expand: Specifies which fields in the response should be expanded.
    payment_method: ID of an existing PaymentMethod.
    payment_method_data: If provided, this hash will be used to create a PaymentMethod.
    payment_method_options: Payment-method-specific configuration for this ConfirmationToken.
    return_url: Return URL used to confirm the Intent.
    setup_future_usage: Indicates that you intend to make future payments with this ConfirmationToken's payment method.

The presence of this property will [attach the payment method](https://stripe.com/docs/payments/save-during-payment) to the PaymentIntent's Customer, if present, after the PaymentIntent is confirmed and any required actions from the user are complete.
    shipping: Shipping information for this ConfirmationToken."""
		...


class Test_Helpers_Customers_Customer_Fund_Cash_Balance(_StripeResourceGroup):
	def create(*, amount=None, currency=None, expand=None, reference=None):
		"""Fund a test mode cash balance

Parameters:
    amount: Amount to be used for this test cash balance transaction. A positive integer representing how much to fund in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to fund $1.00 or 100 to fund ¥100, a zero-decimal currency).
    currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    expand: Specifies which fields in the response should be expanded.
    reference: A description of the test funding. This simulates free-text references supplied by customers when making bank transfers to their cash balance. You can use this to test how Stripe's [reconciliation algorithm](https://stripe.com/docs/payments/customer-balance/reconciliation) applies to different user inputs."""
		...


class Test_Helpers_Issuing_Authorizations(_StripeResourceGroup):
	def create(*, amount=None, amount_details=None, authorization_method=None, card=None, currency=None, expand=None, fleet=None, fuel=None, is_amount_controllable=None, merchant_amount=None, merchant_currency=None, merchant_data=None, network_data=None, verification_data=None, wallet=None):
		"""Create a test-mode authorization

Parameters:
    amount: The total amount to attempt to authorize. This amount is in the provided currency, or defaults to the card's currency, and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    amount_details: Detailed breakdown of amount components. These amounts are denominated in `currency` and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    authorization_method: How the card details were provided. Defaults to online.
    card: Card associated with this authorization.
    currency: The currency of the authorization. If not provided, defaults to the currency of the card. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    expand: Specifies which fields in the response should be expanded.
    fleet: Fleet-specific information for authorizations using Fleet cards.
    fuel: Information about fuel that was purchased with this transaction.
    is_amount_controllable: If set `true`, you may provide [amount](https://stripe.com/docs/api/issuing/authorizations/approve#approve_issuing_authorization-amount) to control how much to hold for the authorization.
    merchant_amount: The total amount to attempt to authorize. This amount is in the provided merchant currency, and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    merchant_currency: The currency of the authorization. If not provided, defaults to the currency of the card. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    merchant_data: Details about the seller (grocery store, e-commerce website, etc.) where the card authorization happened.
    network_data: Details about the authorization, such as identifiers, set by the card network.
    verification_data: Verifications that Stripe performed on information that the cardholder provided to the merchant.
    wallet: The digital wallet used for this transaction. One of `apple_pay`, `google_pay`, or `samsung_pay`. Will populate as `null` when no digital wallet was utilized."""
		...


class Test_Helpers_Issuing_Authorizations_Authorization_Capture(_StripeResourceGroup):
	def create(*, capture_amount=None, close_authorization=None, expand=None, purchase_details=None):
		"""Capture a test-mode authorization

Parameters:
    capture_amount: The amount to capture from the authorization. If not provided, the full amount of the authorization will be captured. This amount is in the authorization currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    close_authorization: Whether to close the authorization after capture. Defaults to true. Set to false to enable multi-capture flows.
    expand: Specifies which fields in the response should be expanded.
    purchase_details: Additional purchase information that is optionally provided by the merchant."""
		...


class Test_Helpers_Issuing_Authorizations_Authorization_Expire(_StripeResourceGroup):
	def create(*, expand=None):
		"""Expire a test-mode authorization

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Test_Helpers_Issuing_Authorizations_Authorization_Finalize_Amount(_StripeResourceGroup):
	def create(*, expand=None, final_amount=None, fleet=None, fuel=None):
		"""Finalize a test-mode authorization's amount

Parameters:
    expand: Specifies which fields in the response should be expanded.
    final_amount: The final authorization amount that will be captured by the merchant. This amount is in the authorization currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    fleet: Fleet-specific information for authorizations using Fleet cards.
    fuel: Information about fuel that was purchased with this transaction."""
		...


class Test_Helpers_Issuing_Authorizations_Authorization_Fraud_Challenges_Respond(_StripeResourceGroup):
	def create(*, confirmed=None, expand=None):
		"""Respond to fraud challenge

Parameters:
    confirmed: Whether to simulate the user confirming that the transaction was legitimate (true) or telling Stripe that it was fraudulent (false).
    expand: Specifies which fields in the response should be expanded."""
		...


class Test_Helpers_Issuing_Authorizations_Authorization_Increment(_StripeResourceGroup):
	def create(*, expand=None, increment_amount=None, is_amount_controllable=None):
		"""Increment a test-mode authorization

Parameters:
    expand: Specifies which fields in the response should be expanded.
    increment_amount: The amount to increment the authorization by. This amount is in the authorization currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    is_amount_controllable: If set `true`, you may provide [amount](https://stripe.com/docs/api/issuing/authorizations/approve#approve_issuing_authorization-amount) to control how much to hold for the authorization."""
		...


class Test_Helpers_Issuing_Authorizations_Authorization_Reverse(_StripeResourceGroup):
	def create(*, expand=None, reverse_amount=None):
		"""Reverse a test-mode authorization

Parameters:
    expand: Specifies which fields in the response should be expanded.
    reverse_amount: The amount to reverse from the authorization. If not provided, the full amount of the authorization will be reversed. This amount is in the authorization currency and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)."""
		...


class Test_Helpers_Issuing_Cards_Card_Shipping_Deliver(_StripeResourceGroup):
	def create(*, expand=None):
		"""Deliver a testmode card

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Test_Helpers_Issuing_Cards_Card_Shipping_Fail(_StripeResourceGroup):
	def create(*, expand=None):
		"""Fail a testmode card

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Test_Helpers_Issuing_Cards_Card_Shipping_Return(_StripeResourceGroup):
	def create(*, expand=None):
		"""Return a testmode card

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Test_Helpers_Issuing_Cards_Card_Shipping_Ship(_StripeResourceGroup):
	def create(*, expand=None):
		"""Ship a testmode card

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Test_Helpers_Issuing_Cards_Card_Shipping_Submit(_StripeResourceGroup):
	def create(*, expand=None):
		"""Submit a testmode card

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Test_Helpers_Issuing_Personalization_Designs_Personalization_Design_Activate(_StripeResourceGroup):
	def create(*, expand=None):
		"""Activate a testmode personalization design

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Test_Helpers_Issuing_Personalization_Designs_Personalization_Design_Deactivate(_StripeResourceGroup):
	def create(*, expand=None):
		"""Deactivate a testmode personalization design

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Test_Helpers_Issuing_Personalization_Designs_Personalization_Design_Reject(_StripeResourceGroup):
	def create(*, expand=None, rejection_reasons=None):
		"""Reject a testmode personalization design

Parameters:
    expand: Specifies which fields in the response should be expanded.
    rejection_reasons: The reason(s) the personalization design was rejected."""
		...


class Test_Helpers_Issuing_Settlements(_StripeResourceGroup):
	def create(*, bin=None, clearing_date=None, currency=None, expand=None, interchange_fees_amount=None, net_total_amount=None, network=None, network_settlement_identifier=None, transaction_amount=None, transaction_count=None):
		"""Create a test-mode settlement

Parameters:
    bin: The Bank Identification Number reflecting this settlement record.
    clearing_date: The date that the transactions are cleared and posted to user's accounts.
    currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    expand: Specifies which fields in the response should be expanded.
    interchange_fees_amount: The total interchange received as reimbursement for the transactions.
    net_total_amount: The total net amount required to settle with the network.
    network: The card network for this settlement. One of ["visa", "maestro"]
    network_settlement_identifier: The Settlement Identification Number assigned by the network.
    transaction_amount: The total transaction amount reflected in this settlement.
    transaction_count: The total number of transactions reflected in this settlement."""
		...


class Test_Helpers_Issuing_Settlements_Settlement_Complete(_StripeResourceGroup):
	def create(*, expand=None):
		"""Complete a test-mode settlement

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Test_Helpers_Issuing_Transactions_Create_Force_Capture(_StripeResourceGroup):
	def create(*, amount=None, card=None, currency=None, expand=None, merchant_data=None, purchase_details=None):
		"""Create a test-mode force capture

Parameters:
    amount: The total amount to attempt to capture. This amount is in the provided currency, or defaults to the cards currency, and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    card: Card associated with this transaction.
    currency: The currency of the capture. If not provided, defaults to the currency of the card. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    expand: Specifies which fields in the response should be expanded.
    merchant_data: Details about the seller (grocery store, e-commerce website, etc.) where the card authorization happened.
    purchase_details: Additional purchase information that is optionally provided by the merchant."""
		...


class Test_Helpers_Issuing_Transactions_Create_Unlinked_Refund(_StripeResourceGroup):
	def create(*, amount=None, card=None, currency=None, expand=None, merchant_data=None, purchase_details=None):
		"""Create a test-mode unlinked refund

Parameters:
    amount: The total amount to attempt to refund. This amount is in the provided currency, or defaults to the cards currency, and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    card: Card associated with this unlinked refund transaction.
    currency: The currency of the unlinked refund. If not provided, defaults to the currency of the card. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    expand: Specifies which fields in the response should be expanded.
    merchant_data: Details about the seller (grocery store, e-commerce website, etc.) where the card authorization happened.
    purchase_details: Additional purchase information that is optionally provided by the merchant."""
		...


class Test_Helpers_Issuing_Transactions_Transaction_Refund(_StripeResourceGroup):
	def create(*, expand=None, refund_amount=None):
		"""Refund a test-mode transaction

Parameters:
    expand: Specifies which fields in the response should be expanded.
    refund_amount: The total amount to attempt to refund. This amount is in the provided currency, or defaults to the cards currency, and in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal)."""
		...


class Test_Helpers_Refunds_Refund_Expire(_StripeResourceGroup):
	def create(*, expand=None):
		"""Expire a pending refund.

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Test_Helpers_Terminal_Readers_Reader_Present_Payment_Method(_StripeResourceGroup):
	def create(*, amount_tip=None, card_present=None, expand=None, interac_present=None, type=None):
		"""Simulate presenting a payment method

Parameters:
    amount_tip: Simulated on-reader tip amount.
    card_present: Simulated data for the card_present payment method.
    expand: Specifies which fields in the response should be expanded.
    interac_present: Simulated data for the interac_present payment method.
    type: Simulated payment type."""
		...


class Test_Helpers_Terminal_Readers_Reader_Succeed_Input_Collection(_StripeResourceGroup):
	def create(*, expand=None, skip_non_required_inputs=None):
		"""Simulate a successful input collection

Parameters:
    expand: Specifies which fields in the response should be expanded.
    skip_non_required_inputs: This parameter defines the skip behavior for input collection."""
		...


class Test_Helpers_Terminal_Readers_Reader_Timeout_Input_Collection(_StripeResourceGroup):
	def create(*, expand=None):
		"""Simulate an input collection timeout

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Test_Helpers_Test_Clocks(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List all test clocks

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, expand=None, frozen_time=None, name=None):
		"""Create a test clock

Parameters:
    expand: Specifies which fields in the response should be expanded.
    frozen_time: The initial frozen time for this test clock.
    name: The name for this test clock."""
		...


class Test_Helpers_Test_Clocks_Test_Clock(_StripeResourceGroup):
	def delete():
		"""Delete a test clock"""
		...
	def fetch(*, expand=None):
		"""Retrieve a test clock

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Test_Helpers_Test_Clocks_Test_Clock_Advance(_StripeResourceGroup):
	def create(*, expand=None, frozen_time=None):
		"""Advance a test clock

Parameters:
    expand: Specifies which fields in the response should be expanded.
    frozen_time: The time to advance the test clock. Must be after the test clock's current frozen time. Cannot be more than two intervals in the future from the shortest subscription in this test clock. If there are no subscriptions in this test clock, it cannot be more than two years in the future."""
		...


class Test_Helpers_Treasury_Inbound_Transfers_Id_Fail(_StripeResourceGroup):
	def create(*, expand=None, failure_details=None):
		"""Test mode: Fail an InboundTransfer

Parameters:
    expand: Specifies which fields in the response should be expanded.
    failure_details: Details about a failed InboundTransfer."""
		...


class Test_Helpers_Treasury_Inbound_Transfers_Id_Return(_StripeResourceGroup):
	def create(*, expand=None):
		"""Test mode: Return an InboundTransfer

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Test_Helpers_Treasury_Inbound_Transfers_Id_Succeed(_StripeResourceGroup):
	def create(*, expand=None):
		"""Test mode: Succeed an InboundTransfer

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Test_Helpers_Treasury_Outbound_Payments_Id(_StripeResourceGroup):
	def create(*, expand=None, tracking_details=None):
		"""Test mode: Update an OutboundPayment

Parameters:
    expand: Specifies which fields in the response should be expanded.
    tracking_details: Details about network-specific tracking information."""
		...


class Test_Helpers_Treasury_Outbound_Payments_Id_Fail(_StripeResourceGroup):
	def create(*, expand=None):
		"""Test mode: Fail an OutboundPayment

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Test_Helpers_Treasury_Outbound_Payments_Id_Post(_StripeResourceGroup):
	def create(*, expand=None):
		"""Test mode: Post an OutboundPayment

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Test_Helpers_Treasury_Outbound_Payments_Id_Return(_StripeResourceGroup):
	def create(*, expand=None, returned_details=None):
		"""Test mode: Return an OutboundPayment

Parameters:
    expand: Specifies which fields in the response should be expanded.
    returned_details: Optional hash to set the return code."""
		...


class Test_Helpers_Treasury_Outbound_Transfers_Outbound_Transfer(_StripeResourceGroup):
	def create(*, expand=None, tracking_details=None):
		"""Test mode: Update an OutboundTransfer

Parameters:
    expand: Specifies which fields in the response should be expanded.
    tracking_details: Details about network-specific tracking information."""
		...


class Test_Helpers_Treasury_Outbound_Transfers_Outbound_Transfer_Fail(_StripeResourceGroup):
	def create(*, expand=None):
		"""Test mode: Fail an OutboundTransfer

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Test_Helpers_Treasury_Outbound_Transfers_Outbound_Transfer_Post(_StripeResourceGroup):
	def create(*, expand=None):
		"""Test mode: Post an OutboundTransfer

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Test_Helpers_Treasury_Outbound_Transfers_Outbound_Transfer_Return(_StripeResourceGroup):
	def create(*, expand=None, returned_details=None):
		"""Test mode: Return an OutboundTransfer

Parameters:
    expand: Specifies which fields in the response should be expanded.
    returned_details: Details about a returned OutboundTransfer."""
		...


class Test_Helpers_Treasury_Received_Credits(_StripeResourceGroup):
	def create(*, amount=None, currency=None, description=None, expand=None, financial_account=None, initiating_payment_method_details=None, network=None):
		"""Test mode: Create a ReceivedCredit

Parameters:
    amount: Amount (in cents) to be transferred.
    currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    description: An arbitrary string attached to the object. Often useful for displaying to users.
    expand: Specifies which fields in the response should be expanded.
    financial_account: The FinancialAccount to send funds to.
    initiating_payment_method_details: Initiating payment method details for the object.
    network: Specifies the network rails to be used. If not set, will default to the PaymentMethod's preferred network. See the [docs](https://stripe.com/docs/treasury/money-movement/timelines) to learn more about money movement timelines for each network type."""
		...


class Test_Helpers_Treasury_Received_Debits(_StripeResourceGroup):
	def create(*, amount=None, currency=None, description=None, expand=None, financial_account=None, initiating_payment_method_details=None, network=None):
		"""Test mode: Create a ReceivedDebit

Parameters:
    amount: Amount (in cents) to be transferred.
    currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    description: An arbitrary string attached to the object. Often useful for displaying to users.
    expand: Specifies which fields in the response should be expanded.
    financial_account: The FinancialAccount to pull funds from.
    initiating_payment_method_details: Initiating payment method details for the object.
    network: Specifies the network rails to be used. If not set, will default to the PaymentMethod's preferred network. See the [docs](https://stripe.com/docs/treasury/money-movement/timelines) to learn more about money movement timelines for each network type."""
		...


class Tokens(_StripeResourceGroup):
	def create(*, account=None, bank_account=None, card=None, customer=None, cvc_update=None, expand=None, person=None, pii=None):
		"""Create a CVC update token

Parameters:
    account: Information for the account this token represents.
    bank_account: The bank account this token will represent.
    card: The card this token will represent. If you also pass in a customer, the card must be the ID of a card belonging to the customer. Otherwise, if you do not pass in a customer, this is a dictionary containing a user's credit card details, with the options described below.
    customer: Create a token for the customer, which is owned by the application's account. You can only use this with an [OAuth access token](https://stripe.com/docs/connect/standard-accounts) or [Stripe-Account header](https://stripe.com/docs/connect/authentication). Learn more about [cloning saved payment methods](https://stripe.com/docs/connect/cloning-saved-payment-methods).
    cvc_update: The updated CVC value this token represents.
    expand: Specifies which fields in the response should be expanded.
    person: Information for the person this token represents.
    pii: The PII this token represents."""
		...


class Tokens_Token(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a token

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Topups(_StripeResourceGroup):
	def fetch(*, amount=None, created=None, ending_before=None, expand=None, limit=None, starting_after=None, status=None):
		"""List all top-ups

Parameters:
    amount: A positive integer representing how much to transfer.
    created: A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    status: Only return top-ups that have the given status. One of `canceled`, `failed`, `pending` or `succeeded`."""
		...
	def create(*, amount=None, currency=None, description=None, expand=None, metadata=None, source=None, statement_descriptor=None, transfer_group=None):
		"""Create a top-up

Parameters:
    amount: A positive integer representing how much to transfer.
    currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    description: An arbitrary string attached to the object. Often useful for displaying to users.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    source: The ID of a source to transfer funds from. For most users, this should be left unspecified which will use the bank account that was set up in the dashboard for the specified currency. In test mode, this can be a test bank token (see [Testing Top-ups](https://stripe.com/docs/connect/testing#testing-top-ups)).
    statement_descriptor: Extra information about a top-up for the source's bank statement. Limited to 15 ASCII characters.
    transfer_group: A string that identifies this top-up as part of a group."""
		...


class Topups_Topup(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a top-up

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, description=None, expand=None, metadata=None):
		"""Update a top-up

Parameters:
    description: An arbitrary string attached to the object. Often useful for displaying to users.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."""
		...


class Topups_Topup_Cancel(_StripeResourceGroup):
	def create(*, expand=None):
		"""Cancel a top-up

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Transfers(_StripeResourceGroup):
	def fetch(*, created=None, destination=None, ending_before=None, expand=None, limit=None, starting_after=None, transfer_group=None):
		"""List all transfers

Parameters:
    created: Only return transfers that were created during the given date interval.
    destination: Only return transfers for the destination specified by this account ID.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    transfer_group: Only return transfers with the specified transfer group."""
		...
	def create(*, amount=None, currency=None, description=None, destination=None, expand=None, metadata=None, source_transaction=None, source_type=None, transfer_group=None):
		"""Create a transfer

Parameters:
    amount: A positive integer in cents (or local equivalent) representing how much to transfer.
    currency: Three-letter [ISO code for currency](https://www.iso.org/iso-4217-currency-codes.html) in lowercase. Must be a [supported currency](https://docs.stripe.com/currencies).
    description: An arbitrary string attached to the object. Often useful for displaying to users.
    destination: The ID of a connected Stripe account. <a href="/docs/connect/separate-charges-and-transfers">See the Connect documentation</a> for details.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    source_transaction: You can use this parameter to transfer funds from a charge before they are added to your available balance. A pending balance will transfer immediately but the funds will not become available until the original charge becomes available. [See the Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-availability) for details.
    source_type: The source balance to use for this transfer. One of `bank_account`, `card`, or `fpx`. For most users, this will default to `card`.
    transfer_group: A string that identifies this transaction as part of a group. See the [Connect documentation](https://stripe.com/docs/connect/separate-charges-and-transfers#transfer-options) for details."""
		...


class Transfers_Id_Reversals(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List all reversals

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, amount=None, description=None, expand=None, metadata=None, refund_application_fee=None):
		"""Create a transfer reversal

Parameters:
    amount: A positive integer in cents (or local equivalent) representing how much of this transfer to reverse. Can only reverse up to the unreversed amount remaining of the transfer. Partial transfer reversals are only allowed for transfers to Stripe Accounts. Defaults to the entire transfer amount.
    description: An arbitrary string which you can attach to a reversal object. This will be unset if you POST an empty value.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    refund_application_fee: Boolean indicating whether the application fee should be refunded when reversing this transfer. If a full transfer reversal is given, the full application fee will be refunded. Otherwise, the application fee will be refunded with an amount proportional to the amount of the transfer reversed."""
		...


class Transfers_Transfer(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a transfer

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, description=None, expand=None, metadata=None):
		"""Update a transfer

Parameters:
    description: An arbitrary string attached to the object. Often useful for displaying to users.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."""
		...


class Transfers_Transfer_Reversals_Id(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a reversal

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, expand=None, metadata=None):
		"""Update a reversal

Parameters:
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`."""
		...


class Treasury_Credit_Reversals(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, financial_account=None, limit=None, received_credit=None, starting_after=None, status=None):
		"""List all CreditReversals

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    financial_account: Returns objects associated with this FinancialAccount.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    received_credit: Only return CreditReversals for the ReceivedCredit ID.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    status: Only return CreditReversals for a given status."""
		...
	def create(*, expand=None, metadata=None, received_credit=None):
		"""Create a CreditReversal

Parameters:
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    received_credit: The ReceivedCredit to reverse."""
		...


class Treasury_Credit_Reversals_Credit_Reversal(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a CreditReversal

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Treasury_Debit_Reversals(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, financial_account=None, limit=None, received_debit=None, resolution=None, starting_after=None, status=None):
		"""List all DebitReversals

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    financial_account: Returns objects associated with this FinancialAccount.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    received_debit: Only return DebitReversals for the ReceivedDebit ID.
    resolution: Only return DebitReversals for a given resolution.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    status: Only return DebitReversals for a given status."""
		...
	def create(*, expand=None, metadata=None, received_debit=None):
		"""Create a DebitReversal

Parameters:
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    received_debit: The ReceivedDebit to reverse."""
		...


class Treasury_Debit_Reversals_Debit_Reversal(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a DebitReversal

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Treasury_Financial_Accounts(_StripeResourceGroup):
	def fetch(*, created=None, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List all FinancialAccounts

Parameters:
    created: Only return FinancialAccounts that were created during the given date interval.
    ending_before: An object ID cursor for use in pagination.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit ranging from 1 to 100 (defaults to 10).
    starting_after: An object ID cursor for use in pagination."""
		...
	def create(*, expand=None, features=None, metadata=None, nickname=None, platform_restrictions=None, supported_currencies=None):
		"""Create a FinancialAccount

Parameters:
    expand: Specifies which fields in the response should be expanded.
    features: Encodes whether a FinancialAccount has access to a particular feature. Stripe or the platform can control features via the requested field.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    nickname: The nickname for the FinancialAccount.
    platform_restrictions: The set of functionalities that the platform can restrict on the FinancialAccount.
    supported_currencies: The currencies the FinancialAccount can hold a balance in."""
		...


class Treasury_Financial_Accounts_Financial_Account(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a FinancialAccount

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, expand=None, features=None, forwarding_settings=None, metadata=None, nickname=None, platform_restrictions=None):
		"""Update a FinancialAccount

Parameters:
    expand: Specifies which fields in the response should be expanded.
    features: Encodes whether a FinancialAccount has access to a particular feature, with a status enum and associated `status_details`. Stripe or the platform may control features via the requested field.
    forwarding_settings: A different bank account where funds can be deposited/debited in order to get the closing FA's balance to $0
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    nickname: The nickname for the FinancialAccount.
    platform_restrictions: The set of functionalities that the platform can restrict on the FinancialAccount."""
		...


class Treasury_Financial_Accounts_Financial_Account_Close(_StripeResourceGroup):
	def create(*, expand=None, forwarding_settings=None):
		"""Close a FinancialAccount

Parameters:
    expand: Specifies which fields in the response should be expanded.
    forwarding_settings: A different bank account where funds can be deposited/debited in order to get the closing FA's balance to $0"""
		...


class Treasury_Financial_Accounts_Financial_Account_Features(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve FinancialAccount Features

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, card_issuing=None, deposit_insurance=None, expand=None, financial_addresses=None, inbound_transfers=None, intra_stripe_flows=None, outbound_payments=None, outbound_transfers=None):
		"""Update FinancialAccount Features

Parameters:
    card_issuing: Encodes the FinancialAccount's ability to be used with the Issuing product, including attaching cards to and drawing funds from the FinancialAccount.
    deposit_insurance: Represents whether this FinancialAccount is eligible for deposit insurance. Various factors determine the insurance amount.
    expand: Specifies which fields in the response should be expanded.
    financial_addresses: Contains Features that add FinancialAddresses to the FinancialAccount.
    inbound_transfers: Contains settings related to adding funds to a FinancialAccount from another Account with the same owner.
    intra_stripe_flows: Represents the ability for the FinancialAccount to send money to, or receive money from other FinancialAccounts (for example, via OutboundPayment).
    outbound_payments: Includes Features related to initiating money movement out of the FinancialAccount to someone else's bucket of money.
    outbound_transfers: Contains a Feature and settings related to moving money out of the FinancialAccount into another Account with the same owner."""
		...


class Treasury_Inbound_Transfers(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, financial_account=None, limit=None, starting_after=None, status=None):
		"""List all InboundTransfers

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    financial_account: Returns objects associated with this FinancialAccount.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    status: Only return InboundTransfers that have the given status: `processing`, `succeeded`, `failed` or `canceled`."""
		...
	def create(*, amount=None, currency=None, description=None, expand=None, financial_account=None, metadata=None, origin_payment_method=None, statement_descriptor=None):
		"""Create an InboundTransfer

Parameters:
    amount: Amount (in cents) to be transferred.
    currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    description: An arbitrary string attached to the object. Often useful for displaying to users.
    expand: Specifies which fields in the response should be expanded.
    financial_account: The FinancialAccount to send funds to.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    origin_payment_method: The origin payment method to be debited for the InboundTransfer.
    statement_descriptor: The complete description that appears on your customers' statements. Maximum 10 characters."""
		...


class Treasury_Inbound_Transfers_Id(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve an InboundTransfer

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Treasury_Inbound_Transfers_Inbound_Transfer_Cancel(_StripeResourceGroup):
	def create(*, expand=None):
		"""Cancel an InboundTransfer

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Treasury_Outbound_Payments(_StripeResourceGroup):
	def fetch(*, created=None, customer=None, ending_before=None, expand=None, financial_account=None, limit=None, starting_after=None, status=None):
		"""List all OutboundPayments

Parameters:
    created: Only return OutboundPayments that were created during the given date interval.
    customer: Only return OutboundPayments sent to this customer.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    financial_account: Returns objects associated with this FinancialAccount.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    status: Only return OutboundPayments that have the given status: `processing`, `failed`, `posted`, `returned`, or `canceled`."""
		...
	def create(*, amount=None, currency=None, customer=None, description=None, destination_payment_method=None, destination_payment_method_data=None, destination_payment_method_options=None, end_user_details=None, expand=None, financial_account=None, metadata=None, statement_descriptor=None):
		"""Create an OutboundPayment

Parameters:
    amount: Amount (in cents) to be transferred.
    currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    customer: ID of the customer to whom the OutboundPayment is sent. Must match the Customer attached to the `destination_payment_method` passed in.
    description: An arbitrary string attached to the object. Often useful for displaying to users.
    destination_payment_method: The PaymentMethod to use as the payment instrument for the OutboundPayment. Exclusive with `destination_payment_method_data`.
    destination_payment_method_data: Hash used to generate the PaymentMethod to be used for this OutboundPayment. Exclusive with `destination_payment_method`.
    destination_payment_method_options: Payment method-specific configuration for this OutboundPayment.
    end_user_details: End user details.
    expand: Specifies which fields in the response should be expanded.
    financial_account: The FinancialAccount to pull funds from.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    statement_descriptor: The description that appears on the receiving end for this OutboundPayment (for example, bank statement for external bank transfer). Maximum 10 characters for `ach` payments, 140 characters for `us_domestic_wire` payments, or 500 characters for `stripe` network transfers. The default value is "payment"."""
		...


class Treasury_Outbound_Payments_Id(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve an OutboundPayment

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Treasury_Outbound_Payments_Id_Cancel(_StripeResourceGroup):
	def create(*, expand=None):
		"""Cancel an OutboundPayment

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Treasury_Outbound_Transfers(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, financial_account=None, limit=None, starting_after=None, status=None):
		"""List all OutboundTransfers

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    financial_account: Returns objects associated with this FinancialAccount.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    status: Only return OutboundTransfers that have the given status: `processing`, `canceled`, `failed`, `posted`, or `returned`."""
		...
	def create(*, amount=None, currency=None, description=None, destination_payment_method=None, destination_payment_method_data=None, destination_payment_method_options=None, expand=None, financial_account=None, metadata=None, statement_descriptor=None):
		"""Create an OutboundTransfer

Parameters:
    amount: Amount (in cents) to be transferred.
    currency: Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    description: An arbitrary string attached to the object. Often useful for displaying to users.
    destination_payment_method: The PaymentMethod to use as the payment instrument for the OutboundTransfer.
    destination_payment_method_data: Hash used to generate the PaymentMethod to be used for this OutboundTransfer. Exclusive with `destination_payment_method`.
    destination_payment_method_options: Hash describing payment method configuration details.
    expand: Specifies which fields in the response should be expanded.
    financial_account: The FinancialAccount to pull funds from.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    statement_descriptor: Statement descriptor to be shown on the receiving end of an OutboundTransfer. Maximum 10 characters for `ach` transfers or 140 characters for `us_domestic_wire` transfers. The default value is "transfer"."""
		...


class Treasury_Outbound_Transfers_Outbound_Transfer(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve an OutboundTransfer

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Treasury_Outbound_Transfers_Outbound_Transfer_Cancel(_StripeResourceGroup):
	def create(*, expand=None):
		"""Cancel an OutboundTransfer

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Treasury_Received_Credits(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, financial_account=None, limit=None, linked_flows=None, starting_after=None, status=None):
		"""List all ReceivedCredits

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    financial_account: The FinancialAccount that received the funds.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    linked_flows: Only return ReceivedCredits described by the flow.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    status: Only return ReceivedCredits that have the given status: `succeeded` or `failed`."""
		...


class Treasury_Received_Credits_Id(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a ReceivedCredit

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Treasury_Received_Debits(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, financial_account=None, limit=None, starting_after=None, status=None):
		"""List all ReceivedDebits

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    financial_account: The FinancialAccount that funds were pulled from.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    status: Only return ReceivedDebits that have the given status: `succeeded` or `failed`."""
		...


class Treasury_Received_Debits_Id(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a ReceivedDebit

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Treasury_Transaction_Entries(_StripeResourceGroup):
	def fetch(*, created=None, effective_at=None, ending_before=None, expand=None, financial_account=None, limit=None, order_by=None, starting_after=None, transaction=None):
		"""List all TransactionEntries

Parameters:
    created: Only return TransactionEntries that were created during the given date interval.
    effective_at: 
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    financial_account: Returns objects associated with this FinancialAccount.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    order_by: The results are in reverse chronological order by `created` or `effective_at`. The default is `created`.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    transaction: Only return TransactionEntries associated with this Transaction."""
		...


class Treasury_Transaction_Entries_Id(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a TransactionEntry

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Treasury_Transactions(_StripeResourceGroup):
	def fetch(*, created=None, ending_before=None, expand=None, financial_account=None, limit=None, order_by=None, starting_after=None, status=None, status_transitions=None):
		"""List all Transactions

Parameters:
    created: Only return Transactions that were created during the given date interval.
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    financial_account: Returns objects associated with this FinancialAccount.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    order_by: The results are in reverse chronological order by `created` or `posted_at`. The default is `created`.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    status: Only return Transactions that have the given status: `open`, `posted`, or `void`.
    status_transitions: A filter for the `status_transitions.posted_at` timestamp. When using this filter, `status=posted` and `order_by=posted_at` must also be specified."""
		...


class Treasury_Transactions_Id(_StripeResourceGroup):
	def fetch(*, expand=None):
		"""Retrieve a Transaction

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...


class Webhook_Endpoints(_StripeResourceGroup):
	def fetch(*, ending_before=None, expand=None, limit=None, starting_after=None):
		"""List all webhook endpoints

Parameters:
    ending_before: A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    expand: Specifies which fields in the response should be expanded.
    limit: A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    starting_after: A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list."""
		...
	def create(*, api_version=None, connect=None, description=None, enabled_events=None, expand=None, metadata=None, url=None):
		"""Create a webhook endpoint

Parameters:
    api_version: Events sent to this endpoint will be generated with this Stripe Version instead of your account's default Stripe Version.
    connect: Whether this endpoint should receive events from connected accounts (`true`), or from your account (`false`). Defaults to `false`.
    description: An optional description of what the webhook is used for.
    enabled_events: The list of events to enable for this endpoint. You may specify `['*']` to enable all events, except those that require explicit selection.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    url: The URL of the webhook endpoint."""
		...


class Webhook_Endpoints_Webhook_Endpoint(_StripeResourceGroup):
	def delete():
		"""Delete a webhook endpoint"""
		...
	def fetch(*, expand=None):
		"""Retrieve a webhook endpoint

Parameters:
    expand: Specifies which fields in the response should be expanded."""
		...
	def create(*, description=None, disabled=None, enabled_events=None, expand=None, metadata=None, url=None):
		"""Update a webhook endpoint

Parameters:
    description: An optional description of what the webhook is used for.
    disabled: Disable the webhook endpoint if set to true.
    enabled_events: The list of events to enable for this endpoint. You may specify `['*']` to enable all events, except those that require explicit selection.
    expand: Specifies which fields in the response should be expanded.
    metadata: Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    url: The URL of the webhook endpoint."""
		...
