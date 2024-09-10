#
# Create a datasource for the application
# Assumes a node scoped JDBC provider (/Node:<insert node here>/JDBCProvider:DB2JDBC01/) is already configured in the WAS installation
# Assumes a node scoped the auth alias (<insert node here>/prod01AuthAlias) is already configured in the WAS installation
#
#
print('[INFO] Creating MQ Connection Factory for ModResorts')

node_name = AdminControl.getNode()
cell_name = AdminControl.getCell()
auth_alias = node_name + '/wmqDetails'

AdminTask.createAuthDataEntry('[-alias ' + auth_alias + ' -user mqmx1 -password MyMqPass ]')

# AdminTask.createWMQConnectionFactory('WebSphere MQ JMS Provider(cells/' + cell_name +'/nodes/' + node_name + '|resources.xml#builtin_mqprovider)', '[-type CF -name mq -jndiName jms/mmxCf -description -qmgrName MMX_QM -wmqTransportType BINDINGS_THEN_CLIENT -qmgrSvrconnChannel -qmgrHostname demo-data-vm1.fyre.ibm.com -mappingAlias DefaultPrincipalMapping -containerAuthAlias DefaultNode01/wmqDetails -componentAuthAlias -xaRecoveryAuthAlias DefaultNode01/wmqDetails -support2PCProtocol true -clonedSubs DISABLED ]')
AdminTask.createWMQConnectionFactory('"WebSphere MQ JMS Provider(cells/DefaultCell01/nodes/DefaultNode01|resources.xml#builtin_mqprovider)"', '[-type CF -name MQ -jndiName jms/mmxCf -description -qmgrName MMX_QM -wmqTransportType BINDINGS_THEN_CLIENT -qmgrSvrconnChannel -qmgrHostname demo-data-vm1.fyre.ibm.com -mappingAlias DefaultPrincipalMapping -containerAuthAlias DefaultNode01/wmqDetails -componentAuthAlias -xaRecoveryAuthAlias DefaultNode01/wmqDetails -support2PCProtocol true -clonedSubs DISABLED ]')
AdminTask.createWMQQueue('DefaultNode01(cells/DefaultCell01/nodes/DefaultNode01|node.xml)', '[-name jmsQueue -jndiName jms/mmxQueue -queueName MMX_Q01 ]')
mqCf = AdminConfig.getid('/MQConnectionFactory:MQ/')

AdminConfig.modify(mqCf, '[[authDataAlias "'+ node_name + '/' + auth_alias + '"] [xaRecoveryAuthAlias "'+ node_name + '/' + auth_alias + '"]]')
AdminConfig.create('MappingModule', mqCf, '[[authDataAlias "' + node_name + '/' + auth_alias + '"] [mappingConfigAlias DefaultPrincipalMapping]]')
AdminConfig.save()