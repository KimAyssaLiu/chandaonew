### chandaopms8.2(禅道项目管理软件v8.2)

- 使用本地压缩包构建`chandaopmsv8.2`，源码包仅限在ubuntu16 64bit及以下版本、centos7.3 64bit及以下版本系统使用

- 当前测试环境：Ubuntu16.04 Desktop

- 构建及运行方法：
  
  - `sudo docker build --no-cache -t dve ./`
  - `sudo docker run --name dve -p 80:80 -v /data/www:/app/zentaopms -v /data/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 -d dve:latest`