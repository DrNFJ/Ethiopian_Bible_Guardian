/**
 * AWS Amplify Configuration
 * This configuration is used for AWS Amplify Hosting and backend services.
 */

const amplifyConfig = {
  aws_project_region: 'us-east-1',
  aws_cognito_identity_pool_id: import.meta.env.VITE_COGNITO_IDENTITY_POOL_ID || undefined,
  aws_cognito_region: 'us-east-1',
  aws_user_pools_id: import.meta.env.VITE_COGNITO_USER_POOL_ID || undefined,
  aws_user_pools_web_client_id: import.meta.env.VITE_COGNITO_WEB_CLIENT_ID || undefined,
  oauth: {},
  aws_appsync_graphqlEndpoint: import.meta.env.VITE_APPSYNC_ENDPOINT || undefined,
  aws_appsync_region: 'us-east-1',
  aws_appsync_authenticationType: 'AWS_IAM',
  aws_appsync_apiKey: import.meta.env.VITE_APPSYNC_API_KEY || undefined,
};

export default amplifyConfig;
