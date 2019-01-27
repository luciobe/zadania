Playbook instaluje na localhoscie(dystrybucja CentOS) bazę Mysql.<br>
Zapisuje hasło roota do pliku /root/.my.cnf.<br>
Należy w inventory (/etc/ansible/hosts lub własnym) dodać wpis
```
localhost              ansible_connection=local
```