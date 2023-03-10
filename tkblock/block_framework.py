#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# kuri_pome
"""BlockFramework"""
import tkinter as tk
from tkinter import ttk
import dataclasses
from typing import Any

from .canvas import ResizingCanvas


PLACE_TAGET_OBJECTS: list[str] = list(
    set(
        # subclassのsubclassをとりたいため。
        # [cls.__name__ for cls in ttk.Widget.__subclasses__()]
        ttk.__all__
        + [cls.__name__ for cls in tk.Widget.__subclasses__()]
        + ["ResizingCanvas", "BlockFrameBase"]
    )
)


class BlockFramework(tk.Tk):
    """WidgetをBlock形式で指定することで配置操作を行うためのFramework

    Args:
        tk (tk.Tk): tk.Tk
    """

    def __init__(self, max_col: int, max_row: int, width: int, height: int) -> None:
        """コンストラクタ

        Args:
            max_col (int): 分割を行う行数
            max_row (int): 分割を行う列数
            width (int): frameの横幅
            height (int): frameの縦幅
        """

        super().__init__()
        self.max_col: int = max_col
        self.max_row: int = max_row
        self.width: int = width
        self.height: int = height
        self._name: str = "main"
        super().geometry(f"{width}x{height}")

    def _override_valiable(
        self, default_valiable: Any, attribute_name: str, class_object: Any
    ) -> Any:
        """値の上書きリターン

        クラスオブジェクトの属性をチェックして、属性が定義されている場合は、
        それをデフォルト値の代わりに返します。属性が定義されていない場合は、
        デフォルト値を返します。

        Args:
            default_valiable (Any): デフォルトの値
            attribute_name (str): チェックする属性名
            class_object (Any): クラスオブジェクト

        Returns:
            Any: デフォルト値またはクラスオブジェクトの属性
        """
        valiable: Any = default_valiable
        if hasattr(class_object, attribute_name):
            valiable = getattr(class_object, attribute_name)
        return valiable

    def _acquire_calc_place_info(
        self, frame_widget: Any
    ) -> tuple[int, int, int, int, float, float]:
        """FrameにWidgetを配置するための情報取得する。

        Args:
             frame_widget (Any): 定義している先の対象class object

        Returns:
            Tuple[int, int, int, int, float, float]: 列数、行数、幅、高さ、列サイズ、行サイズのタプル
        """
        col_num: int = self._override_valiable(self.max_col, "max_col", frame_widget)
        row_num: int = self._override_valiable(self.max_row, "max_row", frame_widget)
        width: int = self._override_valiable(self.width, "width", frame_widget)
        height: int = self._override_valiable(self.height, "height", frame_widget)
        col_size: float = width / col_num
        row_size: float = height / row_num
        return col_num, row_num, width, height, col_size, row_size

    def _calc_place_rel(
        self,
        width: int,
        height: int,
        col_size: int,
        row_size: int,
        col_start: int = 0,
        col_end: int = 1,
        row_start: int = 0,
        row_end: int = 1,
        pad_left: float = 0,
        pad_right: float = 0,
        pad_up: float = 0,
        pad_down: float = 0,
    ) -> tuple[float, float, float, float]:
        """指定された列や行、空白設定から、placeで指定するrelを計算する。

        Args:
            width (int): フレームの横幅
            height (int): フレームの縦幅
            col_size (int): 列サイズ
            row_size (int): 行サイズ
            col_start (int, optional): 列の開始位置. Defaults to 0.
            col_end (int, optional): 列の終了位置. Defaults to 1.
            row_start (int, optional): 行の開始位置. Defaults to 0.
            row_end (int, optional): 行の終了位置. Defaults to 1.
            pad_left (float, optional): 横幅の左側の空白割合. Defaults to 0.
            pad_right (float, optional): 横幅の右側の空白割合. Defaults to 0.
            pad_up (float, optional): 縦幅の上側の空白割合. Defaults to 0.
            pad_down (float, optional): 縦幅の下側の空白割合. Defaults to 0.

        Returns:
            dict: placeで指定する値
        """
        values: dict = {}
        # チェックをコメントアウト、paddingがlayout合計でのpaddingではないため
        # check
        # if pad_left + pad_right >= col_end - col_start:
        #     raise Exception(
        #         f"width_padding value error: {pad_left + pad_right} >= {col_end - col_start}"
        #     )
        # if pad_up + pad_down >= row_end - row_start:
        #     raise Exception(
        #         f"height_padding value error: {pad_up + pad_down} >= {row_end - row_start}"
        #     )

        # relx
        width_start: float = col_size * col_start
        width_end: float = col_size * col_end
        pad_left_size: float = col_size * pad_left
        pad_right_size: float = col_size * pad_right
        width_object_start: float = width_start + pad_left_size
        width_object_end: float = width_end - pad_right_size
        width_object_size: float = width_object_end - width_object_start
        values["relx"]: float = width_object_start / width
        values["relwidth"]: float = width_object_size / width
        # rely
        height_start: float = row_size * row_start
        height_end: float = row_size * row_end
        pad_up_size: float = row_size * pad_up
        pad_down_size: float = row_size * pad_down
        height_object_start: float = height_start + pad_up_size
        height_object_end: float = height_end - pad_down_size
        height_object_size: float = height_object_end - height_object_start
        values["rely"]: float = height_object_start / height
        values["relheight"]: float = height_object_size / height
        return values

    def _place_widget(
        self,
        widget: Any,
        width: int,
        height: int,
        col_size: float,
        row_size: float,
    ) -> None:
        """Widgetを配置する

        Args:
            frame (Any): 配置先のフレーム
            value (Any): 配置対象のウィジェット
            width (int): 配置するフレームの横幅
            height (int): 配置するフレームの縦幅
            col_size (int): 列サイズ
            row_size (int): 行サイズ
            frame (BlockFrameBase): 配置するフレーム
        """
        # objcetが最初に置く対象のクラスなら終了
        if widget.__class__.__name__ not in PLACE_TAGET_OBJECTS:
            raise Exception(f"cannot place object error: {widget.__class__.__name__}")
        # layout属性を持っていないなら終了
        # Frameの下に直接配置しているものはここでreturn
        if not ("layout" in dir(widget)):
            return
        widget.place(
            self._calc_place_rel(
                width,
                height,
                col_size,
                row_size,
                **dataclasses.asdict(widget.layout),
            )
        )

    def place_frame_widget(self, frame: Any = None) -> None:
        """Frame上のwidgetを全て配置する。

        Layout指定をしている全てのwidgetを配置する。
        この関数は、Frame配下に子Frameを考慮して、再起処理で実現している。

        Args:
            frame (Any, optional): 配置する先のFrame. Defaults to None.
        """
        frame: Any = self if frame is None else frame
        width: int
        height: int
        col_size: float
        row_size: float
        (
            _,
            _,
            width,
            height,
            col_size,
            row_size,
        ) = self._acquire_calc_place_info(frame)
        for name, widget in frame.children.items():
            if widget.__class__.__name__ == "Menu":
                # rootフレームの配下のBlockFrameBaseのみが対象。Menu等は何もしない。
                continue
            elif widget.__class__.__name__ == "BlockFrameBase":
                # BlockFrameBaseは作成時に配置するので配置処理は不要。
                # widgetを配置するため再起処理のみ実施
                if hasattr(widget, "layout"):
                    self._place_widget(widget, width, height, col_size, row_size)
                self.place_frame_widget(frame=widget)
            elif widget.__class__.__name__ == "Frame":
                # FrameはFrameの配置を実施。
                self._place_widget(widget, width, height, col_size, row_size)
                # Frameは配置後にサイズが判明するため、ここでサイズをセット
                widget.update_idletasks()
                widget.width = widget.winfo_width()
                widget.height = widget.winfo_height()
                # Frame内のWidgetを配置するための再起処理を実施。
                self.place_frame_widget(frame=widget)
            else:
                # 上記以外は、Widgetのみになるので配置処理を実施。
                self._place_widget(widget, width, height, col_size, row_size)
        # 最後にFrameを最前面に移動しておく。
        for _, widget in frame.children.items():
            if widget.__class__.__name__ in ("Frame", "BlockFrameBase"):
                widget.tkraise()

    def _write_auxiliary_line(self, frame: Any, widget: ResizingCanvas) -> None:
        """debug用に補助線を引く

        Args:
            frame (_type_):  Canvasを保持しているFrameまたは、その上位のFrame
            widget (ResizingCanvas): 補助線を引くcanvas
        """
        col_num: int
        row_num: int
        col_size: float
        row_size: float
        col_num, row_num, _, _, col_size, row_size = self._acquire_calc_place_info(
            frame
        )
        start_y: int = 0
        end_y: int = widget.height
        start_x: int = 0
        end_x: int = widget.width
        for index in range(0, col_num):
            x: int = int(index * col_size)
            widget.create_line(x, start_y, x, end_y)
        for index in range(0, row_num):
            y: int = int(index * row_size)
            widget.create_line(start_x, y, end_x, y)

    def create_auxiliary_line(self, frame: Any = None) -> None:
        """補助線を作成する

        この関数は、Frame配下に子Frameを考慮して、再起処理で実現している。

        Args:
            frame (Any, optional): Canvasを保持しているFrameまたは、その上位のFrame. Defaults to None.
        """
        frame: Any = self if frame is None else frame
        for name, widget in frame.children.items():
            if widget.__class__.__name__ == "ResizingCanvas":
                self._write_auxiliary_line(frame, widget)
            if widget.__class__.__name__ in ("Frame", "BlockFrameBase"):
                self.create_auxiliary_line(widget)
