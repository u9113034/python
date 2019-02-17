# ex2.py
import pygal.maps.world

worldMap = pygal.maps.world.World()                         # 建立世界地圖物件
worldMap.title = ' 英語, 阿拉伯, 西班牙' # 世界地圖標題
worldMap.add('英語系國家',['at', 'au', 'eg'])                     # 標記英語系
worldMap.add('阿拉伯語系國家',['ke', 'ir', 'il'])                   # 標記阿拉伯語系
worldMap.add('西班牙文語系國家',['ar', 'cu', 'uy'])                   # 標記西班牙文語系
worldMap.render_to_file('out24_2.svg')                     # 儲存地圖檔案


