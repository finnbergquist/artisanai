from typing import Literal

# allowed contexts and their corresponding context info to send to LLM
ContextType = Literal[
    "Onboarding",
    "Customer Support",
    "Technical Help",
    "Billing Inquiries",
    "Product Information",
    "Feature Requests"
]

#Here is where we can add more context to the LLM to help it give useful information to the user
context_corpus = {
    "Onboarding": [
        "To create an account, go to our website and click 'Sign Up.' You'll need to provide your email address, create a password, and verify your email.",
        "For added security, we recommend enabling multi-factor authentication. Go to Settings > Security to set this up.",
        "Once signed in, you'll be greeted with a welcome tour that highlights key resources like our Knowledge Base and support channels.",
        "You can personalize your dashboard by navigating to Settings > Preferences. This allows you to choose themes, notification settings, and more.",
        "All new users are required to sign our User Agreement, which ensures compliance with our data privacy and security policies.",
        "New users can access the 'Getting Started' guide, including videos and tutorials, in the Help section to get familiar with our platform."
    ],
    "Customer Support": [
        "You can reach customer support via email at support@ourcompany.com, or through our live chat feature available on the website.",
        "Our support team is available from 9 AM to 8 PM EST for basic support, with 24/7 availability for enterprise customers.",
        "Our response times are typically within 24 hours for basic support requests and within 1 hour for high-severity issues for premium customers.",
        "If your issue persists after initial assistance, request an escalation by asking the support agent or contacting escalations@ourcompany.com.",
        "Common issues such as password resets and connectivity troubleshooting can be resolved through our self-service portal, accessible at selfhelp.ourcompany.com.",
        "When submitting a ticket, please include your user ID and screenshots of the issue to help our team address it quickly."
    ],
    "Technical Help": [
        "If you're experiencing connectivity issues, try restarting your router or checking your firewall settings as a first step.",
        "To resolve software issues, download the latest version from our website and reinstall it, as older versions may have known bugs.",
        "Our system requirements include Windows 10 or macOS 11, 8 GB of RAM, and at least 1 GB of free storage. See full requirements at tech.ourcompany.com.",
        "If needed, you can access error logs by going to Help > Diagnostics > View Logs. These logs help support agents troubleshoot effectively.",
        "Visit our FAQ section for answers to common questions, such as 'How do I reset my password?' and 'Why can't I log in?'",
        "For optimal performance, we recommend using Chrome or Firefox and clearing your browser cache regularly."
    ],
    "Billing Inquiries": [
        "Our billing cycle is monthly, with invoices generated on the 1st of each month. Payments are due by the 15th.",
        "You can update your payment method by logging into your account, going to Billing > Payment Methods, and adding a new card.",
        "Past invoices are accessible under Billing > Invoice History. Click 'Download' next to any invoice for a PDF copy.",
        "If you cancel mid-cycle, you'll receive a prorated refund for unused days in that billing period. Reach out to billing@ourcompany.com for details.",
        "We offer a 10% discount for annual subscriptions paid upfront. This discount is applied automatically during checkout.",
        "To receive alerts for upcoming payments, go to Billing > Notifications and enable reminders for your due dates."
    ],
    "Product Information": [
        "Our Basic Plan includes core features like task management and file sharing, while the Pro Plan adds project analytics and team collaboration.",
        "The Pro version supports integrations with Slack, Google Workspace, and Microsoft 365. See integrations.ourcompany.com for more details.",
        "We release updates every month, and users can review changes in the Release Notes section, accessible in the Help menu.",
        "Our product is compatible with macOS, Windows, and iOS, as well as Chrome, Firefox, and Safari browsers.",
        "You can tailor the product to your team's needs by adjusting permissions under Settings > Team Permissions.",
        "The Basic Plan includes up to 5 GB of storage, while Pro and Enterprise plans offer 50 GB and 500 GB, respectively. See plan comparison at plans.ourcompany.com."
    ],
    "Feature Requests": [
        "To request a new feature, visit feedback.ourcompany.com and fill out the request form with your description and intended use case.",
        "When submitting a feature request, provide a clear title and a brief description of how it will benefit your workflow.",
        "All requests are reviewed monthly. High-demand features are added to the roadmap, which you can view at roadmap.ourcompany.com.",
        "Once submitted, feature requests typically take 3–6 months for consideration and development, depending on priority.",
        "You will receive email updates on the status of your feature request. Sign up for notifications under the 'My Requests' section.",
        "Our community portal allows you to vote on feature requests. The most popular requests are reviewed first during our monthly planning."
    ]
}
