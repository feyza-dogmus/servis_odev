# RectangleArea Servisi (ROS 2 Humble)

İki paket içerir:
- `alan_interfaces`: `RectangleArea.srv` (istek: `width`, `height`; yanıt: `area`, `success`)
- `alan_py`: servis sunucusu (`server`) ve komut satırı istemcisi (`client`)

Bonus: Negatif değerler reddedilir (`success: false`, `area: 0.0`).

## Derleme

```bash
cd ~/ros2_ws
colcon build --packages-select alan_interfaces alan_py
source install/setup.bash
```

## Çalıştırma

Terminal 1 (sunucu):
```bash
ros2 run alan_py server
```

Terminal 2 (istemci):
```bash
ros2 run alan_py client 3 4
ros2 run alan_py client -2 5
```

## ros2 service call ile doğrulama

```bash
ros2 service call /rectangle_area alan_interfaces/srv/RectangleArea "{width: 3.0, height: 4.0}"
ros2 service call /rectangle_area alan_interfaces/srv/RectangleArea "{width: -2.0, height: 5.0}"
```

## Çıktılar

İstemci:
```
[INFO] [rectangle_area_client]: 3.0 x 4.0 = 12.0
[ERROR] [rectangle_area_client]: Negatif deger gonderildi, istek reddedildi.
```

Sunucu:
```
[INFO] [rectangle_area_server]: Rectangle area service ready.
[INFO] [rectangle_area_server]: 3.0 x 4.0 = 12.0
[WARN] [rectangle_area_server]: Negatif deger reddedildi: -2.0, 5.0
```

ros2 service call (pozitif):
```
response:
alan_interfaces.srv.RectangleArea_Response(area=12.0, success=True)
```

ros2 service call (negatif, bonus):
```
response:
alan_interfaces.srv.RectangleArea_Response(area=0.0, success=False)
```
