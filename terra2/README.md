1. задание 1 с вариантом yandex cloud выполнено
2. при помощи какого инструмента (из разобранных на прошлом занятии) можно создать свой образ ami?  
`С помощью Packer`  
3. Ссылку на репозиторий с исходной конфигурацией терраформа - https://github.com/S-Stanislav524/devops-netology/tree/main/terra2/src
```bash
~/devops-netology/terra2/src$ terraform plan

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # yandex_compute_image.netology-image will be created
  + resource "yandex_compute_image" "netology-image" {
      + created_at      = (known after apply)
      + folder_id       = "$YC_FOLDER_ID"
      + id              = (known after apply)
      + min_disk_size   = 50
      + name            = "srv01-image"
      + os_type         = "LINUX"
      + pooled          = (known after apply)
      + product_ids     = (known after apply)
      + size            = (known after apply)
      + source_disk     = (known after apply)
      + source_family   = (known after apply)
      + source_image    = "fd816r0lmfvlh6r9uos5"
      + source_snapshot = (known after apply)
      + source_url      = (known after apply)
      + status          = (known after apply)
    }

Plan: 1 to add, 0 to change, 0 to destroy.

──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform apply" now.
```