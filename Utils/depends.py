from demo import models
def get_servername(host_id):
    data=models.Server.objects.filter(id=host_id).values("")