# Trắc nghiệm toeic theo chủ đề
## Test bot
* Search trên telegram bot 'LoveYourSmile'
* Bắt đầu bằng lệnh '/study'
## Các bước kiểm tra
* Từ vựng được chia theo chủ đề, chọn chủ để để tiến hành ôn tập. 
* Có kết quả số câu đúng khi kết thúc kiểm tra
* Những câu sai sẽ được lưu vào topic 'memo' để kiểm tra lại, vào tự xóa sau khi trả lời đúng hoặc sau 7 ngày

| Chọn chủ đề | Kiểm tra | Kiểm tra lại câu sai |
| --- | --- | --- |
| ![image](https://user-images.githubusercontent.com/36092539/93729416-92afbb80-fbee-11ea-916d-2f81fe875069.png) | [![image](https://user-images.githubusercontent.com/36092539/93729279-fc7b9580-fbed-11ea-90af-ffe5349054c2.png)]()| [![CoreUI Pro Bootstrap Admin Template](https://user-images.githubusercontent.com/36092539/93729896-8cbada00-fbf0-11ea-8402-ca45994a3e75.png)]()

## Build và deploy code
* Thay đổi thông tin tại file docker /.env (build 3 container: redis, bot-core, mongo)
* Chạy lệnh sau để build tại localhost:
```bash
set .env && docker-compose up -d --build
```
![Screenshot from 2020-09-23 16-11-05](https://user-images.githubusercontent.com/36092539/93992271-8d519d00-fdb7-11ea-8e18-a51c0ee062c2.png)

Deploy code lên host:
* Thay host tại file /deployment/hosts
* Chạy ansible để deploy + run container trên host:
```bash
ansible-playbook -i deployment/hosts deployment/site.yml -l telebot -t telebot -u {username}
```