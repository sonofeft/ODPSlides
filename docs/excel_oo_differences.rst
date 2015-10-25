
.. excel_oo_differences

Excel/OpenOffice Differences
============================

Master Styles
-------------

When displaying a page, Excel seems to honor the draw:style-name of the style:master-page from styles.xml
whereas OpenOffice and LibreOffice seem to honor the presentation:style-name of the draw:page from content.xml

ODPSlides therefore makes a new style:master-page and a new draw:page for each slide.
