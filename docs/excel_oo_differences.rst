
.. excel_oo_differences

Excel/OpenOffice Differences
============================

Master Styles
-------------

When displaying a page, Excel seems to honor the 
``draw:style-name`` of the ``style:master-page`` in ``styles.xml``
whereas OpenOffice and LibreOffice seem to honor the 
``presentation:style-name`` of the ``draw:page`` in ``content.xml``

ODPSlides therefore makes a new style:master-page and a new draw:page for each slide.

Scratch That
------------

**New Info**
Seems like the ``'presentation:background-visible'`` attribute of the ``style:drawing-page-properties``
style element needs to be "false".

``style:drawing-page-properties`` is a child of the ``style:style``  element with ``style:family="drawing-page"``

I Surrender
-----------

I added a flag to target Excel or not. Right now I think the un-targeted application will simply show
plain slides without any background colors, gradients or bitmaps.

