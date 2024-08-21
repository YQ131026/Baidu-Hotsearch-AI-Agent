import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config.settings import EMAIL_SENDER, EMAIL_RECEIVER, SMTP_SERVER, SMTP_PORT, EMAIL_PASSWORD

class EmailSender:
    def __init__(self):
        # 初始化邮件发送所需的配置
        self.smtp_server = SMTP_SERVER  # SMTP服务器地址
        self.smtp_port = SMTP_PORT  # SMTP服务器端口
        self.sender_email = EMAIL_SENDER  # 发件人邮箱地址
        self.receiver_emails = EMAIL_RECEIVER  # 收件人邮箱地址列表
        self.password = EMAIL_PASSWORD  # 发件人邮箱的密码或授权码

    def send_email(self, subject, body):
        # 构建邮件对象
        message = MIMEMultipart()
        message['From'] = self.sender_email  # 设置发件人
        message['To'] = ", ".join(self.receiver_emails)  # 设置收件人（多个）
        message['Subject'] = subject  # 设置邮件主题

        # 将生成的摘要作为邮件正文
        message.attach(MIMEText(body, 'plain'))

        try:
            # 连接到SMTP服务器并启用调试输出
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.set_debuglevel(1)  # 启用调试输出（可选）
            server.starttls()  # 启用TLS加密
            server.login(self.sender_email, self.password)  # 登录SMTP服务器
            text = message.as_string()  # 将邮件内容格式化为字符串
            server.sendmail(self.sender_email, self.receiver_emails, text)  # 发送邮件给多个收件人
            server.quit()  # 关闭SMTP服务器连接
            print("Email sent successfully")  # 打印成功信息
        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}")  # 捕获并打印SMTP相关异常
        except Exception as e:
            print(f"An error occurred: {e}")  # 捕获并打印其他异常

