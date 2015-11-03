.. 2015-11-03 sonofeft 56ba027e20f1a47609dd32e7a6e6457e5bea59e9
   Maintain spacing of "History" and "GitHub Log" titles

History
=======

GitHub Log
----------

* Nov 03, 2015
    - (by: sonofeft) 
        - version 0.0.3, updated examples, made beta
* Nov 02, 2015
    - (by: sonofeft) 
        - Removed scary alpha warning
        - Fixed Test Error, Added Example docs
        - Moved some example images around
        - added two examples
* Nov 01, 2015
    - (by: sonofeft) 
        - worked on docs
        - Enabled footer, date and page number with font colors
        - fixed gradient background error
        - added the rest of the chart layouts
* Oct 31, 2015
    - (by: sonofeft) 
        - added content dimension stretching logic
        - added keep_aspect_ratio flag for images
        - Maintain image aspect ratio, added some sample images
        - Text over image added
        - Got Title + Text chart working
        - title + outline works BUT bullets are broken
* Oct 30, 2015
    - (by: sonofeft) 
        - Changed image ref odp file to take out shadow-drop text
        - Got all three background types working with all three apps
        - Working cross-app solid background
* Oct 28, 2015
    - (by: sonofeft) 
        - Version 0.0.2 a set-point before the next refactor
            It's more important that the generated odp files are compatible with
            Excel LibreOffice and OO than it is to have each page of each
            presentation be fully custimizable.
            I'm starting a refactor where every page in the presentation will have
            the same background (solid, gradient or bitmap) but all 3 apps will open
            them pretty much the same.
* Oct 27, 2015
    - (by: sonofeft) 
        - implemented gradient and image for OO
        - minor tweeks
        - added "for_excel" flag, gave up on a single file readable by all apps
            Finally got both Excel and OO to work with primarily content.xml
            statements (i.e. w/o a lot of styles.xml statements)
            For now, fancy backgrounds are application dependent.
    - (by: Charlie Taylor) 
        - Added element to string
* Oct 26, 2015
    - (by: sonofeft) 
        - Back to basic functionality with title slide only
            Removed a bunch of large codegen files (used for development only)
            The "hope" right now is that plain slides can be converted to gradient
            and bitmap by simply changing the drawing:page style
* Oct 25, 2015
    - (by: sonofeft) 
        - Replaced plain_pages.py with generic Page object
        - Fixed unittest for new interface
        - Totally Refactored the approach
            No longer using template odp files.  Used codegen to make native python
            files that generate Element objects for draw:page elements and
            xxxx:style elements
* Oct 21, 2015
    - (by: sonofeft) 
        - page color gradient implemented
* Oct 20, 2015
    - (by: sonofeft) 
        - page number and footer done
        - Font colors and date field working


* Oct 10, 2015
    - (by: sonofeft)
        - First Created ODPSlides with PyHatch
