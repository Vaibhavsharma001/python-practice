class Storage:
    def upload(self, filename):
        print(f"Uploading {filename}")


class AWSStorage(Storage):
    def upload(self, filename):
        print(f"Uploading {filename} to AWS")


class GoogleStorage(Storage):
    def upload(self, filename):
        print(f"Uploading {filename} to Google Cloud")


class AzureStorage(Storage):
    def upload(self, filename):
        print(f"Uploading {filename} to Azure")


storage = AWSStorage()
storage.upload("resume.pdf")