provider "yandex" {
  token                    = "$YC_TOKEN"
  cloud_id                 = "$YC_CLOUD_ID"
  folder_id                = "$YC_FOLDER_ID"
  zone                     = "ru-central1-a"
}



#image id fd816r0lmfvlh6r9uos5
#famaly id ubuntu-2004-lts-a100

resource "yandex_compute_image" "netology-image" {
  name                      = "srv01-image"
  folder_id = "$YC_FOLDER_ID"
  min_disk_size = "50"
  os_type = "LINUX"
  source_image = "fd816r0lmfvlh6r9uos5"
}
