import sys
import argparse
from PIL import Image
import numpy as np

def process_gif_to_sprite(input_path, output_path, flip=False, loop_start=0, crop_square=False):
    # 1. 打开GIF并读取所有帧
    gif = Image.open(input_path)
    frames = []
    try:
        while True:
            frame = gif.convert("RGBA")
            frames.append(frame)
            gif.seek(gif.tell() + 1)
    except EOFError:
        pass

    n_frames = len(frames)
    print(f"原始帧数: {n_frames}")

    # 2. 循环移位（改变起始帧）
    if loop_start > 0:
        loop_start = min(loop_start, n_frames - 1)  # 防止越界
        frames = frames[loop_start:] + frames[:loop_start]
        print(f"循环起点设为第{loop_start}帧（0-index），序列已重排")

    target_count = 50
    cols, rows = 5, 10
    thumbnail_size = (160, 160)
    sprite_width, sprite_height = cols * 160, rows * 160

    # 3. 可选：中心裁切为正方形（若宽高不等）
    if crop_square:
        cropped_frames = []
        for frame in frames:
            w, h = frame.size
            if w != h:
                # 取较小边作为正方形边长
                side = min(w, h)
                left = (w - side) // 2
                top = (h - side) // 2
                right = left + side
                bottom = top + side
                frame = frame.crop((left, top, right, bottom))
            cropped_frames.append(frame)
        frames = cropped_frames
        print("已对每帧进行中心正方形裁剪")

    # 4. 调整帧数到 target_count
    if len(frames) == target_count:
        selected_frames = frames
    elif len(frames) < target_count:
        # 均匀重复填充（新逻辑）
        n_orig = len(frames)
        base = target_count // n_orig          # 每个原帧至少重复的次数
        remainder = target_count % n_orig      # 前 remainder 个原帧多重复一次
        selected_frames = []
        for i in range(n_orig):
            repeat = base + (1 if i < remainder else 0)
            selected_frames.extend([frames[i]] * repeat)
        # 确保恰好50帧（当有小数时可能多1，但整数除法保证了精确）
        selected_frames = selected_frames[:target_count]
        print(f"均匀重复填充后帧数: {len(selected_frames)}")
    else:
        # 超过50帧，均匀采样（保留首尾）
        indices = np.linspace(0, len(frames) - 1, target_count).round().astype(int)
        selected_frames = [frames[i] for i in indices]
        print(f"均匀采样后帧数: {len(selected_frames)}")

    # 5. 缩放至160x160（高质量）
    resized_frames = [f.resize(thumbnail_size, Image.LANCZOS) for f in selected_frames]

    # 6. 可选水平翻转
    if flip:
        resized_frames = [f.transpose(Image.FLIP_LEFT_RIGHT) for f in resized_frames]

    # 7. 拼合贴图集
    sprite = Image.new('RGBA', (sprite_width, sprite_height), (0, 0, 0, 0))
    for idx, img in enumerate(resized_frames):
        if idx >= target_count:
            break
        row, col = divmod(idx, cols)
        x, y = col * 160, row * 160
        sprite.paste(img, (x, y), img)

    sprite.save(output_path, 'PNG')
    print(f"贴图集已保存至: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='将GIF转换为5x10贴图集，支持多种处理选项')
    parser.add_argument('input', help='输入GIF文件')
    parser.add_argument('output', help='输出PNG文件')
    parser.add_argument('--flip', action='store_true', help='对每一帧进行左右翻转')
    parser.add_argument('--loop-start', type=int, default=0,
                        help='循环起始帧索引（0-index），例如 --loop-start 5 表示从第6帧开始')
    parser.add_argument('--crop-square', action='store_true',
                        help='在缩放前将每帧中心裁剪为正方形（以较短的边为准）')
    args = parser.parse_args()
    process_gif_to_sprite(args.input, args.output, args.flip, args.loop_start, args.crop_square)