@echo on

rem
rem 指定queryExecutionListeners参数的spark-submit.cmd脚本
rem

cmd /V /E /C "spark-submit.cmd  --conf spark.sql.queryExecutionListeners=org.example.framework.LineageListener --jars demo-scala-1.0-SNAPSHOT.jar %*"
