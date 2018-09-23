import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def plot_text(text):
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')
    xs, ys = [], []
    for t in text:
        xs.extend([t[0], t[1]])
        ys.extend([t[2], t[3]])
        ax.add_patch(
            patches.Rectangle(
                (t[0], t[1]),
                t[2] - t[0],
                t[3] - t[1]
            )
        )
    ax.set_xlim(min(xs) - 10, max(xs) + 10)
    ax.set_ylim(min(ys) - 10, max(ys) + 10)
    plt.show()


def plot_table(table):
    for row in table.cells:
        for cell in row:
            if cell.left:
                plt.plot([cell.lb[0], cell.lt[0]],
                            [cell.lb[1], cell.lt[1]])
            if cell.right:
                plt.plot([cell.rb[0], cell.rt[0]],
                            [cell.rb[1], cell.rt[1]])
            if cell.top:
                plt.plot([cell.lt[0], cell.rt[0]],
                            [cell.lt[1], cell.rt[1]])
            if cell.bottom:
                plt.plot([cell.lb[0], cell.rb[0]],
                            [cell.lb[1], cell.rb[1]])
    plt.show()


def plot_contour(image):
    img, table_bbox = image
    for t in table_bbox.keys():
        cv2.rectangle(img, (t[0], t[1]),
                      (t[2], t[3]), (255, 0, 0), 20)
    plt.imshow(img)
    plt.show()


def plot_joint(image):
    img, table_bbox = image
    x_coord = []
    y_coord = []
    for k in table_bbox.keys():
        for coord in table_bbox[k]:
            x_coord.append(coord[0])
            y_coord.append(coord[1])
    max_x, max_y = max(x_coord), max(y_coord)
    plt.plot(x_coord, y_coord, 'ro')
    plt.axis([0, max_x + 100, max_y + 100, 0])
    plt.imshow(img)
    plt.show()


def plot_line(segments):
    vertical, horizontal = segments
    for v in vertical:
        plt.plot([v[0], v[2]], [v[1], v[3]])
    for h in horizontal:
        plt.plot([h[0], h[2]], [h[1], h[3]])
    plt.show()