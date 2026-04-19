import os

import numpy as np
import svgwrite


def draw_premium_jieba_svg(output_file='jieba_logo_enhanced.svg'):
    # 创建画布 (宽 800, 高 400)
    dwg = svgwrite.Drawing(output_file, profile='full', size=(800, 400))

    # --- 颜色与样式配置 ---
    text_color = '#2C3E50'
    colors = ['#1F77B4', '#2CA02C', '#48C9B0', '#7DCEA0']
    opacities = [0.9, 0.75, 0.6, 0.45]

    # --- 1. 绘制五边形 ---
    def get_pentagon_points(center, size, rotation_deg):
        angles = np.linspace(0, 2 * np.pi, 6)[:-1] + np.deg2rad(rotation_deg)
        points = []
        for a in angles:
            # 同样应用 0.85 的 Y 轴压缩
            px = center[0] + size * np.cos(a)
            py = center[1] + size * 0.85 * np.sin(a)
            points.append((float(px), float(py)))
        return points

    # 轨迹定义 (SVG 坐标系：左上角为 0,0)
    steps = [
        {'pos': (150, 200), 'size': 60, 'rot': 15},
        {'pos': (250, 120), 'size': 45, 'rot': 35},
        {'pos': (350, 80), 'size': 35, 'rot': 55},
        {'pos': (430, 65), 'size': 25, 'rot': 75},
    ]

    for i, step in enumerate(steps):
        pts = get_pentagon_points(step['pos'], step['size'], step['rot'])

        # 绘制阴影 (稍微偏移)
        shadow_pts = [(p[0] + 3, p[1] + 3) for p in pts]
        dwg.add(dwg.polygon(shadow_pts, fill='black', fill_opacity=0.05))

        # 绘制五边形主体
        dwg.add(dwg.polygon(pts, fill=colors[i], fill_opacity=opacities[i], stroke='white', stroke_width=1.5))

    # --- 2. 绘制文字 "结巴分词" ---
    # SVG 中处理中文字体主要依赖系统安装的字体名称
    font_group = dwg.g(
        style=f"fill:{text_color}; font-family: 'PingFang SC', 'Microsoft YaHei', 'SimHei', sans-serif; font-weight: bold; font-size: 80px;"
    )

    chars = '结巴分词'
    start_x = 220
    base_y = 320
    spacing = 95

    for i, char in enumerate(chars):
        font_group.add(dwg.text(char, insert=(start_x + i * spacing, base_y)))

    dwg.add(font_group)

    # 保存文件
    dwg.save()
    print(f'Success: SVG Logo saved as {os.path.abspath(output_file)}')


if __name__ == '__main__':
    try:
        draw_premium_jieba_svg()
    except Exception as e:
        print(f'Error: {e}')
