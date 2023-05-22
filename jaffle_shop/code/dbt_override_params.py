from dbt.cli.main import dbtRunner
dbt = dbtRunner()

# these are equivalent
dbt.invoke(["--fail-fast", "run", "--select", "tag:my_tag"])
dbt.invoke(["run"], select=["tag:my_tag"], fail_fast=True)