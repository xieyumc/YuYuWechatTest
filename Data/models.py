from django.db import models
from django_cron import CronJobBase, Schedule

class Message(models.Model):
    wechat_name = models.CharField(max_length=100)
    message = models.TextField()
    send_time = models.CharField(max_length=100, help_text="Cron expression for send time")

    def __str__(self):
        return f"{self.wechat_name}: {self.message} at {self.send_time}"

class SendMessageCronJob(CronJobBase):
    RUN_EVERY_MINS = 1  # 每隔1分钟检查一次

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'scheduler.send_message_cron_job'  # 唯一标识cron job

    def do(self):
        # 在这里实现消息发送逻辑
        # 例如：遍历所有消息，检查当前时间是否匹配send_time的cron表达式，如果匹配则发送消息
        pass