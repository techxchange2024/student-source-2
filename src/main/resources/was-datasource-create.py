#
# Create a datasource for the application
# Assumes a node scoped JDBC provider (/Node:<insert node here>/JDBCProvider:DB2JDBC01/) is already configured in the WAS installation
# Assumes a node scoped the auth alias (<insert node here>/prod01AuthAlias) is already configured in the WAS installation
#
#
print('[INFO] Creating data source for ModResorts')

node_name = AdminControl.getNode()
cell_name = AdminControl.getCell()
auth_alias = node_name + '/db2inst'
db2_server = '172.17.0.2'  # change as required
db2_port = '50000'  # change as required

ds = AdminConfig.getid('/DataSource:ModResortsDs/')
if not ds:
	print '[INFO] Datasource does not already exist. Will create now.'
else:
	print '[INFO] Datasource already exists. Delete and recreate'
	AdminTask.deleteDatasource(ds)

AdminTask.createAuthDataEntry('[-alias ' + auth_alias + ' -user db2inst1 -password db2pass ]')
AdminTask.createJDBCProvider('[-scope Node=' + node_name +' -databaseType DB2 -providerType "DB2 Using IBM JCC Driver" -implementationType "XA data source" -name DB2JDBC01 -classpath [/db-drivers/db2jcc.jar /db-drivers/db2jcc_license_cu.jar /db-drivers/db2jcc_license_cisuz.jar ] ]')
db2JdbcProvider = AdminConfig.getid('/Node:' + node_name + '/JDBCProvider:DB2JDBC01/')

AdminTask.createDatasource(db2JdbcProvider, '[-name "ModResortsDs" -jndiName jdbc/ModResortsJndi -containerManagedPersistence true -componentManagedAuthenticationAlias ' + node_name + '/' + auth_alias + ' -xaRecoveryAuthAlias ' + node_name + '/' + auth_alias + ' -dataStoreHelperClassName com.ibm.websphere.rsadapter.DB2UniversalDataStoreHelper -configureResourceProperties [[databaseName java.lang.String PROD01] [driverType java.lang.Integer 4] [serverName java.lang.String ' + db2_server + '] [portNumber java.lang.Integer ' + db2_port +']]]')
newDs = AdminConfig.getid('/DataSource:ModResortsDs/')
AdminConfig.create('MappingModule', newDs, '[[authDataAlias ' + node_name + '/' + auth_alias + '] [mappingConfigAlias DefaultPrincipalMapping]]')
newCF = AdminConfig.getid('/CMPConnectorFactory:ModResortsDs_CF/')
AdminConfig.modify(newCF, '[[name "ModResortsDs_CF"] [authDataAlias "'+ node_name + '/' + auth_alias + '"] [xaRecoveryAuthAlias "'+ node_name + '/' + auth_alias + '"]]')
AdminConfig.create('MappingModule', newCF, '[[authDataAlias ' + node_name +'/' + auth_alias + '] [mappingConfigAlias DefaultPrincipalMapping]]')

print('[INFO] Saving config')
AdminConfig.save()

print('[INFO] Testing connection...')
AdminControl.testConnection(newDs)
print('[INFO] Finished testing connection.')

print('[INFO] Finished creating data source for ModResorts')
