import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

def draw_premium_jieba_logo(output_file='jieba_logo_enhanced.png'):
    # 配置参数
    canvas_width, canvas_height = 12, 6
    fig, ax = plt.subplots(figsize=(canvas_width, canvas_height), dpi=150)
    ax.set_xlim(0, canvas_width)
    ax.set_ylim(0, canvas_height)
    ax.set_aspect('equal')
    ax.axis('off')

    # --- 颜色定义 (更现代的调色板) ---
    # 文字：深邃蓝
    text_color = '#2C3E50' 
    # 图形：从深青到明亮的翠绿渐变
    colors = ['#1F77B4', '#2CA02C', '#48C9B0', '#7DCEA0']
    alphas = [0.9, 0.75, 0.6, 0.45] # 逐渐变透明增加空间感

    # --- 1. 绘制五边形 (沿着抛物线轨迹) ---
    def get_pentagon_verts(center, size, rotation_deg):
        angles = np.linspace(0, 2*np.pi, 6)[:-1] + np.deg2rad(rotation_deg)
        # 稍微压缩一下 Y 轴，让五边形看起来更有动感
        return np.column_stack([
            center[0] + size * np.cos(angles),
            center[1] + size * 0.85 * np.sin(angles)
        ])

    # 轨迹点 (x, y), 大小, 旋转角度
    steps = [
        {'pos': (1.8, 2.2), 'size': 1.0,  'rot': 15},
        {'pos': (3.2, 3.4), 'size': 0.75, 'rot': 35},
        {'pos': (4.5, 4.0), 'size': 0.55, 'rot': 55},
        {'pos': (5.6, 4.3), 'size': 0.4,  'rot': 75},
    ]

    for i, step in enumerate(steps):
        verts = get_pentagon_verts(step['pos'], step['size'], step['rot'])
        poly = patches.Polygon(
            verts, 
            closed=True, 
            color=colors[i], 
            alpha=alphas[i],
            ec='white',     # 白色极细边框增加精致感
            lw=1,
            antialiased=True,
            zorder=10-i
        )
        ax.add_patch(poly)
        
        # 添加微弱阴影
        shadow_verts = verts + 0.04
        shadow = patches.Polygon(
            shadow_verts, 
            closed=True, 
            color='black', 
            alpha=0.05, 
            zorder=1
        )
        ax.add_patch(shadow)

    # --- 2. 绘制文字 "结巴分词" ---
    # 尝试加载中文字体，按优先级排序
    plt.rcParams['font.sans-serif'] = ['SimHei', 'PingFang SC', 'Microsoft YaHei', 'WenQuanYi Micro Hei', 'sans-serif']
    plt.rcParams['axes.unicode_minus'] = False
    
    text_content = "结巴分词"
    start_x = 3.2
    for i, char in enumerate(text_content):
        ax.text(start_x + i*1.3, 1.3, char, 
                fontsize=85, 
                color=text_color, 
                fontweight='bold', 
                va='center', 
                ha='center',
                zorder=20)

    # 保存文件
    plt.savefig(output_file, bbox_inches='tight', transparent=True)
    print(f"Success: Image saved as {os.path.abspath(output_file)}")

if __name__ == "__main__":
    try:
        draw_premium_jieba_logo()
    except Exception as e:
        print(f"Error: {e}")
