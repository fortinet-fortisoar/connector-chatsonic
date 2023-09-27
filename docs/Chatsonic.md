## About the connector

This integration supports Writesonic's Chatsonic generative AI. A powerful language model with real time data
<p>This document provides information about the Writesonic Chatsonic Connector, which facilitates automated interactions, with a Writesonic Chatsonic server using FortiSOAR&trade; playbooks. Add the Writesonic Chatsonic Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Writesonic Chatsonic.</p>

### Version information

Connector Version: 1.0.0


Authored By: Naili.M

Certified: No

## Installing the connector

<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-chatsonic</pre>

## Prerequisites to configuring the connector

- You must have the credentials of Writesonic Chatsonic server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Writesonic Chatsonic server.

## Minimum Permissions Required

- Not applicable

## Configuring the connector

For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)

### Configuration parameters

<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Writesonic Chatsonic</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>API Key</td><td>Specify the API key to access Chatsonic API. You need to have at least the Business plan subscription
</td>
</tr></tbody></table>

## Actions supported by the connector

The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Ask a Question</td><td>Generates a completion for a given chat message using a pre-trained deep learning model.</td><td>chat_completions <br/>Miscellaneous</td></tr>
<tr><td>Converse With Chatsonic</td><td>Ask a question and get the AI answer based on the previous question/responses you had.</td><td>chat_conversation <br/>Miscellaneous</td></tr>
</tbody></table>

### operation: Ask a Question

#### Input parameters

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Message</td><td>Specify the message for which you want to generate a chat completion. Use this field to write your question
</td></tr><tr><td>Enable Google Search</td><td>If enabled, ChatSonic will use Google search results to answer the question. This is useful when trained AI model doesn't have an answer to the question
</td></tr><tr><td>Language</td><td>Specify the language of the conversation
</td></tr></tbody></table>

#### Output

The output contains the following populated JSON schema:

<pre>{
    "message": "",
    "image_urls": []
}</pre>

### operation: Converse With Chatsonic

#### Input parameters

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Message</td><td>Specify the message for which you want to generate a chat completion. Use this field to write your latest question within the conversation
</td></tr><tr><td>Messages</td><td>Specify the previous messages of the conversation
</td></tr><tr><td>Enable Google Search</td><td>If enabled, ChatSonic will use Google search results to answer the question. This is useful when trained AI model doesn't have an answer to the question
</td></tr><tr><td>Language</td><td>Specify the language of the conversation
</td></tr></tbody></table>

#### Output

The output contains the following populated JSON schema:

<pre>{
    "message": "",
    "image_urls": []
}</pre>

## Included playbooks

The `Sample - chatsonic - 1.0.0` playbook collection comes bundled with the Writesonic Chatsonic connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Writesonic Chatsonic connector.

- Ask A Question
- Converse With Chatsonic

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
