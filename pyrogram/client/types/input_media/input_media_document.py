# Pyrogram - Telegram MTProto API Client Library for Python
# Copyright (C) 2017-2019 Dan Tès <https://github.com/delivrance>
#
# This file is part of Pyrogram.
#
# Pyrogram is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyrogram is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from typing import Union

from . import InputMedia


class InputMediaDocument(InputMedia):
    """A generic file to be sent inside an album.

    Parameters:
        media (``str``):
            File to send.
            Pass a file_id as string to send a file that exists on the Telegram servers or
            pass a file path as string to upload a new file that exists on your local machine.

        thumb (``str``):
            Thumbnail of the file sent.
            The thumbnail should be in JPEG format and less than 200 KB in size.
            A thumbnail's width and height should not exceed 320 pixels.
            Thumbnails can't be reused and can be only uploaded as a new file.

        caption (``str``, *optional*):
            Caption of the document to be sent, 0-1024 characters

        parse_mode (``str``, *optional*):
            By default, texts are parsed using both Markdown and HTML styles.
            You can combine both syntaxes together.
            Pass "markdown" or "md" to enable Markdown-style parsing only.
            Pass "html" to enable HTML-style parsing only.
            Pass None to completely disable style parsing.
    """

    __slots__ = ["thumb"]

    def __init__(
        self,
        media: str,
        thumb: str = None,
        caption: str = "",
        parse_mode: Union[str, None] = object
    ):
        super().__init__(media, caption, parse_mode)

        self.thumb = thumb
