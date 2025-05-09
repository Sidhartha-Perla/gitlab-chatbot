---
title: Explore
description: Operations documentation page for Zendesk Explore
canonical_path: "/handbook/security/customer-support-operations/docs/zendesk/explore"
---

{{% alert title="Note" color="primary" %}}

This is all informational on Zendesk Explore. We do not maintain the content within Zendesk Explore.

{{% /alert %}}

## Overview

Zendesk Explore is a powerful analytics and reporting tool offered by Zendesk, designed to provide in-depth insights into customer support metrics and trends. With Explore, our team can analyze and visualize our support data to make informed decisions, improve customer experiences, and optimize support operations.

Explore offers a user-friendly interface that allows admins to create customized dashboards, reports, and queries without the need for coding knowledge. It integrates seamlessly with Zendesk Support, combining data from multiple sources to deliver comprehensive and actionable analytics.

Explore also offers API access, allowing you to programmatically retrieve data, create and manage queries, and integrate Explore with other systems or custom applications.

{{% alert title="Note" color="primary" %}}

Explore refreshes hourly which means Explore based data is not always real time depending on query.

{{% /alert %}}

{{% alert title="Tip" color="success" %}}

Whenever you start working on Explore yourself, please create a copy of dataset with your name or initials. This way it will preserve your own formulas in reports and dashboards you build.

{{% /alert %}}

## Meanings of Common Terms

For detailed Glossary, please visit: https://support.zendesk.com/hc/en-us/articles/4408824134810-Zendesk-Explore-glossary

## Dashboards

In Explore, Dashboards allow you to view, share, create and customize reports that give you an overview of your Zendesk data.

A dashboard consists of following components:

1. `Static widgets`: These widgets inlcude reports, images, text, shapes, and tabs, do not impact the results of a report or how users interact with your dashboard. These widgets provide static content that remains unchanged.

1. `Interactive widgets`: They  allow users to specify the specific results they want to view and how they want to view them. With interactive widgets, viewers can modify metrics or attributes, apply filters to refine results, and utilize what-if variables to perform analysis.

1. `Live data widgets`: As we use Zendesk Explore Enterprise version, we have real time live data widgets available too. These widgets provide real-time updates, ensuring that the data displayed is up-to-date and reflects the latest information available.

## Types of Dashboards

### Custom Dashboards

Custom dashboards in Zendesk Explore allow you to create personalized visualizations and reports tailored to your specific business needs. They enable you to track and analyze key metrics, monitor trends, and gain actionable insights to drive decision-making and improve your customer support operations.

{{% alert title="Tip" color="success" %}}

Always clone the Custom Dashboards whenever you want to change anything in them and work on new cloned Dashboard. You can do so by clicking the dashboard you want to clone. Click `More > Clone`.

{{% /alert %}}

## Creating Custom Dashboards

### Creating Custom Dashboard via Report Builder

To create a custom dashboard using the Report Builder in Zendesk Explore, follow these steps:

1. Open an existing report or create a new one in the Report Builder.
1. Click on the Save button, and then select Add to dashboard.
1. If you want to save the report to a new dashboard, choose the option to create a new dashboard. Enter a name for your dashboard.
1. If you prefer to save the report to an existing dashboard, select the option to use an existing dashboard and choose the desired one.
1. Click Save.

Once the confirmation message appears in the right corner, you'll see the name of the new dashboard in the top toolbar of the Report Builder. You can also find the dashboard in the dashboards library. Simply click on the dashboard name to open it.

{{% alert title="Note" color="primary" %}}

The Report Builder always displays the name of the most recently saved dashboard.

{{% /alert %}}

### Creating a Dashboard from the Dashboards Library

If you prefer to create dashboards rather than reports as part of your workflow, you can create new blank dashboards directly from the Dashboards Library. Follow these steps:

1. Click on the Dashboards Library icon (Dashboards Library Icon) on the left sidebar.
1. Click on the New dashboard option.

### Tips to create effective Dashboards

1. Define your objectives: Clearly outline the goals and objectives of your custom dashboard. Determine the specific metrics and KPIs (Key Performance Indicators) you want to track. For example, you may want to monitor ticket volume, average resolution time, or customer satisfaction scores.
1. Identify relevant data  and datasets: Determine the data sources and datasets you need to connect to your custom dashboard.
1. Select appropriate visualizations: Choose the most appropriate chart types and visualizations that effectively represent your data. Consider the nature of your metrics and the story you want to convey. Line charts, bar charts, and pie charts are commonly used, but explore other options based on your requirements.
1. Create queries: Use the Zendesk Explore Query Builder to create queries that fetch the data for your metrics. Apply filters, groupings, and calculations to generate the desired insights. Leverage the query functionality to analyze data from different angles and create multiple queries for different metrics.
1. Design an intuitive layout: Organize your charts and visualizations in a logical and intuitive manner on the dashboard. Group related metrics together and arrange them in a way that allows for easy comparison and understanding. Consider using sections, columns, and color schemes to enhance clarity.
1. Leverage dashboard interactivity: Take advantage of interactive features to enhance user experience and exploration. Add drill-through links that allow you to navigate to more detailed reports or data. Utilize filters that enable users to dynamically modify the data displayed on the dashboard.
1. Apply contextual filters: Contextual filters allow you to refine the data displayed on your dashboard based on specific criteria, such as time frames, regions, or agent performance. This helps you focus on the relevant data and gain deeper insights.
1. Regularly review and refine: Continuously review and refine your custom dashboard based on evolving business needs and feedback. Keep track of emerging trends, identify anomalies, and adjust your metrics and visualizations accordingly. Regularly revisit your objectives to ensure alignment with your dashboard content.
1. Keep your custom dashboard focused and concise. Include only the most relevant metrics to avoid clutter and information overload.
1. Use color coding and visual cues to highlight important insights or trends. This helps users quickly identify critical information.
1. Leverage text and annotations to provide context and explanations for the metrics displayed on your dashboard. This ensures clarity and understanding for dashboard users.
1. Regularly share and collaborate on your custom dashboard with relevant stakeholders. Encourage feedback and use it to improve the dashboard's effectiveness.
1. Consider setting up scheduled reports to automatically distribute the dashboard to stakeholders. This ensures timely access to updated insights without the need for manual sharing.

Remember, the key to creating an effective custom dashboard lies in aligning it with your business objectives, selecting relevant metrics, and presenting the data in a visually appealing and easily understandable manner. Regularly review and update your custom dashboard to ensure its continued relevance and usefulness.
