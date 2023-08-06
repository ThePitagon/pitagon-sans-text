## Fontbakery report

Fontbakery version: 0.8.11

<details><summary><b>[19] PitagonSansText-ExtraBoldItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check OFL body text is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text">com.google.fonts/check/license/OFL_body_text</a>)</summary><div>


* 🔥 **FAIL** The OFL.txt body text is incorrect. Please use https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt as a template. You should only modify the first line. [code: incorrect-ofl-body-text]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ
at: https://scripts.sil.org/OFL." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks">com.google.fonts/check/name/line_breaks</a>)</summary><div>


* 🔥 **FAIL** Name entry DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1294, but got 1214 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.11, while a newer 0.8.13 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'Pita' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
</div></details><details><summary>⚠ <b>WARN:</b> Description strings in the name table must not exceed 200 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/description_max_length">com.google.fonts/check/name/description_max_length</a>)</summary><div>


* ⚠ **WARN** A few name table entries with ID=10 (NameID.DESCRIPTION) are longer than 200 characters. Please check whether those entries are copyright notices mistakenly stored in the description string entries by a bug in an old FontLab version. If that's the case, then such copyright notices must be removed from these entries. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Pitagon Sans Text ExtraBold' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- periodcentered.001 

	- registered.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* petapp (U+E006): L<<282.0,304.0>--<312.0,286.0>> -> L<<312.0,286.0>--<339.0,271.0>>

	* petapp (U+E006): L<<312.0,333.0>--<273.0,356.0>> -> L<<273.0,356.0>--<257.0,365.0>>

	* petapp (U+E006): L<<355.0,309.0>--<312.0,333.0>> -> L<<312.0,333.0>--<273.0,356.0>>

	* petapp (U+E006): L<<371.0,299.0>--<355.0,309.0>> -> L<<355.0,309.0>--<312.0,333.0>>

	* petapp (U+E006): L<<371.0,640.0>--<467.0,585.0>> -> L<<467.0,585.0>--<515.0,556.0>>

	* petapp (U+E006): L<<373.0,298.0>--<371.0,299.0>> -> L<<371.0,299.0>--<355.0,309.0>>

	* petapp (U+E006): L<<426.0,268.0>--<373.0,298.0>> -> L<<373.0,298.0>--<371.0,299.0>>

	* petapp (U+E006): L<<467.0,585.0>--<515.0,556.0>> -> L<<515.0,556.0>--<534.0,545.0>>

	* petapp (U+E006): L<<468.0,243.0>--<426.0,268.0>> -> L<<426.0,268.0>--<373.0,298.0>>

	* petapp (U+E006): L<<474.0,240.0>--<468.0,243.0>> -> L<<468.0,243.0>--<426.0,268.0>>

	* petapp (U+E006): L<<498.0,226.0>--<474.0,240.0>> -> L<<474.0,240.0>--<468.0,243.0>>

	* petapp (U+E006): L<<505.0,222.0>--<498.0,226.0>> -> L<<498.0,226.0>--<474.0,240.0>>

	* petapp (U+E006): L<<691.0,61.0>--<692.0,60.0>> -> L<<692.0,60.0>--<696.0,56.0>>

	* petapp (U+E006): L<<721.0,485.0>--<725.0,485.0>> -> L<<725.0,485.0>--<764.0,485.0>>

	* petapp.minimal (U+E007): L<<264.0,373.0>--<351.0,339.0>> -> L<<351.0,339.0>--<432.0,305.0>>

	* petapp.minimal (U+E007): L<<351.0,339.0>--<432.0,305.0>> -> L<<432.0,305.0>--<448.0,299.0>>

	* petapp.minimal (U+E007): L<<381.0,352.0>--<331.0,376.0>> -> L<<331.0,376.0>--<305.0,390.0>>

	* petapp.minimal (U+E007): L<<432.0,305.0>--<448.0,299.0>> -> L<<448.0,299.0>--<504.0,276.0>>

	* petapp.minimal (U+E007): L<<432.0,326.0>--<381.0,352.0>> -> L<<381.0,352.0>--<331.0,376.0>>

	* petapp.minimal (U+E007): L<<435.0,187.0>--<405.0,192.0>> -> L<<405.0,192.0>--<304.0,211.0>>

	* petapp.minimal (U+E007): L<<448.0,299.0>--<504.0,276.0>> -> L<<504.0,276.0>--<612.0,232.0>>

	* petapp.minimal (U+E007): L<<455.0,314.0>--<432.0,326.0>> -> L<<432.0,326.0>--<381.0,352.0>>

	* petapp.minimal (U+E007): L<<504.0,175.0>--<435.0,187.0>> -> L<<435.0,187.0>--<405.0,192.0>>

	* petapp.minimal (U+E007): L<<504.0,276.0>--<612.0,232.0>> -> L<<612.0,232.0>--<621.0,229.0>>

	* petapp.minimal (U+E007): L<<504.0,289.0>--<455.0,314.0>> -> L<<455.0,314.0>--<432.0,326.0>>

	* petapp.minimal (U+E007): L<<588.0,160.0>--<504.0,175.0>> -> L<<504.0,175.0>--<435.0,187.0>>

	* petapp.minimal (U+E007): L<<621.0,229.0>--<504.0,289.0>> -> L<<504.0,289.0>--<455.0,314.0>>

	* petapp.minimal (U+E007): L<<742.0,30.0>--<742.0,31.0>> -> L<<742.0,31.0>--<742.0,32.0>>

	* petapp.minimal (U+E007): L<<743.0,33.0>--<743.0,34.0>> -> L<<743.0,34.0>--<743.0,36.0>>

	* petapp.minimal (U+E007): L<<743.0,34.0>--<743.0,36.0>> -> L<<743.0,36.0>--<743.0,37.0>>

	* petapp.minimal (U+E007): L<<747.0,73.0>--<746.0,63.0>> -> L<<746.0,63.0>--<743.0,38.0>>

	* petapp.minimal (U+E007): L<<747.0,74.0>--<747.0,73.0>> -> L<<747.0,73.0>--<746.0,63.0>>

	* petapp.minimal (U+E007): L<<752.0,131.0>--<747.0,74.0>> -> L<<747.0,74.0>--<747.0,73.0>>

	* petapp.minimal (U+E007): L<<754.0,162.0>--<752.0,131.0>> -> L<<752.0,131.0>--<747.0,74.0>>

	* petapp.minimal (U+E007): L<<755.0,175.0>--<754.0,162.0>> -> L<<754.0,162.0>--<752.0,131.0>>

	* petapp.minimal (U+E007): L<<757.0,196.0>--<755.0,175.0>> -> L<<755.0,175.0>--<754.0,162.0>>

	* petapp.minimal (U+E007): L<<758.0,210.0>--<757.0,196.0>> -> L<<757.0,196.0>--<755.0,175.0>>

	* petapp.minimal (U+E007): L<<758.0,213.0>--<758.0,210.0>> -> L<<758.0,210.0>--<757.0,196.0>>

	* petapp.wpda (U+E008): L<<640.0,140.0>--<627.0,132.0>> -> L<<627.0,132.0>--<618.0,127.0>>

	* piads (U+E001): L<<112.0,541.0>--<116.0,544.0>> -> L<<116.0,544.0>--<445.0,782.0>>

	* piads (U+E001): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<878.0,541.0>>

	* picall (U+E009): L<<112.0,541.0>--<116.0,544.0>> -> L<<116.0,544.0>--<445.0,782.0>>

	* picall (U+E009): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<878.0,541.0>>

	* pioffice (U+E002): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<877.0,542.0>>

	* pisafe (U+E010): L<<167.0,362.0>--<167.0,491.0>> -> L<<167.0,491.0>--<167.0,494.0>>

	* pisafe (U+E010): L<<203.0,695.0>--<239.0,708.0>> -> L<<239.0,708.0>--<389.0,762.0>>

	* pisafe (U+E010): L<<239.0,708.0>--<389.0,762.0>> -> L<<389.0,762.0>--<494.0,800.0>>

	* pisafe (U+E010): L<<495.0,800.0>--<600.0,762.0>> -> L<<600.0,762.0>--<750.0,708.0>>

	* pisafe (U+E010): L<<600.0,762.0>--<750.0,708.0>> -> L<<750.0,708.0>--<786.0,695.0>>

	* pisign (U+E005): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<877.0,542.0>>

	* pitagon (U+E000): L<<112.0,543.0>--<116.0,546.0>> -> L<<116.0,546.0>--<445.0,784.0>>

	* pitagon (U+E000): L<<209.0,62.0>--<84.0,446.0>> -> L<<84.0,446.0>--<82.0,452.0>>

	* pitagon (U+E000): L<<547.0,784.0>--<874.0,546.0>> -> L<<874.0,546.0>--<878.0,543.0>>

	* pitagram (U+E003): L<<813.0,512.0>--<810.0,514.0>> -> L<<810.0,514.0>--<537.0,711.0>>

	* piweb (U+E004): L<<813.0,512.0>--<810.0,514.0>> -> L<<810.0,514.0>--<537.0,711.0>>

	* sparks (U+E011): L<<100.0,798.0>--<103.0,797.0>> -> L<<103.0,797.0>--<198.0,762.0>>

	* sparks (U+E011): L<<103.0,797.0>--<198.0,762.0>> -> L<<198.0,762.0>--<209.0,759.0>>

	* sparks (U+E011): L<<198.0,762.0>--<209.0,759.0>> -> L<<209.0,759.0>--<400.0,690.0>>

	* sparks (U+E011): L<<209.0,759.0>--<400.0,690.0>> -> L<<400.0,690.0>--<431.0,680.0>>

	* sparks (U+E011): L<<291.0,596.0>--<363.0,534.0>> -> L<<363.0,534.0>--<382.0,516.0>>

	* sparks (U+E011): L<<381.0,366.0>--<383.0,367.0>> -> L<<383.0,367.0>--<486.0,429.0>>

	* sparks (U+E011): L<<383.0,367.0>--<486.0,429.0>> -> L<<486.0,429.0>--<488.0,430.0>>

	* sparks (U+E011): L<<409.0,102.0>--<98.0,641.0>> -> L<<98.0,641.0>--<47.0,731.0>>

	* sparks (U+E011): L<<440.0,659.0>--<436.0,649.0>> -> L<<436.0,649.0>--<434.0,643.0>>

	* sparks (U+E011): L<<454.0,24.0>--<409.0,102.0>> -> L<<409.0,102.0>--<98.0,641.0>>

	* sparks (U+E011): L<<504.0,429.0>--<606.0,367.0>> -> L<<606.0,367.0>--<608.0,366.0>>

	* sparks (U+E011): L<<558.0,680.0>--<596.0,694.0>> -> L<<596.0,694.0>--<780.0,759.0>>

	* sparks (U+E011): L<<579.0,101.0>--<550.0,51.0>> -> L<<550.0,51.0>--<535.0,24.0>>

	* sparks (U+E011): L<<596.0,694.0>--<780.0,759.0>> -> L<<780.0,759.0>--<807.0,768.0>>

	* sparks (U+E011): L<<607.0,516.0>--<627.0,534.0>> -> L<<627.0,534.0>--<699.0,596.0>>

	* sparks (U+E011): L<<614.0,629.0>--<577.0,632.0>> -> L<<577.0,632.0>--<568.0,633.0>>

	* sparks (U+E011): L<<655.0,626.0>--<614.0,629.0>> -> L<<614.0,629.0>--<577.0,632.0>>

	* sparks (U+E011): L<<656.0,626.0>--<655.0,626.0>> -> L<<655.0,626.0>--<614.0,629.0>>

	* sparks (U+E011): L<<690.0,623.0>--<656.0,626.0>> -> L<<656.0,626.0>--<655.0,626.0>>

	* sparks (U+E011): L<<691.0,623.0>--<690.0,623.0>> -> L<<690.0,623.0>--<656.0,626.0>>

	* sparks (U+E011): L<<750.0,397.0>--<579.0,101.0>> -> L<<579.0,101.0>--<550.0,51.0>>

	* sparks (U+E011): L<<780.0,759.0>--<807.0,768.0>> -> L<<807.0,768.0>--<886.0,797.0>>

	* sparks (U+E011): L<<897.0,652.0>--<750.0,397.0>> -> L<<750.0,397.0>--<579.0,101.0>>

	* sparks (U+E011): L<<942.0,730.0>--<897.0,652.0>> -> L<<897.0,652.0>--<750.0,397.0>> 

	* sparks (U+E011): L<<943.0,732.0>--<942.0,730.0>> -> L<<942.0,730.0>--<897.0,652.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* petapp (U+E006): B<<289.0,471.0>-<290.0,469.0>-<291.0,468.0>>/L<<291.0,468.0>--<289.0,471.0>> = 11.309932474020227

	* petapp (U+E006): B<<295.0,293.0>-<289.0,300.0>-<282.0,304.0>>/L<<282.0,304.0>--<312.0,286.0>> = 1.2188752351307344

	* petapp (U+E006): B<<328.0,429.0>-<329.0,428.0>-<331.0,427.0>>/L<<331.0,427.0>--<328.0,429.0>> = 7.125016348901757

	* petapp (U+E006): B<<415.0,76.0>-<416.0,76.0>-<418.0,75.0>>/L<<418.0,75.0>--<415.0,76.0>> = 8.130102354155916

	* petapp (U+E006): B<<424.0,71.0>-<425.0,71.0>-<427.0,70.0>>/L<<427.0,70.0>--<424.0,71.0>> = 8.130102354155916

	* petapp (U+E006): B<<439.0,65.0>-<440.0,65.0>-<442.0,64.0>>/L<<442.0,64.0>--<439.0,65.0>> = 8.130102354155916

	* petapp (U+E006): B<<483.0,64.0>-<484.0,64.0>-<486.0,65.0>>/L<<486.0,65.0>--<483.0,64.0>> = 8.130102354155916

	* petapp (U+E006): B<<513.0,65.0>-<515.0,65.0>-<517.0,66.0>>/L<<517.0,66.0>--<513.0,65.0>> = 12.528807709151463

	* petapp (U+E006): B<<519.0,66.0>-<521.0,66.0>-<523.0,67.0>>/L<<523.0,67.0>--<519.0,66.0>> = 12.528807709151463

	* petapp (U+E006): B<<529.0,68.0>-<528.0,68.0>-<526.0,67.0>>/L<<526.0,67.0>--<529.0,68.0>> = 8.13010235415587

	* petapp (U+E006): B<<536.0,192.0>-<535.0,194.0>-<534.0,195.0>>/L<<534.0,195.0>--<536.0,192.0>> = 11.309932474020195

	* petapp (U+E006): B<<536.0,69.0>-<534.0,69.0>-<532.0,68.0>>/L<<532.0,68.0>--<536.0,69.0>> = 12.528807709151492

	* petapp (U+E006): B<<537.0,308.0>-<536.0,309.0>-<534.0,310.0>>/L<<534.0,310.0>--<537.0,308.0>> = 7.125016348901757

	* petapp (U+E006): B<<539.0,108.0>-<540.0,109.0>-<541.0,111.0>>/L<<541.0,111.0>--<539.0,108.0>> = 7.125016348901705

	* petapp (U+E006): B<<539.0,438.0>-<538.0,439.0>-<536.0,440.0>>/L<<536.0,440.0>--<539.0,438.0>> = 7.125016348901757

	* petapp (U+E006): B<<545.0,123.0>-<546.0,125.0>-<546.0,127.0>>/L<<546.0,127.0>--<545.0,123.0>> = 14.036243467926484

	* petapp (U+E006): B<<548.0,432.0>-<547.0,433.0>-<545.0,434.0>>/L<<545.0,434.0>--<548.0,432.0>> = 7.125016348901757

	* petapp (U+E006): B<<548.0,72.0>-<549.0,72.0>-<551.0,73.0>>/L<<551.0,73.0>--<548.0,72.0>> = 8.130102354155916

	* petapp (U+E006): B<<575.0,404.0>-<576.0,403.0>-<577.0,401.0>>/L<<577.0,401.0>--<575.0,404.0>> = 7.125016348901705

	* petapp (U+E006): B<<587.0,380.0>-<587.0,382.0>-<586.0,384.0>>/L<<586.0,384.0>--<587.0,380.0>> = 12.528807709151492

	* petapp (U+E006): B<<610.0,384.0>-<611.0,381.0>-<612.0,379.0>>/L<<612.0,379.0>--<610.0,384.0>> = 4.763641690726066

	* petapp (U+E006): B<<614.0,384.0>-<615.0,382.0>-<616.0,379.0>>/L<<616.0,379.0>--<614.0,384.0>> = 3.366460663429615

	* petapp (U+E006): B<<627.0,343.0>-<628.0,342.0>-<629.0,340.0>>/L<<629.0,340.0>--<627.0,343.0>> = 7.125016348901705

	* petapp (U+E006): B<<633.0,334.0>-<633.0,333.0>-<634.0,331.0>>/L<<634.0,331.0>--<633.0,334.0>> = 8.130102354155916

	* petapp (U+E006): B<<638.0,346.0>-<639.0,345.0>-<640.0,343.0>>/L<<640.0,343.0>--<638.0,346.0>> = 7.125016348901705

	* petapp (U+E006): B<<641.0,321.0>-<642.0,320.0>-<643.0,318.0>>/L<<643.0,318.0>--<641.0,321.0>> = 7.125016348901705

	* petapp (U+E006): B<<669.0,316.0>-<670.0,315.0>-<672.0,314.0>>/L<<672.0,314.0>--<669.0,316.0>> = 7.125016348901757

	* petapp (U+E006): B<<669.0,456.0>-<667.0,454.0>-<666.0,452.0>>/L<<666.0,452.0>--<669.0,456.0>> = 10.304846468766044

	* petapp (U+E006): B<<670.0,137.0>-<671.0,138.0>-<672.0,140.0>>/L<<672.0,140.0>--<670.0,137.0>> = 7.125016348901705

	* petapp (U+E006): B<<679.0,141.0>-<681.0,142.0>-<682.0,143.0>>/L<<682.0,143.0>--<679.0,141.0>> = 11.309932474020195

	* petapp (U+E006): B<<687.0,164.0>-<688.0,166.0>-<689.0,167.0>>/L<<689.0,167.0>--<687.0,164.0>> = 11.309932474020227

	* petapp (U+E006): B<<713.0,484.0>-<712.0,484.0>-<710.0,483.0>>/L<<710.0,483.0>--<713.0,484.0>> = 8.13010235415587

	* petapp (U+E006): B<<763.0,5.0>-<762.0,7.0>-<761.0,8.0>>/L<<761.0,8.0>--<763.0,5.0>> = 11.309932474020195

	* petapp (U+E006): L<<274.0,517.0>--<273.0,520.0>>/B<<273.0,520.0>-<274.0,518.0>-<274.0,517.0>> = 8.130102354155916

	* petapp (U+E006): L<<280.0,491.0>--<279.0,494.0>>/B<<279.0,494.0>-<280.0,492.0>-<280.0,491.0>> = 8.130102354155916

	* petapp (U+E006): L<<291.0,468.0>--<289.0,471.0>>/B<<289.0,471.0>-<290.0,469.0>-<291.0,468.0>> = 7.125016348901705

	* petapp (U+E006): L<<296.0,459.0>--<295.0,462.0>>/B<<295.0,462.0>-<296.0,460.0>-<296.0,459.0>> = 8.130102354155916

	* petapp (U+E006): L<<312.0,442.0>--<308.0,445.0>>/B<<308.0,445.0>-<310.0,444.0>-<312.0,442.0>> = 10.304846468766009

	* petapp (U+E006): L<<331.0,427.0>--<328.0,429.0>>/B<<328.0,429.0>-<329.0,428.0>-<331.0,427.0>> = 11.309932474020195

	* petapp (U+E006): L<<380.0,128.0>--<379.0,131.0>>/B<<379.0,131.0>-<380.0,129.0>-<380.0,128.0>> = 8.130102354155916

	* petapp (U+E006): L<<387.0,108.0>--<386.0,111.0>>/B<<386.0,111.0>-<387.0,109.0>-<387.0,108.0>> = 8.130102354155916

	* petapp (U+E006): L<<499.0,225.0>--<505.0,222.0>>/L<<505.0,222.0>--<498.0,226.0>> = 3.1798301198640497

	* petapp (U+E006): L<<504.0,71.0>--<499.0,69.0>>/B<<499.0,69.0>-<502.0,71.0>-<504.0,71.0>> = 11.888658039627936

	* petapp (U+E006): L<<517.0,66.0>--<513.0,65.0>>/B<<513.0,65.0>-<515.0,65.0>-<517.0,66.0>> = 14.036243467926484

	* petapp (U+E006): L<<523.0,67.0>--<519.0,66.0>>/B<<519.0,66.0>-<521.0,66.0>-<523.0,67.0>> = 14.036243467926484

	* petapp (U+E006): L<<532.0,68.0>--<536.0,69.0>>/B<<536.0,69.0>-<534.0,69.0>-<532.0,68.0>> = 14.036243467926484

	* petapp (U+E006): L<<534.0,195.0>--<536.0,192.0>>/B<<536.0,192.0>-<535.0,194.0>-<534.0,195.0>> = 7.125016348901757

	* petapp (U+E006): L<<534.0,310.0>--<537.0,308.0>>/B<<537.0,308.0>-<536.0,309.0>-<534.0,310.0>> = 11.309932474020227

	* petapp (U+E006): L<<536.0,440.0>--<539.0,438.0>>/B<<539.0,438.0>-<538.0,439.0>-<536.0,440.0>> = 11.309932474020227

	* petapp (U+E006): L<<541.0,111.0>--<539.0,108.0>>/B<<539.0,108.0>-<540.0,109.0>-<541.0,111.0>> = 11.309932474020227

	* petapp (U+E006): L<<541.0,70.0>--<545.0,71.0>>/B<<545.0,71.0>-<540.0,70.0>-<541.0,70.0>> = 2.726310993906212

	* petapp (U+E006): L<<542.0,181.0>--<543.0,178.0>>/B<<543.0,178.0>-<542.0,180.0>-<542.0,181.0>> = 8.13010235415587

	* petapp (U+E006): L<<545.0,434.0>--<548.0,432.0>>/B<<548.0,432.0>-<547.0,433.0>-<545.0,434.0>> = 11.309932474020227

	* petapp (U+E006): L<<546.0,127.0>--<545.0,123.0>>/B<<545.0,123.0>-<546.0,125.0>-<546.0,127.0>> = 12.528807709151492

	* petapp (U+E006): L<<556.0,74.0>--<553.0,73.0>>/B<<553.0,73.0>-<555.0,74.0>-<556.0,74.0>> = 8.130102354155916

	* petapp (U+E006): L<<577.0,401.0>--<575.0,404.0>>/B<<575.0,404.0>-<576.0,403.0>-<577.0,401.0>> = 11.309932474020227

	* petapp (U+E006): L<<583.0,256.0>--<584.0,252.0>>/B<<584.0,252.0>-<584.0,254.0>-<583.0,256.0>> = 14.036243467926484

	* petapp (U+E006): L<<586.0,384.0>--<587.0,380.0>>/B<<587.0,380.0>-<587.0,382.0>-<586.0,384.0>> = 14.036243467926484

	* petapp (U+E006): L<<598.0,432.0>--<599.0,429.0>>/B<<599.0,429.0>-<598.0,431.0>-<598.0,432.0>> = 8.13010235415587

	* petapp (U+E006): L<<602.0,122.0>--<601.0,125.0>>/B<<601.0,125.0>-<602.0,123.0>-<602.0,122.0>> = 8.130102354155916

	* petapp (U+E006): L<<611.0,96.0>--<611.0,96.0>>/B<<611.0,96.0>-<607.0,95.0>-<603.5,92.5>> = 14.036243467926484

	* petapp (U+E006): L<<612.0,379.0>--<610.0,384.0>>/B<<610.0,384.0>-<611.0,381.0>-<612.0,379.0>> = 3.366460663429615

	* petapp (U+E006): L<<613.0,374.0>--<612.0,377.0>>/B<<612.0,377.0>-<613.0,375.0>-<613.0,374.0>> = 8.130102354155916

	* petapp (U+E006): L<<615.0,369.0>--<614.0,372.0>>/B<<614.0,372.0>-<615.0,370.0>-<615.0,369.0>> = 8.130102354155916

	* petapp (U+E006): L<<616.0,379.0>--<614.0,384.0>>/B<<614.0,384.0>-<615.0,382.0>-<616.0,379.0>> = 4.763641690726066

	* petapp (U+E006): L<<629.0,340.0>--<627.0,343.0>>/B<<627.0,343.0>-<628.0,342.0>-<629.0,340.0>> = 11.309932474020227

	* petapp (U+E006): L<<640.0,343.0>--<638.0,346.0>>/B<<638.0,346.0>-<639.0,345.0>-<640.0,343.0>> = 11.309932474020227

	* petapp (U+E006): L<<643.0,318.0>--<641.0,321.0>>/B<<641.0,321.0>-<642.0,320.0>-<643.0,318.0>> = 11.309932474020227

	* petapp (U+E006): L<<657.0,433.0>--<658.0,436.0>>/B<<658.0,436.0>-<657.0,434.0>-<657.0,432.5>> = 8.13010235415587

	* petapp (U+E006): L<<661.0,383.0>--<660.0,386.0>>/B<<660.0,386.0>-<661.0,384.0>-<661.0,383.0>> = 8.130102354155916

	* petapp (U+E006): L<<666.0,452.0>--<669.0,456.0>>/B<<669.0,456.0>-<667.0,454.0>-<666.0,452.0>> = 8.13010235415596

	* petapp (U+E006): L<<672.0,140.0>--<670.0,137.0>>/B<<670.0,137.0>-<671.0,138.0>-<672.0,140.0>> = 11.309932474020227

	* petapp (U+E006): L<<682.0,143.0>--<679.0,141.0>>/B<<679.0,141.0>-<681.0,142.0>-<682.0,143.0>> = 7.125016348901757

	* petapp (U+E006): L<<686.0,162.0>--<685.0,159.0>>/B<<685.0,159.0>-<686.0,161.0>-<686.0,162.0>> = 8.130102354155916

	* petapp (U+E006): L<<689.0,167.0>--<687.0,164.0>>/B<<687.0,164.0>-<688.0,166.0>-<689.0,167.0>> = 7.125016348901705

	* petapp (U+E006): L<<689.0,256.0>--<690.0,253.0>>/B<<690.0,253.0>-<689.0,255.0>-<689.0,256.0>> = 8.13010235415587

	* petapp (U+E006): L<<691.0,251.0>--<692.0,248.0>>/B<<692.0,248.0>-<691.0,250.0>-<691.0,251.0>> = 8.13010235415587

	* petapp (U+E006): L<<700.0,480.0>--<703.0,481.0>>/B<<703.0,481.0>-<701.0,480.0>-<700.0,479.5>> = 8.13010235415587

	* petapp (U+E006): L<<705.0,482.0>--<708.0,483.0>>/B<<708.0,483.0>-<706.0,482.0>-<705.0,482.0>> = 8.13010235415587

	* petapp (U+E006): L<<708.0,293.0>--<705.0,294.0>>/B<<705.0,294.0>-<707.0,293.0>-<708.0,293.0>> = 8.130102354155916

	* petapp (U+E006): L<<728.0,285.0>--<725.0,286.0>>/B<<725.0,286.0>-<727.0,285.0>-<728.0,285.0>> = 8.130102354155916

	* petapp (U+E006): L<<761.0,8.0>--<763.0,5.0>>/B<<763.0,5.0>-<762.0,7.0>-<761.0,8.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<581.0,372.0>-<585.0,368.0>-<588.0,366.0>>/L<<588.0,366.0>--<581.0,372.0>> = 6.911227119024609

	* petapp.minimal (U+E007): B<<631.0,435.0>-<631.0,433.0>-<632.0,430.0>>/L<<632.0,430.0>--<631.0,435.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<632.0,481.0>-<632.0,480.0>-<631.0,478.0>>/L<<631.0,478.0>--<632.0,481.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<645.0,399.0>-<646.0,397.0>-<647.0,396.0>>/L<<647.0,396.0>--<645.0,399.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<646.0,510.0>-<645.0,508.0>-<644.0,507.0>>/L<<644.0,507.0>--<646.0,510.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<676.0,538.0>-<674.0,537.0>-<673.0,536.0>>/L<<673.0,536.0>--<676.0,538.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<700.0,247.0>-<699.0,248.0>-<698.0,250.0>>/L<<698.0,250.0>--<700.0,247.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<714.0,147.0>-<714.0,148.0>-<713.0,150.0>>/L<<713.0,150.0>--<714.0,147.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<720.0,137.0>-<719.0,139.0>-<718.0,140.0>>/L<<718.0,140.0>--<720.0,137.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<732.0,185.0>-<731.0,187.0>-<731.0,189.0>>/L<<731.0,189.0>--<732.0,185.0>> = 14.036243467926484

	* petapp.minimal (U+E007): B<<743.0,53.0>-<743.0,54.0>-<742.0,56.0>>/L<<742.0,56.0>--<743.0,53.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<212.0,538.0>--<212.0,800.0>>/B<<212.0,800.0>-<214.0,769.0>-<226.5,742.0>> = 3.6913859864512575

	* petapp.minimal (U+E007): L<<628.0,462.0>--<629.0,465.0>>/B<<629.0,465.0>-<628.0,463.0>-<628.0,462.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<630.0,473.0>--<631.0,476.0>>/B<<631.0,476.0>-<630.0,474.0>-<630.0,473.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<632.0,430.0>--<631.0,435.0>>/B<<631.0,435.0>-<631.0,433.0>-<632.0,430.0>> = 11.309932474020227

	* petapp.minimal (U+E007): L<<637.0,222.0>--<640.0,221.0>>/B<<640.0,221.0>-<638.0,222.0>-<637.0,222.5>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<639.0,498.0>--<640.0,501.0>>/B<<640.0,501.0>-<639.0,499.0>-<639.0,498.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<644.0,507.0>--<646.0,510.0>>/B<<646.0,510.0>-<645.0,508.0>-<644.0,507.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<647.0,396.0>--<645.0,399.0>>/B<<645.0,399.0>-<646.0,397.0>-<647.0,396.0>> = 7.125016348901705

	* petapp.minimal (U+E007): L<<673.0,536.0>--<676.0,538.0>>/B<<676.0,538.0>-<674.0,537.0>-<673.0,536.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<682.0,542.0>--<685.0,543.0>>/B<<685.0,543.0>-<683.0,542.0>-<682.0,542.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<687.0,544.0>--<690.0,545.0>>/B<<690.0,545.0>-<688.0,544.0>-<687.0,544.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<698.0,250.0>--<700.0,247.0>>/B<<700.0,247.0>-<699.0,248.0>-<698.0,250.0>> = 11.309932474020195

	* petapp.minimal (U+E007): L<<718.0,218.0>--<719.0,215.0>>/B<<719.0,215.0>-<718.0,217.0>-<718.0,218.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<731.0,113.0>--<732.0,110.0>>/B<<732.0,110.0>-<731.0,112.0>-<731.0,113.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<740.0,156.0>--<739.0,160.0>>/B<<739.0,160.0>-<740.0,153.0>-<740.0,156.0>> = 5.906141113770497

	* petapp.minimal (U+E007): L<<744.0,137.0>--<743.0,140.0>>/B<<743.0,140.0>-<744.0,138.0>-<744.0,137.0>> = 8.130102354155916

	* petapp.minimal (U+E007): L<<746.0,123.0>--<747.0,120.0>>/B<<747.0,120.0>-<746.0,122.0>-<746.0,123.0>> = 8.13010235415587

	* petapp.wpda (U+E008): B<<485.0,2.0>-<482.0,5.0>-<482.0,6.0>>/L<<482.0,6.0>--<481.0,1.0>> = 11.309932474020227

	* petapp.wpda (U+E008): L<<185.0,222.0>--<180.0,218.0>>/B<<180.0,218.0>-<182.0,219.0>-<183.0,218.0>> = 12.094757077012058

	* pisafe (U+E010): B<<175.0,538.0>-<175.0,536.0>-<174.0,534.0>>/L<<174.0,534.0>--<175.0,538.0>> = 12.528807709151492

	* pisafe (U+E010): B<<190.0,573.0>-<189.0,572.0>-<188.0,570.0>>/L<<188.0,570.0>--<190.0,573.0>> = 7.125016348901757

	* pisafe (U+E010): B<<211.0,602.0>-<210.0,600.0>-<208.0,598.0>>/L<<208.0,598.0>--<211.0,602.0>> = 8.13010235415596

	* pisafe (U+E010): B<<784.0,594.0>-<783.0,596.0>-<782.0,597.0>>/L<<782.0,597.0>--<784.0,594.0>> = 11.309932474020195

	* pisafe (U+E010): B<<797.0,577.0>-<796.0,579.0>-<795.0,580.0>>/L<<795.0,580.0>--<797.0,577.0>> = 11.309932474020195

	* pisafe (U+E010): B<<816.0,530.0>-<816.0,532.0>-<815.0,534.0>>/L<<815.0,534.0>--<816.0,530.0>> = 12.528807709151492

	* pisafe (U+E010): B<<820.0,515.0>-<820.0,516.0>-<819.0,518.0>>/L<<819.0,518.0>--<820.0,515.0>> = 8.13010235415587

	* pisafe (U+E010): L<<174.0,534.0>--<175.0,538.0>>/B<<175.0,538.0>-<175.0,536.0>-<174.0,534.0>> = 14.036243467926484

	* pisafe (U+E010): L<<188.0,570.0>--<190.0,573.0>>/B<<190.0,573.0>-<189.0,572.0>-<188.0,570.0>> = 11.309932474020195

	* pisafe (U+E010): L<<208.0,598.0>--<211.0,602.0>>/B<<211.0,602.0>-<210.0,600.0>-<208.0,598.0>> = 10.304846468766044

	* pisafe (U+E010): L<<750.0,626.0>--<754.0,623.0>>/B<<754.0,623.0>-<752.0,624.0>-<750.0,626.0>> = 10.304846468766009

	* pisafe (U+E010): L<<782.0,597.0>--<784.0,594.0>>/B<<784.0,594.0>-<783.0,596.0>-<782.0,597.0>> = 7.125016348901757

	* pisafe (U+E010): L<<795.0,580.0>--<797.0,577.0>>/B<<797.0,577.0>-<796.0,579.0>-<795.0,580.0>> = 7.125016348901757

	* pisafe (U+E010): L<<815.0,534.0>--<816.0,530.0>>/B<<816.0,530.0>-<816.0,532.0>-<815.0,534.0>> = 14.036243467926484 

	* pisafe (U+E010): L<<817.0,528.0>--<818.0,525.0>>/B<<818.0,525.0>-<817.0,527.0>-<817.0,528.0>> = 8.13010235415587 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[19] PitagonSansText-Bold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check OFL body text is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text">com.google.fonts/check/license/OFL_body_text</a>)</summary><div>


* 🔥 **FAIL** The OFL.txt body text is incorrect. Please use https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt as a template. You should only modify the first line. [code: incorrect-ofl-body-text]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ
at: https://scripts.sil.org/OFL." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks">com.google.fonts/check/name/line_breaks</a>)</summary><div>


* 🔥 **FAIL** Name entry DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1294, but got 1214 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.11, while a newer 0.8.13 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'Pita' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
</div></details><details><summary>⚠ <b>WARN:</b> Description strings in the name table must not exceed 200 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/description_max_length">com.google.fonts/check/name/description_max_length</a>)</summary><div>


* ⚠ **WARN** A few name table entries with ID=10 (NameID.DESCRIPTION) are longer than 200 characters. Please check whether those entries are copyright notices mistakenly stored in the description string entries by a bug in an old FontLab version. If that's the case, then such copyright notices must be removed from these entries. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- dotlessi.wide 

	- registered.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* fl (U+FB02): L<<466.0,427.0>--<463.0,427.0>> -> L<<463.0,427.0>--<255.0,427.0>>

	* petapp (U+E006): L<<284.0,304.0>--<314.0,286.0>> -> L<<314.0,286.0>--<341.0,271.0>>

	* petapp (U+E006): L<<314.0,333.0>--<275.0,356.0>> -> L<<275.0,356.0>--<259.0,365.0>>

	* petapp (U+E006): L<<357.0,309.0>--<314.0,333.0>> -> L<<314.0,333.0>--<275.0,356.0>>

	* petapp (U+E006): L<<373.0,299.0>--<357.0,309.0>> -> L<<357.0,309.0>--<314.0,333.0>>

	* petapp (U+E006): L<<373.0,640.0>--<469.0,585.0>> -> L<<469.0,585.0>--<517.0,556.0>>

	* petapp (U+E006): L<<375.0,298.0>--<373.0,299.0>> -> L<<373.0,299.0>--<357.0,309.0>>

	* petapp (U+E006): L<<428.0,268.0>--<375.0,298.0>> -> L<<375.0,298.0>--<373.0,299.0>>

	* petapp (U+E006): L<<469.0,585.0>--<517.0,556.0>> -> L<<517.0,556.0>--<536.0,545.0>>

	* petapp (U+E006): L<<470.0,243.0>--<428.0,268.0>> -> L<<428.0,268.0>--<375.0,298.0>>

	* petapp (U+E006): L<<476.0,240.0>--<470.0,243.0>> -> L<<470.0,243.0>--<428.0,268.0>>

	* petapp (U+E006): L<<500.0,226.0>--<476.0,240.0>> -> L<<476.0,240.0>--<470.0,243.0>>

	* petapp (U+E006): L<<507.0,222.0>--<500.0,226.0>> -> L<<500.0,226.0>--<476.0,240.0>>

	* petapp (U+E006): L<<599.0,453.0>--<599.0,455.0>> -> L<<599.0,455.0>--<599.0,456.0>>

	* petapp (U+E006): L<<599.0,455.0>--<599.0,454.0>> -> L<<599.0,454.0>--<599.0,453.0>>

	* petapp (U+E006): L<<723.0,485.0>--<727.0,485.0>> -> L<<727.0,485.0>--<766.0,485.0>>

	* petapp.minimal (U+E007): L<<266.0,373.0>--<353.0,339.0>> -> L<<353.0,339.0>--<434.0,305.0>>

	* petapp.minimal (U+E007): L<<353.0,339.0>--<434.0,305.0>> -> L<<434.0,305.0>--<450.0,299.0>>

	* petapp.minimal (U+E007): L<<383.0,352.0>--<333.0,376.0>> -> L<<333.0,376.0>--<307.0,390.0>>

	* petapp.minimal (U+E007): L<<434.0,305.0>--<450.0,299.0>> -> L<<450.0,299.0>--<506.0,276.0>>

	* petapp.minimal (U+E007): L<<434.0,326.0>--<383.0,352.0>> -> L<<383.0,352.0>--<333.0,376.0>>

	* petapp.minimal (U+E007): L<<437.0,187.0>--<407.0,192.0>> -> L<<407.0,192.0>--<306.0,211.0>>

	* petapp.minimal (U+E007): L<<450.0,299.0>--<506.0,276.0>> -> L<<506.0,276.0>--<614.0,232.0>>

	* petapp.minimal (U+E007): L<<457.0,314.0>--<434.0,326.0>> -> L<<434.0,326.0>--<383.0,352.0>>

	* petapp.minimal (U+E007): L<<506.0,175.0>--<437.0,187.0>> -> L<<437.0,187.0>--<407.0,192.0>>

	* petapp.minimal (U+E007): L<<506.0,276.0>--<614.0,232.0>> -> L<<614.0,232.0>--<623.0,229.0>>

	* petapp.minimal (U+E007): L<<506.0,289.0>--<457.0,314.0>> -> L<<457.0,314.0>--<434.0,326.0>>

	* petapp.minimal (U+E007): L<<590.0,160.0>--<506.0,175.0>> -> L<<506.0,175.0>--<437.0,187.0>>

	* petapp.minimal (U+E007): L<<624.0,229.0>--<506.0,289.0>> -> L<<506.0,289.0>--<457.0,314.0>>

	* petapp.minimal (U+E007): L<<745.0,31.0>--<745.0,32.0>> -> L<<745.0,32.0>--<745.0,33.0>>

	* petapp.minimal (U+E007): L<<745.0,32.0>--<745.0,33.0>> -> L<<745.0,33.0>--<745.0,34.0>>

	* petapp.minimal (U+E007): L<<745.0,33.0>--<745.0,34.0>> -> L<<745.0,34.0>--<745.0,36.0>>

	* petapp.minimal (U+E007): L<<745.0,34.0>--<745.0,36.0>> -> L<<745.0,36.0>--<745.0,37.0>>

	* petapp.minimal (U+E007): L<<749.0,73.0>--<748.0,63.0>> -> L<<748.0,63.0>--<745.0,38.0>>

	* petapp.minimal (U+E007): L<<749.0,74.0>--<749.0,73.0>> -> L<<749.0,73.0>--<748.0,63.0>>

	* petapp.minimal (U+E007): L<<754.0,131.0>--<749.0,74.0>> -> L<<749.0,74.0>--<749.0,73.0>>

	* petapp.minimal (U+E007): L<<756.0,162.0>--<754.0,131.0>> -> L<<754.0,131.0>--<749.0,74.0>>

	* petapp.minimal (U+E007): L<<757.0,175.0>--<756.0,162.0>> -> L<<756.0,162.0>--<754.0,131.0>>

	* petapp.minimal (U+E007): L<<759.0,196.0>--<757.0,175.0>> -> L<<757.0,175.0>--<756.0,162.0>>

	* petapp.minimal (U+E007): L<<760.0,210.0>--<759.0,196.0>> -> L<<759.0,196.0>--<757.0,175.0>>

	* petapp.minimal (U+E007): L<<760.0,213.0>--<760.0,210.0>> -> L<<760.0,210.0>--<759.0,196.0>>

	* petapp.wpda (U+E008): L<<642.0,140.0>--<629.0,132.0>> -> L<<629.0,132.0>--<620.0,127.0>>

	* piads (U+E001): L<<114.0,541.0>--<118.0,544.0>> -> L<<118.0,544.0>--<447.0,782.0>>

	* piads (U+E001): L<<548.0,782.0>--<876.0,544.0>> -> L<<876.0,544.0>--<880.0,541.0>>

	* picall (U+E009): L<<114.0,541.0>--<118.0,544.0>> -> L<<118.0,544.0>--<447.0,782.0>>

	* picall (U+E009): L<<548.0,782.0>--<876.0,544.0>> -> L<<876.0,544.0>--<880.0,541.0>>

	* pioffice (U+E002): L<<548.0,782.0>--<876.0,544.0>> -> L<<876.0,544.0>--<879.0,542.0>>

	* pisafe (U+E010): L<<169.0,362.0>--<169.0,491.0>> -> L<<169.0,491.0>--<169.0,494.0>>

	* pisafe (U+E010): L<<205.0,695.0>--<241.0,708.0>> -> L<<241.0,708.0>--<391.0,762.0>>

	* pisafe (U+E010): L<<241.0,708.0>--<391.0,762.0>> -> L<<391.0,762.0>--<496.0,800.0>>

	* pisafe (U+E010): L<<497.0,800.0>--<602.0,762.0>> -> L<<602.0,762.0>--<752.0,708.0>>

	* pisafe (U+E010): L<<602.0,762.0>--<752.0,708.0>> -> L<<752.0,708.0>--<788.0,695.0>>

	* pisign (U+E005): L<<548.0,782.0>--<876.0,544.0>> -> L<<876.0,544.0>--<879.0,542.0>>

	* pitagon (U+E000): L<<114.0,543.0>--<118.0,546.0>> -> L<<118.0,546.0>--<447.0,784.0>>

	* pitagon (U+E000): L<<211.0,62.0>--<86.0,446.0>> -> L<<86.0,446.0>--<84.0,452.0>>

	* pitagon (U+E000): L<<549.0,784.0>--<876.0,546.0>> -> L<<876.0,546.0>--<880.0,543.0>>

	* pitagram (U+E003): L<<815.0,512.0>--<812.0,514.0>> -> L<<812.0,514.0>--<539.0,711.0>>

	* piweb (U+E004): L<<815.0,512.0>--<812.0,514.0>> -> L<<812.0,514.0>--<539.0,711.0>>

	* sparks (U+E011): L<<102.0,798.0>--<105.0,797.0>> -> L<<105.0,797.0>--<200.0,762.0>>

	* sparks (U+E011): L<<105.0,797.0>--<200.0,762.0>> -> L<<200.0,762.0>--<211.0,759.0>>

	* sparks (U+E011): L<<200.0,762.0>--<211.0,759.0>> -> L<<211.0,759.0>--<402.0,690.0>>

	* sparks (U+E011): L<<211.0,759.0>--<402.0,690.0>> -> L<<402.0,690.0>--<433.0,680.0>>

	* sparks (U+E011): L<<293.0,596.0>--<365.0,534.0>> -> L<<365.0,534.0>--<384.0,516.0>>

	* sparks (U+E011): L<<383.0,366.0>--<385.0,367.0>> -> L<<385.0,367.0>--<488.0,429.0>>

	* sparks (U+E011): L<<385.0,367.0>--<488.0,429.0>> -> L<<488.0,429.0>--<490.0,430.0>>

	* sparks (U+E011): L<<411.0,102.0>--<100.0,641.0>> -> L<<100.0,641.0>--<49.0,731.0>>

	* sparks (U+E011): L<<442.0,659.0>--<438.0,649.0>> -> L<<438.0,649.0>--<436.0,643.0>>

	* sparks (U+E011): L<<456.0,24.0>--<411.0,102.0>> -> L<<411.0,102.0>--<100.0,641.0>>

	* sparks (U+E011): L<<506.0,429.0>--<608.0,367.0>> -> L<<608.0,367.0>--<610.0,366.0>>

	* sparks (U+E011): L<<560.0,680.0>--<598.0,694.0>> -> L<<598.0,694.0>--<782.0,759.0>>

	* sparks (U+E011): L<<581.0,101.0>--<552.0,51.0>> -> L<<552.0,51.0>--<537.0,24.0>>

	* sparks (U+E011): L<<598.0,694.0>--<782.0,759.0>> -> L<<782.0,759.0>--<809.0,768.0>>

	* sparks (U+E011): L<<609.0,516.0>--<629.0,534.0>> -> L<<629.0,534.0>--<701.0,596.0>>

	* sparks (U+E011): L<<616.0,629.0>--<579.0,632.0>> -> L<<579.0,632.0>--<570.0,633.0>>

	* sparks (U+E011): L<<657.0,626.0>--<616.0,629.0>> -> L<<616.0,629.0>--<579.0,632.0>>

	* sparks (U+E011): L<<658.0,626.0>--<657.0,626.0>> -> L<<657.0,626.0>--<616.0,629.0>>

	* sparks (U+E011): L<<692.0,623.0>--<658.0,626.0>> -> L<<658.0,626.0>--<657.0,626.0>>

	* sparks (U+E011): L<<693.0,623.0>--<692.0,623.0>> -> L<<692.0,623.0>--<658.0,626.0>>

	* sparks (U+E011): L<<752.0,397.0>--<581.0,101.0>> -> L<<581.0,101.0>--<552.0,51.0>>

	* sparks (U+E011): L<<782.0,759.0>--<809.0,768.0>> -> L<<809.0,768.0>--<888.0,797.0>>

	* sparks (U+E011): L<<899.0,652.0>--<752.0,397.0>> -> L<<752.0,397.0>--<581.0,101.0>>

	* sparks (U+E011): L<<944.0,730.0>--<899.0,652.0>> -> L<<899.0,652.0>--<752.0,397.0>> 

	* sparks (U+E011): L<<945.0,732.0>--<944.0,730.0>> -> L<<944.0,730.0>--<899.0,652.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* petapp (U+E006): B<<297.0,462.0>-<298.0,460.0>-<299.0,459.0>>/L<<299.0,459.0>--<297.0,462.0>> = 11.309932474020227

	* petapp (U+E006): B<<297.5,293.0>-<291.0,300.0>-<284.0,304.0>>/L<<284.0,304.0>--<314.0,286.0>> = 1.2188752351307344

	* petapp (U+E006): B<<321.0,436.0>-<323.0,435.0>-<324.0,434.0>>/L<<324.0,434.0>--<321.0,436.0>> = 11.309932474020195

	* petapp (U+E006): B<<330.0,429.0>-<332.0,428.0>-<333.0,427.0>>/L<<333.0,427.0>--<330.0,429.0>> = 11.309932474020195

	* petapp (U+E006): B<<388.0,111.0>-<389.0,109.0>-<390.0,108.0>>/L<<390.0,108.0>--<388.0,111.0>> = 11.309932474020227

	* petapp (U+E006): B<<441.0,65.0>-<442.0,65.0>-<444.0,64.0>>/L<<444.0,64.0>--<441.0,65.0>> = 8.130102354155916

	* petapp (U+E006): B<<508.0,73.0>-<509.0,73.0>-<511.0,74.0>>/L<<511.0,74.0>--<508.0,73.0>> = 8.130102354155916

	* petapp (U+E006): B<<515.0,65.0>-<517.0,65.0>-<519.0,66.0>>/L<<519.0,66.0>--<515.0,65.0>> = 12.528807709151463

	* petapp (U+E006): B<<522.0,66.0>-<523.0,66.0>-<525.0,67.0>>/L<<525.0,67.0>--<522.0,66.0>> = 8.130102354155916

	* petapp (U+E006): B<<538.0,192.0>-<537.0,194.0>-<536.0,195.0>>/L<<536.0,195.0>--<538.0,192.0>> = 11.309932474020195

	* petapp (U+E006): B<<538.0,69.0>-<536.0,69.0>-<534.0,68.0>>/L<<534.0,68.0>--<538.0,69.0>> = 12.528807709151492

	* petapp (U+E006): B<<539.0,308.0>-<538.0,309.0>-<536.0,310.0>>/L<<536.0,310.0>--<539.0,308.0>> = 7.125016348901757

	* petapp (U+E006): B<<541.0,438.0>-<540.0,439.0>-<538.0,440.0>>/L<<538.0,440.0>--<541.0,438.0>> = 7.125016348901757

	* petapp (U+E006): B<<542.0,108.0>-<542.0,109.0>-<543.0,111.0>>/L<<543.0,111.0>--<542.0,108.0>> = 8.130102354155916

	* petapp (U+E006): B<<547.0,123.0>-<548.0,125.0>-<548.0,127.0>>/L<<548.0,127.0>--<547.0,123.0>> = 14.036243467926484

	* petapp (U+E006): B<<578.0,404.0>-<578.0,403.0>-<580.0,401.0>>/L<<580.0,401.0>--<578.0,404.0>> = 11.309932474020227

	* petapp (U+E006): B<<596.0,222.0>-<596.0,223.0>-<595.0,225.0>>/L<<595.0,225.0>--<596.0,222.0>> = 8.13010235415587

	* petapp (U+E006): B<<599.0,151.0>-<599.0,150.0>-<600.0,148.0>>/L<<600.0,148.0>--<599.0,151.0>> = 8.130102354155916

	* petapp (U+E006): B<<612.0,384.0>-<613.0,381.0>-<614.0,379.0>>/L<<614.0,379.0>--<612.0,384.0>> = 4.763641690726066

	* petapp (U+E006): B<<616.0,384.0>-<617.0,382.0>-<619.0,379.0>>/L<<619.0,379.0>--<616.0,384.0>> = 2.7263109939060786

	* petapp (U+E006): B<<623.0,357.0>-<623.0,356.0>-<624.0,354.0>>/L<<624.0,354.0>--<623.0,357.0>> = 8.130102354155916

	* petapp (U+E006): B<<625.0,368.0>-<626.0,367.0>-<627.0,365.0>>/L<<627.0,365.0>--<625.0,368.0>> = 7.125016348901705

	* petapp (U+E006): B<<630.0,343.0>-<630.0,342.0>-<631.0,340.0>>/L<<631.0,340.0>--<630.0,343.0>> = 8.130102354155916

	* petapp (U+E006): B<<635.0,334.0>-<635.0,333.0>-<636.0,331.0>>/L<<636.0,331.0>--<635.0,334.0>> = 8.130102354155916

	* petapp (U+E006): B<<640.0,346.0>-<641.0,345.0>-<642.0,343.0>>/L<<642.0,343.0>--<640.0,346.0>> = 7.125016348901705

	* petapp (U+E006): B<<644.0,321.0>-<644.0,320.0>-<645.0,318.0>>/L<<645.0,318.0>--<644.0,321.0>> = 8.130102354155916

	* petapp (U+E006): B<<671.0,316.0>-<673.0,315.0>-<674.0,314.0>>/L<<674.0,314.0>--<671.0,316.0>> = 11.309932474020195

	* petapp (U+E006): B<<671.0,456.0>-<670.0,454.0>-<668.0,452.0>>/L<<668.0,452.0>--<671.0,456.0>> = 8.13010235415596

	* petapp (U+E006): B<<684.0,307.0>-<686.0,306.0>-<687.0,305.0>>/L<<687.0,305.0>--<684.0,307.0>> = 11.309932474020195

	* petapp (U+E006): B<<686.0,267.0>-<685.0,269.0>-<684.0,270.0>>/L<<684.0,270.0>--<686.0,267.0>> = 11.309932474020195

	* petapp (U+E006): B<<698.0,191.0>-<699.0,194.0>-<699.0,196.0>>/L<<699.0,196.0>--<698.0,191.0>> = 11.309932474020227

	* petapp (U+E006): B<<703.0,53.0>-<701.0,54.0>-<700.0,55.0>>/L<<700.0,55.0>--<703.0,53.0>> = 11.309932474020227

	* petapp (U+E006): B<<748.0,25.0>-<746.0,26.0>-<745.0,27.0>>/L<<745.0,27.0>--<748.0,25.0>> = 11.309932474020227

	* petapp (U+E006): B<<765.0,5.0>-<764.0,7.0>-<763.0,8.0>>/L<<763.0,8.0>--<765.0,5.0>> = 11.309932474020195

	* petapp (U+E006): L<<278.0,506.0>--<277.0,509.0>>/B<<277.0,509.0>-<278.0,507.0>-<278.0,506.0>> = 8.130102354155916

	* petapp (U+E006): L<<279.0,501.0>--<278.0,504.0>>/B<<278.0,504.0>-<279.0,502.0>-<279.0,501.0>> = 8.130102354155916

	* petapp (U+E006): L<<282.0,491.0>--<281.0,494.0>>/B<<281.0,494.0>-<282.0,492.0>-<282.0,491.0>> = 8.130102354155916

	* petapp (U+E006): L<<299.0,459.0>--<297.0,462.0>>/B<<297.0,462.0>-<298.0,460.0>-<299.0,459.0>> = 7.125016348901705

	* petapp (U+E006): L<<324.0,434.0>--<321.0,436.0>>/B<<321.0,436.0>-<323.0,435.0>-<324.0,434.0>> = 7.125016348901757

	* petapp (U+E006): L<<333.0,427.0>--<330.0,429.0>>/B<<330.0,429.0>-<332.0,428.0>-<333.0,427.0>> = 7.125016348901757

	* petapp (U+E006): L<<390.0,108.0>--<388.0,111.0>>/B<<388.0,111.0>-<389.0,109.0>-<390.0,108.0>> = 7.125016348901705

	* petapp (U+E006): L<<501.0,225.0>--<507.0,222.0>>/L<<507.0,222.0>--<500.0,226.0>> = 3.1798301198640497

	* petapp (U+E006): L<<506.0,71.0>--<501.0,69.0>>/B<<501.0,69.0>-<504.0,71.0>-<506.0,71.0>> = 11.888658039627936

	* petapp (U+E006): L<<519.0,66.0>--<515.0,65.0>>/B<<515.0,65.0>-<517.0,65.0>-<519.0,66.0>> = 14.036243467926484

	* petapp (U+E006): L<<534.0,68.0>--<538.0,69.0>>/B<<538.0,69.0>-<536.0,69.0>-<534.0,68.0>> = 14.036243467926484

	* petapp (U+E006): L<<536.0,195.0>--<538.0,192.0>>/B<<538.0,192.0>-<537.0,194.0>-<536.0,195.0>> = 7.125016348901757

	* petapp (U+E006): L<<536.0,310.0>--<539.0,308.0>>/B<<539.0,308.0>-<538.0,309.0>-<536.0,310.0>> = 11.309932474020227

	* petapp (U+E006): L<<538.0,440.0>--<541.0,438.0>>/B<<541.0,438.0>-<540.0,439.0>-<538.0,440.0>> = 11.309932474020227

	* petapp (U+E006): L<<543.0,70.0>--<547.0,71.0>>/B<<547.0,71.0>-<542.0,70.0>-<543.0,70.0>> = 2.726310993906212

	* petapp (U+E006): L<<546.0,176.0>--<547.0,173.0>>/B<<547.0,173.0>-<546.0,175.0>-<546.0,176.0>> = 8.13010235415587

	* petapp (U+E006): L<<548.0,127.0>--<547.0,123.0>>/B<<547.0,123.0>-<548.0,125.0>-<548.0,127.0>> = 12.528807709151492

	* petapp (U+E006): L<<594.0,230.0>--<595.0,227.0>>/B<<595.0,227.0>-<594.0,229.0>-<594.0,230.0>> = 8.13010235415587

	* petapp (U+E006): L<<601.0,436.0>--<600.0,439.0>>/B<<600.0,439.0>-<601.0,437.0>-<601.0,436.0>> = 8.130102354155916

	* petapp (U+E006): L<<607.0,113.0>--<606.0,116.0>>/B<<606.0,116.0>-<607.0,114.0>-<607.0,113.0>> = 8.130102354155916

	* petapp (U+E006): L<<607.0,398.0>--<606.0,401.0>>/B<<606.0,401.0>-<607.0,399.0>-<607.0,398.0>> = 8.130102354155916

	* petapp (U+E006): L<<614.0,379.0>--<612.0,384.0>>/B<<612.0,384.0>-<613.0,381.0>-<614.0,379.0>> = 3.366460663429615

	* petapp (U+E006): L<<619.0,379.0>--<616.0,384.0>>/B<<616.0,384.0>-<617.0,382.0>-<619.0,379.0>> = 4.398705354995426

	* petapp (U+E006): L<<627.0,365.0>--<625.0,368.0>>/B<<625.0,368.0>-<626.0,367.0>-<627.0,365.0>> = 11.309932474020227

	* petapp (U+E006): L<<642.0,343.0>--<640.0,346.0>>/B<<640.0,346.0>-<641.0,345.0>-<642.0,343.0>> = 11.309932474020227

	* petapp (U+E006): L<<658.0,404.0>--<657.0,408.0>>/B<<657.0,408.0>-<657.0,405.0>-<658.0,404.0>> = 14.036243467926484

	* petapp (U+E006): L<<660.0,393.0>--<659.0,396.0>>/B<<659.0,396.0>-<660.0,394.0>-<660.0,393.0>> = 8.130102354155916

	* petapp (U+E006): L<<668.0,452.0>--<671.0,456.0>>/B<<671.0,456.0>-<670.0,454.0>-<668.0,452.0>> = 10.304846468766044

	* petapp (U+E006): L<<676.0,137.0>--<680.0,140.0>>/B<<680.0,140.0>-<675.0,137.0>-<676.0,137.0>> = 5.906141113770497

	* petapp (U+E006): L<<676.0,94.0>--<675.0,97.0>>/B<<675.0,97.0>-<676.0,95.0>-<676.0,94.0>> = 8.130102354155916

	* petapp (U+E006): L<<679.0,465.0>--<682.0,467.0>>/B<<682.0,467.0>-<680.0,466.0>-<679.5,465.5>> = 7.125016348901757

	* petapp (U+E006): L<<684.0,270.0>--<686.0,267.0>>/B<<686.0,267.0>-<685.0,269.0>-<684.0,270.0>> = 7.125016348901757

	* petapp (U+E006): L<<687.0,305.0>--<684.0,307.0>>/B<<684.0,307.0>-<686.0,306.0>-<687.0,305.0>> = 7.125016348901757

	* petapp (U+E006): L<<688.0,162.0>--<687.0,159.0>>/B<<687.0,159.0>-<688.0,161.0>-<688.0,162.0>> = 8.130102354155916

	* petapp (U+E006): L<<689.0,146.0>--<686.0,144.0>>/B<<686.0,144.0>-<688.0,146.0>-<689.0,146.5>> = 11.309932474020195

	* petapp (U+E006): L<<694.0,60.0>--<699.0,56.0>>/B<<699.0,56.0>-<698.0,57.0>-<696.5,58.0>> = 6.34019174590985

	* petapp (U+E006): L<<695.0,246.0>--<696.0,243.0>>/B<<696.0,243.0>-<695.0,245.0>-<695.0,246.0>> = 8.13010235415587

	* petapp (U+E006): L<<696.0,300.0>--<693.0,301.0>>/B<<693.0,301.0>-<695.0,300.0>-<696.0,300.0>> = 8.130102354155916

	* petapp (U+E006): L<<700.0,55.0>--<703.0,53.0>>/B<<703.0,53.0>-<701.0,54.0>-<700.0,55.0>> = 7.125016348901757

	* petapp (U+E006): L<<715.0,291.0>--<712.0,292.0>>/B<<712.0,292.0>-<714.0,291.0>-<715.0,291.0>> = 8.130102354155916

	* petapp (U+E006): L<<720.0,289.0>--<717.0,290.0>>/B<<717.0,290.0>-<719.0,289.0>-<720.0,289.0>> = 8.130102354155916

	* petapp (U+E006): L<<725.0,287.0>--<722.0,288.0>>/B<<722.0,288.0>-<724.0,287.0>-<725.0,287.0>> = 8.130102354155916

	* petapp (U+E006): L<<730.0,285.0>--<727.0,286.0>>/B<<727.0,286.0>-<729.0,285.0>-<730.0,285.0>> = 8.130102354155916

	* petapp (U+E006): L<<745.0,27.0>--<748.0,25.0>>/B<<748.0,25.0>-<746.0,26.0>-<745.0,27.0>> = 7.125016348901757

	* petapp (U+E006): L<<763.0,8.0>--<765.0,5.0>>/B<<765.0,5.0>-<764.0,7.0>-<763.0,8.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<583.0,372.0>-<587.0,368.0>-<590.0,366.0>>/L<<590.0,366.0>--<583.0,372.0>> = 6.911227119024609

	* petapp.minimal (U+E007): B<<633.0,435.0>-<634.0,433.0>-<634.0,430.0>>/L<<634.0,430.0>--<633.0,435.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<648.0,510.0>-<647.0,508.0>-<646.0,507.0>>/L<<646.0,507.0>--<648.0,510.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<702.0,247.0>-<701.0,248.0>-<700.0,250.0>>/L<<700.0,250.0>--<702.0,247.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<717.0,147.0>-<716.0,148.0>-<715.0,150.0>>/L<<715.0,150.0>--<717.0,147.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<722.0,137.0>-<721.0,139.0>-<720.0,140.0>>/L<<720.0,140.0>--<722.0,137.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<732.0,115.0>-<732.0,116.0>-<731.0,118.0>>/L<<731.0,118.0>--<732.0,115.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<732.0,191.0>-<732.0,192.0>-<731.0,194.0>>/L<<731.0,194.0>--<732.0,191.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<734.0,185.0>-<734.0,187.0>-<733.0,189.0>>/L<<733.0,189.0>--<734.0,185.0>> = 12.528807709151492

	* petapp.minimal (U+E007): B<<740.0,90.0>-<740.0,91.0>-<739.0,93.0>>/L<<739.0,93.0>--<740.0,90.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<750.0,110.0>-<750.0,111.0>-<749.0,113.0>>/L<<749.0,113.0>--<750.0,110.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<214.0,538.0>--<214.0,800.0>>/B<<214.0,800.0>-<216.0,769.0>-<228.5,742.0>> = 3.6913859864512575

	* petapp.minimal (U+E007): L<<632.0,473.0>--<633.0,476.0>>/B<<633.0,476.0>-<632.0,474.0>-<632.0,473.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<633.0,225.0>--<630.0,226.0>>/B<<630.0,226.0>-<632.0,225.0>-<633.0,225.0>> = 8.130102354155916

	* petapp.minimal (U+E007): L<<637.0,420.0>--<636.0,423.0>>/B<<636.0,423.0>-<637.0,421.0>-<637.0,420.0>> = 8.130102354155916

	* petapp.minimal (U+E007): L<<639.0,222.0>--<642.0,221.0>>/B<<642.0,221.0>-<640.0,222.0>-<639.0,222.5>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<646.0,507.0>--<648.0,510.0>>/B<<648.0,510.0>-<647.0,508.0>-<646.0,507.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<700.0,250.0>--<702.0,247.0>>/B<<702.0,247.0>-<701.0,248.0>-<700.0,250.0>> = 11.309932474020195

	* petapp.minimal (U+E007): L<<715.0,150.0>--<717.0,147.0>>/B<<717.0,147.0>-<716.0,148.0>-<715.0,150.0>> = 11.309932474020195

	* petapp.minimal (U+E007): L<<735.0,108.0>--<736.0,105.0>>/B<<736.0,105.0>-<735.0,107.0>-<735.0,108.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<738.0,98.0>--<739.0,95.0>>/B<<739.0,95.0>-<738.0,97.0>-<738.0,98.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<742.0,156.0>--<741.0,160.0>>/B<<741.0,160.0>-<743.0,153.0>-<742.0,156.0>> = 1.9091524329963898

	* petapp.minimal (U+E007): L<<744.0,148.0>--<743.0,151.0>>/B<<743.0,151.0>-<744.0,149.0>-<744.0,148.0>> = 8.130102354155916

	* petapp.minimal (U+E007): L<<744.0,61.0>--<745.0,58.0>>/B<<745.0,58.0>-<744.0,60.0>-<744.0,61.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<745.0,142.0>--<744.0,145.0>>/B<<744.0,145.0>-<745.0,143.0>-<745.0,142.0>> = 8.130102354155916

	* petapp.minimal (U+E007): L<<746.0,137.0>--<745.0,140.0>>/B<<745.0,140.0>-<746.0,138.0>-<746.0,137.0>> = 8.130102354155916

	* petapp.minimal (U+E007): L<<749.0,78.0>--<750.0,81.0>>/B<<750.0,81.0>-<749.0,79.0>-<749.0,78.0>> = 8.13010235415587

	* petapp.wpda (U+E008): L<<187.0,222.0>--<181.0,218.0>>/B<<181.0,218.0>-<183.0,219.0>-<185.0,218.0>> = 7.125016348901757

	* pisafe (U+E010): B<<177.0,538.0>-<177.0,536.0>-<176.0,534.0>>/L<<176.0,534.0>--<177.0,538.0>> = 12.528807709151492

	* pisafe (U+E010): B<<799.0,577.0>-<798.0,579.0>-<797.0,580.0>>/L<<797.0,580.0>--<799.0,577.0>> = 11.309932474020195

	* pisafe (U+E010): B<<804.0,568.0>-<804.0,569.0>-<803.0,571.0>>/L<<803.0,571.0>--<804.0,568.0>> = 8.13010235415587

	* pisafe (U+E010): B<<807.0,563.0>-<806.0,565.0>-<805.0,566.0>>/L<<805.0,566.0>--<807.0,563.0>> = 11.309932474020195

	* pisafe (U+E010): B<<818.0,530.0>-<818.0,532.0>-<817.0,534.0>>/L<<817.0,534.0>--<818.0,530.0>> = 12.528807709151492

	* pisafe (U+E010): L<<176.0,534.0>--<177.0,538.0>>/B<<177.0,538.0>-<177.0,536.0>-<176.0,534.0>> = 14.036243467926484

	* pisafe (U+E010): L<<182.0,551.0>--<183.0,554.0>>/B<<183.0,554.0>-<182.0,552.0>-<182.0,551.0>> = 8.13010235415587

	* pisafe (U+E010): L<<752.0,626.0>--<756.0,623.0>>/B<<756.0,623.0>-<754.0,624.0>-<752.0,626.0>> = 10.304846468766009

	* pisafe (U+E010): L<<797.0,580.0>--<799.0,577.0>>/B<<799.0,577.0>-<798.0,579.0>-<797.0,580.0>> = 7.125016348901757

	* pisafe (U+E010): L<<805.0,566.0>--<807.0,563.0>>/B<<807.0,563.0>-<806.0,565.0>-<805.0,566.0>> = 7.125016348901757

	* pisafe (U+E010): L<<817.0,534.0>--<818.0,530.0>>/B<<818.0,530.0>-<818.0,532.0>-<817.0,534.0>> = 14.036243467926484 

	* pisafe (U+E010): L<<823.0,507.0>--<824.0,504.0>>/B<<824.0,504.0>-<823.0,506.0>-<823.0,507.0>> = 8.13010235415587 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* fi (U+FB01): L<<255.0,544.0>--<463.0,543.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[18] PitagonSansText-Italic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check OFL body text is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text">com.google.fonts/check/license/OFL_body_text</a>)</summary><div>


* 🔥 **FAIL** The OFL.txt body text is incorrect. Please use https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt as a template. You should only modify the first line. [code: incorrect-ofl-body-text]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ
at: https://scripts.sil.org/OFL." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks">com.google.fonts/check/name/line_breaks</a>)</summary><div>


* 🔥 **FAIL** Name entry DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1294, but got 1214 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.11, while a newer 0.8.13 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'Pita' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
</div></details><details><summary>⚠ <b>WARN:</b> Description strings in the name table must not exceed 200 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/description_max_length">com.google.fonts/check/name/description_max_length</a>)</summary><div>


* ⚠ **WARN** A few name table entries with ID=10 (NameID.DESCRIPTION) are longer than 200 characters. Please check whether those entries are copyright notices mistakenly stored in the description string entries by a bug in an old FontLab version. If that's the case, then such copyright notices must be removed from these entries. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- periodcentered.001 

	- registered.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* petapp (U+E006): L<<282.0,304.0>--<312.0,286.0>> -> L<<312.0,286.0>--<339.0,271.0>>

	* petapp (U+E006): L<<312.0,333.0>--<273.0,356.0>> -> L<<273.0,356.0>--<257.0,365.0>>

	* petapp (U+E006): L<<355.0,309.0>--<312.0,333.0>> -> L<<312.0,333.0>--<273.0,356.0>>

	* petapp (U+E006): L<<371.0,299.0>--<355.0,309.0>> -> L<<355.0,309.0>--<312.0,333.0>>

	* petapp (U+E006): L<<371.0,640.0>--<467.0,585.0>> -> L<<467.0,585.0>--<515.0,556.0>>

	* petapp (U+E006): L<<373.0,298.0>--<371.0,299.0>> -> L<<371.0,299.0>--<355.0,309.0>>

	* petapp (U+E006): L<<426.0,268.0>--<373.0,298.0>> -> L<<373.0,298.0>--<371.0,299.0>>

	* petapp (U+E006): L<<467.0,585.0>--<515.0,556.0>> -> L<<515.0,556.0>--<534.0,545.0>>

	* petapp (U+E006): L<<468.0,243.0>--<426.0,268.0>> -> L<<426.0,268.0>--<373.0,298.0>>

	* petapp (U+E006): L<<474.0,240.0>--<468.0,243.0>> -> L<<468.0,243.0>--<426.0,268.0>>

	* petapp (U+E006): L<<498.0,226.0>--<474.0,240.0>> -> L<<474.0,240.0>--<468.0,243.0>>

	* petapp (U+E006): L<<505.0,222.0>--<498.0,226.0>> -> L<<498.0,226.0>--<474.0,240.0>>

	* petapp (U+E006): L<<691.0,61.0>--<692.0,60.0>> -> L<<692.0,60.0>--<696.0,56.0>>

	* petapp (U+E006): L<<721.0,485.0>--<725.0,485.0>> -> L<<725.0,485.0>--<764.0,485.0>>

	* petapp.minimal (U+E007): L<<264.0,373.0>--<351.0,339.0>> -> L<<351.0,339.0>--<432.0,305.0>>

	* petapp.minimal (U+E007): L<<351.0,339.0>--<432.0,305.0>> -> L<<432.0,305.0>--<448.0,299.0>>

	* petapp.minimal (U+E007): L<<381.0,352.0>--<331.0,376.0>> -> L<<331.0,376.0>--<305.0,390.0>>

	* petapp.minimal (U+E007): L<<432.0,305.0>--<448.0,299.0>> -> L<<448.0,299.0>--<504.0,276.0>>

	* petapp.minimal (U+E007): L<<432.0,326.0>--<381.0,352.0>> -> L<<381.0,352.0>--<331.0,376.0>>

	* petapp.minimal (U+E007): L<<435.0,187.0>--<405.0,192.0>> -> L<<405.0,192.0>--<304.0,211.0>>

	* petapp.minimal (U+E007): L<<448.0,299.0>--<504.0,276.0>> -> L<<504.0,276.0>--<612.0,232.0>>

	* petapp.minimal (U+E007): L<<455.0,314.0>--<432.0,326.0>> -> L<<432.0,326.0>--<381.0,352.0>>

	* petapp.minimal (U+E007): L<<504.0,175.0>--<435.0,187.0>> -> L<<435.0,187.0>--<405.0,192.0>>

	* petapp.minimal (U+E007): L<<504.0,276.0>--<612.0,232.0>> -> L<<612.0,232.0>--<621.0,229.0>>

	* petapp.minimal (U+E007): L<<504.0,289.0>--<455.0,314.0>> -> L<<455.0,314.0>--<432.0,326.0>>

	* petapp.minimal (U+E007): L<<588.0,160.0>--<504.0,175.0>> -> L<<504.0,175.0>--<435.0,187.0>>

	* petapp.minimal (U+E007): L<<621.0,229.0>--<504.0,289.0>> -> L<<504.0,289.0>--<455.0,314.0>>

	* petapp.minimal (U+E007): L<<742.0,30.0>--<742.0,31.0>> -> L<<742.0,31.0>--<742.0,32.0>>

	* petapp.minimal (U+E007): L<<743.0,33.0>--<743.0,34.0>> -> L<<743.0,34.0>--<743.0,36.0>>

	* petapp.minimal (U+E007): L<<743.0,34.0>--<743.0,36.0>> -> L<<743.0,36.0>--<743.0,37.0>>

	* petapp.minimal (U+E007): L<<747.0,73.0>--<746.0,63.0>> -> L<<746.0,63.0>--<743.0,38.0>>

	* petapp.minimal (U+E007): L<<747.0,74.0>--<747.0,73.0>> -> L<<747.0,73.0>--<746.0,63.0>>

	* petapp.minimal (U+E007): L<<752.0,131.0>--<747.0,74.0>> -> L<<747.0,74.0>--<747.0,73.0>>

	* petapp.minimal (U+E007): L<<754.0,162.0>--<752.0,131.0>> -> L<<752.0,131.0>--<747.0,74.0>>

	* petapp.minimal (U+E007): L<<755.0,175.0>--<754.0,162.0>> -> L<<754.0,162.0>--<752.0,131.0>>

	* petapp.minimal (U+E007): L<<757.0,196.0>--<755.0,175.0>> -> L<<755.0,175.0>--<754.0,162.0>>

	* petapp.minimal (U+E007): L<<758.0,210.0>--<757.0,196.0>> -> L<<757.0,196.0>--<755.0,175.0>>

	* petapp.minimal (U+E007): L<<758.0,213.0>--<758.0,210.0>> -> L<<758.0,210.0>--<757.0,196.0>>

	* petapp.wpda (U+E008): L<<640.0,140.0>--<627.0,132.0>> -> L<<627.0,132.0>--<618.0,127.0>>

	* piads (U+E001): L<<112.0,541.0>--<116.0,544.0>> -> L<<116.0,544.0>--<445.0,782.0>>

	* piads (U+E001): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<878.0,541.0>>

	* picall (U+E009): L<<112.0,541.0>--<116.0,544.0>> -> L<<116.0,544.0>--<445.0,782.0>>

	* picall (U+E009): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<878.0,541.0>>

	* pioffice (U+E002): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<877.0,542.0>>

	* pisafe (U+E010): L<<167.0,362.0>--<167.0,491.0>> -> L<<167.0,491.0>--<167.0,494.0>>

	* pisafe (U+E010): L<<203.0,695.0>--<239.0,708.0>> -> L<<239.0,708.0>--<389.0,762.0>>

	* pisafe (U+E010): L<<239.0,708.0>--<389.0,762.0>> -> L<<389.0,762.0>--<494.0,800.0>>

	* pisafe (U+E010): L<<495.0,800.0>--<600.0,762.0>> -> L<<600.0,762.0>--<750.0,708.0>>

	* pisafe (U+E010): L<<600.0,762.0>--<750.0,708.0>> -> L<<750.0,708.0>--<786.0,695.0>>

	* pisign (U+E005): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<877.0,542.0>>

	* pitagon (U+E000): L<<112.0,543.0>--<116.0,546.0>> -> L<<116.0,546.0>--<445.0,784.0>>

	* pitagon (U+E000): L<<209.0,62.0>--<84.0,446.0>> -> L<<84.0,446.0>--<82.0,452.0>>

	* pitagon (U+E000): L<<547.0,784.0>--<874.0,546.0>> -> L<<874.0,546.0>--<878.0,543.0>>

	* pitagram (U+E003): L<<813.0,512.0>--<810.0,514.0>> -> L<<810.0,514.0>--<537.0,711.0>>

	* piweb (U+E004): L<<813.0,512.0>--<810.0,514.0>> -> L<<810.0,514.0>--<537.0,711.0>>

	* sparks (U+E011): L<<100.0,798.0>--<103.0,797.0>> -> L<<103.0,797.0>--<198.0,762.0>>

	* sparks (U+E011): L<<103.0,797.0>--<198.0,762.0>> -> L<<198.0,762.0>--<209.0,759.0>>

	* sparks (U+E011): L<<198.0,762.0>--<209.0,759.0>> -> L<<209.0,759.0>--<400.0,690.0>>

	* sparks (U+E011): L<<209.0,759.0>--<400.0,690.0>> -> L<<400.0,690.0>--<431.0,680.0>>

	* sparks (U+E011): L<<291.0,596.0>--<363.0,534.0>> -> L<<363.0,534.0>--<382.0,516.0>>

	* sparks (U+E011): L<<381.0,366.0>--<383.0,367.0>> -> L<<383.0,367.0>--<486.0,429.0>>

	* sparks (U+E011): L<<383.0,367.0>--<486.0,429.0>> -> L<<486.0,429.0>--<488.0,430.0>>

	* sparks (U+E011): L<<409.0,102.0>--<98.0,641.0>> -> L<<98.0,641.0>--<47.0,731.0>>

	* sparks (U+E011): L<<440.0,659.0>--<436.0,649.0>> -> L<<436.0,649.0>--<434.0,643.0>>

	* sparks (U+E011): L<<454.0,24.0>--<409.0,102.0>> -> L<<409.0,102.0>--<98.0,641.0>>

	* sparks (U+E011): L<<504.0,429.0>--<606.0,367.0>> -> L<<606.0,367.0>--<608.0,366.0>>

	* sparks (U+E011): L<<558.0,680.0>--<596.0,694.0>> -> L<<596.0,694.0>--<780.0,759.0>>

	* sparks (U+E011): L<<579.0,101.0>--<550.0,51.0>> -> L<<550.0,51.0>--<535.0,24.0>>

	* sparks (U+E011): L<<596.0,694.0>--<780.0,759.0>> -> L<<780.0,759.0>--<807.0,768.0>>

	* sparks (U+E011): L<<607.0,516.0>--<627.0,534.0>> -> L<<627.0,534.0>--<699.0,596.0>>

	* sparks (U+E011): L<<614.0,629.0>--<577.0,632.0>> -> L<<577.0,632.0>--<568.0,633.0>>

	* sparks (U+E011): L<<655.0,626.0>--<614.0,629.0>> -> L<<614.0,629.0>--<577.0,632.0>>

	* sparks (U+E011): L<<656.0,626.0>--<655.0,626.0>> -> L<<655.0,626.0>--<614.0,629.0>>

	* sparks (U+E011): L<<690.0,623.0>--<656.0,626.0>> -> L<<656.0,626.0>--<655.0,626.0>>

	* sparks (U+E011): L<<691.0,623.0>--<690.0,623.0>> -> L<<690.0,623.0>--<656.0,626.0>>

	* sparks (U+E011): L<<750.0,397.0>--<579.0,101.0>> -> L<<579.0,101.0>--<550.0,51.0>>

	* sparks (U+E011): L<<780.0,759.0>--<807.0,768.0>> -> L<<807.0,768.0>--<886.0,797.0>>

	* sparks (U+E011): L<<897.0,652.0>--<750.0,397.0>> -> L<<750.0,397.0>--<579.0,101.0>>

	* sparks (U+E011): L<<942.0,730.0>--<897.0,652.0>> -> L<<897.0,652.0>--<750.0,397.0>> 

	* sparks (U+E011): L<<943.0,732.0>--<942.0,730.0>> -> L<<942.0,730.0>--<897.0,652.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* petapp (U+E006): B<<289.0,471.0>-<290.0,469.0>-<291.0,468.0>>/L<<291.0,468.0>--<289.0,471.0>> = 11.309932474020227

	* petapp (U+E006): B<<295.0,293.0>-<289.0,300.0>-<282.0,304.0>>/L<<282.0,304.0>--<312.0,286.0>> = 1.2188752351307344

	* petapp (U+E006): B<<328.0,429.0>-<329.0,428.0>-<331.0,427.0>>/L<<331.0,427.0>--<328.0,429.0>> = 7.125016348901757

	* petapp (U+E006): B<<415.0,76.0>-<416.0,76.0>-<418.0,75.0>>/L<<418.0,75.0>--<415.0,76.0>> = 8.130102354155916

	* petapp (U+E006): B<<424.0,71.0>-<425.0,71.0>-<427.0,70.0>>/L<<427.0,70.0>--<424.0,71.0>> = 8.130102354155916

	* petapp (U+E006): B<<439.0,65.0>-<440.0,65.0>-<442.0,64.0>>/L<<442.0,64.0>--<439.0,65.0>> = 8.130102354155916

	* petapp (U+E006): B<<483.0,64.0>-<484.0,64.0>-<486.0,65.0>>/L<<486.0,65.0>--<483.0,64.0>> = 8.130102354155916

	* petapp (U+E006): B<<513.0,65.0>-<515.0,65.0>-<517.0,66.0>>/L<<517.0,66.0>--<513.0,65.0>> = 12.528807709151463

	* petapp (U+E006): B<<519.0,66.0>-<521.0,66.0>-<523.0,67.0>>/L<<523.0,67.0>--<519.0,66.0>> = 12.528807709151463

	* petapp (U+E006): B<<529.0,68.0>-<528.0,68.0>-<526.0,67.0>>/L<<526.0,67.0>--<529.0,68.0>> = 8.13010235415587

	* petapp (U+E006): B<<536.0,192.0>-<535.0,194.0>-<534.0,195.0>>/L<<534.0,195.0>--<536.0,192.0>> = 11.309932474020195

	* petapp (U+E006): B<<536.0,69.0>-<534.0,69.0>-<532.0,68.0>>/L<<532.0,68.0>--<536.0,69.0>> = 12.528807709151492

	* petapp (U+E006): B<<537.0,308.0>-<536.0,309.0>-<534.0,310.0>>/L<<534.0,310.0>--<537.0,308.0>> = 7.125016348901757

	* petapp (U+E006): B<<539.0,108.0>-<540.0,109.0>-<541.0,111.0>>/L<<541.0,111.0>--<539.0,108.0>> = 7.125016348901705

	* petapp (U+E006): B<<539.0,438.0>-<538.0,439.0>-<536.0,440.0>>/L<<536.0,440.0>--<539.0,438.0>> = 7.125016348901757

	* petapp (U+E006): B<<545.0,123.0>-<546.0,125.0>-<546.0,127.0>>/L<<546.0,127.0>--<545.0,123.0>> = 14.036243467926484

	* petapp (U+E006): B<<548.0,432.0>-<547.0,433.0>-<545.0,434.0>>/L<<545.0,434.0>--<548.0,432.0>> = 7.125016348901757

	* petapp (U+E006): B<<548.0,72.0>-<549.0,72.0>-<551.0,73.0>>/L<<551.0,73.0>--<548.0,72.0>> = 8.130102354155916

	* petapp (U+E006): B<<575.0,404.0>-<576.0,403.0>-<577.0,401.0>>/L<<577.0,401.0>--<575.0,404.0>> = 7.125016348901705

	* petapp (U+E006): B<<587.0,380.0>-<587.0,382.0>-<586.0,384.0>>/L<<586.0,384.0>--<587.0,380.0>> = 12.528807709151492

	* petapp (U+E006): B<<610.0,384.0>-<611.0,381.0>-<612.0,379.0>>/L<<612.0,379.0>--<610.0,384.0>> = 4.763641690726066

	* petapp (U+E006): B<<614.0,384.0>-<615.0,382.0>-<616.0,379.0>>/L<<616.0,379.0>--<614.0,384.0>> = 3.366460663429615

	* petapp (U+E006): B<<627.0,343.0>-<628.0,342.0>-<629.0,340.0>>/L<<629.0,340.0>--<627.0,343.0>> = 7.125016348901705

	* petapp (U+E006): B<<633.0,334.0>-<633.0,333.0>-<634.0,331.0>>/L<<634.0,331.0>--<633.0,334.0>> = 8.130102354155916

	* petapp (U+E006): B<<638.0,346.0>-<639.0,345.0>-<640.0,343.0>>/L<<640.0,343.0>--<638.0,346.0>> = 7.125016348901705

	* petapp (U+E006): B<<641.0,321.0>-<642.0,320.0>-<643.0,318.0>>/L<<643.0,318.0>--<641.0,321.0>> = 7.125016348901705

	* petapp (U+E006): B<<669.0,316.0>-<670.0,315.0>-<672.0,314.0>>/L<<672.0,314.0>--<669.0,316.0>> = 7.125016348901757

	* petapp (U+E006): B<<669.0,456.0>-<667.0,454.0>-<666.0,452.0>>/L<<666.0,452.0>--<669.0,456.0>> = 10.304846468766044

	* petapp (U+E006): B<<670.0,137.0>-<671.0,138.0>-<672.0,140.0>>/L<<672.0,140.0>--<670.0,137.0>> = 7.125016348901705

	* petapp (U+E006): B<<679.0,141.0>-<681.0,142.0>-<682.0,143.0>>/L<<682.0,143.0>--<679.0,141.0>> = 11.309932474020195

	* petapp (U+E006): B<<687.0,164.0>-<688.0,166.0>-<689.0,167.0>>/L<<689.0,167.0>--<687.0,164.0>> = 11.309932474020227

	* petapp (U+E006): B<<713.0,484.0>-<712.0,484.0>-<710.0,483.0>>/L<<710.0,483.0>--<713.0,484.0>> = 8.13010235415587

	* petapp (U+E006): B<<763.0,5.0>-<762.0,7.0>-<761.0,8.0>>/L<<761.0,8.0>--<763.0,5.0>> = 11.309932474020195

	* petapp (U+E006): L<<274.0,517.0>--<273.0,520.0>>/B<<273.0,520.0>-<274.0,518.0>-<274.0,517.0>> = 8.130102354155916

	* petapp (U+E006): L<<280.0,491.0>--<279.0,494.0>>/B<<279.0,494.0>-<280.0,492.0>-<280.0,491.0>> = 8.130102354155916

	* petapp (U+E006): L<<291.0,468.0>--<289.0,471.0>>/B<<289.0,471.0>-<290.0,469.0>-<291.0,468.0>> = 7.125016348901705

	* petapp (U+E006): L<<296.0,459.0>--<295.0,462.0>>/B<<295.0,462.0>-<296.0,460.0>-<296.0,459.0>> = 8.130102354155916

	* petapp (U+E006): L<<312.0,442.0>--<308.0,445.0>>/B<<308.0,445.0>-<310.0,444.0>-<312.0,442.0>> = 10.304846468766009

	* petapp (U+E006): L<<331.0,427.0>--<328.0,429.0>>/B<<328.0,429.0>-<329.0,428.0>-<331.0,427.0>> = 11.309932474020195

	* petapp (U+E006): L<<380.0,128.0>--<379.0,131.0>>/B<<379.0,131.0>-<380.0,129.0>-<380.0,128.0>> = 8.130102354155916

	* petapp (U+E006): L<<387.0,108.0>--<386.0,111.0>>/B<<386.0,111.0>-<387.0,109.0>-<387.0,108.0>> = 8.130102354155916

	* petapp (U+E006): L<<499.0,225.0>--<505.0,222.0>>/L<<505.0,222.0>--<498.0,226.0>> = 3.1798301198640497

	* petapp (U+E006): L<<504.0,71.0>--<499.0,69.0>>/B<<499.0,69.0>-<502.0,71.0>-<504.0,71.0>> = 11.888658039627936

	* petapp (U+E006): L<<517.0,66.0>--<513.0,65.0>>/B<<513.0,65.0>-<515.0,65.0>-<517.0,66.0>> = 14.036243467926484

	* petapp (U+E006): L<<523.0,67.0>--<519.0,66.0>>/B<<519.0,66.0>-<521.0,66.0>-<523.0,67.0>> = 14.036243467926484

	* petapp (U+E006): L<<532.0,68.0>--<536.0,69.0>>/B<<536.0,69.0>-<534.0,69.0>-<532.0,68.0>> = 14.036243467926484

	* petapp (U+E006): L<<534.0,195.0>--<536.0,192.0>>/B<<536.0,192.0>-<535.0,194.0>-<534.0,195.0>> = 7.125016348901757

	* petapp (U+E006): L<<534.0,310.0>--<537.0,308.0>>/B<<537.0,308.0>-<536.0,309.0>-<534.0,310.0>> = 11.309932474020227

	* petapp (U+E006): L<<536.0,440.0>--<539.0,438.0>>/B<<539.0,438.0>-<538.0,439.0>-<536.0,440.0>> = 11.309932474020227

	* petapp (U+E006): L<<541.0,111.0>--<539.0,108.0>>/B<<539.0,108.0>-<540.0,109.0>-<541.0,111.0>> = 11.309932474020227

	* petapp (U+E006): L<<541.0,70.0>--<545.0,71.0>>/B<<545.0,71.0>-<540.0,70.0>-<541.0,70.0>> = 2.726310993906212

	* petapp (U+E006): L<<542.0,181.0>--<543.0,178.0>>/B<<543.0,178.0>-<542.0,180.0>-<542.0,181.0>> = 8.13010235415587

	* petapp (U+E006): L<<545.0,434.0>--<548.0,432.0>>/B<<548.0,432.0>-<547.0,433.0>-<545.0,434.0>> = 11.309932474020227

	* petapp (U+E006): L<<546.0,127.0>--<545.0,123.0>>/B<<545.0,123.0>-<546.0,125.0>-<546.0,127.0>> = 12.528807709151492

	* petapp (U+E006): L<<556.0,74.0>--<553.0,73.0>>/B<<553.0,73.0>-<555.0,74.0>-<556.0,74.0>> = 8.130102354155916

	* petapp (U+E006): L<<577.0,401.0>--<575.0,404.0>>/B<<575.0,404.0>-<576.0,403.0>-<577.0,401.0>> = 11.309932474020227

	* petapp (U+E006): L<<583.0,256.0>--<584.0,252.0>>/B<<584.0,252.0>-<584.0,254.0>-<583.0,256.0>> = 14.036243467926484

	* petapp (U+E006): L<<586.0,384.0>--<587.0,380.0>>/B<<587.0,380.0>-<587.0,382.0>-<586.0,384.0>> = 14.036243467926484

	* petapp (U+E006): L<<598.0,432.0>--<599.0,429.0>>/B<<599.0,429.0>-<598.0,431.0>-<598.0,432.0>> = 8.13010235415587

	* petapp (U+E006): L<<602.0,122.0>--<601.0,125.0>>/B<<601.0,125.0>-<602.0,123.0>-<602.0,122.0>> = 8.130102354155916

	* petapp (U+E006): L<<611.0,96.0>--<611.0,96.0>>/B<<611.0,96.0>-<607.0,95.0>-<603.5,92.5>> = 14.036243467926484

	* petapp (U+E006): L<<612.0,379.0>--<610.0,384.0>>/B<<610.0,384.0>-<611.0,381.0>-<612.0,379.0>> = 3.366460663429615

	* petapp (U+E006): L<<613.0,374.0>--<612.0,377.0>>/B<<612.0,377.0>-<613.0,375.0>-<613.0,374.0>> = 8.130102354155916

	* petapp (U+E006): L<<615.0,369.0>--<614.0,372.0>>/B<<614.0,372.0>-<615.0,370.0>-<615.0,369.0>> = 8.130102354155916

	* petapp (U+E006): L<<616.0,379.0>--<614.0,384.0>>/B<<614.0,384.0>-<615.0,382.0>-<616.0,379.0>> = 4.763641690726066

	* petapp (U+E006): L<<629.0,340.0>--<627.0,343.0>>/B<<627.0,343.0>-<628.0,342.0>-<629.0,340.0>> = 11.309932474020227

	* petapp (U+E006): L<<640.0,343.0>--<638.0,346.0>>/B<<638.0,346.0>-<639.0,345.0>-<640.0,343.0>> = 11.309932474020227

	* petapp (U+E006): L<<643.0,318.0>--<641.0,321.0>>/B<<641.0,321.0>-<642.0,320.0>-<643.0,318.0>> = 11.309932474020227

	* petapp (U+E006): L<<657.0,433.0>--<658.0,436.0>>/B<<658.0,436.0>-<657.0,434.0>-<657.0,432.5>> = 8.13010235415587

	* petapp (U+E006): L<<661.0,383.0>--<660.0,386.0>>/B<<660.0,386.0>-<661.0,384.0>-<661.0,383.0>> = 8.130102354155916

	* petapp (U+E006): L<<666.0,452.0>--<669.0,456.0>>/B<<669.0,456.0>-<667.0,454.0>-<666.0,452.0>> = 8.13010235415596

	* petapp (U+E006): L<<672.0,140.0>--<670.0,137.0>>/B<<670.0,137.0>-<671.0,138.0>-<672.0,140.0>> = 11.309932474020227

	* petapp (U+E006): L<<682.0,143.0>--<679.0,141.0>>/B<<679.0,141.0>-<681.0,142.0>-<682.0,143.0>> = 7.125016348901757

	* petapp (U+E006): L<<686.0,162.0>--<685.0,159.0>>/B<<685.0,159.0>-<686.0,161.0>-<686.0,162.0>> = 8.130102354155916

	* petapp (U+E006): L<<689.0,167.0>--<687.0,164.0>>/B<<687.0,164.0>-<688.0,166.0>-<689.0,167.0>> = 7.125016348901705

	* petapp (U+E006): L<<689.0,256.0>--<690.0,253.0>>/B<<690.0,253.0>-<689.0,255.0>-<689.0,256.0>> = 8.13010235415587

	* petapp (U+E006): L<<691.0,251.0>--<692.0,248.0>>/B<<692.0,248.0>-<691.0,250.0>-<691.0,251.0>> = 8.13010235415587

	* petapp (U+E006): L<<700.0,480.0>--<703.0,481.0>>/B<<703.0,481.0>-<701.0,480.0>-<700.0,479.5>> = 8.13010235415587

	* petapp (U+E006): L<<705.0,482.0>--<708.0,483.0>>/B<<708.0,483.0>-<706.0,482.0>-<705.0,482.0>> = 8.13010235415587

	* petapp (U+E006): L<<708.0,293.0>--<705.0,294.0>>/B<<705.0,294.0>-<707.0,293.0>-<708.0,293.0>> = 8.130102354155916

	* petapp (U+E006): L<<728.0,285.0>--<725.0,286.0>>/B<<725.0,286.0>-<727.0,285.0>-<728.0,285.0>> = 8.130102354155916

	* petapp (U+E006): L<<761.0,8.0>--<763.0,5.0>>/B<<763.0,5.0>-<762.0,7.0>-<761.0,8.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<581.0,372.0>-<585.0,368.0>-<588.0,366.0>>/L<<588.0,366.0>--<581.0,372.0>> = 6.911227119024609

	* petapp.minimal (U+E007): B<<631.0,435.0>-<631.0,433.0>-<632.0,430.0>>/L<<632.0,430.0>--<631.0,435.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<632.0,481.0>-<632.0,480.0>-<631.0,478.0>>/L<<631.0,478.0>--<632.0,481.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<645.0,399.0>-<646.0,397.0>-<647.0,396.0>>/L<<647.0,396.0>--<645.0,399.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<646.0,510.0>-<645.0,508.0>-<644.0,507.0>>/L<<644.0,507.0>--<646.0,510.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<676.0,538.0>-<674.0,537.0>-<673.0,536.0>>/L<<673.0,536.0>--<676.0,538.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<700.0,247.0>-<699.0,248.0>-<698.0,250.0>>/L<<698.0,250.0>--<700.0,247.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<714.0,147.0>-<714.0,148.0>-<713.0,150.0>>/L<<713.0,150.0>--<714.0,147.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<720.0,137.0>-<719.0,139.0>-<718.0,140.0>>/L<<718.0,140.0>--<720.0,137.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<732.0,185.0>-<731.0,187.0>-<731.0,189.0>>/L<<731.0,189.0>--<732.0,185.0>> = 14.036243467926484

	* petapp.minimal (U+E007): B<<743.0,53.0>-<743.0,54.0>-<742.0,56.0>>/L<<742.0,56.0>--<743.0,53.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<212.0,538.0>--<212.0,800.0>>/B<<212.0,800.0>-<214.0,769.0>-<226.5,742.0>> = 3.6913859864512575

	* petapp.minimal (U+E007): L<<628.0,462.0>--<629.0,465.0>>/B<<629.0,465.0>-<628.0,463.0>-<628.0,462.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<630.0,473.0>--<631.0,476.0>>/B<<631.0,476.0>-<630.0,474.0>-<630.0,473.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<632.0,430.0>--<631.0,435.0>>/B<<631.0,435.0>-<631.0,433.0>-<632.0,430.0>> = 11.309932474020227

	* petapp.minimal (U+E007): L<<637.0,222.0>--<640.0,221.0>>/B<<640.0,221.0>-<638.0,222.0>-<637.0,222.5>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<639.0,498.0>--<640.0,501.0>>/B<<640.0,501.0>-<639.0,499.0>-<639.0,498.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<644.0,507.0>--<646.0,510.0>>/B<<646.0,510.0>-<645.0,508.0>-<644.0,507.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<647.0,396.0>--<645.0,399.0>>/B<<645.0,399.0>-<646.0,397.0>-<647.0,396.0>> = 7.125016348901705

	* petapp.minimal (U+E007): L<<673.0,536.0>--<676.0,538.0>>/B<<676.0,538.0>-<674.0,537.0>-<673.0,536.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<682.0,542.0>--<685.0,543.0>>/B<<685.0,543.0>-<683.0,542.0>-<682.0,542.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<687.0,544.0>--<690.0,545.0>>/B<<690.0,545.0>-<688.0,544.0>-<687.0,544.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<698.0,250.0>--<700.0,247.0>>/B<<700.0,247.0>-<699.0,248.0>-<698.0,250.0>> = 11.309932474020195

	* petapp.minimal (U+E007): L<<718.0,218.0>--<719.0,215.0>>/B<<719.0,215.0>-<718.0,217.0>-<718.0,218.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<731.0,113.0>--<732.0,110.0>>/B<<732.0,110.0>-<731.0,112.0>-<731.0,113.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<740.0,156.0>--<739.0,160.0>>/B<<739.0,160.0>-<740.0,153.0>-<740.0,156.0>> = 5.906141113770497

	* petapp.minimal (U+E007): L<<744.0,137.0>--<743.0,140.0>>/B<<743.0,140.0>-<744.0,138.0>-<744.0,137.0>> = 8.130102354155916

	* petapp.minimal (U+E007): L<<746.0,123.0>--<747.0,120.0>>/B<<747.0,120.0>-<746.0,122.0>-<746.0,123.0>> = 8.13010235415587

	* petapp.wpda (U+E008): B<<485.0,2.0>-<482.0,5.0>-<482.0,6.0>>/L<<482.0,6.0>--<481.0,1.0>> = 11.309932474020227

	* petapp.wpda (U+E008): L<<185.0,222.0>--<180.0,218.0>>/B<<180.0,218.0>-<182.0,219.0>-<183.0,218.0>> = 12.094757077012058

	* pisafe (U+E010): B<<175.0,538.0>-<175.0,536.0>-<174.0,534.0>>/L<<174.0,534.0>--<175.0,538.0>> = 12.528807709151492

	* pisafe (U+E010): B<<190.0,573.0>-<189.0,572.0>-<188.0,570.0>>/L<<188.0,570.0>--<190.0,573.0>> = 7.125016348901757

	* pisafe (U+E010): B<<211.0,602.0>-<210.0,600.0>-<208.0,598.0>>/L<<208.0,598.0>--<211.0,602.0>> = 8.13010235415596

	* pisafe (U+E010): B<<784.0,594.0>-<783.0,596.0>-<782.0,597.0>>/L<<782.0,597.0>--<784.0,594.0>> = 11.309932474020195

	* pisafe (U+E010): B<<797.0,577.0>-<796.0,579.0>-<795.0,580.0>>/L<<795.0,580.0>--<797.0,577.0>> = 11.309932474020195

	* pisafe (U+E010): B<<816.0,530.0>-<816.0,532.0>-<815.0,534.0>>/L<<815.0,534.0>--<816.0,530.0>> = 12.528807709151492

	* pisafe (U+E010): B<<820.0,515.0>-<820.0,516.0>-<819.0,518.0>>/L<<819.0,518.0>--<820.0,515.0>> = 8.13010235415587

	* pisafe (U+E010): L<<174.0,534.0>--<175.0,538.0>>/B<<175.0,538.0>-<175.0,536.0>-<174.0,534.0>> = 14.036243467926484

	* pisafe (U+E010): L<<188.0,570.0>--<190.0,573.0>>/B<<190.0,573.0>-<189.0,572.0>-<188.0,570.0>> = 11.309932474020195

	* pisafe (U+E010): L<<208.0,598.0>--<211.0,602.0>>/B<<211.0,602.0>-<210.0,600.0>-<208.0,598.0>> = 10.304846468766044

	* pisafe (U+E010): L<<750.0,626.0>--<754.0,623.0>>/B<<754.0,623.0>-<752.0,624.0>-<750.0,626.0>> = 10.304846468766009

	* pisafe (U+E010): L<<782.0,597.0>--<784.0,594.0>>/B<<784.0,594.0>-<783.0,596.0>-<782.0,597.0>> = 7.125016348901757

	* pisafe (U+E010): L<<795.0,580.0>--<797.0,577.0>>/B<<797.0,577.0>-<796.0,579.0>-<795.0,580.0>> = 7.125016348901757

	* pisafe (U+E010): L<<815.0,534.0>--<816.0,530.0>>/B<<816.0,530.0>-<816.0,532.0>-<815.0,534.0>> = 14.036243467926484 

	* pisafe (U+E010): L<<817.0,528.0>--<818.0,525.0>>/B<<818.0,525.0>-<817.0,527.0>-<817.0,528.0>> = 8.13010235415587 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[19] PitagonSansText-Medium.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check OFL body text is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text">com.google.fonts/check/license/OFL_body_text</a>)</summary><div>


* 🔥 **FAIL** The OFL.txt body text is incorrect. Please use https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt as a template. You should only modify the first line. [code: incorrect-ofl-body-text]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ
at: https://scripts.sil.org/OFL." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks">com.google.fonts/check/name/line_breaks</a>)</summary><div>


* 🔥 **FAIL** Name entry DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1294, but got 1214 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.11, while a newer 0.8.13 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'Pita' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
</div></details><details><summary>⚠ <b>WARN:</b> Description strings in the name table must not exceed 200 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/description_max_length">com.google.fonts/check/name/description_max_length</a>)</summary><div>


* ⚠ **WARN** A few name table entries with ID=10 (NameID.DESCRIPTION) are longer than 200 characters. Please check whether those entries are copyright notices mistakenly stored in the description string entries by a bug in an old FontLab version. If that's the case, then such copyright notices must be removed from these entries. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Pitagon Sans Text Medium' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- dotlessi.wide 

	- registered.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* petapp (U+E006): L<<283.0,304.0>--<313.0,286.0>> -> L<<313.0,286.0>--<340.0,271.0>>

	* petapp (U+E006): L<<313.0,333.0>--<274.0,356.0>> -> L<<274.0,356.0>--<258.0,365.0>>

	* petapp (U+E006): L<<356.0,309.0>--<313.0,333.0>> -> L<<313.0,333.0>--<274.0,356.0>>

	* petapp (U+E006): L<<372.0,299.0>--<356.0,309.0>> -> L<<356.0,309.0>--<313.0,333.0>>

	* petapp (U+E006): L<<372.0,640.0>--<468.0,585.0>> -> L<<468.0,585.0>--<516.0,556.0>>

	* petapp (U+E006): L<<374.0,298.0>--<372.0,299.0>> -> L<<372.0,299.0>--<356.0,309.0>>

	* petapp (U+E006): L<<427.0,268.0>--<374.0,298.0>> -> L<<374.0,298.0>--<372.0,299.0>>

	* petapp (U+E006): L<<468.0,585.0>--<516.0,556.0>> -> L<<516.0,556.0>--<535.0,545.0>>

	* petapp (U+E006): L<<469.0,243.0>--<427.0,268.0>> -> L<<427.0,268.0>--<374.0,298.0>>

	* petapp (U+E006): L<<475.0,240.0>--<469.0,243.0>> -> L<<469.0,243.0>--<427.0,268.0>>

	* petapp (U+E006): L<<499.0,226.0>--<475.0,240.0>> -> L<<475.0,240.0>--<469.0,243.0>>

	* petapp (U+E006): L<<506.0,222.0>--<499.0,226.0>> -> L<<499.0,226.0>--<475.0,240.0>>

	* petapp (U+E006): L<<597.0,453.0>--<597.0,455.0>> -> L<<597.0,455.0>--<597.0,456.0>>

	* petapp (U+E006): L<<597.0,455.0>--<597.0,454.0>> -> L<<597.0,454.0>--<597.0,453.0>>

	* petapp (U+E006): L<<692.0,61.0>--<693.0,60.0>> -> L<<693.0,60.0>--<697.0,56.0>>

	* petapp (U+E006): L<<722.0,485.0>--<726.0,485.0>> -> L<<726.0,485.0>--<765.0,485.0>>

	* petapp.minimal (U+E007): L<<265.0,373.0>--<352.0,339.0>> -> L<<352.0,339.0>--<433.0,305.0>>

	* petapp.minimal (U+E007): L<<352.0,339.0>--<433.0,305.0>> -> L<<433.0,305.0>--<449.0,299.0>>

	* petapp.minimal (U+E007): L<<382.0,352.0>--<332.0,376.0>> -> L<<332.0,376.0>--<306.0,390.0>>

	* petapp.minimal (U+E007): L<<433.0,305.0>--<449.0,299.0>> -> L<<449.0,299.0>--<505.0,276.0>>

	* petapp.minimal (U+E007): L<<433.0,326.0>--<382.0,352.0>> -> L<<382.0,352.0>--<332.0,376.0>>

	* petapp.minimal (U+E007): L<<436.0,187.0>--<406.0,192.0>> -> L<<406.0,192.0>--<305.0,211.0>>

	* petapp.minimal (U+E007): L<<449.0,299.0>--<505.0,276.0>> -> L<<505.0,276.0>--<613.0,232.0>>

	* petapp.minimal (U+E007): L<<456.0,314.0>--<433.0,326.0>> -> L<<433.0,326.0>--<382.0,352.0>>

	* petapp.minimal (U+E007): L<<505.0,175.0>--<436.0,187.0>> -> L<<436.0,187.0>--<406.0,192.0>>

	* petapp.minimal (U+E007): L<<505.0,276.0>--<613.0,232.0>> -> L<<613.0,232.0>--<622.0,229.0>>

	* petapp.minimal (U+E007): L<<505.0,289.0>--<456.0,314.0>> -> L<<456.0,314.0>--<433.0,326.0>>

	* petapp.minimal (U+E007): L<<589.0,160.0>--<505.0,175.0>> -> L<<505.0,175.0>--<436.0,187.0>>

	* petapp.minimal (U+E007): L<<622.0,229.0>--<505.0,289.0>> -> L<<505.0,289.0>--<456.0,314.0>>

	* petapp.minimal (U+E007): L<<743.0,30.0>--<743.0,31.0>> -> L<<743.0,31.0>--<743.0,32.0>>

	* petapp.minimal (U+E007): L<<743.0,31.0>--<743.0,32.0>> -> L<<743.0,32.0>--<743.0,33.0>>

	* petapp.minimal (U+E007): L<<743.0,32.0>--<743.0,33.0>> -> L<<743.0,33.0>--<743.0,34.0>>

	* petapp.minimal (U+E007): L<<748.0,73.0>--<747.0,63.0>> -> L<<747.0,63.0>--<744.0,38.0>>

	* petapp.minimal (U+E007): L<<748.0,74.0>--<748.0,73.0>> -> L<<748.0,73.0>--<747.0,63.0>>

	* petapp.minimal (U+E007): L<<753.0,131.0>--<748.0,74.0>> -> L<<748.0,74.0>--<748.0,73.0>>

	* petapp.minimal (U+E007): L<<755.0,162.0>--<753.0,131.0>> -> L<<753.0,131.0>--<748.0,74.0>>

	* petapp.minimal (U+E007): L<<756.0,175.0>--<755.0,162.0>> -> L<<755.0,162.0>--<753.0,131.0>>

	* petapp.minimal (U+E007): L<<758.0,196.0>--<756.0,175.0>> -> L<<756.0,175.0>--<755.0,162.0>>

	* petapp.minimal (U+E007): L<<759.0,210.0>--<758.0,196.0>> -> L<<758.0,196.0>--<756.0,175.0>>

	* petapp.minimal (U+E007): L<<759.0,213.0>--<759.0,210.0>> -> L<<759.0,210.0>--<758.0,196.0>>

	* petapp.wpda (U+E008): L<<641.0,140.0>--<628.0,132.0>> -> L<<628.0,132.0>--<619.0,127.0>>

	* piads (U+E001): L<<113.0,541.0>--<117.0,544.0>> -> L<<117.0,544.0>--<446.0,782.0>>

	* piads (U+E001): L<<547.0,782.0>--<875.0,544.0>> -> L<<875.0,544.0>--<879.0,541.0>>

	* picall (U+E009): L<<113.0,541.0>--<117.0,544.0>> -> L<<117.0,544.0>--<446.0,782.0>>

	* picall (U+E009): L<<547.0,782.0>--<875.0,544.0>> -> L<<875.0,544.0>--<879.0,541.0>>

	* pioffice (U+E002): L<<547.0,782.0>--<875.0,544.0>> -> L<<875.0,544.0>--<878.0,542.0>>

	* pisafe (U+E010): L<<168.0,362.0>--<168.0,491.0>> -> L<<168.0,491.0>--<168.0,494.0>>

	* pisafe (U+E010): L<<204.0,695.0>--<240.0,708.0>> -> L<<240.0,708.0>--<390.0,762.0>>

	* pisafe (U+E010): L<<240.0,708.0>--<390.0,762.0>> -> L<<390.0,762.0>--<495.0,800.0>>

	* pisafe (U+E010): L<<496.0,800.0>--<601.0,762.0>> -> L<<601.0,762.0>--<751.0,708.0>>

	* pisafe (U+E010): L<<601.0,762.0>--<751.0,708.0>> -> L<<751.0,708.0>--<787.0,695.0>>

	* pisign (U+E005): L<<547.0,782.0>--<875.0,544.0>> -> L<<875.0,544.0>--<878.0,542.0>>

	* pitagon (U+E000): L<<113.0,543.0>--<117.0,546.0>> -> L<<117.0,546.0>--<446.0,784.0>>

	* pitagon (U+E000): L<<210.0,62.0>--<85.0,446.0>> -> L<<85.0,446.0>--<83.0,452.0>>

	* pitagon (U+E000): L<<548.0,784.0>--<875.0,546.0>> -> L<<875.0,546.0>--<879.0,543.0>>

	* pitagram (U+E003): L<<814.0,512.0>--<811.0,514.0>> -> L<<811.0,514.0>--<538.0,711.0>>

	* piweb (U+E004): L<<814.0,512.0>--<811.0,514.0>> -> L<<811.0,514.0>--<538.0,711.0>>

	* sparks (U+E011): L<<101.0,798.0>--<104.0,797.0>> -> L<<104.0,797.0>--<199.0,762.0>>

	* sparks (U+E011): L<<104.0,797.0>--<199.0,762.0>> -> L<<199.0,762.0>--<210.0,759.0>>

	* sparks (U+E011): L<<199.0,762.0>--<210.0,759.0>> -> L<<210.0,759.0>--<401.0,690.0>>

	* sparks (U+E011): L<<210.0,759.0>--<401.0,690.0>> -> L<<401.0,690.0>--<432.0,680.0>>

	* sparks (U+E011): L<<292.0,596.0>--<364.0,534.0>> -> L<<364.0,534.0>--<383.0,516.0>>

	* sparks (U+E011): L<<382.0,366.0>--<384.0,367.0>> -> L<<384.0,367.0>--<487.0,429.0>>

	* sparks (U+E011): L<<384.0,367.0>--<487.0,429.0>> -> L<<487.0,429.0>--<489.0,430.0>>

	* sparks (U+E011): L<<410.0,102.0>--<99.0,641.0>> -> L<<99.0,641.0>--<48.0,731.0>>

	* sparks (U+E011): L<<441.0,659.0>--<437.0,649.0>> -> L<<437.0,649.0>--<435.0,643.0>>

	* sparks (U+E011): L<<455.0,24.0>--<410.0,102.0>> -> L<<410.0,102.0>--<99.0,641.0>>

	* sparks (U+E011): L<<505.0,429.0>--<607.0,367.0>> -> L<<607.0,367.0>--<609.0,366.0>>

	* sparks (U+E011): L<<559.0,680.0>--<597.0,694.0>> -> L<<597.0,694.0>--<781.0,759.0>>

	* sparks (U+E011): L<<580.0,101.0>--<551.0,51.0>> -> L<<551.0,51.0>--<536.0,24.0>>

	* sparks (U+E011): L<<597.0,694.0>--<781.0,759.0>> -> L<<781.0,759.0>--<808.0,768.0>>

	* sparks (U+E011): L<<608.0,516.0>--<628.0,534.0>> -> L<<628.0,534.0>--<700.0,596.0>>

	* sparks (U+E011): L<<615.0,629.0>--<578.0,632.0>> -> L<<578.0,632.0>--<569.0,633.0>>

	* sparks (U+E011): L<<656.0,626.0>--<615.0,629.0>> -> L<<615.0,629.0>--<578.0,632.0>>

	* sparks (U+E011): L<<657.0,626.0>--<656.0,626.0>> -> L<<656.0,626.0>--<615.0,629.0>>

	* sparks (U+E011): L<<691.0,623.0>--<657.0,626.0>> -> L<<657.0,626.0>--<656.0,626.0>>

	* sparks (U+E011): L<<692.0,623.0>--<691.0,623.0>> -> L<<691.0,623.0>--<657.0,626.0>>

	* sparks (U+E011): L<<751.0,397.0>--<580.0,101.0>> -> L<<580.0,101.0>--<551.0,51.0>>

	* sparks (U+E011): L<<781.0,759.0>--<808.0,768.0>> -> L<<808.0,768.0>--<887.0,797.0>>

	* sparks (U+E011): L<<898.0,652.0>--<751.0,397.0>> -> L<<751.0,397.0>--<580.0,101.0>>

	* sparks (U+E011): L<<943.0,730.0>--<898.0,652.0>> -> L<<898.0,652.0>--<751.0,397.0>> 

	* sparks (U+E011): L<<944.0,732.0>--<943.0,730.0>> -> L<<943.0,730.0>--<898.0,652.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* petapp (U+E006): B<<296.0,293.0>-<290.0,300.0>-<283.0,304.0>>/L<<283.0,304.0>--<313.0,286.0>> = 1.2188752351307344

	* petapp (U+E006): B<<511.0,75.0>-<512.0,76.0>-<514.0,77.0>>/L<<514.0,77.0>--<511.0,75.0>> = 7.125016348901757

	* petapp (U+E006): B<<520.0,66.0>-<521.0,66.0>-<524.0,67.0>>/L<<524.0,67.0>--<520.0,66.0>> = 4.398705354995508

	* petapp (U+E006): B<<530.0,68.0>-<529.0,68.0>-<527.0,67.0>>/L<<527.0,67.0>--<530.0,68.0>> = 8.13010235415587

	* petapp (U+E006): B<<537.0,69.0>-<535.0,69.0>-<533.0,68.0>>/L<<533.0,68.0>--<537.0,69.0>> = 12.528807709151492

	* petapp (U+E006): B<<540.0,438.0>-<538.0,439.0>-<537.0,440.0>>/L<<537.0,440.0>--<540.0,438.0>> = 11.309932474020227

	* petapp (U+E006): B<<541.0,183.0>-<541.0,184.0>-<540.0,186.0>>/L<<540.0,186.0>--<541.0,183.0>> = 8.13010235415587

	* petapp (U+E006): B<<546.0,123.0>-<546.0,125.0>-<547.0,127.0>>/L<<547.0,127.0>--<546.0,123.0>> = 12.528807709151492

	* petapp (U+E006): B<<549.0,158.0>-<549.0,159.0>-<548.0,161.0>>/L<<548.0,161.0>--<549.0,158.0>> = 8.13010235415587

	* petapp (U+E006): B<<549.0,72.0>-<550.0,72.0>-<552.0,73.0>>/L<<552.0,73.0>--<549.0,72.0>> = 8.130102354155916

	* petapp (U+E006): B<<576.0,404.0>-<577.0,403.0>-<578.0,401.0>>/L<<578.0,401.0>--<576.0,404.0>> = 7.125016348901705

	* petapp (U+E006): B<<588.0,380.0>-<588.0,382.0>-<587.0,384.0>>/L<<587.0,384.0>--<588.0,380.0>> = 12.528807709151492

	* petapp (U+E006): B<<601.0,130.0>-<601.0,129.0>-<602.0,127.0>>/L<<602.0,127.0>--<601.0,130.0>> = 8.130102354155916

	* petapp (U+E006): B<<611.0,384.0>-<612.0,381.0>-<612.0,379.0>>/L<<612.0,379.0>--<611.0,384.0>> = 11.309932474020227

	* petapp (U+E006): B<<615.0,384.0>-<616.0,382.0>-<617.0,379.0>>/L<<617.0,379.0>--<615.0,384.0>> = 3.366460663429615

	* petapp (U+E006): B<<617.0,367.0>-<617.0,366.0>-<618.0,364.0>>/L<<618.0,364.0>--<617.0,367.0>> = 8.130102354155916

	* petapp (U+E006): B<<619.0,362.0>-<619.0,361.0>-<620.0,359.0>>/L<<620.0,359.0>--<619.0,362.0>> = 8.130102354155916

	* petapp (U+E006): B<<624.0,368.0>-<624.0,367.0>-<625.0,365.0>>/L<<625.0,365.0>--<624.0,368.0>> = 8.130102354155916

	* petapp (U+E006): B<<633.0,334.0>-<634.0,333.0>-<635.0,331.0>>/L<<635.0,331.0>--<633.0,334.0>> = 7.125016348901705

	* petapp (U+E006): B<<639.0,346.0>-<640.0,345.0>-<641.0,343.0>>/L<<641.0,343.0>--<639.0,346.0>> = 7.125016348901705

	* petapp (U+E006): B<<642.0,321.0>-<643.0,320.0>-<644.0,318.0>>/L<<644.0,318.0>--<642.0,321.0>> = 7.125016348901705

	* petapp (U+E006): B<<660.0,441.0>-<660.0,440.0>-<659.0,438.0>>/L<<659.0,438.0>--<660.0,441.0>> = 8.13010235415587

	* petapp (U+E006): B<<670.0,456.0>-<668.0,454.0>-<667.0,452.0>>/L<<667.0,452.0>--<670.0,456.0>> = 10.304846468766044

	* petapp (U+E006): B<<671.0,137.0>-<672.0,138.0>-<673.0,140.0>>/L<<673.0,140.0>--<671.0,137.0>> = 7.125016348901705

	* petapp (U+E006): B<<680.0,141.0>-<681.0,142.0>-<683.0,143.0>>/L<<683.0,143.0>--<680.0,141.0>> = 7.125016348901757

	* petapp (U+E006): B<<687.0,304.0>-<689.0,303.0>-<690.0,302.0>>/L<<690.0,302.0>--<687.0,304.0>> = 11.309932474020195

	* petapp (U+E006): B<<719.0,485.0>-<718.0,485.0>-<716.0,484.0>>/L<<716.0,484.0>--<719.0,485.0>> = 8.13010235415587

	* petapp (U+E006): B<<742.0,28.0>-<740.0,29.0>-<739.0,30.0>>/L<<739.0,30.0>--<742.0,28.0>> = 11.309932474020227

	* petapp (U+E006): B<<766.0,0.0>-<765.0,2.0>-<764.0,3.0>>/L<<764.0,3.0>--<766.0,0.0>> = 11.309932474020195

	* petapp (U+E006): L<<279.0,496.0>--<278.0,499.0>>/B<<278.0,499.0>-<279.0,497.0>-<279.0,496.0>> = 8.130102354155916

	* petapp (U+E006): L<<291.0,468.0>--<290.0,471.0>>/B<<290.0,471.0>-<291.0,469.0>-<291.0,468.0>> = 8.130102354155916

	* petapp (U+E006): L<<313.0,442.0>--<309.0,445.0>>/B<<309.0,445.0>-<311.0,444.0>-<313.0,442.0>> = 10.304846468766009

	* petapp (U+E006): L<<380.0,133.0>--<379.0,136.0>>/B<<379.0,136.0>-<380.0,134.0>-<380.0,133.0>> = 8.130102354155916

	* petapp (U+E006): L<<381.0,128.0>--<380.0,131.0>>/B<<380.0,131.0>-<381.0,129.0>-<381.0,128.0>> = 8.130102354155916

	* petapp (U+E006): L<<382.0,123.0>--<381.0,126.0>>/B<<381.0,126.0>-<382.0,124.0>-<382.0,123.0>> = 8.130102354155916

	* petapp (U+E006): L<<458.0,61.0>--<455.0,62.0>>/B<<455.0,62.0>-<457.0,61.0>-<458.0,61.0>> = 8.130102354155916

	* petapp (U+E006): L<<500.0,225.0>--<506.0,222.0>>/L<<506.0,222.0>--<499.0,226.0>> = 3.1798301198640497

	* petapp (U+E006): L<<505.0,71.0>--<500.0,69.0>>/B<<500.0,69.0>-<503.0,71.0>-<505.0,71.0>> = 11.888658039627936

	* petapp (U+E006): L<<514.0,77.0>--<511.0,75.0>>/B<<511.0,75.0>-<512.0,76.0>-<514.0,77.0>> = 11.309932474020195

	* petapp (U+E006): L<<524.0,67.0>--<520.0,66.0>>/B<<520.0,66.0>-<521.0,66.0>-<524.0,67.0>> = 14.036243467926484

	* petapp (U+E006): L<<533.0,68.0>--<537.0,69.0>>/B<<537.0,69.0>-<535.0,69.0>-<533.0,68.0>> = 14.036243467926484

	* petapp (U+E006): L<<537.0,440.0>--<540.0,438.0>>/B<<540.0,438.0>-<538.0,439.0>-<537.0,440.0>> = 7.125016348901757

	* petapp (U+E006): L<<541.0,70.0>--<546.0,71.0>>/B<<546.0,71.0>-<540.0,70.0>-<541.0,70.0>> = 1.8476102659943183

	* petapp (U+E006): L<<546.0,171.0>--<547.0,168.0>>/B<<547.0,168.0>-<546.0,170.0>-<546.0,171.0>> = 8.13010235415587

	* petapp (U+E006): L<<547.0,127.0>--<546.0,123.0>>/B<<546.0,123.0>-<546.0,125.0>-<547.0,127.0>> = 14.036243467926484

	* petapp (U+E006): L<<557.0,74.0>--<554.0,73.0>>/B<<554.0,73.0>-<556.0,74.0>-<557.0,74.0>> = 8.130102354155916

	* petapp (U+E006): L<<578.0,401.0>--<576.0,404.0>>/B<<576.0,404.0>-<577.0,403.0>-<578.0,401.0>> = 11.309932474020227

	* petapp (U+E006): L<<584.0,256.0>--<585.0,252.0>>/B<<585.0,252.0>-<585.0,254.0>-<584.0,256.0>> = 14.036243467926484

	* petapp (U+E006): L<<587.0,384.0>--<588.0,380.0>>/B<<588.0,380.0>-<588.0,382.0>-<587.0,384.0>> = 14.036243467926484

	* petapp (U+E006): L<<599.0,143.0>--<598.0,146.0>>/B<<598.0,146.0>-<599.0,144.0>-<599.0,143.0>> = 8.130102354155916

	* petapp (U+E006): L<<601.0,426.0>--<600.0,429.0>>/B<<600.0,429.0>-<601.0,427.0>-<601.0,426.0>> = 8.130102354155916

	* petapp (U+E006): L<<603.0,122.0>--<602.0,125.0>>/B<<602.0,125.0>-<603.0,123.0>-<603.0,122.0>> = 8.130102354155916

	* petapp (U+E006): L<<612.0,379.0>--<611.0,384.0>>/B<<611.0,384.0>-<612.0,381.0>-<612.0,379.0>> = 7.125016348901757

	* petapp (U+E006): L<<612.0,96.0>--<612.0,96.0>>/B<<612.0,96.0>-<608.0,95.0>-<604.5,92.5>> = 14.036243467926484

	* petapp (U+E006): L<<614.0,374.0>--<613.0,377.0>>/B<<613.0,377.0>-<614.0,375.0>-<614.0,374.0>> = 8.130102354155916

	* petapp (U+E006): L<<617.0,379.0>--<615.0,384.0>>/B<<615.0,384.0>-<616.0,382.0>-<617.0,379.0>> = 4.763641690726066

	* petapp (U+E006): L<<635.0,331.0>--<633.0,334.0>>/B<<633.0,334.0>-<634.0,333.0>-<635.0,331.0>> = 11.309932474020227

	* petapp (U+E006): L<<641.0,343.0>--<639.0,346.0>>/B<<639.0,346.0>-<640.0,345.0>-<641.0,343.0>> = 11.309932474020227

	* petapp (U+E006): L<<644.0,318.0>--<642.0,321.0>>/B<<642.0,321.0>-<643.0,320.0>-<644.0,318.0>> = 11.309932474020227

	* petapp (U+E006): L<<658.0,433.0>--<659.0,436.0>>/B<<659.0,436.0>-<658.0,434.0>-<657.5,432.5>> = 8.13010235415587

	* petapp (U+E006): L<<660.0,388.0>--<659.0,391.0>>/B<<659.0,391.0>-<660.0,389.0>-<660.0,388.0>> = 8.130102354155916

	* petapp (U+E006): L<<662.0,383.0>--<661.0,386.0>>/B<<661.0,386.0>-<662.0,384.0>-<662.0,383.0>> = 8.130102354155916

	* petapp (U+E006): L<<667.0,452.0>--<670.0,456.0>>/B<<670.0,456.0>-<668.0,454.0>-<667.0,452.0>> = 8.13010235415596

	* petapp (U+E006): L<<672.0,104.0>--<671.0,107.0>>/B<<671.0,107.0>-<672.0,105.0>-<672.0,104.0>> = 8.130102354155916

	* petapp (U+E006): L<<673.0,140.0>--<671.0,137.0>>/B<<671.0,137.0>-<672.0,138.0>-<673.0,140.0>> = 11.309932474020227

	* petapp (U+E006): L<<673.0,99.0>--<672.0,102.0>>/B<<672.0,102.0>-<673.0,100.0>-<673.0,99.0>> = 8.130102354155916

	* petapp (U+E006): L<<676.0,89.0>--<675.0,92.0>>/B<<675.0,92.0>-<676.0,90.0>-<676.5,89.0>> = 8.130102354155916

	* petapp (U+E006): L<<683.0,143.0>--<680.0,141.0>>/B<<680.0,141.0>-<681.0,142.0>-<683.0,143.0>> = 11.309932474020195

	* petapp (U+E006): L<<683.0,270.0>--<684.0,267.0>>/B<<684.0,267.0>-<683.0,269.0>-<683.0,270.0>> = 8.13010235415587

	* petapp (U+E006): L<<689.0,167.0>--<688.0,164.0>>/B<<688.0,164.0>-<689.0,166.0>-<689.0,167.0>> = 8.130102354155916

	* petapp (U+E006): L<<690.0,256.0>--<691.0,253.0>>/B<<691.0,253.0>-<690.0,255.0>-<690.0,256.0>> = 8.13010235415587

	* petapp (U+E006): L<<690.0,302.0>--<687.0,304.0>>/B<<687.0,304.0>-<689.0,303.0>-<690.0,302.0>> = 7.125016348901757

	* petapp (U+E006): L<<691.0,172.0>--<690.0,169.0>>/B<<690.0,169.0>-<691.0,171.0>-<691.5,172.0>> = 8.130102354155916

	* petapp (U+E006): L<<695.0,477.0>--<698.0,478.0>>/B<<698.0,478.0>-<696.0,477.0>-<695.0,477.0>> = 8.13010235415587

	* petapp (U+E006): L<<696.0,235.0>--<697.0,232.0>>/B<<697.0,232.0>-<696.0,234.0>-<696.0,235.0>> = 8.13010235415587

	* petapp (U+E006): L<<699.0,207.0>--<698.0,204.0>>/B<<698.0,204.0>-<699.0,206.0>-<699.0,207.5>> = 8.130102354155916

	* petapp (U+E006): L<<701.0,480.0>--<704.0,481.0>>/B<<704.0,481.0>-<702.0,480.0>-<701.0,479.5>> = 8.13010235415587

	* petapp (U+E006): L<<739.0,30.0>--<742.0,28.0>>/B<<742.0,28.0>-<740.0,29.0>-<739.0,30.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<582.0,372.0>-<586.0,368.0>-<589.0,366.0>>/L<<589.0,366.0>--<582.0,372.0>> = 6.911227119024609

	* petapp.minimal (U+E007): B<<632.0,435.0>-<632.0,433.0>-<633.0,430.0>>/L<<633.0,430.0>--<632.0,435.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<638.0,413.0>-<639.0,411.0>-<640.0,410.0>>/L<<640.0,410.0>--<638.0,413.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<641.0,408.0>-<641.0,407.0>-<642.0,405.0>>/L<<642.0,405.0>--<641.0,408.0>> = 8.130102354155916

	* petapp.minimal (U+E007): B<<646.0,399.0>-<647.0,397.0>-<648.0,396.0>>/L<<648.0,396.0>--<646.0,399.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<654.0,212.0>-<653.0,213.0>-<651.0,214.0>>/L<<651.0,214.0>--<654.0,212.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<701.0,247.0>-<700.0,248.0>-<699.0,250.0>>/L<<699.0,250.0>--<701.0,247.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<701.0,549.0>-<700.0,549.0>-<698.0,548.0>>/L<<698.0,548.0>--<701.0,549.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<720.0,215.0>-<719.0,217.0>-<718.0,218.0>>/L<<718.0,218.0>--<720.0,215.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<721.0,137.0>-<720.0,139.0>-<719.0,140.0>>/L<<719.0,140.0>--<721.0,137.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<741.0,10.5>-<740.0,5.0>-<739.0,0.0>>/B<<739.0,0.0>-<739.0,4.0>-<739.0,8.5>> = 11.309932474020195

	* petapp.minimal (U+E007): L<<213.0,538.0>--<213.0,800.0>>/B<<213.0,800.0>-<214.0,769.0>-<226.5,742.0>> = 1.8476102659945155

	* petapp.minimal (U+E007): L<<632.0,225.0>--<628.0,226.0>>/B<<628.0,226.0>-<630.0,225.0>-<632.0,225.0>> = 12.528807709151463

	* petapp.minimal (U+E007): L<<632.0,225.0>--<632.0,225.0>>/L<<632.0,225.0>--<628.0,226.0>> = 14.036243467926484

	* petapp.minimal (U+E007): L<<633.0,430.0>--<632.0,435.0>>/B<<632.0,435.0>-<632.0,433.0>-<633.0,430.0>> = 11.309932474020227

	* petapp.minimal (U+E007): L<<634.0,425.0>--<633.0,428.0>>/B<<633.0,428.0>-<634.0,426.0>-<634.0,425.0>> = 8.130102354155916

	* petapp.minimal (U+E007): L<<637.0,415.0>--<636.0,418.0>>/B<<636.0,418.0>-<637.0,416.0>-<637.0,415.0>> = 8.130102354155916

	* petapp.minimal (U+E007): L<<640.0,410.0>--<638.0,413.0>>/B<<638.0,413.0>-<639.0,411.0>-<640.0,410.0>> = 7.125016348901705

	* petapp.minimal (U+E007): L<<640.0,498.0>--<641.0,501.0>>/B<<641.0,501.0>-<640.0,499.0>-<640.0,498.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<645.0,507.0>--<646.0,510.0>>/B<<646.0,510.0>-<645.0,508.0>-<645.0,507.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<648.0,396.0>--<646.0,399.0>>/B<<646.0,399.0>-<647.0,397.0>-<648.0,396.0>> = 7.125016348901705

	* petapp.minimal (U+E007): L<<651.0,214.0>--<654.0,212.0>>/B<<654.0,212.0>-<653.0,213.0>-<651.0,214.0>> = 11.309932474020227

	* petapp.minimal (U+E007): L<<683.0,542.0>--<686.0,543.0>>/B<<686.0,543.0>-<684.0,542.0>-<683.0,542.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<688.0,544.0>--<691.0,545.0>>/B<<691.0,545.0>-<689.0,544.0>-<688.0,544.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<699.0,250.0>--<701.0,247.0>>/B<<701.0,247.0>-<700.0,248.0>-<699.0,250.0>> = 11.309932474020195

	* petapp.minimal (U+E007): L<<711.0,232.0>--<712.0,229.0>>/B<<712.0,229.0>-<711.0,231.0>-<711.0,232.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<718.0,218.0>--<720.0,215.0>>/B<<720.0,215.0>-<719.0,217.0>-<718.0,218.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<735.0,103.0>--<736.0,100.0>>/B<<736.0,100.0>-<735.0,102.0>-<735.0,103.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<738.0,166.0>--<739.0,163.0>>/B<<739.0,163.0>-<738.0,165.0>-<738.0,166.5>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<740.0,156.0>--<740.0,160.0>>/B<<740.0,160.0>-<741.0,153.0>-<740.0,156.0>> = 8.13010235415596

	* petapp.minimal (U+E007): L<<749.0,88.0>--<748.0,85.0>>/B<<748.0,85.0>-<749.0,87.0>-<749.0,88.0>> = 8.130102354155916

	* petapp.wpda (U+E008): L<<186.0,222.0>--<180.0,218.0>>/B<<180.0,218.0>-<182.0,219.0>-<184.0,218.0>> = 7.125016348901757

	* pisafe (U+E010): B<<176.0,538.0>-<175.0,536.0>-<175.0,534.0>>/L<<175.0,534.0>--<176.0,538.0>> = 14.036243467926484

	* pisafe (U+E010): B<<190.0,573.0>-<190.0,572.0>-<189.0,570.0>>/L<<189.0,570.0>--<190.0,573.0>> = 8.13010235415587

	* pisafe (U+E010): B<<212.0,602.0>-<210.0,600.0>-<209.0,598.0>>/L<<209.0,598.0>--<212.0,602.0>> = 10.304846468766044

	* pisafe (U+E010): B<<236.0,623.0>-<234.0,622.0>-<233.0,621.0>>/L<<233.0,621.0>--<236.0,623.0>> = 11.309932474020227

	* pisafe (U+E010): B<<785.0,594.0>-<784.0,596.0>-<783.0,597.0>>/L<<783.0,597.0>--<785.0,594.0>> = 11.309932474020195

	* pisafe (U+E010): B<<803.0,568.0>-<802.0,569.0>-<801.0,571.0>>/L<<801.0,571.0>--<803.0,568.0>> = 7.125016348901757

	* pisafe (U+E010): B<<817.0,530.0>-<816.0,532.0>-<816.0,534.0>>/L<<816.0,534.0>--<817.0,530.0>> = 14.036243467926484

	* pisafe (U+E010): L<<175.0,534.0>--<176.0,538.0>>/B<<176.0,538.0>-<175.0,536.0>-<175.0,534.0>> = 12.528807709151492

	* pisafe (U+E010): L<<209.0,598.0>--<212.0,602.0>>/B<<212.0,602.0>-<210.0,600.0>-<209.0,598.0>> = 8.13010235415596

	* pisafe (U+E010): L<<233.0,621.0>--<236.0,623.0>>/B<<236.0,623.0>-<234.0,622.0>-<233.0,621.0>> = 7.125016348901757

	* pisafe (U+E010): L<<751.0,626.0>--<755.0,623.0>>/B<<755.0,623.0>-<753.0,624.0>-<751.0,626.0>> = 10.304846468766009

	* pisafe (U+E010): L<<783.0,597.0>--<785.0,594.0>>/B<<785.0,594.0>-<784.0,596.0>-<783.0,597.0>> = 7.125016348901757

	* pisafe (U+E010): L<<801.0,571.0>--<803.0,568.0>>/B<<803.0,568.0>-<802.0,569.0>-<801.0,571.0>> = 11.309932474020195

	* pisafe (U+E010): L<<804.0,566.0>--<805.0,563.0>>/B<<805.0,563.0>-<804.0,565.0>-<804.0,566.0>> = 8.13010235415587

	* pisafe (U+E010): L<<816.0,534.0>--<817.0,530.0>>/B<<817.0,530.0>-<816.0,532.0>-<816.0,534.0>> = 12.528807709151492 

	* pisafe (U+E010): L<<819.0,523.0>--<820.0,520.0>>/B<<820.0,520.0>-<819.0,522.0>-<819.0,523.0>> = 8.13010235415587 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[19] PitagonSansText-SemiBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check OFL body text is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text">com.google.fonts/check/license/OFL_body_text</a>)</summary><div>


* 🔥 **FAIL** The OFL.txt body text is incorrect. Please use https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt as a template. You should only modify the first line. [code: incorrect-ofl-body-text]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ
at: https://scripts.sil.org/OFL." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks">com.google.fonts/check/name/line_breaks</a>)</summary><div>


* 🔥 **FAIL** Name entry DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1294, but got 1214 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.11, while a newer 0.8.13 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'Pita' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
</div></details><details><summary>⚠ <b>WARN:</b> Description strings in the name table must not exceed 200 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/description_max_length">com.google.fonts/check/name/description_max_length</a>)</summary><div>


* ⚠ **WARN** A few name table entries with ID=10 (NameID.DESCRIPTION) are longer than 200 characters. Please check whether those entries are copyright notices mistakenly stored in the description string entries by a bug in an old FontLab version. If that's the case, then such copyright notices must be removed from these entries. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Pitagon Sans Text SemiBold' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- dotlessi.wide 

	- registered.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* fi (U+FB01): L<<239.0,541.0>--<470.0,541.0>> -> L<<470.0,541.0>--<472.0,541.0>>

	* fi (U+FB01): L<<470.0,541.0>--<472.0,541.0>> -> L<<472.0,541.0>--<473.0,541.0>>

	* fi (U+FB01): L<<472.0,541.0>--<473.0,541.0>> -> L<<473.0,541.0>--<529.0,541.0>>

	* petapp (U+E006): L<<284.0,304.0>--<314.0,286.0>> -> L<<314.0,286.0>--<341.0,271.0>>

	* petapp (U+E006): L<<314.0,333.0>--<275.0,356.0>> -> L<<275.0,356.0>--<259.0,365.0>>

	* petapp (U+E006): L<<357.0,309.0>--<314.0,333.0>> -> L<<314.0,333.0>--<275.0,356.0>>

	* petapp (U+E006): L<<373.0,299.0>--<357.0,309.0>> -> L<<357.0,309.0>--<314.0,333.0>>

	* petapp (U+E006): L<<373.0,640.0>--<469.0,585.0>> -> L<<469.0,585.0>--<517.0,556.0>>

	* petapp (U+E006): L<<375.0,298.0>--<373.0,299.0>> -> L<<373.0,299.0>--<357.0,309.0>>

	* petapp (U+E006): L<<428.0,268.0>--<375.0,298.0>> -> L<<375.0,298.0>--<373.0,299.0>>

	* petapp (U+E006): L<<469.0,585.0>--<517.0,556.0>> -> L<<517.0,556.0>--<536.0,545.0>>

	* petapp (U+E006): L<<470.0,243.0>--<428.0,268.0>> -> L<<428.0,268.0>--<375.0,298.0>>

	* petapp (U+E006): L<<476.0,240.0>--<470.0,243.0>> -> L<<470.0,243.0>--<428.0,268.0>>

	* petapp (U+E006): L<<500.0,226.0>--<476.0,240.0>> -> L<<476.0,240.0>--<470.0,243.0>>

	* petapp (U+E006): L<<507.0,222.0>--<500.0,226.0>> -> L<<500.0,226.0>--<476.0,240.0>>

	* petapp (U+E006): L<<598.0,453.0>--<598.0,455.0>> -> L<<598.0,455.0>--<598.0,456.0>>

	* petapp (U+E006): L<<598.0,455.0>--<598.0,454.0>> -> L<<598.0,454.0>--<598.0,453.0>>

	* petapp (U+E006): L<<693.0,61.0>--<694.0,60.0>> -> L<<694.0,60.0>--<698.0,56.0>>

	* petapp (U+E006): L<<722.0,485.0>--<727.0,485.0>> -> L<<727.0,485.0>--<766.0,485.0>>

	* petapp.minimal (U+E007): L<<266.0,373.0>--<353.0,339.0>> -> L<<353.0,339.0>--<434.0,305.0>>

	* petapp.minimal (U+E007): L<<353.0,339.0>--<434.0,305.0>> -> L<<434.0,305.0>--<450.0,299.0>>

	* petapp.minimal (U+E007): L<<383.0,352.0>--<333.0,376.0>> -> L<<333.0,376.0>--<307.0,390.0>>

	* petapp.minimal (U+E007): L<<434.0,305.0>--<450.0,299.0>> -> L<<450.0,299.0>--<506.0,276.0>>

	* petapp.minimal (U+E007): L<<434.0,326.0>--<383.0,352.0>> -> L<<383.0,352.0>--<333.0,376.0>>

	* petapp.minimal (U+E007): L<<437.0,187.0>--<407.0,192.0>> -> L<<407.0,192.0>--<306.0,211.0>>

	* petapp.minimal (U+E007): L<<450.0,299.0>--<506.0,276.0>> -> L<<506.0,276.0>--<614.0,232.0>>

	* petapp.minimal (U+E007): L<<457.0,314.0>--<434.0,326.0>> -> L<<434.0,326.0>--<383.0,352.0>>

	* petapp.minimal (U+E007): L<<506.0,175.0>--<437.0,187.0>> -> L<<437.0,187.0>--<407.0,192.0>>

	* petapp.minimal (U+E007): L<<506.0,276.0>--<614.0,232.0>> -> L<<614.0,232.0>--<623.0,229.0>>

	* petapp.minimal (U+E007): L<<506.0,289.0>--<457.0,314.0>> -> L<<457.0,314.0>--<434.0,326.0>>

	* petapp.minimal (U+E007): L<<590.0,160.0>--<506.0,175.0>> -> L<<506.0,175.0>--<437.0,187.0>>

	* petapp.minimal (U+E007): L<<623.0,229.0>--<506.0,289.0>> -> L<<506.0,289.0>--<457.0,314.0>>

	* petapp.minimal (U+E007): L<<744.0,30.0>--<744.0,31.0>> -> L<<744.0,31.0>--<744.0,32.0>>

	* petapp.minimal (U+E007): L<<744.0,31.0>--<744.0,32.0>> -> L<<744.0,32.0>--<744.0,33.0>>

	* petapp.minimal (U+E007): L<<744.0,32.0>--<744.0,33.0>> -> L<<744.0,33.0>--<744.0,34.0>>

	* petapp.minimal (U+E007): L<<744.0,33.0>--<744.0,34.0>> -> L<<744.0,34.0>--<744.0,36.0>>

	* petapp.minimal (U+E007): L<<744.0,34.0>--<744.0,36.0>> -> L<<744.0,36.0>--<744.0,37.0>>

	* petapp.minimal (U+E007): L<<744.0,37.0>--<744.0,30.0>> -> L<<744.0,30.0>--<744.0,22.0>>

	* petapp.minimal (U+E007): L<<744.0,38.0>--<744.0,37.0>> -> L<<744.0,37.0>--<744.0,30.0>>

	* petapp.minimal (U+E007): L<<749.0,73.0>--<748.0,63.0>> -> L<<748.0,63.0>--<744.0,38.0>>

	* petapp.minimal (U+E007): L<<749.0,74.0>--<749.0,73.0>> -> L<<749.0,73.0>--<748.0,63.0>>

	* petapp.minimal (U+E007): L<<754.0,131.0>--<749.0,74.0>> -> L<<749.0,74.0>--<749.0,73.0>>

	* petapp.minimal (U+E007): L<<756.0,162.0>--<754.0,131.0>> -> L<<754.0,131.0>--<749.0,74.0>>

	* petapp.minimal (U+E007): L<<757.0,175.0>--<756.0,162.0>> -> L<<756.0,162.0>--<754.0,131.0>>

	* petapp.minimal (U+E007): L<<759.0,196.0>--<757.0,175.0>> -> L<<757.0,175.0>--<756.0,162.0>>

	* petapp.minimal (U+E007): L<<760.0,210.0>--<759.0,196.0>> -> L<<759.0,196.0>--<757.0,175.0>>

	* petapp.minimal (U+E007): L<<760.0,213.0>--<760.0,210.0>> -> L<<760.0,210.0>--<759.0,196.0>>

	* petapp.wpda (U+E008): L<<641.0,140.0>--<628.0,132.0>> -> L<<628.0,132.0>--<619.0,127.0>>

	* piads (U+E001): L<<114.0,541.0>--<118.0,544.0>> -> L<<118.0,544.0>--<447.0,782.0>>

	* piads (U+E001): L<<548.0,782.0>--<876.0,544.0>> -> L<<876.0,544.0>--<880.0,541.0>>

	* picall (U+E009): L<<114.0,541.0>--<118.0,544.0>> -> L<<118.0,544.0>--<447.0,782.0>>

	* picall (U+E009): L<<548.0,782.0>--<876.0,544.0>> -> L<<876.0,544.0>--<880.0,541.0>>

	* pioffice (U+E002): L<<548.0,782.0>--<876.0,544.0>> -> L<<876.0,544.0>--<879.0,542.0>>

	* pisafe (U+E010): L<<169.0,362.0>--<169.0,491.0>> -> L<<169.0,491.0>--<169.0,494.0>>

	* pisafe (U+E010): L<<205.0,695.0>--<241.0,708.0>> -> L<<241.0,708.0>--<391.0,762.0>>

	* pisafe (U+E010): L<<241.0,708.0>--<391.0,762.0>> -> L<<391.0,762.0>--<496.0,800.0>>

	* pisafe (U+E010): L<<497.0,800.0>--<602.0,762.0>> -> L<<602.0,762.0>--<752.0,708.0>>

	* pisafe (U+E010): L<<602.0,762.0>--<752.0,708.0>> -> L<<752.0,708.0>--<788.0,695.0>>

	* pisign (U+E005): L<<548.0,782.0>--<876.0,544.0>> -> L<<876.0,544.0>--<879.0,542.0>>

	* pitagon (U+E000): L<<114.0,543.0>--<118.0,546.0>> -> L<<118.0,546.0>--<447.0,784.0>>

	* pitagon (U+E000): L<<211.0,62.0>--<86.0,446.0>> -> L<<86.0,446.0>--<84.0,452.0>>

	* pitagon (U+E000): L<<549.0,784.0>--<876.0,546.0>> -> L<<876.0,546.0>--<880.0,543.0>>

	* pitagram (U+E003): L<<815.0,512.0>--<812.0,514.0>> -> L<<812.0,514.0>--<539.0,711.0>>

	* piweb (U+E004): L<<815.0,512.0>--<812.0,514.0>> -> L<<812.0,514.0>--<539.0,711.0>>

	* sparks (U+E011): L<<102.0,798.0>--<105.0,797.0>> -> L<<105.0,797.0>--<200.0,762.0>>

	* sparks (U+E011): L<<105.0,797.0>--<200.0,762.0>> -> L<<200.0,762.0>--<211.0,759.0>>

	* sparks (U+E011): L<<200.0,762.0>--<211.0,759.0>> -> L<<211.0,759.0>--<402.0,690.0>>

	* sparks (U+E011): L<<211.0,759.0>--<402.0,690.0>> -> L<<402.0,690.0>--<433.0,680.0>>

	* sparks (U+E011): L<<293.0,596.0>--<365.0,534.0>> -> L<<365.0,534.0>--<384.0,516.0>>

	* sparks (U+E011): L<<383.0,366.0>--<385.0,367.0>> -> L<<385.0,367.0>--<488.0,429.0>>

	* sparks (U+E011): L<<385.0,367.0>--<488.0,429.0>> -> L<<488.0,429.0>--<490.0,430.0>>

	* sparks (U+E011): L<<411.0,102.0>--<100.0,641.0>> -> L<<100.0,641.0>--<49.0,731.0>>

	* sparks (U+E011): L<<442.0,659.0>--<438.0,649.0>> -> L<<438.0,649.0>--<436.0,643.0>>

	* sparks (U+E011): L<<456.0,24.0>--<411.0,102.0>> -> L<<411.0,102.0>--<100.0,641.0>>

	* sparks (U+E011): L<<506.0,429.0>--<608.0,367.0>> -> L<<608.0,367.0>--<610.0,366.0>>

	* sparks (U+E011): L<<560.0,680.0>--<598.0,694.0>> -> L<<598.0,694.0>--<782.0,759.0>>

	* sparks (U+E011): L<<581.0,101.0>--<552.0,51.0>> -> L<<552.0,51.0>--<537.0,24.0>>

	* sparks (U+E011): L<<598.0,694.0>--<782.0,759.0>> -> L<<782.0,759.0>--<809.0,768.0>>

	* sparks (U+E011): L<<609.0,516.0>--<629.0,534.0>> -> L<<629.0,534.0>--<701.0,596.0>>

	* sparks (U+E011): L<<616.0,629.0>--<579.0,632.0>> -> L<<579.0,632.0>--<570.0,633.0>>

	* sparks (U+E011): L<<657.0,626.0>--<616.0,629.0>> -> L<<616.0,629.0>--<579.0,632.0>>

	* sparks (U+E011): L<<658.0,626.0>--<657.0,626.0>> -> L<<657.0,626.0>--<616.0,629.0>>

	* sparks (U+E011): L<<692.0,623.0>--<658.0,626.0>> -> L<<658.0,626.0>--<657.0,626.0>>

	* sparks (U+E011): L<<693.0,623.0>--<692.0,623.0>> -> L<<692.0,623.0>--<658.0,626.0>>

	* sparks (U+E011): L<<752.0,397.0>--<581.0,101.0>> -> L<<581.0,101.0>--<552.0,51.0>>

	* sparks (U+E011): L<<782.0,759.0>--<809.0,768.0>> -> L<<809.0,768.0>--<888.0,797.0>>

	* sparks (U+E011): L<<899.0,652.0>--<752.0,397.0>> -> L<<752.0,397.0>--<581.0,101.0>>

	* sparks (U+E011): L<<944.0,730.0>--<899.0,652.0>> -> L<<899.0,652.0>--<752.0,397.0>> 

	* sparks (U+E011): L<<945.0,732.0>--<944.0,730.0>> -> L<<944.0,730.0>--<899.0,652.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* petapp (U+E006): B<<296.0,462.0>-<297.0,460.0>-<298.0,459.0>>/L<<298.0,459.0>--<296.0,462.0>> = 11.309932474020227

	* petapp (U+E006): B<<296.5,293.0>-<290.0,300.0>-<284.0,304.0>>/L<<284.0,304.0>--<314.0,286.0>> = 2.7263109939060786

	* petapp (U+E006): B<<402.0,89.0>-<404.0,88.0>-<406.0,86.0>>/L<<406.0,86.0>--<402.0,89.0>> = 8.13010235415596

	* petapp (U+E006): B<<421.0,74.0>-<422.0,73.0>-<424.0,72.0>>/L<<424.0,72.0>--<421.0,74.0>> = 7.125016348901757

	* petapp (U+E006): B<<515.0,65.0>-<516.0,65.0>-<518.0,66.0>>/L<<518.0,66.0>--<515.0,65.0>> = 8.130102354155916

	* petapp (U+E006): B<<516.0,78.0>-<517.0,79.0>-<519.0,80.0>>/L<<519.0,80.0>--<516.0,78.0>> = 7.125016348901757

	* petapp (U+E006): B<<521.0,66.0>-<522.0,66.0>-<524.0,67.0>>/L<<524.0,67.0>--<521.0,66.0>> = 8.130102354155916

	* petapp (U+E006): B<<542.0,183.0>-<542.0,184.0>-<541.0,186.0>>/L<<541.0,186.0>--<542.0,183.0>> = 8.13010235415587

	* petapp (U+E006): B<<547.0,123.0>-<547.0,125.0>-<548.0,127.0>>/L<<548.0,127.0>--<547.0,123.0>> = 12.528807709151492

	* petapp (U+E006): B<<550.0,142.0>-<551.0,144.0>-<551.0,147.0>>/L<<551.0,147.0>--<550.0,142.0>> = 11.309932474020227

	* petapp (U+E006): B<<577.0,404.0>-<577.0,403.0>-<579.0,401.0>>/L<<579.0,401.0>--<577.0,404.0>> = 11.309932474020227

	* petapp (U+E006): B<<589.0,380.0>-<588.0,382.0>-<588.0,384.0>>/L<<588.0,384.0>--<589.0,380.0>> = 14.036243467926484

	* petapp (U+E006): B<<598.0,450.0>-<599.0,448.0>-<599.0,446.0>>/L<<599.0,446.0>--<598.0,450.0>> = 14.036243467926484

	* petapp (U+E006): B<<616.0,384.0>-<617.0,382.0>-<618.0,379.0>>/L<<618.0,379.0>--<616.0,384.0>> = 3.366460663429615

	* petapp (U+E006): B<<618.0,367.0>-<618.0,366.0>-<619.0,364.0>>/L<<619.0,364.0>--<618.0,367.0>> = 8.130102354155916

	* petapp (U+E006): B<<620.0,362.0>-<620.0,361.0>-<621.0,359.0>>/L<<621.0,359.0>--<620.0,362.0>> = 8.130102354155916

	* petapp (U+E006): B<<622.0,357.0>-<622.0,356.0>-<623.0,354.0>>/L<<623.0,354.0>--<622.0,357.0>> = 8.130102354155916

	* petapp (U+E006): B<<624.0,368.0>-<625.0,367.0>-<626.0,365.0>>/L<<626.0,365.0>--<624.0,368.0>> = 7.125016348901705

	* petapp (U+E006): B<<629.0,343.0>-<629.0,342.0>-<630.0,340.0>>/L<<630.0,340.0>--<629.0,343.0>> = 8.130102354155916

	* petapp (U+E006): B<<634.0,334.0>-<635.0,333.0>-<636.0,331.0>>/L<<636.0,331.0>--<634.0,334.0>> = 7.125016348901705

	* petapp (U+E006): B<<640.0,346.0>-<640.0,345.0>-<641.0,343.0>>/L<<641.0,343.0>--<640.0,346.0>> = 8.130102354155916

	* petapp (U+E006): B<<643.0,321.0>-<644.0,320.0>-<645.0,318.0>>/L<<645.0,318.0>--<643.0,321.0>> = 7.125016348901705

	* petapp (U+E006): B<<661.0,441.0>-<661.0,440.0>-<660.0,438.0>>/L<<660.0,438.0>--<661.0,441.0>> = 8.13010235415587

	* petapp (U+E006): B<<671.0,316.0>-<672.0,315.0>-<673.0,314.0>>/L<<673.0,314.0>--<670.0,316.0>> = 11.309932474020195

	* petapp (U+E006): B<<672.0,137.0>-<673.0,138.0>-<674.0,140.0>>/L<<674.0,140.0>--<672.0,137.0>> = 7.125016348901705

	* petapp (U+E006): B<<679.0,310.0>-<681.0,309.0>-<682.0,308.0>>/L<<682.0,308.0>--<679.0,310.0>> = 11.309932474020195

	* petapp (U+E006): B<<681.0,141.0>-<682.0,142.0>-<684.0,143.0>>/L<<684.0,143.0>--<681.0,141.0>> = 7.125016348901757

	* petapp (U+E006): B<<685.0,267.0>-<684.0,269.0>-<683.0,270.0>>/L<<683.0,270.0>--<685.0,267.0>> = 11.309932474020195

	* petapp (U+E006): B<<697.0,299.0>-<699.0,298.0>-<700.0,297.0>>/L<<700.0,297.0>--<697.0,299.0>> = 11.309932474020195

	* petapp (U+E006): B<<702.0,53.0>-<701.0,54.0>-<699.0,55.0>>/L<<699.0,55.0>--<702.0,53.0>> = 7.125016348901757

	* petapp (U+E006): B<<767.0,0.0>-<766.0,2.0>-<765.0,3.0>>/L<<765.0,3.0>--<767.0,0.0>> = 11.309932474020195

	* petapp (U+E006): L<<277.0,506.0>--<276.0,509.0>>/B<<276.0,509.0>-<277.0,507.0>-<277.0,506.0>> = 8.130102354155916

	* petapp (U+E006): L<<292.0,468.0>--<291.0,471.0>>/B<<291.0,471.0>-<292.0,469.0>-<292.0,468.0>> = 8.130102354155916

	* petapp (U+E006): L<<298.0,459.0>--<296.0,462.0>>/B<<296.0,462.0>-<297.0,460.0>-<298.0,459.0>> = 7.125016348901705

	* petapp (U+E006): L<<314.0,442.0>--<310.0,445.0>>/B<<310.0,445.0>-<312.0,444.0>-<313.0,442.0>> = 10.304846468766009

	* petapp (U+E006): L<<383.0,123.0>--<382.0,126.0>>/B<<382.0,126.0>-<383.0,124.0>-<383.0,123.0>> = 8.130102354155916

	* petapp (U+E006): L<<406.0,86.0>--<402.0,89.0>>/B<<402.0,89.0>-<404.0,88.0>-<406.0,86.0>> = 10.304846468766009

	* petapp (U+E006): L<<424.0,72.0>--<421.0,74.0>>/B<<421.0,74.0>-<422.0,73.0>-<424.0,72.0>> = 11.309932474020195

	* petapp (U+E006): L<<438.0,66.0>--<435.0,67.0>>/B<<435.0,67.0>-<437.0,66.0>-<438.0,66.0>> = 8.130102354155916

	* petapp (U+E006): L<<501.0,225.0>--<507.0,222.0>>/L<<507.0,222.0>--<500.0,226.0>> = 3.1798301198640497

	* petapp (U+E006): L<<505.0,71.0>--<501.0,69.0>>/B<<501.0,69.0>-<504.0,71.0>-<505.0,71.0>> = 7.125016348901757

	* petapp (U+E006): L<<519.0,80.0>--<516.0,78.0>>/B<<516.0,78.0>-<517.0,79.0>-<519.0,80.0>> = 11.309932474020195

	* petapp (U+E006): L<<523.0,84.0>--<520.0,82.0>>/B<<520.0,82.0>-<521.0,83.0>-<523.0,84.0>> = 11.309932474020195

	* petapp (U+E006): L<<533.0,68.0>--<538.0,69.0>>/B<<538.0,69.0>-<535.0,69.0>-<533.0,68.0>> = 11.309932474020195

	* petapp (U+E006): L<<542.0,70.0>--<546.0,71.0>>/B<<546.0,71.0>-<541.0,70.0>-<542.0,70.0>> = 2.726310993906212

	* petapp (U+E006): L<<548.0,127.0>--<547.0,123.0>>/B<<547.0,123.0>-<547.0,125.0>-<548.0,127.0>> = 14.036243467926484

	* petapp (U+E006): L<<548.0,166.0>--<549.0,163.0>>/B<<549.0,163.0>-<548.0,165.0>-<548.0,166.0>> = 8.13010235415587

	* petapp (U+E006): L<<585.0,256.0>--<586.0,252.0>>/B<<586.0,252.0>-<585.0,254.0>-<585.0,256.0>> = 12.528807709151492

	* petapp (U+E006): L<<588.0,384.0>--<589.0,380.0>>/B<<589.0,380.0>-<588.0,382.0>-<588.0,384.0>> = 12.528807709151492

	* petapp (U+E006): L<<592.0,235.0>--<593.0,232.0>>/B<<593.0,232.0>-<592.0,234.0>-<592.0,235.0>> = 8.13010235415587

	* petapp (U+E006): L<<596.0,353.0>--<597.0,350.0>>/B<<597.0,350.0>-<596.0,352.0>-<596.0,353.0>> = 8.13010235415587

	* petapp (U+E006): L<<599.0,438.0>--<600.0,435.0>>/B<<600.0,435.0>-<599.0,437.0>-<599.0,438.0>> = 8.13010235415587

	* petapp (U+E006): L<<599.0,446.0>--<598.0,450.0>>/B<<598.0,450.0>-<599.0,448.0>-<599.0,446.0>> = 12.528807709151492

	* petapp (U+E006): L<<599.0,447.0>--<598.0,450.0>>/B<<598.0,450.0>-<599.0,448.0>-<599.0,447.0>> = 8.130102354155916

	* petapp (U+E006): L<<601.0,431.0>--<600.0,434.0>>/B<<600.0,434.0>-<601.0,432.0>-<601.0,431.0>> = 8.130102354155916

	* petapp (U+E006): L<<602.0,426.0>--<601.0,429.0>>/B<<601.0,429.0>-<602.0,427.0>-<602.0,426.0>> = 8.130102354155916

	* petapp (U+E006): L<<612.0,96.0>--<613.0,96.0>>/B<<613.0,96.0>-<609.0,95.0>-<605.0,92.5>> = 14.036243467926484

	* petapp (U+E006): L<<613.0,379.0>--<612.0,384.0>>/B<<612.0,384.0>-<612.0,381.0>-<613.0,379.0>> = 11.309932474020227

	* petapp (U+E006): L<<618.0,379.0>--<616.0,384.0>>/B<<616.0,384.0>-<617.0,382.0>-<618.0,379.0>> = 4.763641690726066

	* petapp (U+E006): L<<626.0,365.0>--<624.0,368.0>>/B<<624.0,368.0>-<625.0,367.0>-<626.0,365.0>> = 11.309932474020227

	* petapp (U+E006): L<<636.0,331.0>--<634.0,334.0>>/B<<634.0,334.0>-<635.0,333.0>-<636.0,331.0>> = 11.309932474020227

	* petapp (U+E006): L<<645.0,318.0>--<643.0,321.0>>/B<<643.0,321.0>-<644.0,320.0>-<645.0,318.0>> = 11.309932474020227

	* petapp (U+E006): L<<658.0,398.0>--<657.0,401.0>>/B<<657.0,401.0>-<658.0,399.0>-<658.0,398.0>> = 8.130102354155916

	* petapp (U+E006): L<<674.0,140.0>--<672.0,137.0>>/B<<672.0,137.0>-<673.0,138.0>-<674.0,140.0>> = 11.309932474020227

	* petapp (U+E006): L<<675.0,137.0>--<679.0,140.0>>/B<<679.0,140.0>-<674.0,137.0>-<675.0,137.0>> = 5.906141113770497

	* petapp (U+E006): L<<677.0,89.0>--<676.0,92.0>>/B<<676.0,92.0>-<677.0,90.0>-<677.0,89.0>> = 8.130102354155916

	* petapp (U+E006): L<<682.0,308.0>--<679.0,310.0>>/B<<679.0,310.0>-<681.0,309.0>-<682.0,308.0>> = 7.125016348901757

	* petapp (U+E006): L<<683.0,270.0>--<685.0,267.0>>/B<<685.0,267.0>-<684.0,269.0>-<683.0,270.0>> = 7.125016348901757

	* petapp (U+E006): L<<684.0,143.0>--<681.0,141.0>>/B<<681.0,141.0>-<682.0,142.0>-<684.0,143.0>> = 11.309932474020195

	* petapp (U+E006): L<<691.0,475.0>--<694.0,476.0>>/B<<694.0,476.0>-<692.0,475.0>-<691.0,475.0>> = 8.13010235415587

	* petapp (U+E006): L<<692.0,172.0>--<691.0,169.0>>/B<<691.0,169.0>-<692.0,171.0>-<692.5,172.0>> = 8.130102354155916

	* petapp (U+E006): L<<694.0,246.0>--<695.0,243.0>>/B<<695.0,243.0>-<694.0,245.0>-<694.0,246.0>> = 8.13010235415587

	* petapp (U+E006): L<<697.0,235.0>--<698.0,232.0>>/B<<698.0,232.0>-<697.0,234.0>-<697.0,235.0>> = 8.13010235415587

	* petapp (U+E006): L<<699.0,55.0>--<702.0,53.0>>/B<<702.0,53.0>-<701.0,54.0>-<699.0,55.0>> = 11.309932474020227

	* petapp (U+E006): L<<700.0,297.0>--<697.0,299.0>>/B<<697.0,299.0>-<699.0,298.0>-<700.0,297.0>> = 7.125016348901757

	* petapp (U+E006): L<<763.0,8.0>--<764.0,5.0>>/B<<764.0,5.0>-<763.0,7.0>-<763.0,8.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<583.0,372.0>-<587.0,368.0>-<590.0,366.0>>/L<<590.0,366.0>--<583.0,372.0>> = 6.911227119024609

	* petapp.minimal (U+E007): B<<642.0,408.0>-<642.0,407.0>-<643.0,405.0>>/L<<643.0,405.0>--<642.0,408.0>> = 8.130102354155916

	* petapp.minimal (U+E007): B<<642.0,501.0>-<641.0,499.0>-<640.0,498.0>>/L<<640.0,498.0>--<642.0,501.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<713.0,229.0>-<712.0,231.0>-<711.0,232.0>>/L<<711.0,232.0>--<713.0,229.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<716.0,147.0>-<715.0,148.0>-<714.0,150.0>>/L<<714.0,150.0>--<716.0,147.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<721.0,137.0>-<721.0,139.0>-<720.0,140.0>>/L<<720.0,140.0>--<722.0,137.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<731.0,115.0>-<731.0,116.0>-<730.0,118.0>>/L<<730.0,118.0>--<731.0,115.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<731.0,191.0>-<731.0,192.0>-<730.0,194.0>>/L<<730.0,194.0>--<731.0,191.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<739.0,90.0>-<739.0,91.0>-<738.0,93.0>>/L<<738.0,93.0>--<739.0,90.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<742.0,10.5>-<741.0,5.0>-<740.0,0.0>>/B<<740.0,0.0>-<740.0,4.0>-<739.5,8.5>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<743.0,69.0>-<743.0,70.0>-<742.0,72.0>>/L<<742.0,72.0>--<743.0,69.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<745.0,46.0>-<744.0,48.0>-<744.0,50.0>>/L<<744.0,50.0>--<745.0,46.0>> = 14.036243467926484

	* petapp.minimal (U+E007): L<<214.0,538.0>--<214.0,800.0>>/B<<214.0,800.0>-<215.0,769.0>-<227.5,742.0>> = 1.8476102659945155

	* petapp.minimal (U+E007): L<<633.0,225.0>--<629.0,226.0>>/B<<629.0,226.0>-<631.0,225.0>-<633.0,225.0>> = 12.528807709151463

	* petapp.minimal (U+E007): L<<633.0,225.0>--<633.0,225.0>>/L<<633.0,225.0>--<629.0,226.0>> = 14.036243467926484

	* petapp.minimal (U+E007): L<<636.0,420.0>--<635.0,423.0>>/B<<635.0,423.0>-<636.0,421.0>-<636.0,420.0>> = 8.130102354155916

	* petapp.minimal (U+E007): L<<638.0,415.0>--<637.0,418.0>>/B<<637.0,418.0>-<638.0,416.0>-<638.0,415.0>> = 8.130102354155916

	* petapp.minimal (U+E007): L<<640.0,410.0>--<639.0,413.0>>/B<<639.0,413.0>-<640.0,411.0>-<640.0,410.0>> = 8.130102354155916

	* petapp.minimal (U+E007): L<<640.0,498.0>--<642.0,501.0>>/B<<642.0,501.0>-<641.0,499.0>-<640.0,498.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<643.0,219.0>--<646.0,218.0>>/B<<646.0,218.0>-<644.0,219.0>-<643.0,219.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<646.0,507.0>--<647.0,510.0>>/B<<647.0,510.0>-<646.0,508.0>-<646.0,507.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<689.0,544.0>--<692.0,545.0>>/B<<692.0,545.0>-<690.0,544.0>-<689.0,544.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<704.0,550.0>--<707.0,551.0>>/B<<707.0,551.0>-<705.0,550.0>-<704.0,550.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<711.0,232.0>--<713.0,229.0>>/B<<713.0,229.0>-<712.0,231.0>-<711.0,232.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<714.0,150.0>--<716.0,147.0>>/B<<716.0,147.0>-<715.0,148.0>-<714.0,150.0>> = 11.309932474020195

	* petapp.minimal (U+E007): L<<734.0,108.0>--<735.0,105.0>>/B<<735.0,105.0>-<734.0,107.0>-<734.0,108.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<737.0,98.0>--<738.0,95.0>>/B<<738.0,95.0>-<737.0,97.0>-<737.0,98.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<739.0,166.0>--<740.0,163.0>>/B<<740.0,163.0>-<739.0,165.0>-<738.5,166.5>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<741.0,156.0>--<740.0,160.0>>/B<<740.0,160.0>-<742.0,153.0>-<741.0,156.0>> = 1.9091524329963898

	* petapp.minimal (U+E007): L<<744.0,50.0>--<745.0,46.0>>/B<<745.0,46.0>-<744.0,48.0>-<744.0,50.0>> = 12.528807709151492

	* petapp.minimal (U+E007): L<<749.0,97.0>--<750.0,92.0>>/B<<750.0,92.0>-<750.0,95.0>-<749.0,97.0>> = 11.309932474020195

	* petapp.wpda (U+E008): B<<486.0,2.0>-<483.0,5.0>-<483.0,6.0>>/L<<483.0,6.0>--<482.0,1.0>> = 11.309932474020227

	* petapp.wpda (U+E008): L<<186.0,222.0>--<181.0,218.0>>/B<<181.0,218.0>-<183.0,219.0>-<184.0,218.0>> = 12.094757077012058

	* pisafe (U+E010): B<<170.0,511.0>-<170.0,510.0>-<169.0,508.0>>/L<<169.0,508.0>--<170.0,511.0>> = 8.13010235415587

	* pisafe (U+E010): B<<177.0,538.0>-<176.0,536.0>-<176.0,534.0>>/L<<176.0,534.0>--<177.0,538.0>> = 14.036243467926484

	* pisafe (U+E010): B<<191.0,573.0>-<191.0,572.0>-<190.0,570.0>>/L<<190.0,570.0>--<191.0,573.0>> = 8.13010235415587

	* pisafe (U+E010): B<<213.0,602.0>-<211.0,600.0>-<210.0,598.0>>/L<<210.0,598.0>--<213.0,602.0>> = 10.304846468766044

	* pisafe (U+E010): B<<786.0,594.0>-<785.0,596.0>-<784.0,597.0>>/L<<784.0,597.0>--<786.0,594.0>> = 11.309932474020195

	* pisafe (U+E010): B<<803.0,568.0>-<803.0,569.0>-<802.0,571.0>>/L<<802.0,571.0>--<803.0,568.0>> = 8.13010235415587

	* pisafe (U+E010): B<<818.0,530.0>-<817.0,532.0>-<817.0,534.0>>/L<<817.0,534.0>--<818.0,530.0>> = 14.036243467926484

	* pisafe (U+E010): L<<176.0,534.0>--<177.0,538.0>>/B<<177.0,538.0>-<176.0,536.0>-<176.0,534.0>> = 12.528807709151492

	* pisafe (U+E010): L<<181.0,551.0>--<182.0,554.0>>/B<<182.0,554.0>-<181.0,552.0>-<181.0,551.0>> = 8.13010235415587

	* pisafe (U+E010): L<<210.0,598.0>--<213.0,602.0>>/B<<213.0,602.0>-<211.0,600.0>-<210.0,598.0>> = 8.13010235415596

	* pisafe (U+E010): L<<752.0,626.0>--<756.0,623.0>>/B<<756.0,623.0>-<754.0,624.0>-<752.0,626.0>> = 10.304846468766009

	* pisafe (U+E010): L<<784.0,597.0>--<786.0,594.0>>/B<<786.0,594.0>-<785.0,596.0>-<784.0,597.0>> = 7.125016348901757

	* pisafe (U+E010): L<<797.0,580.0>--<798.0,577.0>>/B<<798.0,577.0>-<797.0,579.0>-<797.0,580.0>> = 8.13010235415587

	* pisafe (U+E010): L<<805.0,566.0>--<806.0,563.0>>/B<<806.0,563.0>-<805.0,565.0>-<805.0,566.0>> = 8.13010235415587 

	* pisafe (U+E010): L<<817.0,534.0>--<818.0,530.0>>/B<<818.0,530.0>-<817.0,532.0>-<817.0,534.0>> = 12.528807709151492 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[19] PitagonSansText-SemiBoldItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check OFL body text is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text">com.google.fonts/check/license/OFL_body_text</a>)</summary><div>


* 🔥 **FAIL** The OFL.txt body text is incorrect. Please use https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt as a template. You should only modify the first line. [code: incorrect-ofl-body-text]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ
at: https://scripts.sil.org/OFL." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks">com.google.fonts/check/name/line_breaks</a>)</summary><div>


* 🔥 **FAIL** Name entry DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1294, but got 1214 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.11, while a newer 0.8.13 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'Pita' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
</div></details><details><summary>⚠ <b>WARN:</b> Description strings in the name table must not exceed 200 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/description_max_length">com.google.fonts/check/name/description_max_length</a>)</summary><div>


* ⚠ **WARN** A few name table entries with ID=10 (NameID.DESCRIPTION) are longer than 200 characters. Please check whether those entries are copyright notices mistakenly stored in the description string entries by a bug in an old FontLab version. If that's the case, then such copyright notices must be removed from these entries. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Pitagon Sans Text SemiBold' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- periodcentered.001 

	- registered.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni0200	Contours detected: 3	Expected: 4

	- Glyph name: uni0201	Contours detected: 3	Expected: 4

	- Glyph name: uni0204	Contours detected: 2	Expected: 3

	- Glyph name: uni0205	Contours detected: 3	Expected: 4

	- Glyph name: uni0208	Contours detected: 2	Expected: 3

	- Glyph name: uni0209	Contours detected: 2	Expected: 3

	- Glyph name: uni020C	Contours detected: 3	Expected: 4

	- Glyph name: uni020D	Contours detected: 3	Expected: 4

	- Glyph name: uni0210	Contours detected: 3	Expected: 4

	- Glyph name: uni0211	Contours detected: 2	Expected: 3

	- Glyph name: uni0214	Contours detected: 2	Expected: 3

	- Glyph name: uni0215	Contours detected: 2	Expected: 3

	- Glyph name: uni030F	Contours detected: 1	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni030F	Contours detected: 1	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* fi (U+FB01): L<<277.0,541.0>--<507.0,541.0>> -> L<<507.0,541.0>--<508.0,541.0>>

	* fi (U+FB01): L<<507.0,541.0>--<508.0,541.0>> -> L<<508.0,541.0>--<509.0,541.0>>

	* fi (U+FB01): L<<508.0,541.0>--<509.0,541.0>> -> L<<509.0,541.0>--<567.0,541.0>>

	* petapp (U+E006): L<<282.0,304.0>--<312.0,286.0>> -> L<<312.0,286.0>--<339.0,271.0>>

	* petapp (U+E006): L<<312.0,333.0>--<273.0,356.0>> -> L<<273.0,356.0>--<257.0,365.0>>

	* petapp (U+E006): L<<355.0,309.0>--<312.0,333.0>> -> L<<312.0,333.0>--<273.0,356.0>>

	* petapp (U+E006): L<<371.0,299.0>--<355.0,309.0>> -> L<<355.0,309.0>--<312.0,333.0>>

	* petapp (U+E006): L<<371.0,640.0>--<467.0,585.0>> -> L<<467.0,585.0>--<515.0,556.0>>

	* petapp (U+E006): L<<373.0,298.0>--<371.0,299.0>> -> L<<371.0,299.0>--<355.0,309.0>>

	* petapp (U+E006): L<<426.0,268.0>--<373.0,298.0>> -> L<<373.0,298.0>--<371.0,299.0>>

	* petapp (U+E006): L<<467.0,585.0>--<515.0,556.0>> -> L<<515.0,556.0>--<534.0,545.0>>

	* petapp (U+E006): L<<468.0,243.0>--<426.0,268.0>> -> L<<426.0,268.0>--<373.0,298.0>>

	* petapp (U+E006): L<<474.0,240.0>--<468.0,243.0>> -> L<<468.0,243.0>--<426.0,268.0>>

	* petapp (U+E006): L<<498.0,226.0>--<474.0,240.0>> -> L<<474.0,240.0>--<468.0,243.0>>

	* petapp (U+E006): L<<505.0,222.0>--<498.0,226.0>> -> L<<498.0,226.0>--<474.0,240.0>>

	* petapp (U+E006): L<<691.0,61.0>--<692.0,60.0>> -> L<<692.0,60.0>--<696.0,56.0>>

	* petapp (U+E006): L<<721.0,485.0>--<725.0,485.0>> -> L<<725.0,485.0>--<764.0,485.0>>

	* petapp.minimal (U+E007): L<<264.0,373.0>--<351.0,339.0>> -> L<<351.0,339.0>--<432.0,305.0>>

	* petapp.minimal (U+E007): L<<351.0,339.0>--<432.0,305.0>> -> L<<432.0,305.0>--<448.0,299.0>>

	* petapp.minimal (U+E007): L<<381.0,352.0>--<331.0,376.0>> -> L<<331.0,376.0>--<305.0,390.0>>

	* petapp.minimal (U+E007): L<<432.0,305.0>--<448.0,299.0>> -> L<<448.0,299.0>--<504.0,276.0>>

	* petapp.minimal (U+E007): L<<432.0,326.0>--<381.0,352.0>> -> L<<381.0,352.0>--<331.0,376.0>>

	* petapp.minimal (U+E007): L<<435.0,187.0>--<405.0,192.0>> -> L<<405.0,192.0>--<304.0,211.0>>

	* petapp.minimal (U+E007): L<<448.0,299.0>--<504.0,276.0>> -> L<<504.0,276.0>--<612.0,232.0>>

	* petapp.minimal (U+E007): L<<455.0,314.0>--<432.0,326.0>> -> L<<432.0,326.0>--<381.0,352.0>>

	* petapp.minimal (U+E007): L<<504.0,175.0>--<435.0,187.0>> -> L<<435.0,187.0>--<405.0,192.0>>

	* petapp.minimal (U+E007): L<<504.0,276.0>--<612.0,232.0>> -> L<<612.0,232.0>--<621.0,229.0>>

	* petapp.minimal (U+E007): L<<504.0,289.0>--<455.0,314.0>> -> L<<455.0,314.0>--<432.0,326.0>>

	* petapp.minimal (U+E007): L<<588.0,160.0>--<504.0,175.0>> -> L<<504.0,175.0>--<435.0,187.0>>

	* petapp.minimal (U+E007): L<<621.0,229.0>--<504.0,289.0>> -> L<<504.0,289.0>--<455.0,314.0>>

	* petapp.minimal (U+E007): L<<742.0,30.0>--<742.0,31.0>> -> L<<742.0,31.0>--<742.0,32.0>>

	* petapp.minimal (U+E007): L<<743.0,33.0>--<743.0,34.0>> -> L<<743.0,34.0>--<743.0,36.0>>

	* petapp.minimal (U+E007): L<<743.0,34.0>--<743.0,36.0>> -> L<<743.0,36.0>--<743.0,37.0>>

	* petapp.minimal (U+E007): L<<747.0,73.0>--<746.0,63.0>> -> L<<746.0,63.0>--<743.0,38.0>>

	* petapp.minimal (U+E007): L<<747.0,74.0>--<747.0,73.0>> -> L<<747.0,73.0>--<746.0,63.0>>

	* petapp.minimal (U+E007): L<<752.0,131.0>--<747.0,74.0>> -> L<<747.0,74.0>--<747.0,73.0>>

	* petapp.minimal (U+E007): L<<754.0,162.0>--<752.0,131.0>> -> L<<752.0,131.0>--<747.0,74.0>>

	* petapp.minimal (U+E007): L<<755.0,175.0>--<754.0,162.0>> -> L<<754.0,162.0>--<752.0,131.0>>

	* petapp.minimal (U+E007): L<<757.0,196.0>--<755.0,175.0>> -> L<<755.0,175.0>--<754.0,162.0>>

	* petapp.minimal (U+E007): L<<758.0,210.0>--<757.0,196.0>> -> L<<757.0,196.0>--<755.0,175.0>>

	* petapp.minimal (U+E007): L<<758.0,213.0>--<758.0,210.0>> -> L<<758.0,210.0>--<757.0,196.0>>

	* petapp.wpda (U+E008): L<<640.0,140.0>--<627.0,132.0>> -> L<<627.0,132.0>--<618.0,127.0>>

	* piads (U+E001): L<<112.0,541.0>--<116.0,544.0>> -> L<<116.0,544.0>--<445.0,782.0>>

	* piads (U+E001): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<878.0,541.0>>

	* picall (U+E009): L<<112.0,541.0>--<116.0,544.0>> -> L<<116.0,544.0>--<445.0,782.0>>

	* picall (U+E009): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<878.0,541.0>>

	* pioffice (U+E002): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<877.0,542.0>>

	* pisafe (U+E010): L<<167.0,362.0>--<167.0,491.0>> -> L<<167.0,491.0>--<167.0,494.0>>

	* pisafe (U+E010): L<<203.0,695.0>--<239.0,708.0>> -> L<<239.0,708.0>--<389.0,762.0>>

	* pisafe (U+E010): L<<239.0,708.0>--<389.0,762.0>> -> L<<389.0,762.0>--<494.0,800.0>>

	* pisafe (U+E010): L<<495.0,800.0>--<600.0,762.0>> -> L<<600.0,762.0>--<750.0,708.0>>

	* pisafe (U+E010): L<<600.0,762.0>--<750.0,708.0>> -> L<<750.0,708.0>--<786.0,695.0>>

	* pisign (U+E005): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<877.0,542.0>>

	* pitagon (U+E000): L<<112.0,543.0>--<116.0,546.0>> -> L<<116.0,546.0>--<445.0,784.0>>

	* pitagon (U+E000): L<<209.0,62.0>--<84.0,446.0>> -> L<<84.0,446.0>--<82.0,452.0>>

	* pitagon (U+E000): L<<547.0,784.0>--<874.0,546.0>> -> L<<874.0,546.0>--<878.0,543.0>>

	* pitagram (U+E003): L<<813.0,512.0>--<810.0,514.0>> -> L<<810.0,514.0>--<537.0,711.0>>

	* piweb (U+E004): L<<813.0,512.0>--<810.0,514.0>> -> L<<810.0,514.0>--<537.0,711.0>>

	* sparks (U+E011): L<<100.0,798.0>--<103.0,797.0>> -> L<<103.0,797.0>--<198.0,762.0>>

	* sparks (U+E011): L<<103.0,797.0>--<198.0,762.0>> -> L<<198.0,762.0>--<209.0,759.0>>

	* sparks (U+E011): L<<198.0,762.0>--<209.0,759.0>> -> L<<209.0,759.0>--<400.0,690.0>>

	* sparks (U+E011): L<<209.0,759.0>--<400.0,690.0>> -> L<<400.0,690.0>--<431.0,680.0>>

	* sparks (U+E011): L<<291.0,596.0>--<363.0,534.0>> -> L<<363.0,534.0>--<382.0,516.0>>

	* sparks (U+E011): L<<381.0,366.0>--<383.0,367.0>> -> L<<383.0,367.0>--<486.0,429.0>>

	* sparks (U+E011): L<<383.0,367.0>--<486.0,429.0>> -> L<<486.0,429.0>--<488.0,430.0>>

	* sparks (U+E011): L<<409.0,102.0>--<98.0,641.0>> -> L<<98.0,641.0>--<47.0,731.0>>

	* sparks (U+E011): L<<440.0,659.0>--<436.0,649.0>> -> L<<436.0,649.0>--<434.0,643.0>>

	* sparks (U+E011): L<<454.0,24.0>--<409.0,102.0>> -> L<<409.0,102.0>--<98.0,641.0>>

	* sparks (U+E011): L<<504.0,429.0>--<606.0,367.0>> -> L<<606.0,367.0>--<608.0,366.0>>

	* sparks (U+E011): L<<558.0,680.0>--<596.0,694.0>> -> L<<596.0,694.0>--<780.0,759.0>>

	* sparks (U+E011): L<<579.0,101.0>--<550.0,51.0>> -> L<<550.0,51.0>--<535.0,24.0>>

	* sparks (U+E011): L<<596.0,694.0>--<780.0,759.0>> -> L<<780.0,759.0>--<807.0,768.0>>

	* sparks (U+E011): L<<607.0,516.0>--<627.0,534.0>> -> L<<627.0,534.0>--<699.0,596.0>>

	* sparks (U+E011): L<<614.0,629.0>--<577.0,632.0>> -> L<<577.0,632.0>--<568.0,633.0>>

	* sparks (U+E011): L<<655.0,626.0>--<614.0,629.0>> -> L<<614.0,629.0>--<577.0,632.0>>

	* sparks (U+E011): L<<656.0,626.0>--<655.0,626.0>> -> L<<655.0,626.0>--<614.0,629.0>>

	* sparks (U+E011): L<<690.0,623.0>--<656.0,626.0>> -> L<<656.0,626.0>--<655.0,626.0>>

	* sparks (U+E011): L<<691.0,623.0>--<690.0,623.0>> -> L<<690.0,623.0>--<656.0,626.0>>

	* sparks (U+E011): L<<750.0,397.0>--<579.0,101.0>> -> L<<579.0,101.0>--<550.0,51.0>>

	* sparks (U+E011): L<<780.0,759.0>--<807.0,768.0>> -> L<<807.0,768.0>--<886.0,797.0>>

	* sparks (U+E011): L<<897.0,652.0>--<750.0,397.0>> -> L<<750.0,397.0>--<579.0,101.0>>

	* sparks (U+E011): L<<942.0,730.0>--<897.0,652.0>> -> L<<897.0,652.0>--<750.0,397.0>> 

	* sparks (U+E011): L<<943.0,732.0>--<942.0,730.0>> -> L<<942.0,730.0>--<897.0,652.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* petapp (U+E006): B<<289.0,471.0>-<290.0,469.0>-<291.0,468.0>>/L<<291.0,468.0>--<289.0,471.0>> = 11.309932474020227

	* petapp (U+E006): B<<295.0,293.0>-<289.0,300.0>-<282.0,304.0>>/L<<282.0,304.0>--<312.0,286.0>> = 1.2188752351307344

	* petapp (U+E006): B<<328.0,429.0>-<329.0,428.0>-<331.0,427.0>>/L<<331.0,427.0>--<328.0,429.0>> = 7.125016348901757

	* petapp (U+E006): B<<415.0,76.0>-<416.0,76.0>-<418.0,75.0>>/L<<418.0,75.0>--<415.0,76.0>> = 8.130102354155916

	* petapp (U+E006): B<<424.0,71.0>-<425.0,71.0>-<427.0,70.0>>/L<<427.0,70.0>--<424.0,71.0>> = 8.130102354155916

	* petapp (U+E006): B<<439.0,65.0>-<440.0,65.0>-<442.0,64.0>>/L<<442.0,64.0>--<439.0,65.0>> = 8.130102354155916

	* petapp (U+E006): B<<483.0,64.0>-<484.0,64.0>-<486.0,65.0>>/L<<486.0,65.0>--<483.0,64.0>> = 8.130102354155916

	* petapp (U+E006): B<<513.0,65.0>-<515.0,65.0>-<517.0,66.0>>/L<<517.0,66.0>--<513.0,65.0>> = 12.528807709151463

	* petapp (U+E006): B<<519.0,66.0>-<521.0,66.0>-<523.0,67.0>>/L<<523.0,67.0>--<519.0,66.0>> = 12.528807709151463

	* petapp (U+E006): B<<529.0,68.0>-<528.0,68.0>-<526.0,67.0>>/L<<526.0,67.0>--<529.0,68.0>> = 8.13010235415587

	* petapp (U+E006): B<<536.0,192.0>-<535.0,194.0>-<534.0,195.0>>/L<<534.0,195.0>--<536.0,192.0>> = 11.309932474020195

	* petapp (U+E006): B<<536.0,69.0>-<534.0,69.0>-<532.0,68.0>>/L<<532.0,68.0>--<536.0,69.0>> = 12.528807709151492

	* petapp (U+E006): B<<537.0,308.0>-<536.0,309.0>-<534.0,310.0>>/L<<534.0,310.0>--<537.0,308.0>> = 7.125016348901757

	* petapp (U+E006): B<<539.0,108.0>-<540.0,109.0>-<541.0,111.0>>/L<<541.0,111.0>--<539.0,108.0>> = 7.125016348901705

	* petapp (U+E006): B<<539.0,438.0>-<538.0,439.0>-<536.0,440.0>>/L<<536.0,440.0>--<539.0,438.0>> = 7.125016348901757

	* petapp (U+E006): B<<545.0,123.0>-<546.0,125.0>-<546.0,127.0>>/L<<546.0,127.0>--<545.0,123.0>> = 14.036243467926484

	* petapp (U+E006): B<<548.0,432.0>-<547.0,433.0>-<545.0,434.0>>/L<<545.0,434.0>--<548.0,432.0>> = 7.125016348901757

	* petapp (U+E006): B<<548.0,72.0>-<549.0,72.0>-<551.0,73.0>>/L<<551.0,73.0>--<548.0,72.0>> = 8.130102354155916

	* petapp (U+E006): B<<575.0,404.0>-<576.0,403.0>-<577.0,401.0>>/L<<577.0,401.0>--<575.0,404.0>> = 7.125016348901705

	* petapp (U+E006): B<<587.0,380.0>-<587.0,382.0>-<586.0,384.0>>/L<<586.0,384.0>--<587.0,380.0>> = 12.528807709151492

	* petapp (U+E006): B<<610.0,384.0>-<611.0,381.0>-<612.0,379.0>>/L<<612.0,379.0>--<610.0,384.0>> = 4.763641690726066

	* petapp (U+E006): B<<614.0,384.0>-<615.0,382.0>-<616.0,379.0>>/L<<616.0,379.0>--<614.0,384.0>> = 3.366460663429615

	* petapp (U+E006): B<<627.0,343.0>-<628.0,342.0>-<629.0,340.0>>/L<<629.0,340.0>--<627.0,343.0>> = 7.125016348901705

	* petapp (U+E006): B<<633.0,334.0>-<633.0,333.0>-<634.0,331.0>>/L<<634.0,331.0>--<633.0,334.0>> = 8.130102354155916

	* petapp (U+E006): B<<638.0,346.0>-<639.0,345.0>-<640.0,343.0>>/L<<640.0,343.0>--<638.0,346.0>> = 7.125016348901705

	* petapp (U+E006): B<<641.0,321.0>-<642.0,320.0>-<643.0,318.0>>/L<<643.0,318.0>--<641.0,321.0>> = 7.125016348901705

	* petapp (U+E006): B<<669.0,316.0>-<670.0,315.0>-<672.0,314.0>>/L<<672.0,314.0>--<669.0,316.0>> = 7.125016348901757

	* petapp (U+E006): B<<669.0,456.0>-<667.0,454.0>-<666.0,452.0>>/L<<666.0,452.0>--<669.0,456.0>> = 10.304846468766044

	* petapp (U+E006): B<<670.0,137.0>-<671.0,138.0>-<672.0,140.0>>/L<<672.0,140.0>--<670.0,137.0>> = 7.125016348901705

	* petapp (U+E006): B<<679.0,141.0>-<681.0,142.0>-<682.0,143.0>>/L<<682.0,143.0>--<679.0,141.0>> = 11.309932474020195

	* petapp (U+E006): B<<687.0,164.0>-<688.0,166.0>-<689.0,167.0>>/L<<689.0,167.0>--<687.0,164.0>> = 11.309932474020227

	* petapp (U+E006): B<<713.0,484.0>-<712.0,484.0>-<710.0,483.0>>/L<<710.0,483.0>--<713.0,484.0>> = 8.13010235415587

	* petapp (U+E006): B<<763.0,5.0>-<762.0,7.0>-<761.0,8.0>>/L<<761.0,8.0>--<763.0,5.0>> = 11.309932474020195

	* petapp (U+E006): L<<274.0,517.0>--<273.0,520.0>>/B<<273.0,520.0>-<274.0,518.0>-<274.0,517.0>> = 8.130102354155916

	* petapp (U+E006): L<<280.0,491.0>--<279.0,494.0>>/B<<279.0,494.0>-<280.0,492.0>-<280.0,491.0>> = 8.130102354155916

	* petapp (U+E006): L<<291.0,468.0>--<289.0,471.0>>/B<<289.0,471.0>-<290.0,469.0>-<291.0,468.0>> = 7.125016348901705

	* petapp (U+E006): L<<296.0,459.0>--<295.0,462.0>>/B<<295.0,462.0>-<296.0,460.0>-<296.0,459.0>> = 8.130102354155916

	* petapp (U+E006): L<<312.0,442.0>--<308.0,445.0>>/B<<308.0,445.0>-<310.0,444.0>-<312.0,442.0>> = 10.304846468766009

	* petapp (U+E006): L<<331.0,427.0>--<328.0,429.0>>/B<<328.0,429.0>-<329.0,428.0>-<331.0,427.0>> = 11.309932474020195

	* petapp (U+E006): L<<380.0,128.0>--<379.0,131.0>>/B<<379.0,131.0>-<380.0,129.0>-<380.0,128.0>> = 8.130102354155916

	* petapp (U+E006): L<<387.0,108.0>--<386.0,111.0>>/B<<386.0,111.0>-<387.0,109.0>-<387.0,108.0>> = 8.130102354155916

	* petapp (U+E006): L<<499.0,225.0>--<505.0,222.0>>/L<<505.0,222.0>--<498.0,226.0>> = 3.1798301198640497

	* petapp (U+E006): L<<504.0,71.0>--<499.0,69.0>>/B<<499.0,69.0>-<502.0,71.0>-<504.0,71.0>> = 11.888658039627936

	* petapp (U+E006): L<<517.0,66.0>--<513.0,65.0>>/B<<513.0,65.0>-<515.0,65.0>-<517.0,66.0>> = 14.036243467926484

	* petapp (U+E006): L<<523.0,67.0>--<519.0,66.0>>/B<<519.0,66.0>-<521.0,66.0>-<523.0,67.0>> = 14.036243467926484

	* petapp (U+E006): L<<532.0,68.0>--<536.0,69.0>>/B<<536.0,69.0>-<534.0,69.0>-<532.0,68.0>> = 14.036243467926484

	* petapp (U+E006): L<<534.0,195.0>--<536.0,192.0>>/B<<536.0,192.0>-<535.0,194.0>-<534.0,195.0>> = 7.125016348901757

	* petapp (U+E006): L<<534.0,310.0>--<537.0,308.0>>/B<<537.0,308.0>-<536.0,309.0>-<534.0,310.0>> = 11.309932474020227

	* petapp (U+E006): L<<536.0,440.0>--<539.0,438.0>>/B<<539.0,438.0>-<538.0,439.0>-<536.0,440.0>> = 11.309932474020227

	* petapp (U+E006): L<<541.0,111.0>--<539.0,108.0>>/B<<539.0,108.0>-<540.0,109.0>-<541.0,111.0>> = 11.309932474020227

	* petapp (U+E006): L<<541.0,70.0>--<545.0,71.0>>/B<<545.0,71.0>-<540.0,70.0>-<541.0,70.0>> = 2.726310993906212

	* petapp (U+E006): L<<542.0,181.0>--<543.0,178.0>>/B<<543.0,178.0>-<542.0,180.0>-<542.0,181.0>> = 8.13010235415587

	* petapp (U+E006): L<<545.0,434.0>--<548.0,432.0>>/B<<548.0,432.0>-<547.0,433.0>-<545.0,434.0>> = 11.309932474020227

	* petapp (U+E006): L<<546.0,127.0>--<545.0,123.0>>/B<<545.0,123.0>-<546.0,125.0>-<546.0,127.0>> = 12.528807709151492

	* petapp (U+E006): L<<556.0,74.0>--<553.0,73.0>>/B<<553.0,73.0>-<555.0,74.0>-<556.0,74.0>> = 8.130102354155916

	* petapp (U+E006): L<<577.0,401.0>--<575.0,404.0>>/B<<575.0,404.0>-<576.0,403.0>-<577.0,401.0>> = 11.309932474020227

	* petapp (U+E006): L<<583.0,256.0>--<584.0,252.0>>/B<<584.0,252.0>-<584.0,254.0>-<583.0,256.0>> = 14.036243467926484

	* petapp (U+E006): L<<586.0,384.0>--<587.0,380.0>>/B<<587.0,380.0>-<587.0,382.0>-<586.0,384.0>> = 14.036243467926484

	* petapp (U+E006): L<<598.0,432.0>--<599.0,429.0>>/B<<599.0,429.0>-<598.0,431.0>-<598.0,432.0>> = 8.13010235415587

	* petapp (U+E006): L<<602.0,122.0>--<601.0,125.0>>/B<<601.0,125.0>-<602.0,123.0>-<602.0,122.0>> = 8.130102354155916

	* petapp (U+E006): L<<611.0,96.0>--<611.0,96.0>>/B<<611.0,96.0>-<607.0,95.0>-<603.5,92.5>> = 14.036243467926484

	* petapp (U+E006): L<<612.0,379.0>--<610.0,384.0>>/B<<610.0,384.0>-<611.0,381.0>-<612.0,379.0>> = 3.366460663429615

	* petapp (U+E006): L<<613.0,374.0>--<612.0,377.0>>/B<<612.0,377.0>-<613.0,375.0>-<613.0,374.0>> = 8.130102354155916

	* petapp (U+E006): L<<615.0,369.0>--<614.0,372.0>>/B<<614.0,372.0>-<615.0,370.0>-<615.0,369.0>> = 8.130102354155916

	* petapp (U+E006): L<<616.0,379.0>--<614.0,384.0>>/B<<614.0,384.0>-<615.0,382.0>-<616.0,379.0>> = 4.763641690726066

	* petapp (U+E006): L<<629.0,340.0>--<627.0,343.0>>/B<<627.0,343.0>-<628.0,342.0>-<629.0,340.0>> = 11.309932474020227

	* petapp (U+E006): L<<640.0,343.0>--<638.0,346.0>>/B<<638.0,346.0>-<639.0,345.0>-<640.0,343.0>> = 11.309932474020227

	* petapp (U+E006): L<<643.0,318.0>--<641.0,321.0>>/B<<641.0,321.0>-<642.0,320.0>-<643.0,318.0>> = 11.309932474020227

	* petapp (U+E006): L<<657.0,433.0>--<658.0,436.0>>/B<<658.0,436.0>-<657.0,434.0>-<657.0,432.5>> = 8.13010235415587

	* petapp (U+E006): L<<661.0,383.0>--<660.0,386.0>>/B<<660.0,386.0>-<661.0,384.0>-<661.0,383.0>> = 8.130102354155916

	* petapp (U+E006): L<<666.0,452.0>--<669.0,456.0>>/B<<669.0,456.0>-<667.0,454.0>-<666.0,452.0>> = 8.13010235415596

	* petapp (U+E006): L<<672.0,140.0>--<670.0,137.0>>/B<<670.0,137.0>-<671.0,138.0>-<672.0,140.0>> = 11.309932474020227

	* petapp (U+E006): L<<682.0,143.0>--<679.0,141.0>>/B<<679.0,141.0>-<681.0,142.0>-<682.0,143.0>> = 7.125016348901757

	* petapp (U+E006): L<<686.0,162.0>--<685.0,159.0>>/B<<685.0,159.0>-<686.0,161.0>-<686.0,162.0>> = 8.130102354155916

	* petapp (U+E006): L<<689.0,167.0>--<687.0,164.0>>/B<<687.0,164.0>-<688.0,166.0>-<689.0,167.0>> = 7.125016348901705

	* petapp (U+E006): L<<689.0,256.0>--<690.0,253.0>>/B<<690.0,253.0>-<689.0,255.0>-<689.0,256.0>> = 8.13010235415587

	* petapp (U+E006): L<<691.0,251.0>--<692.0,248.0>>/B<<692.0,248.0>-<691.0,250.0>-<691.0,251.0>> = 8.13010235415587

	* petapp (U+E006): L<<700.0,480.0>--<703.0,481.0>>/B<<703.0,481.0>-<701.0,480.0>-<700.0,479.5>> = 8.13010235415587

	* petapp (U+E006): L<<705.0,482.0>--<708.0,483.0>>/B<<708.0,483.0>-<706.0,482.0>-<705.0,482.0>> = 8.13010235415587

	* petapp (U+E006): L<<708.0,293.0>--<705.0,294.0>>/B<<705.0,294.0>-<707.0,293.0>-<708.0,293.0>> = 8.130102354155916

	* petapp (U+E006): L<<728.0,285.0>--<725.0,286.0>>/B<<725.0,286.0>-<727.0,285.0>-<728.0,285.0>> = 8.130102354155916

	* petapp (U+E006): L<<761.0,8.0>--<763.0,5.0>>/B<<763.0,5.0>-<762.0,7.0>-<761.0,8.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<581.0,372.0>-<585.0,368.0>-<588.0,366.0>>/L<<588.0,366.0>--<581.0,372.0>> = 6.911227119024609

	* petapp.minimal (U+E007): B<<631.0,435.0>-<631.0,433.0>-<632.0,430.0>>/L<<632.0,430.0>--<631.0,435.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<632.0,481.0>-<632.0,480.0>-<631.0,478.0>>/L<<631.0,478.0>--<632.0,481.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<645.0,399.0>-<646.0,397.0>-<647.0,396.0>>/L<<647.0,396.0>--<645.0,399.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<646.0,510.0>-<645.0,508.0>-<644.0,507.0>>/L<<644.0,507.0>--<646.0,510.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<676.0,538.0>-<674.0,537.0>-<673.0,536.0>>/L<<673.0,536.0>--<676.0,538.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<700.0,247.0>-<699.0,248.0>-<698.0,250.0>>/L<<698.0,250.0>--<700.0,247.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<714.0,147.0>-<714.0,148.0>-<713.0,150.0>>/L<<713.0,150.0>--<714.0,147.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<720.0,137.0>-<719.0,139.0>-<718.0,140.0>>/L<<718.0,140.0>--<720.0,137.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<732.0,185.0>-<731.0,187.0>-<731.0,189.0>>/L<<731.0,189.0>--<732.0,185.0>> = 14.036243467926484

	* petapp.minimal (U+E007): B<<743.0,53.0>-<743.0,54.0>-<742.0,56.0>>/L<<742.0,56.0>--<743.0,53.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<212.0,538.0>--<212.0,800.0>>/B<<212.0,800.0>-<214.0,769.0>-<226.5,742.0>> = 3.6913859864512575

	* petapp.minimal (U+E007): L<<628.0,462.0>--<629.0,465.0>>/B<<629.0,465.0>-<628.0,463.0>-<628.0,462.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<630.0,473.0>--<631.0,476.0>>/B<<631.0,476.0>-<630.0,474.0>-<630.0,473.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<632.0,430.0>--<631.0,435.0>>/B<<631.0,435.0>-<631.0,433.0>-<632.0,430.0>> = 11.309932474020227

	* petapp.minimal (U+E007): L<<637.0,222.0>--<640.0,221.0>>/B<<640.0,221.0>-<638.0,222.0>-<637.0,222.5>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<639.0,498.0>--<640.0,501.0>>/B<<640.0,501.0>-<639.0,499.0>-<639.0,498.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<644.0,507.0>--<646.0,510.0>>/B<<646.0,510.0>-<645.0,508.0>-<644.0,507.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<647.0,396.0>--<645.0,399.0>>/B<<645.0,399.0>-<646.0,397.0>-<647.0,396.0>> = 7.125016348901705

	* petapp.minimal (U+E007): L<<673.0,536.0>--<676.0,538.0>>/B<<676.0,538.0>-<674.0,537.0>-<673.0,536.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<682.0,542.0>--<685.0,543.0>>/B<<685.0,543.0>-<683.0,542.0>-<682.0,542.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<687.0,544.0>--<690.0,545.0>>/B<<690.0,545.0>-<688.0,544.0>-<687.0,544.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<698.0,250.0>--<700.0,247.0>>/B<<700.0,247.0>-<699.0,248.0>-<698.0,250.0>> = 11.309932474020195

	* petapp.minimal (U+E007): L<<718.0,218.0>--<719.0,215.0>>/B<<719.0,215.0>-<718.0,217.0>-<718.0,218.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<731.0,113.0>--<732.0,110.0>>/B<<732.0,110.0>-<731.0,112.0>-<731.0,113.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<740.0,156.0>--<739.0,160.0>>/B<<739.0,160.0>-<740.0,153.0>-<740.0,156.0>> = 5.906141113770497

	* petapp.minimal (U+E007): L<<744.0,137.0>--<743.0,140.0>>/B<<743.0,140.0>-<744.0,138.0>-<744.0,137.0>> = 8.130102354155916

	* petapp.minimal (U+E007): L<<746.0,123.0>--<747.0,120.0>>/B<<747.0,120.0>-<746.0,122.0>-<746.0,123.0>> = 8.13010235415587

	* petapp.wpda (U+E008): B<<485.0,2.0>-<482.0,5.0>-<482.0,6.0>>/L<<482.0,6.0>--<481.0,1.0>> = 11.309932474020227

	* petapp.wpda (U+E008): L<<185.0,222.0>--<180.0,218.0>>/B<<180.0,218.0>-<182.0,219.0>-<183.0,218.0>> = 12.094757077012058

	* pisafe (U+E010): B<<175.0,538.0>-<175.0,536.0>-<174.0,534.0>>/L<<174.0,534.0>--<175.0,538.0>> = 12.528807709151492

	* pisafe (U+E010): B<<190.0,573.0>-<189.0,572.0>-<188.0,570.0>>/L<<188.0,570.0>--<190.0,573.0>> = 7.125016348901757

	* pisafe (U+E010): B<<211.0,602.0>-<210.0,600.0>-<208.0,598.0>>/L<<208.0,598.0>--<211.0,602.0>> = 8.13010235415596

	* pisafe (U+E010): B<<784.0,594.0>-<783.0,596.0>-<782.0,597.0>>/L<<782.0,597.0>--<784.0,594.0>> = 11.309932474020195

	* pisafe (U+E010): B<<797.0,577.0>-<796.0,579.0>-<795.0,580.0>>/L<<795.0,580.0>--<797.0,577.0>> = 11.309932474020195

	* pisafe (U+E010): B<<816.0,530.0>-<816.0,532.0>-<815.0,534.0>>/L<<815.0,534.0>--<816.0,530.0>> = 12.528807709151492

	* pisafe (U+E010): B<<820.0,515.0>-<820.0,516.0>-<819.0,518.0>>/L<<819.0,518.0>--<820.0,515.0>> = 8.13010235415587

	* pisafe (U+E010): L<<174.0,534.0>--<175.0,538.0>>/B<<175.0,538.0>-<175.0,536.0>-<174.0,534.0>> = 14.036243467926484

	* pisafe (U+E010): L<<188.0,570.0>--<190.0,573.0>>/B<<190.0,573.0>-<189.0,572.0>-<188.0,570.0>> = 11.309932474020195

	* pisafe (U+E010): L<<208.0,598.0>--<211.0,602.0>>/B<<211.0,602.0>-<210.0,600.0>-<208.0,598.0>> = 10.304846468766044

	* pisafe (U+E010): L<<750.0,626.0>--<754.0,623.0>>/B<<754.0,623.0>-<752.0,624.0>-<750.0,626.0>> = 10.304846468766009

	* pisafe (U+E010): L<<782.0,597.0>--<784.0,594.0>>/B<<784.0,594.0>-<783.0,596.0>-<782.0,597.0>> = 7.125016348901757

	* pisafe (U+E010): L<<795.0,580.0>--<797.0,577.0>>/B<<797.0,577.0>-<796.0,579.0>-<795.0,580.0>> = 7.125016348901757

	* pisafe (U+E010): L<<815.0,534.0>--<816.0,530.0>>/B<<816.0,530.0>-<816.0,532.0>-<815.0,534.0>> = 14.036243467926484 

	* pisafe (U+E010): L<<817.0,528.0>--<818.0,525.0>>/B<<818.0,525.0>-<817.0,527.0>-<817.0,528.0>> = 8.13010235415587 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[19] PitagonSansText-MediumItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check OFL body text is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text">com.google.fonts/check/license/OFL_body_text</a>)</summary><div>


* 🔥 **FAIL** The OFL.txt body text is incorrect. Please use https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt as a template. You should only modify the first line. [code: incorrect-ofl-body-text]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ
at: https://scripts.sil.org/OFL." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks">com.google.fonts/check/name/line_breaks</a>)</summary><div>


* 🔥 **FAIL** Name entry DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1294, but got 1214 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.11, while a newer 0.8.13 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'Pita' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
</div></details><details><summary>⚠ <b>WARN:</b> Description strings in the name table must not exceed 200 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/description_max_length">com.google.fonts/check/name/description_max_length</a>)</summary><div>


* ⚠ **WARN** A few name table entries with ID=10 (NameID.DESCRIPTION) are longer than 200 characters. Please check whether those entries are copyright notices mistakenly stored in the description string entries by a bug in an old FontLab version. If that's the case, then such copyright notices must be removed from these entries. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Pitagon Sans Text Medium' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- periodcentered.001 

	- registered.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni0200	Contours detected: 3	Expected: 4

	- Glyph name: uni0201	Contours detected: 3	Expected: 4

	- Glyph name: uni0204	Contours detected: 2	Expected: 3

	- Glyph name: uni0205	Contours detected: 3	Expected: 4

	- Glyph name: uni0208	Contours detected: 2	Expected: 3

	- Glyph name: uni0209	Contours detected: 2	Expected: 3

	- Glyph name: uni020C	Contours detected: 3	Expected: 4

	- Glyph name: uni020D	Contours detected: 3	Expected: 4

	- Glyph name: uni0210	Contours detected: 3	Expected: 4

	- Glyph name: uni0211	Contours detected: 2	Expected: 3

	- Glyph name: uni0214	Contours detected: 2	Expected: 3

	- Glyph name: uni0215	Contours detected: 2	Expected: 3

	- Glyph name: uni030F	Contours detected: 1	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni030F	Contours detected: 1	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* petapp (U+E006): L<<282.0,304.0>--<312.0,286.0>> -> L<<312.0,286.0>--<339.0,271.0>>

	* petapp (U+E006): L<<312.0,333.0>--<273.0,356.0>> -> L<<273.0,356.0>--<257.0,365.0>>

	* petapp (U+E006): L<<355.0,309.0>--<312.0,333.0>> -> L<<312.0,333.0>--<273.0,356.0>>

	* petapp (U+E006): L<<371.0,299.0>--<355.0,309.0>> -> L<<355.0,309.0>--<312.0,333.0>>

	* petapp (U+E006): L<<371.0,640.0>--<467.0,585.0>> -> L<<467.0,585.0>--<515.0,556.0>>

	* petapp (U+E006): L<<373.0,298.0>--<371.0,299.0>> -> L<<371.0,299.0>--<355.0,309.0>>

	* petapp (U+E006): L<<426.0,268.0>--<373.0,298.0>> -> L<<373.0,298.0>--<371.0,299.0>>

	* petapp (U+E006): L<<467.0,585.0>--<515.0,556.0>> -> L<<515.0,556.0>--<534.0,545.0>>

	* petapp (U+E006): L<<468.0,243.0>--<426.0,268.0>> -> L<<426.0,268.0>--<373.0,298.0>>

	* petapp (U+E006): L<<474.0,240.0>--<468.0,243.0>> -> L<<468.0,243.0>--<426.0,268.0>>

	* petapp (U+E006): L<<498.0,226.0>--<474.0,240.0>> -> L<<474.0,240.0>--<468.0,243.0>>

	* petapp (U+E006): L<<505.0,222.0>--<498.0,226.0>> -> L<<498.0,226.0>--<474.0,240.0>>

	* petapp (U+E006): L<<691.0,61.0>--<692.0,60.0>> -> L<<692.0,60.0>--<696.0,56.0>>

	* petapp (U+E006): L<<721.0,485.0>--<725.0,485.0>> -> L<<725.0,485.0>--<764.0,485.0>>

	* petapp.minimal (U+E007): L<<264.0,373.0>--<351.0,339.0>> -> L<<351.0,339.0>--<432.0,305.0>>

	* petapp.minimal (U+E007): L<<351.0,339.0>--<432.0,305.0>> -> L<<432.0,305.0>--<448.0,299.0>>

	* petapp.minimal (U+E007): L<<381.0,352.0>--<331.0,376.0>> -> L<<331.0,376.0>--<305.0,390.0>>

	* petapp.minimal (U+E007): L<<432.0,305.0>--<448.0,299.0>> -> L<<448.0,299.0>--<504.0,276.0>>

	* petapp.minimal (U+E007): L<<432.0,326.0>--<381.0,352.0>> -> L<<381.0,352.0>--<331.0,376.0>>

	* petapp.minimal (U+E007): L<<435.0,187.0>--<405.0,192.0>> -> L<<405.0,192.0>--<304.0,211.0>>

	* petapp.minimal (U+E007): L<<448.0,299.0>--<504.0,276.0>> -> L<<504.0,276.0>--<612.0,232.0>>

	* petapp.minimal (U+E007): L<<455.0,314.0>--<432.0,326.0>> -> L<<432.0,326.0>--<381.0,352.0>>

	* petapp.minimal (U+E007): L<<504.0,175.0>--<435.0,187.0>> -> L<<435.0,187.0>--<405.0,192.0>>

	* petapp.minimal (U+E007): L<<504.0,276.0>--<612.0,232.0>> -> L<<612.0,232.0>--<621.0,229.0>>

	* petapp.minimal (U+E007): L<<504.0,289.0>--<455.0,314.0>> -> L<<455.0,314.0>--<432.0,326.0>>

	* petapp.minimal (U+E007): L<<588.0,160.0>--<504.0,175.0>> -> L<<504.0,175.0>--<435.0,187.0>>

	* petapp.minimal (U+E007): L<<621.0,229.0>--<504.0,289.0>> -> L<<504.0,289.0>--<455.0,314.0>>

	* petapp.minimal (U+E007): L<<742.0,30.0>--<742.0,31.0>> -> L<<742.0,31.0>--<742.0,32.0>>

	* petapp.minimal (U+E007): L<<743.0,33.0>--<743.0,34.0>> -> L<<743.0,34.0>--<743.0,36.0>>

	* petapp.minimal (U+E007): L<<743.0,34.0>--<743.0,36.0>> -> L<<743.0,36.0>--<743.0,37.0>>

	* petapp.minimal (U+E007): L<<747.0,73.0>--<746.0,63.0>> -> L<<746.0,63.0>--<743.0,38.0>>

	* petapp.minimal (U+E007): L<<747.0,74.0>--<747.0,73.0>> -> L<<747.0,73.0>--<746.0,63.0>>

	* petapp.minimal (U+E007): L<<752.0,131.0>--<747.0,74.0>> -> L<<747.0,74.0>--<747.0,73.0>>

	* petapp.minimal (U+E007): L<<754.0,162.0>--<752.0,131.0>> -> L<<752.0,131.0>--<747.0,74.0>>

	* petapp.minimal (U+E007): L<<755.0,175.0>--<754.0,162.0>> -> L<<754.0,162.0>--<752.0,131.0>>

	* petapp.minimal (U+E007): L<<757.0,196.0>--<755.0,175.0>> -> L<<755.0,175.0>--<754.0,162.0>>

	* petapp.minimal (U+E007): L<<758.0,210.0>--<757.0,196.0>> -> L<<757.0,196.0>--<755.0,175.0>>

	* petapp.minimal (U+E007): L<<758.0,213.0>--<758.0,210.0>> -> L<<758.0,210.0>--<757.0,196.0>>

	* petapp.wpda (U+E008): L<<640.0,140.0>--<627.0,132.0>> -> L<<627.0,132.0>--<618.0,127.0>>

	* piads (U+E001): L<<112.0,541.0>--<116.0,544.0>> -> L<<116.0,544.0>--<445.0,782.0>>

	* piads (U+E001): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<878.0,541.0>>

	* picall (U+E009): L<<112.0,541.0>--<116.0,544.0>> -> L<<116.0,544.0>--<445.0,782.0>>

	* picall (U+E009): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<878.0,541.0>>

	* pioffice (U+E002): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<877.0,542.0>>

	* pisafe (U+E010): L<<167.0,362.0>--<167.0,491.0>> -> L<<167.0,491.0>--<167.0,494.0>>

	* pisafe (U+E010): L<<203.0,695.0>--<239.0,708.0>> -> L<<239.0,708.0>--<389.0,762.0>>

	* pisafe (U+E010): L<<239.0,708.0>--<389.0,762.0>> -> L<<389.0,762.0>--<494.0,800.0>>

	* pisafe (U+E010): L<<495.0,800.0>--<600.0,762.0>> -> L<<600.0,762.0>--<750.0,708.0>>

	* pisafe (U+E010): L<<600.0,762.0>--<750.0,708.0>> -> L<<750.0,708.0>--<786.0,695.0>>

	* pisign (U+E005): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<877.0,542.0>>

	* pitagon (U+E000): L<<112.0,543.0>--<116.0,546.0>> -> L<<116.0,546.0>--<445.0,784.0>>

	* pitagon (U+E000): L<<209.0,62.0>--<84.0,446.0>> -> L<<84.0,446.0>--<82.0,452.0>>

	* pitagon (U+E000): L<<547.0,784.0>--<874.0,546.0>> -> L<<874.0,546.0>--<878.0,543.0>>

	* pitagram (U+E003): L<<813.0,512.0>--<810.0,514.0>> -> L<<810.0,514.0>--<537.0,711.0>>

	* piweb (U+E004): L<<813.0,512.0>--<810.0,514.0>> -> L<<810.0,514.0>--<537.0,711.0>>

	* sparks (U+E011): L<<100.0,798.0>--<103.0,797.0>> -> L<<103.0,797.0>--<198.0,762.0>>

	* sparks (U+E011): L<<103.0,797.0>--<198.0,762.0>> -> L<<198.0,762.0>--<209.0,759.0>>

	* sparks (U+E011): L<<198.0,762.0>--<209.0,759.0>> -> L<<209.0,759.0>--<400.0,690.0>>

	* sparks (U+E011): L<<209.0,759.0>--<400.0,690.0>> -> L<<400.0,690.0>--<431.0,680.0>>

	* sparks (U+E011): L<<291.0,596.0>--<363.0,534.0>> -> L<<363.0,534.0>--<382.0,516.0>>

	* sparks (U+E011): L<<381.0,366.0>--<383.0,367.0>> -> L<<383.0,367.0>--<486.0,429.0>>

	* sparks (U+E011): L<<383.0,367.0>--<486.0,429.0>> -> L<<486.0,429.0>--<488.0,430.0>>

	* sparks (U+E011): L<<409.0,102.0>--<98.0,641.0>> -> L<<98.0,641.0>--<47.0,731.0>>

	* sparks (U+E011): L<<440.0,659.0>--<436.0,649.0>> -> L<<436.0,649.0>--<434.0,643.0>>

	* sparks (U+E011): L<<454.0,24.0>--<409.0,102.0>> -> L<<409.0,102.0>--<98.0,641.0>>

	* sparks (U+E011): L<<504.0,429.0>--<606.0,367.0>> -> L<<606.0,367.0>--<608.0,366.0>>

	* sparks (U+E011): L<<558.0,680.0>--<596.0,694.0>> -> L<<596.0,694.0>--<780.0,759.0>>

	* sparks (U+E011): L<<579.0,101.0>--<550.0,51.0>> -> L<<550.0,51.0>--<535.0,24.0>>

	* sparks (U+E011): L<<596.0,694.0>--<780.0,759.0>> -> L<<780.0,759.0>--<807.0,768.0>>

	* sparks (U+E011): L<<607.0,516.0>--<627.0,534.0>> -> L<<627.0,534.0>--<699.0,596.0>>

	* sparks (U+E011): L<<614.0,629.0>--<577.0,632.0>> -> L<<577.0,632.0>--<568.0,633.0>>

	* sparks (U+E011): L<<655.0,626.0>--<614.0,629.0>> -> L<<614.0,629.0>--<577.0,632.0>>

	* sparks (U+E011): L<<656.0,626.0>--<655.0,626.0>> -> L<<655.0,626.0>--<614.0,629.0>>

	* sparks (U+E011): L<<690.0,623.0>--<656.0,626.0>> -> L<<656.0,626.0>--<655.0,626.0>>

	* sparks (U+E011): L<<691.0,623.0>--<690.0,623.0>> -> L<<690.0,623.0>--<656.0,626.0>>

	* sparks (U+E011): L<<750.0,397.0>--<579.0,101.0>> -> L<<579.0,101.0>--<550.0,51.0>>

	* sparks (U+E011): L<<780.0,759.0>--<807.0,768.0>> -> L<<807.0,768.0>--<886.0,797.0>>

	* sparks (U+E011): L<<897.0,652.0>--<750.0,397.0>> -> L<<750.0,397.0>--<579.0,101.0>>

	* sparks (U+E011): L<<942.0,730.0>--<897.0,652.0>> -> L<<897.0,652.0>--<750.0,397.0>> 

	* sparks (U+E011): L<<943.0,732.0>--<942.0,730.0>> -> L<<942.0,730.0>--<897.0,652.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* petapp (U+E006): B<<289.0,471.0>-<290.0,469.0>-<291.0,468.0>>/L<<291.0,468.0>--<289.0,471.0>> = 11.309932474020227

	* petapp (U+E006): B<<295.0,293.0>-<289.0,300.0>-<282.0,304.0>>/L<<282.0,304.0>--<312.0,286.0>> = 1.2188752351307344

	* petapp (U+E006): B<<328.0,429.0>-<329.0,428.0>-<331.0,427.0>>/L<<331.0,427.0>--<328.0,429.0>> = 7.125016348901757

	* petapp (U+E006): B<<415.0,76.0>-<416.0,76.0>-<418.0,75.0>>/L<<418.0,75.0>--<415.0,76.0>> = 8.130102354155916

	* petapp (U+E006): B<<424.0,71.0>-<425.0,71.0>-<427.0,70.0>>/L<<427.0,70.0>--<424.0,71.0>> = 8.130102354155916

	* petapp (U+E006): B<<439.0,65.0>-<440.0,65.0>-<442.0,64.0>>/L<<442.0,64.0>--<439.0,65.0>> = 8.130102354155916

	* petapp (U+E006): B<<483.0,64.0>-<484.0,64.0>-<486.0,65.0>>/L<<486.0,65.0>--<483.0,64.0>> = 8.130102354155916

	* petapp (U+E006): B<<513.0,65.0>-<515.0,65.0>-<517.0,66.0>>/L<<517.0,66.0>--<513.0,65.0>> = 12.528807709151463

	* petapp (U+E006): B<<519.0,66.0>-<521.0,66.0>-<523.0,67.0>>/L<<523.0,67.0>--<519.0,66.0>> = 12.528807709151463

	* petapp (U+E006): B<<529.0,68.0>-<528.0,68.0>-<526.0,67.0>>/L<<526.0,67.0>--<529.0,68.0>> = 8.13010235415587

	* petapp (U+E006): B<<536.0,192.0>-<535.0,194.0>-<534.0,195.0>>/L<<534.0,195.0>--<536.0,192.0>> = 11.309932474020195

	* petapp (U+E006): B<<536.0,69.0>-<534.0,69.0>-<532.0,68.0>>/L<<532.0,68.0>--<536.0,69.0>> = 12.528807709151492

	* petapp (U+E006): B<<537.0,308.0>-<536.0,309.0>-<534.0,310.0>>/L<<534.0,310.0>--<537.0,308.0>> = 7.125016348901757

	* petapp (U+E006): B<<539.0,108.0>-<540.0,109.0>-<541.0,111.0>>/L<<541.0,111.0>--<539.0,108.0>> = 7.125016348901705

	* petapp (U+E006): B<<539.0,438.0>-<538.0,439.0>-<536.0,440.0>>/L<<536.0,440.0>--<539.0,438.0>> = 7.125016348901757

	* petapp (U+E006): B<<545.0,123.0>-<546.0,125.0>-<546.0,127.0>>/L<<546.0,127.0>--<545.0,123.0>> = 14.036243467926484

	* petapp (U+E006): B<<548.0,432.0>-<547.0,433.0>-<545.0,434.0>>/L<<545.0,434.0>--<548.0,432.0>> = 7.125016348901757

	* petapp (U+E006): B<<548.0,72.0>-<549.0,72.0>-<551.0,73.0>>/L<<551.0,73.0>--<548.0,72.0>> = 8.130102354155916

	* petapp (U+E006): B<<575.0,404.0>-<576.0,403.0>-<577.0,401.0>>/L<<577.0,401.0>--<575.0,404.0>> = 7.125016348901705

	* petapp (U+E006): B<<587.0,380.0>-<587.0,382.0>-<586.0,384.0>>/L<<586.0,384.0>--<587.0,380.0>> = 12.528807709151492

	* petapp (U+E006): B<<610.0,384.0>-<611.0,381.0>-<612.0,379.0>>/L<<612.0,379.0>--<610.0,384.0>> = 4.763641690726066

	* petapp (U+E006): B<<614.0,384.0>-<615.0,382.0>-<616.0,379.0>>/L<<616.0,379.0>--<614.0,384.0>> = 3.366460663429615

	* petapp (U+E006): B<<627.0,343.0>-<628.0,342.0>-<629.0,340.0>>/L<<629.0,340.0>--<627.0,343.0>> = 7.125016348901705

	* petapp (U+E006): B<<633.0,334.0>-<633.0,333.0>-<634.0,331.0>>/L<<634.0,331.0>--<633.0,334.0>> = 8.130102354155916

	* petapp (U+E006): B<<638.0,346.0>-<639.0,345.0>-<640.0,343.0>>/L<<640.0,343.0>--<638.0,346.0>> = 7.125016348901705

	* petapp (U+E006): B<<641.0,321.0>-<642.0,320.0>-<643.0,318.0>>/L<<643.0,318.0>--<641.0,321.0>> = 7.125016348901705

	* petapp (U+E006): B<<669.0,316.0>-<670.0,315.0>-<672.0,314.0>>/L<<672.0,314.0>--<669.0,316.0>> = 7.125016348901757

	* petapp (U+E006): B<<669.0,456.0>-<667.0,454.0>-<666.0,452.0>>/L<<666.0,452.0>--<669.0,456.0>> = 10.304846468766044

	* petapp (U+E006): B<<670.0,137.0>-<671.0,138.0>-<672.0,140.0>>/L<<672.0,140.0>--<670.0,137.0>> = 7.125016348901705

	* petapp (U+E006): B<<679.0,141.0>-<681.0,142.0>-<682.0,143.0>>/L<<682.0,143.0>--<679.0,141.0>> = 11.309932474020195

	* petapp (U+E006): B<<687.0,164.0>-<688.0,166.0>-<689.0,167.0>>/L<<689.0,167.0>--<687.0,164.0>> = 11.309932474020227

	* petapp (U+E006): B<<713.0,484.0>-<712.0,484.0>-<710.0,483.0>>/L<<710.0,483.0>--<713.0,484.0>> = 8.13010235415587

	* petapp (U+E006): B<<763.0,5.0>-<762.0,7.0>-<761.0,8.0>>/L<<761.0,8.0>--<763.0,5.0>> = 11.309932474020195

	* petapp (U+E006): L<<274.0,517.0>--<273.0,520.0>>/B<<273.0,520.0>-<274.0,518.0>-<274.0,517.0>> = 8.130102354155916

	* petapp (U+E006): L<<280.0,491.0>--<279.0,494.0>>/B<<279.0,494.0>-<280.0,492.0>-<280.0,491.0>> = 8.130102354155916

	* petapp (U+E006): L<<291.0,468.0>--<289.0,471.0>>/B<<289.0,471.0>-<290.0,469.0>-<291.0,468.0>> = 7.125016348901705

	* petapp (U+E006): L<<296.0,459.0>--<295.0,462.0>>/B<<295.0,462.0>-<296.0,460.0>-<296.0,459.0>> = 8.130102354155916

	* petapp (U+E006): L<<312.0,442.0>--<308.0,445.0>>/B<<308.0,445.0>-<310.0,444.0>-<312.0,442.0>> = 10.304846468766009

	* petapp (U+E006): L<<331.0,427.0>--<328.0,429.0>>/B<<328.0,429.0>-<329.0,428.0>-<331.0,427.0>> = 11.309932474020195

	* petapp (U+E006): L<<380.0,128.0>--<379.0,131.0>>/B<<379.0,131.0>-<380.0,129.0>-<380.0,128.0>> = 8.130102354155916

	* petapp (U+E006): L<<387.0,108.0>--<386.0,111.0>>/B<<386.0,111.0>-<387.0,109.0>-<387.0,108.0>> = 8.130102354155916

	* petapp (U+E006): L<<499.0,225.0>--<505.0,222.0>>/L<<505.0,222.0>--<498.0,226.0>> = 3.1798301198640497

	* petapp (U+E006): L<<504.0,71.0>--<499.0,69.0>>/B<<499.0,69.0>-<502.0,71.0>-<504.0,71.0>> = 11.888658039627936

	* petapp (U+E006): L<<517.0,66.0>--<513.0,65.0>>/B<<513.0,65.0>-<515.0,65.0>-<517.0,66.0>> = 14.036243467926484

	* petapp (U+E006): L<<523.0,67.0>--<519.0,66.0>>/B<<519.0,66.0>-<521.0,66.0>-<523.0,67.0>> = 14.036243467926484

	* petapp (U+E006): L<<532.0,68.0>--<536.0,69.0>>/B<<536.0,69.0>-<534.0,69.0>-<532.0,68.0>> = 14.036243467926484

	* petapp (U+E006): L<<534.0,195.0>--<536.0,192.0>>/B<<536.0,192.0>-<535.0,194.0>-<534.0,195.0>> = 7.125016348901757

	* petapp (U+E006): L<<534.0,310.0>--<537.0,308.0>>/B<<537.0,308.0>-<536.0,309.0>-<534.0,310.0>> = 11.309932474020227

	* petapp (U+E006): L<<536.0,440.0>--<539.0,438.0>>/B<<539.0,438.0>-<538.0,439.0>-<536.0,440.0>> = 11.309932474020227

	* petapp (U+E006): L<<541.0,111.0>--<539.0,108.0>>/B<<539.0,108.0>-<540.0,109.0>-<541.0,111.0>> = 11.309932474020227

	* petapp (U+E006): L<<541.0,70.0>--<545.0,71.0>>/B<<545.0,71.0>-<540.0,70.0>-<541.0,70.0>> = 2.726310993906212

	* petapp (U+E006): L<<542.0,181.0>--<543.0,178.0>>/B<<543.0,178.0>-<542.0,180.0>-<542.0,181.0>> = 8.13010235415587

	* petapp (U+E006): L<<545.0,434.0>--<548.0,432.0>>/B<<548.0,432.0>-<547.0,433.0>-<545.0,434.0>> = 11.309932474020227

	* petapp (U+E006): L<<546.0,127.0>--<545.0,123.0>>/B<<545.0,123.0>-<546.0,125.0>-<546.0,127.0>> = 12.528807709151492

	* petapp (U+E006): L<<556.0,74.0>--<553.0,73.0>>/B<<553.0,73.0>-<555.0,74.0>-<556.0,74.0>> = 8.130102354155916

	* petapp (U+E006): L<<577.0,401.0>--<575.0,404.0>>/B<<575.0,404.0>-<576.0,403.0>-<577.0,401.0>> = 11.309932474020227

	* petapp (U+E006): L<<583.0,256.0>--<584.0,252.0>>/B<<584.0,252.0>-<584.0,254.0>-<583.0,256.0>> = 14.036243467926484

	* petapp (U+E006): L<<586.0,384.0>--<587.0,380.0>>/B<<587.0,380.0>-<587.0,382.0>-<586.0,384.0>> = 14.036243467926484

	* petapp (U+E006): L<<598.0,432.0>--<599.0,429.0>>/B<<599.0,429.0>-<598.0,431.0>-<598.0,432.0>> = 8.13010235415587

	* petapp (U+E006): L<<602.0,122.0>--<601.0,125.0>>/B<<601.0,125.0>-<602.0,123.0>-<602.0,122.0>> = 8.130102354155916

	* petapp (U+E006): L<<611.0,96.0>--<611.0,96.0>>/B<<611.0,96.0>-<607.0,95.0>-<603.5,92.5>> = 14.036243467926484

	* petapp (U+E006): L<<612.0,379.0>--<610.0,384.0>>/B<<610.0,384.0>-<611.0,381.0>-<612.0,379.0>> = 3.366460663429615

	* petapp (U+E006): L<<613.0,374.0>--<612.0,377.0>>/B<<612.0,377.0>-<613.0,375.0>-<613.0,374.0>> = 8.130102354155916

	* petapp (U+E006): L<<615.0,369.0>--<614.0,372.0>>/B<<614.0,372.0>-<615.0,370.0>-<615.0,369.0>> = 8.130102354155916

	* petapp (U+E006): L<<616.0,379.0>--<614.0,384.0>>/B<<614.0,384.0>-<615.0,382.0>-<616.0,379.0>> = 4.763641690726066

	* petapp (U+E006): L<<629.0,340.0>--<627.0,343.0>>/B<<627.0,343.0>-<628.0,342.0>-<629.0,340.0>> = 11.309932474020227

	* petapp (U+E006): L<<640.0,343.0>--<638.0,346.0>>/B<<638.0,346.0>-<639.0,345.0>-<640.0,343.0>> = 11.309932474020227

	* petapp (U+E006): L<<643.0,318.0>--<641.0,321.0>>/B<<641.0,321.0>-<642.0,320.0>-<643.0,318.0>> = 11.309932474020227

	* petapp (U+E006): L<<657.0,433.0>--<658.0,436.0>>/B<<658.0,436.0>-<657.0,434.0>-<657.0,432.5>> = 8.13010235415587

	* petapp (U+E006): L<<661.0,383.0>--<660.0,386.0>>/B<<660.0,386.0>-<661.0,384.0>-<661.0,383.0>> = 8.130102354155916

	* petapp (U+E006): L<<666.0,452.0>--<669.0,456.0>>/B<<669.0,456.0>-<667.0,454.0>-<666.0,452.0>> = 8.13010235415596

	* petapp (U+E006): L<<672.0,140.0>--<670.0,137.0>>/B<<670.0,137.0>-<671.0,138.0>-<672.0,140.0>> = 11.309932474020227

	* petapp (U+E006): L<<682.0,143.0>--<679.0,141.0>>/B<<679.0,141.0>-<681.0,142.0>-<682.0,143.0>> = 7.125016348901757

	* petapp (U+E006): L<<686.0,162.0>--<685.0,159.0>>/B<<685.0,159.0>-<686.0,161.0>-<686.0,162.0>> = 8.130102354155916

	* petapp (U+E006): L<<689.0,167.0>--<687.0,164.0>>/B<<687.0,164.0>-<688.0,166.0>-<689.0,167.0>> = 7.125016348901705

	* petapp (U+E006): L<<689.0,256.0>--<690.0,253.0>>/B<<690.0,253.0>-<689.0,255.0>-<689.0,256.0>> = 8.13010235415587

	* petapp (U+E006): L<<691.0,251.0>--<692.0,248.0>>/B<<692.0,248.0>-<691.0,250.0>-<691.0,251.0>> = 8.13010235415587

	* petapp (U+E006): L<<700.0,480.0>--<703.0,481.0>>/B<<703.0,481.0>-<701.0,480.0>-<700.0,479.5>> = 8.13010235415587

	* petapp (U+E006): L<<705.0,482.0>--<708.0,483.0>>/B<<708.0,483.0>-<706.0,482.0>-<705.0,482.0>> = 8.13010235415587

	* petapp (U+E006): L<<708.0,293.0>--<705.0,294.0>>/B<<705.0,294.0>-<707.0,293.0>-<708.0,293.0>> = 8.130102354155916

	* petapp (U+E006): L<<728.0,285.0>--<725.0,286.0>>/B<<725.0,286.0>-<727.0,285.0>-<728.0,285.0>> = 8.130102354155916

	* petapp (U+E006): L<<761.0,8.0>--<763.0,5.0>>/B<<763.0,5.0>-<762.0,7.0>-<761.0,8.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<581.0,372.0>-<585.0,368.0>-<588.0,366.0>>/L<<588.0,366.0>--<581.0,372.0>> = 6.911227119024609

	* petapp.minimal (U+E007): B<<631.0,435.0>-<631.0,433.0>-<632.0,430.0>>/L<<632.0,430.0>--<631.0,435.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<632.0,481.0>-<632.0,480.0>-<631.0,478.0>>/L<<631.0,478.0>--<632.0,481.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<645.0,399.0>-<646.0,397.0>-<647.0,396.0>>/L<<647.0,396.0>--<645.0,399.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<646.0,510.0>-<645.0,508.0>-<644.0,507.0>>/L<<644.0,507.0>--<646.0,510.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<676.0,538.0>-<674.0,537.0>-<673.0,536.0>>/L<<673.0,536.0>--<676.0,538.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<700.0,247.0>-<699.0,248.0>-<698.0,250.0>>/L<<698.0,250.0>--<700.0,247.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<714.0,147.0>-<714.0,148.0>-<713.0,150.0>>/L<<713.0,150.0>--<714.0,147.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<720.0,137.0>-<719.0,139.0>-<718.0,140.0>>/L<<718.0,140.0>--<720.0,137.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<732.0,185.0>-<731.0,187.0>-<731.0,189.0>>/L<<731.0,189.0>--<732.0,185.0>> = 14.036243467926484

	* petapp.minimal (U+E007): B<<743.0,53.0>-<743.0,54.0>-<742.0,56.0>>/L<<742.0,56.0>--<743.0,53.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<212.0,538.0>--<212.0,800.0>>/B<<212.0,800.0>-<214.0,769.0>-<226.5,742.0>> = 3.6913859864512575

	* petapp.minimal (U+E007): L<<628.0,462.0>--<629.0,465.0>>/B<<629.0,465.0>-<628.0,463.0>-<628.0,462.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<630.0,473.0>--<631.0,476.0>>/B<<631.0,476.0>-<630.0,474.0>-<630.0,473.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<632.0,430.0>--<631.0,435.0>>/B<<631.0,435.0>-<631.0,433.0>-<632.0,430.0>> = 11.309932474020227

	* petapp.minimal (U+E007): L<<637.0,222.0>--<640.0,221.0>>/B<<640.0,221.0>-<638.0,222.0>-<637.0,222.5>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<639.0,498.0>--<640.0,501.0>>/B<<640.0,501.0>-<639.0,499.0>-<639.0,498.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<644.0,507.0>--<646.0,510.0>>/B<<646.0,510.0>-<645.0,508.0>-<644.0,507.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<647.0,396.0>--<645.0,399.0>>/B<<645.0,399.0>-<646.0,397.0>-<647.0,396.0>> = 7.125016348901705

	* petapp.minimal (U+E007): L<<673.0,536.0>--<676.0,538.0>>/B<<676.0,538.0>-<674.0,537.0>-<673.0,536.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<682.0,542.0>--<685.0,543.0>>/B<<685.0,543.0>-<683.0,542.0>-<682.0,542.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<687.0,544.0>--<690.0,545.0>>/B<<690.0,545.0>-<688.0,544.0>-<687.0,544.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<698.0,250.0>--<700.0,247.0>>/B<<700.0,247.0>-<699.0,248.0>-<698.0,250.0>> = 11.309932474020195

	* petapp.minimal (U+E007): L<<718.0,218.0>--<719.0,215.0>>/B<<719.0,215.0>-<718.0,217.0>-<718.0,218.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<731.0,113.0>--<732.0,110.0>>/B<<732.0,110.0>-<731.0,112.0>-<731.0,113.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<740.0,156.0>--<739.0,160.0>>/B<<739.0,160.0>-<740.0,153.0>-<740.0,156.0>> = 5.906141113770497

	* petapp.minimal (U+E007): L<<744.0,137.0>--<743.0,140.0>>/B<<743.0,140.0>-<744.0,138.0>-<744.0,137.0>> = 8.130102354155916

	* petapp.minimal (U+E007): L<<746.0,123.0>--<747.0,120.0>>/B<<747.0,120.0>-<746.0,122.0>-<746.0,123.0>> = 8.13010235415587

	* petapp.wpda (U+E008): B<<485.0,2.0>-<482.0,5.0>-<482.0,6.0>>/L<<482.0,6.0>--<481.0,1.0>> = 11.309932474020227

	* petapp.wpda (U+E008): L<<185.0,222.0>--<180.0,218.0>>/B<<180.0,218.0>-<182.0,219.0>-<183.0,218.0>> = 12.094757077012058

	* pisafe (U+E010): B<<175.0,538.0>-<175.0,536.0>-<174.0,534.0>>/L<<174.0,534.0>--<175.0,538.0>> = 12.528807709151492

	* pisafe (U+E010): B<<190.0,573.0>-<189.0,572.0>-<188.0,570.0>>/L<<188.0,570.0>--<190.0,573.0>> = 7.125016348901757

	* pisafe (U+E010): B<<211.0,602.0>-<210.0,600.0>-<208.0,598.0>>/L<<208.0,598.0>--<211.0,602.0>> = 8.13010235415596

	* pisafe (U+E010): B<<784.0,594.0>-<783.0,596.0>-<782.0,597.0>>/L<<782.0,597.0>--<784.0,594.0>> = 11.309932474020195

	* pisafe (U+E010): B<<797.0,577.0>-<796.0,579.0>-<795.0,580.0>>/L<<795.0,580.0>--<797.0,577.0>> = 11.309932474020195

	* pisafe (U+E010): B<<816.0,530.0>-<816.0,532.0>-<815.0,534.0>>/L<<815.0,534.0>--<816.0,530.0>> = 12.528807709151492

	* pisafe (U+E010): B<<820.0,515.0>-<820.0,516.0>-<819.0,518.0>>/L<<819.0,518.0>--<820.0,515.0>> = 8.13010235415587

	* pisafe (U+E010): L<<174.0,534.0>--<175.0,538.0>>/B<<175.0,538.0>-<175.0,536.0>-<174.0,534.0>> = 14.036243467926484

	* pisafe (U+E010): L<<188.0,570.0>--<190.0,573.0>>/B<<190.0,573.0>-<189.0,572.0>-<188.0,570.0>> = 11.309932474020195

	* pisafe (U+E010): L<<208.0,598.0>--<211.0,602.0>>/B<<211.0,602.0>-<210.0,600.0>-<208.0,598.0>> = 10.304846468766044

	* pisafe (U+E010): L<<750.0,626.0>--<754.0,623.0>>/B<<754.0,623.0>-<752.0,624.0>-<750.0,626.0>> = 10.304846468766009

	* pisafe (U+E010): L<<782.0,597.0>--<784.0,594.0>>/B<<784.0,594.0>-<783.0,596.0>-<782.0,597.0>> = 7.125016348901757

	* pisafe (U+E010): L<<795.0,580.0>--<797.0,577.0>>/B<<797.0,577.0>-<796.0,579.0>-<795.0,580.0>> = 7.125016348901757

	* pisafe (U+E010): L<<815.0,534.0>--<816.0,530.0>>/B<<816.0,530.0>-<816.0,532.0>-<815.0,534.0>> = 14.036243467926484 

	* pisafe (U+E010): L<<817.0,528.0>--<818.0,525.0>>/B<<818.0,525.0>-<817.0,527.0>-<817.0,528.0>> = 8.13010235415587 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[18] PitagonSansText-Regular.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check OFL body text is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text">com.google.fonts/check/license/OFL_body_text</a>)</summary><div>


* 🔥 **FAIL** The OFL.txt body text is incorrect. Please use https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt as a template. You should only modify the first line. [code: incorrect-ofl-body-text]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ
at: https://scripts.sil.org/OFL." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks">com.google.fonts/check/name/line_breaks</a>)</summary><div>


* 🔥 **FAIL** Name entry DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1294, but got 1214 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.11, while a newer 0.8.13 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'Pita' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
</div></details><details><summary>⚠ <b>WARN:</b> Description strings in the name table must not exceed 200 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/description_max_length">com.google.fonts/check/name/description_max_length</a>)</summary><div>


* ⚠ **WARN** A few name table entries with ID=10 (NameID.DESCRIPTION) are longer than 200 characters. Please check whether those entries are copyright notices mistakenly stored in the description string entries by a bug in an old FontLab version. If that's the case, then such copyright notices must be removed from these entries. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- dotlessi.wide 

	- registered.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* petapp (U+E006): L<<282.0,304.0>--<312.0,286.0>> -> L<<312.0,286.0>--<339.0,271.0>>

	* petapp (U+E006): L<<312.0,333.0>--<273.0,356.0>> -> L<<273.0,356.0>--<257.0,365.0>>

	* petapp (U+E006): L<<355.0,309.0>--<312.0,333.0>> -> L<<312.0,333.0>--<273.0,356.0>>

	* petapp (U+E006): L<<371.0,299.0>--<355.0,309.0>> -> L<<355.0,309.0>--<312.0,333.0>>

	* petapp (U+E006): L<<371.0,640.0>--<467.0,585.0>> -> L<<467.0,585.0>--<515.0,556.0>>

	* petapp (U+E006): L<<373.0,298.0>--<371.0,299.0>> -> L<<371.0,299.0>--<355.0,309.0>>

	* petapp (U+E006): L<<426.0,268.0>--<373.0,298.0>> -> L<<373.0,298.0>--<371.0,299.0>>

	* petapp (U+E006): L<<467.0,585.0>--<515.0,556.0>> -> L<<515.0,556.0>--<534.0,545.0>>

	* petapp (U+E006): L<<468.0,243.0>--<426.0,268.0>> -> L<<426.0,268.0>--<373.0,298.0>>

	* petapp (U+E006): L<<474.0,240.0>--<468.0,243.0>> -> L<<468.0,243.0>--<426.0,268.0>>

	* petapp (U+E006): L<<498.0,226.0>--<474.0,240.0>> -> L<<474.0,240.0>--<468.0,243.0>>

	* petapp (U+E006): L<<505.0,222.0>--<498.0,226.0>> -> L<<498.0,226.0>--<474.0,240.0>>

	* petapp (U+E006): L<<691.0,61.0>--<692.0,60.0>> -> L<<692.0,60.0>--<696.0,56.0>>

	* petapp (U+E006): L<<721.0,485.0>--<725.0,485.0>> -> L<<725.0,485.0>--<764.0,485.0>>

	* petapp.minimal (U+E007): L<<264.0,373.0>--<351.0,339.0>> -> L<<351.0,339.0>--<432.0,305.0>>

	* petapp.minimal (U+E007): L<<351.0,339.0>--<432.0,305.0>> -> L<<432.0,305.0>--<448.0,299.0>>

	* petapp.minimal (U+E007): L<<381.0,352.0>--<331.0,376.0>> -> L<<331.0,376.0>--<305.0,390.0>>

	* petapp.minimal (U+E007): L<<432.0,305.0>--<448.0,299.0>> -> L<<448.0,299.0>--<504.0,276.0>>

	* petapp.minimal (U+E007): L<<432.0,326.0>--<381.0,352.0>> -> L<<381.0,352.0>--<331.0,376.0>>

	* petapp.minimal (U+E007): L<<435.0,187.0>--<405.0,192.0>> -> L<<405.0,192.0>--<304.0,211.0>>

	* petapp.minimal (U+E007): L<<448.0,299.0>--<504.0,276.0>> -> L<<504.0,276.0>--<612.0,232.0>>

	* petapp.minimal (U+E007): L<<455.0,314.0>--<432.0,326.0>> -> L<<432.0,326.0>--<381.0,352.0>>

	* petapp.minimal (U+E007): L<<504.0,175.0>--<435.0,187.0>> -> L<<435.0,187.0>--<405.0,192.0>>

	* petapp.minimal (U+E007): L<<504.0,276.0>--<612.0,232.0>> -> L<<612.0,232.0>--<621.0,229.0>>

	* petapp.minimal (U+E007): L<<504.0,289.0>--<455.0,314.0>> -> L<<455.0,314.0>--<432.0,326.0>>

	* petapp.minimal (U+E007): L<<588.0,160.0>--<504.0,175.0>> -> L<<504.0,175.0>--<435.0,187.0>>

	* petapp.minimal (U+E007): L<<621.0,229.0>--<504.0,289.0>> -> L<<504.0,289.0>--<455.0,314.0>>

	* petapp.minimal (U+E007): L<<742.0,30.0>--<742.0,31.0>> -> L<<742.0,31.0>--<742.0,32.0>>

	* petapp.minimal (U+E007): L<<743.0,33.0>--<743.0,34.0>> -> L<<743.0,34.0>--<743.0,36.0>>

	* petapp.minimal (U+E007): L<<743.0,34.0>--<743.0,36.0>> -> L<<743.0,36.0>--<743.0,37.0>>

	* petapp.minimal (U+E007): L<<747.0,73.0>--<746.0,63.0>> -> L<<746.0,63.0>--<743.0,38.0>>

	* petapp.minimal (U+E007): L<<747.0,74.0>--<747.0,73.0>> -> L<<747.0,73.0>--<746.0,63.0>>

	* petapp.minimal (U+E007): L<<752.0,131.0>--<747.0,74.0>> -> L<<747.0,74.0>--<747.0,73.0>>

	* petapp.minimal (U+E007): L<<754.0,162.0>--<752.0,131.0>> -> L<<752.0,131.0>--<747.0,74.0>>

	* petapp.minimal (U+E007): L<<755.0,175.0>--<754.0,162.0>> -> L<<754.0,162.0>--<752.0,131.0>>

	* petapp.minimal (U+E007): L<<757.0,196.0>--<755.0,175.0>> -> L<<755.0,175.0>--<754.0,162.0>>

	* petapp.minimal (U+E007): L<<758.0,210.0>--<757.0,196.0>> -> L<<757.0,196.0>--<755.0,175.0>>

	* petapp.minimal (U+E007): L<<758.0,213.0>--<758.0,210.0>> -> L<<758.0,210.0>--<757.0,196.0>>

	* petapp.wpda (U+E008): L<<640.0,140.0>--<627.0,132.0>> -> L<<627.0,132.0>--<618.0,127.0>>

	* piads (U+E001): L<<112.0,541.0>--<116.0,544.0>> -> L<<116.0,544.0>--<445.0,782.0>>

	* piads (U+E001): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<878.0,541.0>>

	* picall (U+E009): L<<112.0,541.0>--<116.0,544.0>> -> L<<116.0,544.0>--<445.0,782.0>>

	* picall (U+E009): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<878.0,541.0>>

	* pioffice (U+E002): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<877.0,542.0>>

	* pisafe (U+E010): L<<167.0,362.0>--<167.0,491.0>> -> L<<167.0,491.0>--<167.0,494.0>>

	* pisafe (U+E010): L<<203.0,695.0>--<239.0,708.0>> -> L<<239.0,708.0>--<389.0,762.0>>

	* pisafe (U+E010): L<<239.0,708.0>--<389.0,762.0>> -> L<<389.0,762.0>--<494.0,800.0>>

	* pisafe (U+E010): L<<495.0,800.0>--<600.0,762.0>> -> L<<600.0,762.0>--<750.0,708.0>>

	* pisafe (U+E010): L<<600.0,762.0>--<750.0,708.0>> -> L<<750.0,708.0>--<786.0,695.0>>

	* pisign (U+E005): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<877.0,542.0>>

	* pitagon (U+E000): L<<112.0,543.0>--<116.0,546.0>> -> L<<116.0,546.0>--<445.0,784.0>>

	* pitagon (U+E000): L<<209.0,62.0>--<84.0,446.0>> -> L<<84.0,446.0>--<82.0,452.0>>

	* pitagon (U+E000): L<<547.0,784.0>--<874.0,546.0>> -> L<<874.0,546.0>--<878.0,543.0>>

	* pitagram (U+E003): L<<813.0,512.0>--<810.0,514.0>> -> L<<810.0,514.0>--<537.0,711.0>>

	* piweb (U+E004): L<<813.0,512.0>--<810.0,514.0>> -> L<<810.0,514.0>--<537.0,711.0>>

	* sparks (U+E011): L<<100.0,798.0>--<103.0,797.0>> -> L<<103.0,797.0>--<198.0,762.0>>

	* sparks (U+E011): L<<103.0,797.0>--<198.0,762.0>> -> L<<198.0,762.0>--<209.0,759.0>>

	* sparks (U+E011): L<<198.0,762.0>--<209.0,759.0>> -> L<<209.0,759.0>--<400.0,690.0>>

	* sparks (U+E011): L<<209.0,759.0>--<400.0,690.0>> -> L<<400.0,690.0>--<431.0,680.0>>

	* sparks (U+E011): L<<291.0,596.0>--<363.0,534.0>> -> L<<363.0,534.0>--<382.0,516.0>>

	* sparks (U+E011): L<<381.0,366.0>--<383.0,367.0>> -> L<<383.0,367.0>--<486.0,429.0>>

	* sparks (U+E011): L<<383.0,367.0>--<486.0,429.0>> -> L<<486.0,429.0>--<488.0,430.0>>

	* sparks (U+E011): L<<409.0,102.0>--<98.0,641.0>> -> L<<98.0,641.0>--<47.0,731.0>>

	* sparks (U+E011): L<<440.0,659.0>--<436.0,649.0>> -> L<<436.0,649.0>--<434.0,643.0>>

	* sparks (U+E011): L<<454.0,24.0>--<409.0,102.0>> -> L<<409.0,102.0>--<98.0,641.0>>

	* sparks (U+E011): L<<504.0,429.0>--<606.0,367.0>> -> L<<606.0,367.0>--<608.0,366.0>>

	* sparks (U+E011): L<<558.0,680.0>--<596.0,694.0>> -> L<<596.0,694.0>--<780.0,759.0>>

	* sparks (U+E011): L<<579.0,101.0>--<550.0,51.0>> -> L<<550.0,51.0>--<535.0,24.0>>

	* sparks (U+E011): L<<596.0,694.0>--<780.0,759.0>> -> L<<780.0,759.0>--<807.0,768.0>>

	* sparks (U+E011): L<<607.0,516.0>--<627.0,534.0>> -> L<<627.0,534.0>--<699.0,596.0>>

	* sparks (U+E011): L<<614.0,629.0>--<577.0,632.0>> -> L<<577.0,632.0>--<568.0,633.0>>

	* sparks (U+E011): L<<655.0,626.0>--<614.0,629.0>> -> L<<614.0,629.0>--<577.0,632.0>>

	* sparks (U+E011): L<<656.0,626.0>--<655.0,626.0>> -> L<<655.0,626.0>--<614.0,629.0>>

	* sparks (U+E011): L<<690.0,623.0>--<656.0,626.0>> -> L<<656.0,626.0>--<655.0,626.0>>

	* sparks (U+E011): L<<691.0,623.0>--<690.0,623.0>> -> L<<690.0,623.0>--<656.0,626.0>>

	* sparks (U+E011): L<<750.0,397.0>--<579.0,101.0>> -> L<<579.0,101.0>--<550.0,51.0>>

	* sparks (U+E011): L<<780.0,759.0>--<807.0,768.0>> -> L<<807.0,768.0>--<886.0,797.0>>

	* sparks (U+E011): L<<897.0,652.0>--<750.0,397.0>> -> L<<750.0,397.0>--<579.0,101.0>>

	* sparks (U+E011): L<<942.0,730.0>--<897.0,652.0>> -> L<<897.0,652.0>--<750.0,397.0>> 

	* sparks (U+E011): L<<943.0,732.0>--<942.0,730.0>> -> L<<942.0,730.0>--<897.0,652.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* petapp (U+E006): B<<289.0,471.0>-<290.0,469.0>-<291.0,468.0>>/L<<291.0,468.0>--<289.0,471.0>> = 11.309932474020227

	* petapp (U+E006): B<<295.0,293.0>-<289.0,300.0>-<282.0,304.0>>/L<<282.0,304.0>--<312.0,286.0>> = 1.2188752351307344

	* petapp (U+E006): B<<328.0,429.0>-<329.0,428.0>-<331.0,427.0>>/L<<331.0,427.0>--<328.0,429.0>> = 7.125016348901757

	* petapp (U+E006): B<<415.0,76.0>-<416.0,76.0>-<418.0,75.0>>/L<<418.0,75.0>--<415.0,76.0>> = 8.130102354155916

	* petapp (U+E006): B<<424.0,71.0>-<425.0,71.0>-<427.0,70.0>>/L<<427.0,70.0>--<424.0,71.0>> = 8.130102354155916

	* petapp (U+E006): B<<439.0,65.0>-<440.0,65.0>-<442.0,64.0>>/L<<442.0,64.0>--<439.0,65.0>> = 8.130102354155916

	* petapp (U+E006): B<<483.0,64.0>-<484.0,64.0>-<486.0,65.0>>/L<<486.0,65.0>--<483.0,64.0>> = 8.130102354155916

	* petapp (U+E006): B<<513.0,65.0>-<515.0,65.0>-<517.0,66.0>>/L<<517.0,66.0>--<513.0,65.0>> = 12.528807709151463

	* petapp (U+E006): B<<519.0,66.0>-<521.0,66.0>-<523.0,67.0>>/L<<523.0,67.0>--<519.0,66.0>> = 12.528807709151463

	* petapp (U+E006): B<<529.0,68.0>-<528.0,68.0>-<526.0,67.0>>/L<<526.0,67.0>--<529.0,68.0>> = 8.13010235415587

	* petapp (U+E006): B<<536.0,192.0>-<535.0,194.0>-<534.0,195.0>>/L<<534.0,195.0>--<536.0,192.0>> = 11.309932474020195

	* petapp (U+E006): B<<536.0,69.0>-<534.0,69.0>-<532.0,68.0>>/L<<532.0,68.0>--<536.0,69.0>> = 12.528807709151492

	* petapp (U+E006): B<<537.0,308.0>-<536.0,309.0>-<534.0,310.0>>/L<<534.0,310.0>--<537.0,308.0>> = 7.125016348901757

	* petapp (U+E006): B<<539.0,108.0>-<540.0,109.0>-<541.0,111.0>>/L<<541.0,111.0>--<539.0,108.0>> = 7.125016348901705

	* petapp (U+E006): B<<539.0,438.0>-<538.0,439.0>-<536.0,440.0>>/L<<536.0,440.0>--<539.0,438.0>> = 7.125016348901757

	* petapp (U+E006): B<<545.0,123.0>-<546.0,125.0>-<546.0,127.0>>/L<<546.0,127.0>--<545.0,123.0>> = 14.036243467926484

	* petapp (U+E006): B<<548.0,432.0>-<547.0,433.0>-<545.0,434.0>>/L<<545.0,434.0>--<548.0,432.0>> = 7.125016348901757

	* petapp (U+E006): B<<548.0,72.0>-<549.0,72.0>-<551.0,73.0>>/L<<551.0,73.0>--<548.0,72.0>> = 8.130102354155916

	* petapp (U+E006): B<<575.0,404.0>-<576.0,403.0>-<577.0,401.0>>/L<<577.0,401.0>--<575.0,404.0>> = 7.125016348901705

	* petapp (U+E006): B<<587.0,380.0>-<587.0,382.0>-<586.0,384.0>>/L<<586.0,384.0>--<587.0,380.0>> = 12.528807709151492

	* petapp (U+E006): B<<610.0,384.0>-<611.0,381.0>-<612.0,379.0>>/L<<612.0,379.0>--<610.0,384.0>> = 4.763641690726066

	* petapp (U+E006): B<<614.0,384.0>-<615.0,382.0>-<616.0,379.0>>/L<<616.0,379.0>--<614.0,384.0>> = 3.366460663429615

	* petapp (U+E006): B<<627.0,343.0>-<628.0,342.0>-<629.0,340.0>>/L<<629.0,340.0>--<627.0,343.0>> = 7.125016348901705

	* petapp (U+E006): B<<633.0,334.0>-<633.0,333.0>-<634.0,331.0>>/L<<634.0,331.0>--<633.0,334.0>> = 8.130102354155916

	* petapp (U+E006): B<<638.0,346.0>-<639.0,345.0>-<640.0,343.0>>/L<<640.0,343.0>--<638.0,346.0>> = 7.125016348901705

	* petapp (U+E006): B<<641.0,321.0>-<642.0,320.0>-<643.0,318.0>>/L<<643.0,318.0>--<641.0,321.0>> = 7.125016348901705

	* petapp (U+E006): B<<669.0,316.0>-<670.0,315.0>-<672.0,314.0>>/L<<672.0,314.0>--<669.0,316.0>> = 7.125016348901757

	* petapp (U+E006): B<<669.0,456.0>-<667.0,454.0>-<666.0,452.0>>/L<<666.0,452.0>--<669.0,456.0>> = 10.304846468766044

	* petapp (U+E006): B<<670.0,137.0>-<671.0,138.0>-<672.0,140.0>>/L<<672.0,140.0>--<670.0,137.0>> = 7.125016348901705

	* petapp (U+E006): B<<679.0,141.0>-<681.0,142.0>-<682.0,143.0>>/L<<682.0,143.0>--<679.0,141.0>> = 11.309932474020195

	* petapp (U+E006): B<<687.0,164.0>-<688.0,166.0>-<689.0,167.0>>/L<<689.0,167.0>--<687.0,164.0>> = 11.309932474020227

	* petapp (U+E006): B<<713.0,484.0>-<712.0,484.0>-<710.0,483.0>>/L<<710.0,483.0>--<713.0,484.0>> = 8.13010235415587

	* petapp (U+E006): B<<763.0,5.0>-<762.0,7.0>-<761.0,8.0>>/L<<761.0,8.0>--<763.0,5.0>> = 11.309932474020195

	* petapp (U+E006): L<<274.0,517.0>--<273.0,520.0>>/B<<273.0,520.0>-<274.0,518.0>-<274.0,517.0>> = 8.130102354155916

	* petapp (U+E006): L<<280.0,491.0>--<279.0,494.0>>/B<<279.0,494.0>-<280.0,492.0>-<280.0,491.0>> = 8.130102354155916

	* petapp (U+E006): L<<291.0,468.0>--<289.0,471.0>>/B<<289.0,471.0>-<290.0,469.0>-<291.0,468.0>> = 7.125016348901705

	* petapp (U+E006): L<<296.0,459.0>--<295.0,462.0>>/B<<295.0,462.0>-<296.0,460.0>-<296.0,459.0>> = 8.130102354155916

	* petapp (U+E006): L<<312.0,442.0>--<308.0,445.0>>/B<<308.0,445.0>-<310.0,444.0>-<312.0,442.0>> = 10.304846468766009

	* petapp (U+E006): L<<331.0,427.0>--<328.0,429.0>>/B<<328.0,429.0>-<329.0,428.0>-<331.0,427.0>> = 11.309932474020195

	* petapp (U+E006): L<<380.0,128.0>--<379.0,131.0>>/B<<379.0,131.0>-<380.0,129.0>-<380.0,128.0>> = 8.130102354155916

	* petapp (U+E006): L<<387.0,108.0>--<386.0,111.0>>/B<<386.0,111.0>-<387.0,109.0>-<387.0,108.0>> = 8.130102354155916

	* petapp (U+E006): L<<499.0,225.0>--<505.0,222.0>>/L<<505.0,222.0>--<498.0,226.0>> = 3.1798301198640497

	* petapp (U+E006): L<<504.0,71.0>--<499.0,69.0>>/B<<499.0,69.0>-<502.0,71.0>-<504.0,71.0>> = 11.888658039627936

	* petapp (U+E006): L<<517.0,66.0>--<513.0,65.0>>/B<<513.0,65.0>-<515.0,65.0>-<517.0,66.0>> = 14.036243467926484

	* petapp (U+E006): L<<523.0,67.0>--<519.0,66.0>>/B<<519.0,66.0>-<521.0,66.0>-<523.0,67.0>> = 14.036243467926484

	* petapp (U+E006): L<<532.0,68.0>--<536.0,69.0>>/B<<536.0,69.0>-<534.0,69.0>-<532.0,68.0>> = 14.036243467926484

	* petapp (U+E006): L<<534.0,195.0>--<536.0,192.0>>/B<<536.0,192.0>-<535.0,194.0>-<534.0,195.0>> = 7.125016348901757

	* petapp (U+E006): L<<534.0,310.0>--<537.0,308.0>>/B<<537.0,308.0>-<536.0,309.0>-<534.0,310.0>> = 11.309932474020227

	* petapp (U+E006): L<<536.0,440.0>--<539.0,438.0>>/B<<539.0,438.0>-<538.0,439.0>-<536.0,440.0>> = 11.309932474020227

	* petapp (U+E006): L<<541.0,111.0>--<539.0,108.0>>/B<<539.0,108.0>-<540.0,109.0>-<541.0,111.0>> = 11.309932474020227

	* petapp (U+E006): L<<541.0,70.0>--<545.0,71.0>>/B<<545.0,71.0>-<540.0,70.0>-<541.0,70.0>> = 2.726310993906212

	* petapp (U+E006): L<<542.0,181.0>--<543.0,178.0>>/B<<543.0,178.0>-<542.0,180.0>-<542.0,181.0>> = 8.13010235415587

	* petapp (U+E006): L<<545.0,434.0>--<548.0,432.0>>/B<<548.0,432.0>-<547.0,433.0>-<545.0,434.0>> = 11.309932474020227

	* petapp (U+E006): L<<546.0,127.0>--<545.0,123.0>>/B<<545.0,123.0>-<546.0,125.0>-<546.0,127.0>> = 12.528807709151492

	* petapp (U+E006): L<<556.0,74.0>--<553.0,73.0>>/B<<553.0,73.0>-<555.0,74.0>-<556.0,74.0>> = 8.130102354155916

	* petapp (U+E006): L<<577.0,401.0>--<575.0,404.0>>/B<<575.0,404.0>-<576.0,403.0>-<577.0,401.0>> = 11.309932474020227

	* petapp (U+E006): L<<583.0,256.0>--<584.0,252.0>>/B<<584.0,252.0>-<584.0,254.0>-<583.0,256.0>> = 14.036243467926484

	* petapp (U+E006): L<<586.0,384.0>--<587.0,380.0>>/B<<587.0,380.0>-<587.0,382.0>-<586.0,384.0>> = 14.036243467926484

	* petapp (U+E006): L<<598.0,432.0>--<599.0,429.0>>/B<<599.0,429.0>-<598.0,431.0>-<598.0,432.0>> = 8.13010235415587

	* petapp (U+E006): L<<602.0,122.0>--<601.0,125.0>>/B<<601.0,125.0>-<602.0,123.0>-<602.0,122.0>> = 8.130102354155916

	* petapp (U+E006): L<<611.0,96.0>--<611.0,96.0>>/B<<611.0,96.0>-<607.0,95.0>-<603.5,92.5>> = 14.036243467926484

	* petapp (U+E006): L<<612.0,379.0>--<610.0,384.0>>/B<<610.0,384.0>-<611.0,381.0>-<612.0,379.0>> = 3.366460663429615

	* petapp (U+E006): L<<613.0,374.0>--<612.0,377.0>>/B<<612.0,377.0>-<613.0,375.0>-<613.0,374.0>> = 8.130102354155916

	* petapp (U+E006): L<<615.0,369.0>--<614.0,372.0>>/B<<614.0,372.0>-<615.0,370.0>-<615.0,369.0>> = 8.130102354155916

	* petapp (U+E006): L<<616.0,379.0>--<614.0,384.0>>/B<<614.0,384.0>-<615.0,382.0>-<616.0,379.0>> = 4.763641690726066

	* petapp (U+E006): L<<629.0,340.0>--<627.0,343.0>>/B<<627.0,343.0>-<628.0,342.0>-<629.0,340.0>> = 11.309932474020227

	* petapp (U+E006): L<<640.0,343.0>--<638.0,346.0>>/B<<638.0,346.0>-<639.0,345.0>-<640.0,343.0>> = 11.309932474020227

	* petapp (U+E006): L<<643.0,318.0>--<641.0,321.0>>/B<<641.0,321.0>-<642.0,320.0>-<643.0,318.0>> = 11.309932474020227

	* petapp (U+E006): L<<657.0,433.0>--<658.0,436.0>>/B<<658.0,436.0>-<657.0,434.0>-<657.0,432.5>> = 8.13010235415587

	* petapp (U+E006): L<<661.0,383.0>--<660.0,386.0>>/B<<660.0,386.0>-<661.0,384.0>-<661.0,383.0>> = 8.130102354155916

	* petapp (U+E006): L<<666.0,452.0>--<669.0,456.0>>/B<<669.0,456.0>-<667.0,454.0>-<666.0,452.0>> = 8.13010235415596

	* petapp (U+E006): L<<672.0,140.0>--<670.0,137.0>>/B<<670.0,137.0>-<671.0,138.0>-<672.0,140.0>> = 11.309932474020227

	* petapp (U+E006): L<<682.0,143.0>--<679.0,141.0>>/B<<679.0,141.0>-<681.0,142.0>-<682.0,143.0>> = 7.125016348901757

	* petapp (U+E006): L<<686.0,162.0>--<685.0,159.0>>/B<<685.0,159.0>-<686.0,161.0>-<686.0,162.0>> = 8.130102354155916

	* petapp (U+E006): L<<689.0,167.0>--<687.0,164.0>>/B<<687.0,164.0>-<688.0,166.0>-<689.0,167.0>> = 7.125016348901705

	* petapp (U+E006): L<<689.0,256.0>--<690.0,253.0>>/B<<690.0,253.0>-<689.0,255.0>-<689.0,256.0>> = 8.13010235415587

	* petapp (U+E006): L<<691.0,251.0>--<692.0,248.0>>/B<<692.0,248.0>-<691.0,250.0>-<691.0,251.0>> = 8.13010235415587

	* petapp (U+E006): L<<700.0,480.0>--<703.0,481.0>>/B<<703.0,481.0>-<701.0,480.0>-<700.0,479.5>> = 8.13010235415587

	* petapp (U+E006): L<<705.0,482.0>--<708.0,483.0>>/B<<708.0,483.0>-<706.0,482.0>-<705.0,482.0>> = 8.13010235415587

	* petapp (U+E006): L<<708.0,293.0>--<705.0,294.0>>/B<<705.0,294.0>-<707.0,293.0>-<708.0,293.0>> = 8.130102354155916

	* petapp (U+E006): L<<728.0,285.0>--<725.0,286.0>>/B<<725.0,286.0>-<727.0,285.0>-<728.0,285.0>> = 8.130102354155916

	* petapp (U+E006): L<<761.0,8.0>--<763.0,5.0>>/B<<763.0,5.0>-<762.0,7.0>-<761.0,8.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<581.0,372.0>-<585.0,368.0>-<588.0,366.0>>/L<<588.0,366.0>--<581.0,372.0>> = 6.911227119024609

	* petapp.minimal (U+E007): B<<631.0,435.0>-<631.0,433.0>-<632.0,430.0>>/L<<632.0,430.0>--<631.0,435.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<632.0,481.0>-<632.0,480.0>-<631.0,478.0>>/L<<631.0,478.0>--<632.0,481.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<645.0,399.0>-<646.0,397.0>-<647.0,396.0>>/L<<647.0,396.0>--<645.0,399.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<646.0,510.0>-<645.0,508.0>-<644.0,507.0>>/L<<644.0,507.0>--<646.0,510.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<676.0,538.0>-<674.0,537.0>-<673.0,536.0>>/L<<673.0,536.0>--<676.0,538.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<700.0,247.0>-<699.0,248.0>-<698.0,250.0>>/L<<698.0,250.0>--<700.0,247.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<714.0,147.0>-<714.0,148.0>-<713.0,150.0>>/L<<713.0,150.0>--<714.0,147.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<720.0,137.0>-<719.0,139.0>-<718.0,140.0>>/L<<718.0,140.0>--<720.0,137.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<732.0,185.0>-<731.0,187.0>-<731.0,189.0>>/L<<731.0,189.0>--<732.0,185.0>> = 14.036243467926484

	* petapp.minimal (U+E007): B<<743.0,53.0>-<743.0,54.0>-<742.0,56.0>>/L<<742.0,56.0>--<743.0,53.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<212.0,538.0>--<212.0,800.0>>/B<<212.0,800.0>-<214.0,769.0>-<226.5,742.0>> = 3.6913859864512575

	* petapp.minimal (U+E007): L<<628.0,462.0>--<629.0,465.0>>/B<<629.0,465.0>-<628.0,463.0>-<628.0,462.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<630.0,473.0>--<631.0,476.0>>/B<<631.0,476.0>-<630.0,474.0>-<630.0,473.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<632.0,430.0>--<631.0,435.0>>/B<<631.0,435.0>-<631.0,433.0>-<632.0,430.0>> = 11.309932474020227

	* petapp.minimal (U+E007): L<<637.0,222.0>--<640.0,221.0>>/B<<640.0,221.0>-<638.0,222.0>-<637.0,222.5>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<639.0,498.0>--<640.0,501.0>>/B<<640.0,501.0>-<639.0,499.0>-<639.0,498.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<644.0,507.0>--<646.0,510.0>>/B<<646.0,510.0>-<645.0,508.0>-<644.0,507.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<647.0,396.0>--<645.0,399.0>>/B<<645.0,399.0>-<646.0,397.0>-<647.0,396.0>> = 7.125016348901705

	* petapp.minimal (U+E007): L<<673.0,536.0>--<676.0,538.0>>/B<<676.0,538.0>-<674.0,537.0>-<673.0,536.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<682.0,542.0>--<685.0,543.0>>/B<<685.0,543.0>-<683.0,542.0>-<682.0,542.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<687.0,544.0>--<690.0,545.0>>/B<<690.0,545.0>-<688.0,544.0>-<687.0,544.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<698.0,250.0>--<700.0,247.0>>/B<<700.0,247.0>-<699.0,248.0>-<698.0,250.0>> = 11.309932474020195

	* petapp.minimal (U+E007): L<<718.0,218.0>--<719.0,215.0>>/B<<719.0,215.0>-<718.0,217.0>-<718.0,218.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<731.0,113.0>--<732.0,110.0>>/B<<732.0,110.0>-<731.0,112.0>-<731.0,113.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<740.0,156.0>--<739.0,160.0>>/B<<739.0,160.0>-<740.0,153.0>-<740.0,156.0>> = 5.906141113770497

	* petapp.minimal (U+E007): L<<744.0,137.0>--<743.0,140.0>>/B<<743.0,140.0>-<744.0,138.0>-<744.0,137.0>> = 8.130102354155916

	* petapp.minimal (U+E007): L<<746.0,123.0>--<747.0,120.0>>/B<<747.0,120.0>-<746.0,122.0>-<746.0,123.0>> = 8.13010235415587

	* petapp.wpda (U+E008): B<<485.0,2.0>-<482.0,5.0>-<482.0,6.0>>/L<<482.0,6.0>--<481.0,1.0>> = 11.309932474020227

	* petapp.wpda (U+E008): L<<185.0,222.0>--<180.0,218.0>>/B<<180.0,218.0>-<182.0,219.0>-<183.0,218.0>> = 12.094757077012058

	* pisafe (U+E010): B<<175.0,538.0>-<175.0,536.0>-<174.0,534.0>>/L<<174.0,534.0>--<175.0,538.0>> = 12.528807709151492

	* pisafe (U+E010): B<<190.0,573.0>-<189.0,572.0>-<188.0,570.0>>/L<<188.0,570.0>--<190.0,573.0>> = 7.125016348901757

	* pisafe (U+E010): B<<211.0,602.0>-<210.0,600.0>-<208.0,598.0>>/L<<208.0,598.0>--<211.0,602.0>> = 8.13010235415596

	* pisafe (U+E010): B<<784.0,594.0>-<783.0,596.0>-<782.0,597.0>>/L<<782.0,597.0>--<784.0,594.0>> = 11.309932474020195

	* pisafe (U+E010): B<<797.0,577.0>-<796.0,579.0>-<795.0,580.0>>/L<<795.0,580.0>--<797.0,577.0>> = 11.309932474020195

	* pisafe (U+E010): B<<816.0,530.0>-<816.0,532.0>-<815.0,534.0>>/L<<815.0,534.0>--<816.0,530.0>> = 12.528807709151492

	* pisafe (U+E010): B<<820.0,515.0>-<820.0,516.0>-<819.0,518.0>>/L<<819.0,518.0>--<820.0,515.0>> = 8.13010235415587

	* pisafe (U+E010): L<<174.0,534.0>--<175.0,538.0>>/B<<175.0,538.0>-<175.0,536.0>-<174.0,534.0>> = 14.036243467926484

	* pisafe (U+E010): L<<188.0,570.0>--<190.0,573.0>>/B<<190.0,573.0>-<189.0,572.0>-<188.0,570.0>> = 11.309932474020195

	* pisafe (U+E010): L<<208.0,598.0>--<211.0,602.0>>/B<<211.0,602.0>-<210.0,600.0>-<208.0,598.0>> = 10.304846468766044

	* pisafe (U+E010): L<<750.0,626.0>--<754.0,623.0>>/B<<754.0,623.0>-<752.0,624.0>-<750.0,626.0>> = 10.304846468766009

	* pisafe (U+E010): L<<782.0,597.0>--<784.0,594.0>>/B<<784.0,594.0>-<783.0,596.0>-<782.0,597.0>> = 7.125016348901757

	* pisafe (U+E010): L<<795.0,580.0>--<797.0,577.0>>/B<<797.0,577.0>-<796.0,579.0>-<795.0,580.0>> = 7.125016348901757

	* pisafe (U+E010): L<<815.0,534.0>--<816.0,530.0>>/B<<816.0,530.0>-<816.0,532.0>-<815.0,534.0>> = 14.036243467926484 

	* pisafe (U+E010): L<<817.0,528.0>--<818.0,525.0>>/B<<818.0,525.0>-<817.0,527.0>-<817.0,528.0>> = 8.13010235415587 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[19] PitagonSansText-LightItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check OFL body text is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text">com.google.fonts/check/license/OFL_body_text</a>)</summary><div>


* 🔥 **FAIL** The OFL.txt body text is incorrect. Please use https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt as a template. You should only modify the first line. [code: incorrect-ofl-body-text]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ
at: https://scripts.sil.org/OFL." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks">com.google.fonts/check/name/line_breaks</a>)</summary><div>


* 🔥 **FAIL** Name entry DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1294, but got 1214 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.11, while a newer 0.8.13 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'Pita' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
</div></details><details><summary>⚠ <b>WARN:</b> Description strings in the name table must not exceed 200 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/description_max_length">com.google.fonts/check/name/description_max_length</a>)</summary><div>


* ⚠ **WARN** A few name table entries with ID=10 (NameID.DESCRIPTION) are longer than 200 characters. Please check whether those entries are copyright notices mistakenly stored in the description string entries by a bug in an old FontLab version. If that's the case, then such copyright notices must be removed from these entries. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Pitagon Sans Text Light' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- periodcentered.001 

	- registered.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni0200	Contours detected: 3	Expected: 4

	- Glyph name: uni0201	Contours detected: 3	Expected: 4

	- Glyph name: uni0204	Contours detected: 2	Expected: 3

	- Glyph name: uni0205	Contours detected: 3	Expected: 4

	- Glyph name: uni0208	Contours detected: 2	Expected: 3

	- Glyph name: uni0209	Contours detected: 2	Expected: 3

	- Glyph name: uni020C	Contours detected: 3	Expected: 4

	- Glyph name: uni020D	Contours detected: 3	Expected: 4

	- Glyph name: uni0210	Contours detected: 3	Expected: 4

	- Glyph name: uni0211	Contours detected: 2	Expected: 3

	- Glyph name: uni0214	Contours detected: 2	Expected: 3

	- Glyph name: uni0215	Contours detected: 2	Expected: 3

	- Glyph name: uni030F	Contours detected: 1	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni030F	Contours detected: 1	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* petapp (U+E006): L<<282.0,304.0>--<312.0,286.0>> -> L<<312.0,286.0>--<339.0,271.0>>

	* petapp (U+E006): L<<312.0,333.0>--<273.0,356.0>> -> L<<273.0,356.0>--<257.0,365.0>>

	* petapp (U+E006): L<<355.0,309.0>--<312.0,333.0>> -> L<<312.0,333.0>--<273.0,356.0>>

	* petapp (U+E006): L<<371.0,299.0>--<355.0,309.0>> -> L<<355.0,309.0>--<312.0,333.0>>

	* petapp (U+E006): L<<371.0,640.0>--<467.0,585.0>> -> L<<467.0,585.0>--<515.0,556.0>>

	* petapp (U+E006): L<<373.0,298.0>--<371.0,299.0>> -> L<<371.0,299.0>--<355.0,309.0>>

	* petapp (U+E006): L<<426.0,268.0>--<373.0,298.0>> -> L<<373.0,298.0>--<371.0,299.0>>

	* petapp (U+E006): L<<467.0,585.0>--<515.0,556.0>> -> L<<515.0,556.0>--<534.0,545.0>>

	* petapp (U+E006): L<<468.0,243.0>--<426.0,268.0>> -> L<<426.0,268.0>--<373.0,298.0>>

	* petapp (U+E006): L<<474.0,240.0>--<468.0,243.0>> -> L<<468.0,243.0>--<426.0,268.0>>

	* petapp (U+E006): L<<498.0,226.0>--<474.0,240.0>> -> L<<474.0,240.0>--<468.0,243.0>>

	* petapp (U+E006): L<<505.0,222.0>--<498.0,226.0>> -> L<<498.0,226.0>--<474.0,240.0>>

	* petapp (U+E006): L<<691.0,61.0>--<692.0,60.0>> -> L<<692.0,60.0>--<696.0,56.0>>

	* petapp (U+E006): L<<721.0,485.0>--<725.0,485.0>> -> L<<725.0,485.0>--<764.0,485.0>>

	* petapp.minimal (U+E007): L<<264.0,373.0>--<351.0,339.0>> -> L<<351.0,339.0>--<432.0,305.0>>

	* petapp.minimal (U+E007): L<<351.0,339.0>--<432.0,305.0>> -> L<<432.0,305.0>--<448.0,299.0>>

	* petapp.minimal (U+E007): L<<381.0,352.0>--<331.0,376.0>> -> L<<331.0,376.0>--<305.0,390.0>>

	* petapp.minimal (U+E007): L<<432.0,305.0>--<448.0,299.0>> -> L<<448.0,299.0>--<504.0,276.0>>

	* petapp.minimal (U+E007): L<<432.0,326.0>--<381.0,352.0>> -> L<<381.0,352.0>--<331.0,376.0>>

	* petapp.minimal (U+E007): L<<435.0,187.0>--<405.0,192.0>> -> L<<405.0,192.0>--<304.0,211.0>>

	* petapp.minimal (U+E007): L<<448.0,299.0>--<504.0,276.0>> -> L<<504.0,276.0>--<612.0,232.0>>

	* petapp.minimal (U+E007): L<<455.0,314.0>--<432.0,326.0>> -> L<<432.0,326.0>--<381.0,352.0>>

	* petapp.minimal (U+E007): L<<504.0,175.0>--<435.0,187.0>> -> L<<435.0,187.0>--<405.0,192.0>>

	* petapp.minimal (U+E007): L<<504.0,276.0>--<612.0,232.0>> -> L<<612.0,232.0>--<621.0,229.0>>

	* petapp.minimal (U+E007): L<<504.0,289.0>--<455.0,314.0>> -> L<<455.0,314.0>--<432.0,326.0>>

	* petapp.minimal (U+E007): L<<588.0,160.0>--<504.0,175.0>> -> L<<504.0,175.0>--<435.0,187.0>>

	* petapp.minimal (U+E007): L<<621.0,229.0>--<504.0,289.0>> -> L<<504.0,289.0>--<455.0,314.0>>

	* petapp.minimal (U+E007): L<<742.0,30.0>--<742.0,31.0>> -> L<<742.0,31.0>--<742.0,32.0>>

	* petapp.minimal (U+E007): L<<743.0,33.0>--<743.0,34.0>> -> L<<743.0,34.0>--<743.0,36.0>>

	* petapp.minimal (U+E007): L<<743.0,34.0>--<743.0,36.0>> -> L<<743.0,36.0>--<743.0,37.0>>

	* petapp.minimal (U+E007): L<<747.0,73.0>--<746.0,63.0>> -> L<<746.0,63.0>--<743.0,38.0>>

	* petapp.minimal (U+E007): L<<747.0,74.0>--<747.0,73.0>> -> L<<747.0,73.0>--<746.0,63.0>>

	* petapp.minimal (U+E007): L<<752.0,131.0>--<747.0,74.0>> -> L<<747.0,74.0>--<747.0,73.0>>

	* petapp.minimal (U+E007): L<<754.0,162.0>--<752.0,131.0>> -> L<<752.0,131.0>--<747.0,74.0>>

	* petapp.minimal (U+E007): L<<755.0,175.0>--<754.0,162.0>> -> L<<754.0,162.0>--<752.0,131.0>>

	* petapp.minimal (U+E007): L<<757.0,196.0>--<755.0,175.0>> -> L<<755.0,175.0>--<754.0,162.0>>

	* petapp.minimal (U+E007): L<<758.0,210.0>--<757.0,196.0>> -> L<<757.0,196.0>--<755.0,175.0>>

	* petapp.minimal (U+E007): L<<758.0,213.0>--<758.0,210.0>> -> L<<758.0,210.0>--<757.0,196.0>>

	* petapp.wpda (U+E008): L<<640.0,140.0>--<627.0,132.0>> -> L<<627.0,132.0>--<618.0,127.0>>

	* piads (U+E001): L<<112.0,541.0>--<116.0,544.0>> -> L<<116.0,544.0>--<445.0,782.0>>

	* piads (U+E001): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<878.0,541.0>>

	* picall (U+E009): L<<112.0,541.0>--<116.0,544.0>> -> L<<116.0,544.0>--<445.0,782.0>>

	* picall (U+E009): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<878.0,541.0>>

	* pioffice (U+E002): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<877.0,542.0>>

	* pisafe (U+E010): L<<167.0,362.0>--<167.0,491.0>> -> L<<167.0,491.0>--<167.0,494.0>>

	* pisafe (U+E010): L<<203.0,695.0>--<239.0,708.0>> -> L<<239.0,708.0>--<389.0,762.0>>

	* pisafe (U+E010): L<<239.0,708.0>--<389.0,762.0>> -> L<<389.0,762.0>--<494.0,800.0>>

	* pisafe (U+E010): L<<495.0,800.0>--<600.0,762.0>> -> L<<600.0,762.0>--<750.0,708.0>>

	* pisafe (U+E010): L<<600.0,762.0>--<750.0,708.0>> -> L<<750.0,708.0>--<786.0,695.0>>

	* pisign (U+E005): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<877.0,542.0>>

	* pitagon (U+E000): L<<112.0,543.0>--<116.0,546.0>> -> L<<116.0,546.0>--<445.0,784.0>>

	* pitagon (U+E000): L<<209.0,62.0>--<84.0,446.0>> -> L<<84.0,446.0>--<82.0,452.0>>

	* pitagon (U+E000): L<<547.0,784.0>--<874.0,546.0>> -> L<<874.0,546.0>--<878.0,543.0>>

	* pitagram (U+E003): L<<813.0,512.0>--<810.0,514.0>> -> L<<810.0,514.0>--<537.0,711.0>>

	* piweb (U+E004): L<<813.0,512.0>--<810.0,514.0>> -> L<<810.0,514.0>--<537.0,711.0>>

	* sparks (U+E011): L<<100.0,798.0>--<103.0,797.0>> -> L<<103.0,797.0>--<198.0,762.0>>

	* sparks (U+E011): L<<103.0,797.0>--<198.0,762.0>> -> L<<198.0,762.0>--<209.0,759.0>>

	* sparks (U+E011): L<<198.0,762.0>--<209.0,759.0>> -> L<<209.0,759.0>--<400.0,690.0>>

	* sparks (U+E011): L<<209.0,759.0>--<400.0,690.0>> -> L<<400.0,690.0>--<431.0,680.0>>

	* sparks (U+E011): L<<291.0,596.0>--<363.0,534.0>> -> L<<363.0,534.0>--<382.0,516.0>>

	* sparks (U+E011): L<<381.0,366.0>--<383.0,367.0>> -> L<<383.0,367.0>--<486.0,429.0>>

	* sparks (U+E011): L<<383.0,367.0>--<486.0,429.0>> -> L<<486.0,429.0>--<488.0,430.0>>

	* sparks (U+E011): L<<409.0,102.0>--<98.0,641.0>> -> L<<98.0,641.0>--<47.0,731.0>>

	* sparks (U+E011): L<<440.0,659.0>--<436.0,649.0>> -> L<<436.0,649.0>--<434.0,643.0>>

	* sparks (U+E011): L<<454.0,24.0>--<409.0,102.0>> -> L<<409.0,102.0>--<98.0,641.0>>

	* sparks (U+E011): L<<504.0,429.0>--<606.0,367.0>> -> L<<606.0,367.0>--<608.0,366.0>>

	* sparks (U+E011): L<<558.0,680.0>--<596.0,694.0>> -> L<<596.0,694.0>--<780.0,759.0>>

	* sparks (U+E011): L<<579.0,101.0>--<550.0,51.0>> -> L<<550.0,51.0>--<535.0,24.0>>

	* sparks (U+E011): L<<596.0,694.0>--<780.0,759.0>> -> L<<780.0,759.0>--<807.0,768.0>>

	* sparks (U+E011): L<<607.0,516.0>--<627.0,534.0>> -> L<<627.0,534.0>--<699.0,596.0>>

	* sparks (U+E011): L<<614.0,629.0>--<577.0,632.0>> -> L<<577.0,632.0>--<568.0,633.0>>

	* sparks (U+E011): L<<655.0,626.0>--<614.0,629.0>> -> L<<614.0,629.0>--<577.0,632.0>>

	* sparks (U+E011): L<<656.0,626.0>--<655.0,626.0>> -> L<<655.0,626.0>--<614.0,629.0>>

	* sparks (U+E011): L<<690.0,623.0>--<656.0,626.0>> -> L<<656.0,626.0>--<655.0,626.0>>

	* sparks (U+E011): L<<691.0,623.0>--<690.0,623.0>> -> L<<690.0,623.0>--<656.0,626.0>>

	* sparks (U+E011): L<<750.0,397.0>--<579.0,101.0>> -> L<<579.0,101.0>--<550.0,51.0>>

	* sparks (U+E011): L<<780.0,759.0>--<807.0,768.0>> -> L<<807.0,768.0>--<886.0,797.0>>

	* sparks (U+E011): L<<897.0,652.0>--<750.0,397.0>> -> L<<750.0,397.0>--<579.0,101.0>>

	* sparks (U+E011): L<<942.0,730.0>--<897.0,652.0>> -> L<<897.0,652.0>--<750.0,397.0>> 

	* sparks (U+E011): L<<943.0,732.0>--<942.0,730.0>> -> L<<942.0,730.0>--<897.0,652.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* petapp (U+E006): B<<289.0,471.0>-<290.0,469.0>-<291.0,468.0>>/L<<291.0,468.0>--<289.0,471.0>> = 11.309932474020227

	* petapp (U+E006): B<<295.0,293.0>-<289.0,300.0>-<282.0,304.0>>/L<<282.0,304.0>--<312.0,286.0>> = 1.2188752351307344

	* petapp (U+E006): B<<328.0,429.0>-<329.0,428.0>-<331.0,427.0>>/L<<331.0,427.0>--<328.0,429.0>> = 7.125016348901757

	* petapp (U+E006): B<<415.0,76.0>-<416.0,76.0>-<418.0,75.0>>/L<<418.0,75.0>--<415.0,76.0>> = 8.130102354155916

	* petapp (U+E006): B<<424.0,71.0>-<425.0,71.0>-<427.0,70.0>>/L<<427.0,70.0>--<424.0,71.0>> = 8.130102354155916

	* petapp (U+E006): B<<439.0,65.0>-<440.0,65.0>-<442.0,64.0>>/L<<442.0,64.0>--<439.0,65.0>> = 8.130102354155916

	* petapp (U+E006): B<<483.0,64.0>-<484.0,64.0>-<486.0,65.0>>/L<<486.0,65.0>--<483.0,64.0>> = 8.130102354155916

	* petapp (U+E006): B<<513.0,65.0>-<515.0,65.0>-<517.0,66.0>>/L<<517.0,66.0>--<513.0,65.0>> = 12.528807709151463

	* petapp (U+E006): B<<519.0,66.0>-<521.0,66.0>-<523.0,67.0>>/L<<523.0,67.0>--<519.0,66.0>> = 12.528807709151463

	* petapp (U+E006): B<<529.0,68.0>-<528.0,68.0>-<526.0,67.0>>/L<<526.0,67.0>--<529.0,68.0>> = 8.13010235415587

	* petapp (U+E006): B<<536.0,192.0>-<535.0,194.0>-<534.0,195.0>>/L<<534.0,195.0>--<536.0,192.0>> = 11.309932474020195

	* petapp (U+E006): B<<536.0,69.0>-<534.0,69.0>-<532.0,68.0>>/L<<532.0,68.0>--<536.0,69.0>> = 12.528807709151492

	* petapp (U+E006): B<<537.0,308.0>-<536.0,309.0>-<534.0,310.0>>/L<<534.0,310.0>--<537.0,308.0>> = 7.125016348901757

	* petapp (U+E006): B<<539.0,108.0>-<540.0,109.0>-<541.0,111.0>>/L<<541.0,111.0>--<539.0,108.0>> = 7.125016348901705

	* petapp (U+E006): B<<539.0,438.0>-<538.0,439.0>-<536.0,440.0>>/L<<536.0,440.0>--<539.0,438.0>> = 7.125016348901757

	* petapp (U+E006): B<<545.0,123.0>-<546.0,125.0>-<546.0,127.0>>/L<<546.0,127.0>--<545.0,123.0>> = 14.036243467926484

	* petapp (U+E006): B<<548.0,432.0>-<547.0,433.0>-<545.0,434.0>>/L<<545.0,434.0>--<548.0,432.0>> = 7.125016348901757

	* petapp (U+E006): B<<548.0,72.0>-<549.0,72.0>-<551.0,73.0>>/L<<551.0,73.0>--<548.0,72.0>> = 8.130102354155916

	* petapp (U+E006): B<<575.0,404.0>-<576.0,403.0>-<577.0,401.0>>/L<<577.0,401.0>--<575.0,404.0>> = 7.125016348901705

	* petapp (U+E006): B<<587.0,380.0>-<587.0,382.0>-<586.0,384.0>>/L<<586.0,384.0>--<587.0,380.0>> = 12.528807709151492

	* petapp (U+E006): B<<610.0,384.0>-<611.0,381.0>-<612.0,379.0>>/L<<612.0,379.0>--<610.0,384.0>> = 4.763641690726066

	* petapp (U+E006): B<<614.0,384.0>-<615.0,382.0>-<616.0,379.0>>/L<<616.0,379.0>--<614.0,384.0>> = 3.366460663429615

	* petapp (U+E006): B<<627.0,343.0>-<628.0,342.0>-<629.0,340.0>>/L<<629.0,340.0>--<627.0,343.0>> = 7.125016348901705

	* petapp (U+E006): B<<633.0,334.0>-<633.0,333.0>-<634.0,331.0>>/L<<634.0,331.0>--<633.0,334.0>> = 8.130102354155916

	* petapp (U+E006): B<<638.0,346.0>-<639.0,345.0>-<640.0,343.0>>/L<<640.0,343.0>--<638.0,346.0>> = 7.125016348901705

	* petapp (U+E006): B<<641.0,321.0>-<642.0,320.0>-<643.0,318.0>>/L<<643.0,318.0>--<641.0,321.0>> = 7.125016348901705

	* petapp (U+E006): B<<669.0,316.0>-<670.0,315.0>-<672.0,314.0>>/L<<672.0,314.0>--<669.0,316.0>> = 7.125016348901757

	* petapp (U+E006): B<<669.0,456.0>-<667.0,454.0>-<666.0,452.0>>/L<<666.0,452.0>--<669.0,456.0>> = 10.304846468766044

	* petapp (U+E006): B<<670.0,137.0>-<671.0,138.0>-<672.0,140.0>>/L<<672.0,140.0>--<670.0,137.0>> = 7.125016348901705

	* petapp (U+E006): B<<679.0,141.0>-<681.0,142.0>-<682.0,143.0>>/L<<682.0,143.0>--<679.0,141.0>> = 11.309932474020195

	* petapp (U+E006): B<<687.0,164.0>-<688.0,166.0>-<689.0,167.0>>/L<<689.0,167.0>--<687.0,164.0>> = 11.309932474020227

	* petapp (U+E006): B<<713.0,484.0>-<712.0,484.0>-<710.0,483.0>>/L<<710.0,483.0>--<713.0,484.0>> = 8.13010235415587

	* petapp (U+E006): B<<763.0,5.0>-<762.0,7.0>-<761.0,8.0>>/L<<761.0,8.0>--<763.0,5.0>> = 11.309932474020195

	* petapp (U+E006): L<<274.0,517.0>--<273.0,520.0>>/B<<273.0,520.0>-<274.0,518.0>-<274.0,517.0>> = 8.130102354155916

	* petapp (U+E006): L<<280.0,491.0>--<279.0,494.0>>/B<<279.0,494.0>-<280.0,492.0>-<280.0,491.0>> = 8.130102354155916

	* petapp (U+E006): L<<291.0,468.0>--<289.0,471.0>>/B<<289.0,471.0>-<290.0,469.0>-<291.0,468.0>> = 7.125016348901705

	* petapp (U+E006): L<<296.0,459.0>--<295.0,462.0>>/B<<295.0,462.0>-<296.0,460.0>-<296.0,459.0>> = 8.130102354155916

	* petapp (U+E006): L<<312.0,442.0>--<308.0,445.0>>/B<<308.0,445.0>-<310.0,444.0>-<312.0,442.0>> = 10.304846468766009

	* petapp (U+E006): L<<331.0,427.0>--<328.0,429.0>>/B<<328.0,429.0>-<329.0,428.0>-<331.0,427.0>> = 11.309932474020195

	* petapp (U+E006): L<<380.0,128.0>--<379.0,131.0>>/B<<379.0,131.0>-<380.0,129.0>-<380.0,128.0>> = 8.130102354155916

	* petapp (U+E006): L<<387.0,108.0>--<386.0,111.0>>/B<<386.0,111.0>-<387.0,109.0>-<387.0,108.0>> = 8.130102354155916

	* petapp (U+E006): L<<499.0,225.0>--<505.0,222.0>>/L<<505.0,222.0>--<498.0,226.0>> = 3.1798301198640497

	* petapp (U+E006): L<<504.0,71.0>--<499.0,69.0>>/B<<499.0,69.0>-<502.0,71.0>-<504.0,71.0>> = 11.888658039627936

	* petapp (U+E006): L<<517.0,66.0>--<513.0,65.0>>/B<<513.0,65.0>-<515.0,65.0>-<517.0,66.0>> = 14.036243467926484

	* petapp (U+E006): L<<523.0,67.0>--<519.0,66.0>>/B<<519.0,66.0>-<521.0,66.0>-<523.0,67.0>> = 14.036243467926484

	* petapp (U+E006): L<<532.0,68.0>--<536.0,69.0>>/B<<536.0,69.0>-<534.0,69.0>-<532.0,68.0>> = 14.036243467926484

	* petapp (U+E006): L<<534.0,195.0>--<536.0,192.0>>/B<<536.0,192.0>-<535.0,194.0>-<534.0,195.0>> = 7.125016348901757

	* petapp (U+E006): L<<534.0,310.0>--<537.0,308.0>>/B<<537.0,308.0>-<536.0,309.0>-<534.0,310.0>> = 11.309932474020227

	* petapp (U+E006): L<<536.0,440.0>--<539.0,438.0>>/B<<539.0,438.0>-<538.0,439.0>-<536.0,440.0>> = 11.309932474020227

	* petapp (U+E006): L<<541.0,111.0>--<539.0,108.0>>/B<<539.0,108.0>-<540.0,109.0>-<541.0,111.0>> = 11.309932474020227

	* petapp (U+E006): L<<541.0,70.0>--<545.0,71.0>>/B<<545.0,71.0>-<540.0,70.0>-<541.0,70.0>> = 2.726310993906212

	* petapp (U+E006): L<<542.0,181.0>--<543.0,178.0>>/B<<543.0,178.0>-<542.0,180.0>-<542.0,181.0>> = 8.13010235415587

	* petapp (U+E006): L<<545.0,434.0>--<548.0,432.0>>/B<<548.0,432.0>-<547.0,433.0>-<545.0,434.0>> = 11.309932474020227

	* petapp (U+E006): L<<546.0,127.0>--<545.0,123.0>>/B<<545.0,123.0>-<546.0,125.0>-<546.0,127.0>> = 12.528807709151492

	* petapp (U+E006): L<<556.0,74.0>--<553.0,73.0>>/B<<553.0,73.0>-<555.0,74.0>-<556.0,74.0>> = 8.130102354155916

	* petapp (U+E006): L<<577.0,401.0>--<575.0,404.0>>/B<<575.0,404.0>-<576.0,403.0>-<577.0,401.0>> = 11.309932474020227

	* petapp (U+E006): L<<583.0,256.0>--<584.0,252.0>>/B<<584.0,252.0>-<584.0,254.0>-<583.0,256.0>> = 14.036243467926484

	* petapp (U+E006): L<<586.0,384.0>--<587.0,380.0>>/B<<587.0,380.0>-<587.0,382.0>-<586.0,384.0>> = 14.036243467926484

	* petapp (U+E006): L<<598.0,432.0>--<599.0,429.0>>/B<<599.0,429.0>-<598.0,431.0>-<598.0,432.0>> = 8.13010235415587

	* petapp (U+E006): L<<602.0,122.0>--<601.0,125.0>>/B<<601.0,125.0>-<602.0,123.0>-<602.0,122.0>> = 8.130102354155916

	* petapp (U+E006): L<<611.0,96.0>--<611.0,96.0>>/B<<611.0,96.0>-<607.0,95.0>-<603.5,92.5>> = 14.036243467926484

	* petapp (U+E006): L<<612.0,379.0>--<610.0,384.0>>/B<<610.0,384.0>-<611.0,381.0>-<612.0,379.0>> = 3.366460663429615

	* petapp (U+E006): L<<613.0,374.0>--<612.0,377.0>>/B<<612.0,377.0>-<613.0,375.0>-<613.0,374.0>> = 8.130102354155916

	* petapp (U+E006): L<<615.0,369.0>--<614.0,372.0>>/B<<614.0,372.0>-<615.0,370.0>-<615.0,369.0>> = 8.130102354155916

	* petapp (U+E006): L<<616.0,379.0>--<614.0,384.0>>/B<<614.0,384.0>-<615.0,382.0>-<616.0,379.0>> = 4.763641690726066

	* petapp (U+E006): L<<629.0,340.0>--<627.0,343.0>>/B<<627.0,343.0>-<628.0,342.0>-<629.0,340.0>> = 11.309932474020227

	* petapp (U+E006): L<<640.0,343.0>--<638.0,346.0>>/B<<638.0,346.0>-<639.0,345.0>-<640.0,343.0>> = 11.309932474020227

	* petapp (U+E006): L<<643.0,318.0>--<641.0,321.0>>/B<<641.0,321.0>-<642.0,320.0>-<643.0,318.0>> = 11.309932474020227

	* petapp (U+E006): L<<657.0,433.0>--<658.0,436.0>>/B<<658.0,436.0>-<657.0,434.0>-<657.0,432.5>> = 8.13010235415587

	* petapp (U+E006): L<<661.0,383.0>--<660.0,386.0>>/B<<660.0,386.0>-<661.0,384.0>-<661.0,383.0>> = 8.130102354155916

	* petapp (U+E006): L<<666.0,452.0>--<669.0,456.0>>/B<<669.0,456.0>-<667.0,454.0>-<666.0,452.0>> = 8.13010235415596

	* petapp (U+E006): L<<672.0,140.0>--<670.0,137.0>>/B<<670.0,137.0>-<671.0,138.0>-<672.0,140.0>> = 11.309932474020227

	* petapp (U+E006): L<<682.0,143.0>--<679.0,141.0>>/B<<679.0,141.0>-<681.0,142.0>-<682.0,143.0>> = 7.125016348901757

	* petapp (U+E006): L<<686.0,162.0>--<685.0,159.0>>/B<<685.0,159.0>-<686.0,161.0>-<686.0,162.0>> = 8.130102354155916

	* petapp (U+E006): L<<689.0,167.0>--<687.0,164.0>>/B<<687.0,164.0>-<688.0,166.0>-<689.0,167.0>> = 7.125016348901705

	* petapp (U+E006): L<<689.0,256.0>--<690.0,253.0>>/B<<690.0,253.0>-<689.0,255.0>-<689.0,256.0>> = 8.13010235415587

	* petapp (U+E006): L<<691.0,251.0>--<692.0,248.0>>/B<<692.0,248.0>-<691.0,250.0>-<691.0,251.0>> = 8.13010235415587

	* petapp (U+E006): L<<700.0,480.0>--<703.0,481.0>>/B<<703.0,481.0>-<701.0,480.0>-<700.0,479.5>> = 8.13010235415587

	* petapp (U+E006): L<<705.0,482.0>--<708.0,483.0>>/B<<708.0,483.0>-<706.0,482.0>-<705.0,482.0>> = 8.13010235415587

	* petapp (U+E006): L<<708.0,293.0>--<705.0,294.0>>/B<<705.0,294.0>-<707.0,293.0>-<708.0,293.0>> = 8.130102354155916

	* petapp (U+E006): L<<728.0,285.0>--<725.0,286.0>>/B<<725.0,286.0>-<727.0,285.0>-<728.0,285.0>> = 8.130102354155916

	* petapp (U+E006): L<<761.0,8.0>--<763.0,5.0>>/B<<763.0,5.0>-<762.0,7.0>-<761.0,8.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<581.0,372.0>-<585.0,368.0>-<588.0,366.0>>/L<<588.0,366.0>--<581.0,372.0>> = 6.911227119024609

	* petapp.minimal (U+E007): B<<631.0,435.0>-<631.0,433.0>-<632.0,430.0>>/L<<632.0,430.0>--<631.0,435.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<632.0,481.0>-<632.0,480.0>-<631.0,478.0>>/L<<631.0,478.0>--<632.0,481.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<645.0,399.0>-<646.0,397.0>-<647.0,396.0>>/L<<647.0,396.0>--<645.0,399.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<646.0,510.0>-<645.0,508.0>-<644.0,507.0>>/L<<644.0,507.0>--<646.0,510.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<676.0,538.0>-<674.0,537.0>-<673.0,536.0>>/L<<673.0,536.0>--<676.0,538.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<700.0,247.0>-<699.0,248.0>-<698.0,250.0>>/L<<698.0,250.0>--<700.0,247.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<714.0,147.0>-<714.0,148.0>-<713.0,150.0>>/L<<713.0,150.0>--<714.0,147.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<720.0,137.0>-<719.0,139.0>-<718.0,140.0>>/L<<718.0,140.0>--<720.0,137.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<732.0,185.0>-<731.0,187.0>-<731.0,189.0>>/L<<731.0,189.0>--<732.0,185.0>> = 14.036243467926484

	* petapp.minimal (U+E007): B<<743.0,53.0>-<743.0,54.0>-<742.0,56.0>>/L<<742.0,56.0>--<743.0,53.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<212.0,538.0>--<212.0,800.0>>/B<<212.0,800.0>-<214.0,769.0>-<226.5,742.0>> = 3.6913859864512575

	* petapp.minimal (U+E007): L<<628.0,462.0>--<629.0,465.0>>/B<<629.0,465.0>-<628.0,463.0>-<628.0,462.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<630.0,473.0>--<631.0,476.0>>/B<<631.0,476.0>-<630.0,474.0>-<630.0,473.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<632.0,430.0>--<631.0,435.0>>/B<<631.0,435.0>-<631.0,433.0>-<632.0,430.0>> = 11.309932474020227

	* petapp.minimal (U+E007): L<<637.0,222.0>--<640.0,221.0>>/B<<640.0,221.0>-<638.0,222.0>-<637.0,222.5>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<639.0,498.0>--<640.0,501.0>>/B<<640.0,501.0>-<639.0,499.0>-<639.0,498.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<644.0,507.0>--<646.0,510.0>>/B<<646.0,510.0>-<645.0,508.0>-<644.0,507.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<647.0,396.0>--<645.0,399.0>>/B<<645.0,399.0>-<646.0,397.0>-<647.0,396.0>> = 7.125016348901705

	* petapp.minimal (U+E007): L<<673.0,536.0>--<676.0,538.0>>/B<<676.0,538.0>-<674.0,537.0>-<673.0,536.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<682.0,542.0>--<685.0,543.0>>/B<<685.0,543.0>-<683.0,542.0>-<682.0,542.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<687.0,544.0>--<690.0,545.0>>/B<<690.0,545.0>-<688.0,544.0>-<687.0,544.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<698.0,250.0>--<700.0,247.0>>/B<<700.0,247.0>-<699.0,248.0>-<698.0,250.0>> = 11.309932474020195

	* petapp.minimal (U+E007): L<<718.0,218.0>--<719.0,215.0>>/B<<719.0,215.0>-<718.0,217.0>-<718.0,218.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<731.0,113.0>--<732.0,110.0>>/B<<732.0,110.0>-<731.0,112.0>-<731.0,113.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<740.0,156.0>--<739.0,160.0>>/B<<739.0,160.0>-<740.0,153.0>-<740.0,156.0>> = 5.906141113770497

	* petapp.minimal (U+E007): L<<744.0,137.0>--<743.0,140.0>>/B<<743.0,140.0>-<744.0,138.0>-<744.0,137.0>> = 8.130102354155916

	* petapp.minimal (U+E007): L<<746.0,123.0>--<747.0,120.0>>/B<<747.0,120.0>-<746.0,122.0>-<746.0,123.0>> = 8.13010235415587

	* petapp.wpda (U+E008): B<<485.0,2.0>-<482.0,5.0>-<482.0,6.0>>/L<<482.0,6.0>--<481.0,1.0>> = 11.309932474020227

	* petapp.wpda (U+E008): L<<185.0,222.0>--<180.0,218.0>>/B<<180.0,218.0>-<182.0,219.0>-<183.0,218.0>> = 12.094757077012058

	* pisafe (U+E010): B<<175.0,538.0>-<175.0,536.0>-<174.0,534.0>>/L<<174.0,534.0>--<175.0,538.0>> = 12.528807709151492

	* pisafe (U+E010): B<<190.0,573.0>-<189.0,572.0>-<188.0,570.0>>/L<<188.0,570.0>--<190.0,573.0>> = 7.125016348901757

	* pisafe (U+E010): B<<211.0,602.0>-<210.0,600.0>-<208.0,598.0>>/L<<208.0,598.0>--<211.0,602.0>> = 8.13010235415596

	* pisafe (U+E010): B<<784.0,594.0>-<783.0,596.0>-<782.0,597.0>>/L<<782.0,597.0>--<784.0,594.0>> = 11.309932474020195

	* pisafe (U+E010): B<<797.0,577.0>-<796.0,579.0>-<795.0,580.0>>/L<<795.0,580.0>--<797.0,577.0>> = 11.309932474020195

	* pisafe (U+E010): B<<816.0,530.0>-<816.0,532.0>-<815.0,534.0>>/L<<815.0,534.0>--<816.0,530.0>> = 12.528807709151492

	* pisafe (U+E010): B<<820.0,515.0>-<820.0,516.0>-<819.0,518.0>>/L<<819.0,518.0>--<820.0,515.0>> = 8.13010235415587

	* pisafe (U+E010): L<<174.0,534.0>--<175.0,538.0>>/B<<175.0,538.0>-<175.0,536.0>-<174.0,534.0>> = 14.036243467926484

	* pisafe (U+E010): L<<188.0,570.0>--<190.0,573.0>>/B<<190.0,573.0>-<189.0,572.0>-<188.0,570.0>> = 11.309932474020195

	* pisafe (U+E010): L<<208.0,598.0>--<211.0,602.0>>/B<<211.0,602.0>-<210.0,600.0>-<208.0,598.0>> = 10.304846468766044

	* pisafe (U+E010): L<<750.0,626.0>--<754.0,623.0>>/B<<754.0,623.0>-<752.0,624.0>-<750.0,626.0>> = 10.304846468766009

	* pisafe (U+E010): L<<782.0,597.0>--<784.0,594.0>>/B<<784.0,594.0>-<783.0,596.0>-<782.0,597.0>> = 7.125016348901757

	* pisafe (U+E010): L<<795.0,580.0>--<797.0,577.0>>/B<<797.0,577.0>-<796.0,579.0>-<795.0,580.0>> = 7.125016348901757

	* pisafe (U+E010): L<<815.0,534.0>--<816.0,530.0>>/B<<816.0,530.0>-<816.0,532.0>-<815.0,534.0>> = 14.036243467926484 

	* pisafe (U+E010): L<<817.0,528.0>--<818.0,525.0>>/B<<818.0,525.0>-<817.0,527.0>-<817.0,528.0>> = 8.13010235415587 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[22] PitagonSansText-BoldItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check OFL body text is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text">com.google.fonts/check/license/OFL_body_text</a>)</summary><div>


* 🔥 **FAIL** The OFL.txt body text is incorrect. Please use https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt as a template. You should only modify the first line. [code: incorrect-ofl-body-text]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ
at: https://scripts.sil.org/OFL." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>🔥 <b>FAIL:</b> Check font names are correct (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/font_names">com.google.fonts/check/font_names</a>)</summary><div>


* 🔥 **FAIL** Font names are incorrect:

| nameID | current | expected |
| :--- | :--- | :--- |
| Family Name | Pitagon Sans Text Bold | Pitagon Sans Text |
| Subfamily Name | Italic | Bold Italic |
| Full Name | Pitagon Sans Text Bold Italic | Pitagon Sans Text Bold Italic |
| Poscript Name | PitagonSansText-BoldItalic | PitagonSansText-BoldItalic |
| Typographic Family Name | Pitagon Sans Text | N/A |
| Typographic Subfamily Name | Bold Italic | N/A | [code: bad-names]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks">com.google.fonts/check/name/line_breaks</a>)</summary><div>


* 🔥 **FAIL** Name entry DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1294, but got 1214 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.11, while a newer 0.8.13 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking head.macStyle value. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/head.html#com.google.fonts/check/mac_style">com.google.fonts/check/mac_style</a>)</summary><div>


* 🔥 **FAIL** head macStyle BOLD bit should be set. [code: bad-BOLD]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 fsSelection value. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/os2.html#com.google.fonts/check/fsselection">com.google.fonts/check/fsselection</a>)</summary><div>


* 🔥 **FAIL** OS/2 fsSelection BOLD bit should be set. [code: bad-BOLD]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'Pita' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
</div></details><details><summary>⚠ <b>WARN:</b> Description strings in the name table must not exceed 200 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/description_max_length">com.google.fonts/check/name/description_max_length</a>)</summary><div>


* ⚠ **WARN** A few name table entries with ID=10 (NameID.DESCRIPTION) are longer than 200 characters. Please check whether those entries are copyright notices mistakenly stored in the description string entries by a bug in an old FontLab version. If that's the case, then such copyright notices must be removed from these entries. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Pitagon Sans Text Bold' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- periodcentered.001 

	- registered.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni0200	Contours detected: 3	Expected: 4

	- Glyph name: uni0201	Contours detected: 3	Expected: 4

	- Glyph name: uni0204	Contours detected: 2	Expected: 3

	- Glyph name: uni0205	Contours detected: 3	Expected: 4

	- Glyph name: uni0208	Contours detected: 2	Expected: 3

	- Glyph name: uni0209	Contours detected: 2	Expected: 3

	- Glyph name: uni020C	Contours detected: 3	Expected: 4

	- Glyph name: uni020D	Contours detected: 3	Expected: 4

	- Glyph name: uni0210	Contours detected: 3	Expected: 4

	- Glyph name: uni0211	Contours detected: 2	Expected: 3

	- Glyph name: uni0214	Contours detected: 2	Expected: 3

	- Glyph name: uni0215	Contours detected: 2	Expected: 3

	- Glyph name: uni030F	Contours detected: 1	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni030F	Contours detected: 1	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* fl (U+FB02): L<<489.0,427.0>--<488.0,427.0>> -> L<<488.0,427.0>--<277.0,427.0>>

	* petapp (U+E006): L<<282.0,304.0>--<312.0,286.0>> -> L<<312.0,286.0>--<339.0,271.0>>

	* petapp (U+E006): L<<312.0,333.0>--<273.0,356.0>> -> L<<273.0,356.0>--<257.0,365.0>>

	* petapp (U+E006): L<<355.0,309.0>--<312.0,333.0>> -> L<<312.0,333.0>--<273.0,356.0>>

	* petapp (U+E006): L<<371.0,299.0>--<355.0,309.0>> -> L<<355.0,309.0>--<312.0,333.0>>

	* petapp (U+E006): L<<371.0,640.0>--<467.0,585.0>> -> L<<467.0,585.0>--<515.0,556.0>>

	* petapp (U+E006): L<<373.0,298.0>--<371.0,299.0>> -> L<<371.0,299.0>--<355.0,309.0>>

	* petapp (U+E006): L<<426.0,268.0>--<373.0,298.0>> -> L<<373.0,298.0>--<371.0,299.0>>

	* petapp (U+E006): L<<467.0,585.0>--<515.0,556.0>> -> L<<515.0,556.0>--<534.0,545.0>>

	* petapp (U+E006): L<<468.0,243.0>--<426.0,268.0>> -> L<<426.0,268.0>--<373.0,298.0>>

	* petapp (U+E006): L<<474.0,240.0>--<468.0,243.0>> -> L<<468.0,243.0>--<426.0,268.0>>

	* petapp (U+E006): L<<498.0,226.0>--<474.0,240.0>> -> L<<474.0,240.0>--<468.0,243.0>>

	* petapp (U+E006): L<<505.0,222.0>--<498.0,226.0>> -> L<<498.0,226.0>--<474.0,240.0>>

	* petapp (U+E006): L<<691.0,61.0>--<692.0,60.0>> -> L<<692.0,60.0>--<696.0,56.0>>

	* petapp (U+E006): L<<721.0,485.0>--<725.0,485.0>> -> L<<725.0,485.0>--<764.0,485.0>>

	* petapp.minimal (U+E007): L<<264.0,373.0>--<351.0,339.0>> -> L<<351.0,339.0>--<432.0,305.0>>

	* petapp.minimal (U+E007): L<<351.0,339.0>--<432.0,305.0>> -> L<<432.0,305.0>--<448.0,299.0>>

	* petapp.minimal (U+E007): L<<381.0,352.0>--<331.0,376.0>> -> L<<331.0,376.0>--<305.0,390.0>>

	* petapp.minimal (U+E007): L<<432.0,305.0>--<448.0,299.0>> -> L<<448.0,299.0>--<504.0,276.0>>

	* petapp.minimal (U+E007): L<<432.0,326.0>--<381.0,352.0>> -> L<<381.0,352.0>--<331.0,376.0>>

	* petapp.minimal (U+E007): L<<435.0,187.0>--<405.0,192.0>> -> L<<405.0,192.0>--<304.0,211.0>>

	* petapp.minimal (U+E007): L<<448.0,299.0>--<504.0,276.0>> -> L<<504.0,276.0>--<612.0,232.0>>

	* petapp.minimal (U+E007): L<<455.0,314.0>--<432.0,326.0>> -> L<<432.0,326.0>--<381.0,352.0>>

	* petapp.minimal (U+E007): L<<504.0,175.0>--<435.0,187.0>> -> L<<435.0,187.0>--<405.0,192.0>>

	* petapp.minimal (U+E007): L<<504.0,276.0>--<612.0,232.0>> -> L<<612.0,232.0>--<621.0,229.0>>

	* petapp.minimal (U+E007): L<<504.0,289.0>--<455.0,314.0>> -> L<<455.0,314.0>--<432.0,326.0>>

	* petapp.minimal (U+E007): L<<588.0,160.0>--<504.0,175.0>> -> L<<504.0,175.0>--<435.0,187.0>>

	* petapp.minimal (U+E007): L<<621.0,229.0>--<504.0,289.0>> -> L<<504.0,289.0>--<455.0,314.0>>

	* petapp.minimal (U+E007): L<<742.0,30.0>--<742.0,31.0>> -> L<<742.0,31.0>--<742.0,32.0>>

	* petapp.minimal (U+E007): L<<743.0,33.0>--<743.0,34.0>> -> L<<743.0,34.0>--<743.0,36.0>>

	* petapp.minimal (U+E007): L<<743.0,34.0>--<743.0,36.0>> -> L<<743.0,36.0>--<743.0,37.0>>

	* petapp.minimal (U+E007): L<<747.0,73.0>--<746.0,63.0>> -> L<<746.0,63.0>--<743.0,38.0>>

	* petapp.minimal (U+E007): L<<747.0,74.0>--<747.0,73.0>> -> L<<747.0,73.0>--<746.0,63.0>>

	* petapp.minimal (U+E007): L<<752.0,131.0>--<747.0,74.0>> -> L<<747.0,74.0>--<747.0,73.0>>

	* petapp.minimal (U+E007): L<<754.0,162.0>--<752.0,131.0>> -> L<<752.0,131.0>--<747.0,74.0>>

	* petapp.minimal (U+E007): L<<755.0,175.0>--<754.0,162.0>> -> L<<754.0,162.0>--<752.0,131.0>>

	* petapp.minimal (U+E007): L<<757.0,196.0>--<755.0,175.0>> -> L<<755.0,175.0>--<754.0,162.0>>

	* petapp.minimal (U+E007): L<<758.0,210.0>--<757.0,196.0>> -> L<<757.0,196.0>--<755.0,175.0>>

	* petapp.minimal (U+E007): L<<758.0,213.0>--<758.0,210.0>> -> L<<758.0,210.0>--<757.0,196.0>>

	* petapp.wpda (U+E008): L<<640.0,140.0>--<627.0,132.0>> -> L<<627.0,132.0>--<618.0,127.0>>

	* piads (U+E001): L<<112.0,541.0>--<116.0,544.0>> -> L<<116.0,544.0>--<445.0,782.0>>

	* piads (U+E001): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<878.0,541.0>>

	* picall (U+E009): L<<112.0,541.0>--<116.0,544.0>> -> L<<116.0,544.0>--<445.0,782.0>>

	* picall (U+E009): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<878.0,541.0>>

	* pioffice (U+E002): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<877.0,542.0>>

	* pisafe (U+E010): L<<167.0,362.0>--<167.0,491.0>> -> L<<167.0,491.0>--<167.0,494.0>>

	* pisafe (U+E010): L<<203.0,695.0>--<239.0,708.0>> -> L<<239.0,708.0>--<389.0,762.0>>

	* pisafe (U+E010): L<<239.0,708.0>--<389.0,762.0>> -> L<<389.0,762.0>--<494.0,800.0>>

	* pisafe (U+E010): L<<495.0,800.0>--<600.0,762.0>> -> L<<600.0,762.0>--<750.0,708.0>>

	* pisafe (U+E010): L<<600.0,762.0>--<750.0,708.0>> -> L<<750.0,708.0>--<786.0,695.0>>

	* pisign (U+E005): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<877.0,542.0>>

	* pitagon (U+E000): L<<112.0,543.0>--<116.0,546.0>> -> L<<116.0,546.0>--<445.0,784.0>>

	* pitagon (U+E000): L<<209.0,62.0>--<84.0,446.0>> -> L<<84.0,446.0>--<82.0,452.0>>

	* pitagon (U+E000): L<<547.0,784.0>--<874.0,546.0>> -> L<<874.0,546.0>--<878.0,543.0>>

	* pitagram (U+E003): L<<813.0,512.0>--<810.0,514.0>> -> L<<810.0,514.0>--<537.0,711.0>>

	* piweb (U+E004): L<<813.0,512.0>--<810.0,514.0>> -> L<<810.0,514.0>--<537.0,711.0>>

	* sparks (U+E011): L<<100.0,798.0>--<103.0,797.0>> -> L<<103.0,797.0>--<198.0,762.0>>

	* sparks (U+E011): L<<103.0,797.0>--<198.0,762.0>> -> L<<198.0,762.0>--<209.0,759.0>>

	* sparks (U+E011): L<<198.0,762.0>--<209.0,759.0>> -> L<<209.0,759.0>--<400.0,690.0>>

	* sparks (U+E011): L<<209.0,759.0>--<400.0,690.0>> -> L<<400.0,690.0>--<431.0,680.0>>

	* sparks (U+E011): L<<291.0,596.0>--<363.0,534.0>> -> L<<363.0,534.0>--<382.0,516.0>>

	* sparks (U+E011): L<<381.0,366.0>--<383.0,367.0>> -> L<<383.0,367.0>--<486.0,429.0>>

	* sparks (U+E011): L<<383.0,367.0>--<486.0,429.0>> -> L<<486.0,429.0>--<488.0,430.0>>

	* sparks (U+E011): L<<409.0,102.0>--<98.0,641.0>> -> L<<98.0,641.0>--<47.0,731.0>>

	* sparks (U+E011): L<<440.0,659.0>--<436.0,649.0>> -> L<<436.0,649.0>--<434.0,643.0>>

	* sparks (U+E011): L<<454.0,24.0>--<409.0,102.0>> -> L<<409.0,102.0>--<98.0,641.0>>

	* sparks (U+E011): L<<504.0,429.0>--<606.0,367.0>> -> L<<606.0,367.0>--<608.0,366.0>>

	* sparks (U+E011): L<<558.0,680.0>--<596.0,694.0>> -> L<<596.0,694.0>--<780.0,759.0>>

	* sparks (U+E011): L<<579.0,101.0>--<550.0,51.0>> -> L<<550.0,51.0>--<535.0,24.0>>

	* sparks (U+E011): L<<596.0,694.0>--<780.0,759.0>> -> L<<780.0,759.0>--<807.0,768.0>>

	* sparks (U+E011): L<<607.0,516.0>--<627.0,534.0>> -> L<<627.0,534.0>--<699.0,596.0>>

	* sparks (U+E011): L<<614.0,629.0>--<577.0,632.0>> -> L<<577.0,632.0>--<568.0,633.0>>

	* sparks (U+E011): L<<655.0,626.0>--<614.0,629.0>> -> L<<614.0,629.0>--<577.0,632.0>>

	* sparks (U+E011): L<<656.0,626.0>--<655.0,626.0>> -> L<<655.0,626.0>--<614.0,629.0>>

	* sparks (U+E011): L<<690.0,623.0>--<656.0,626.0>> -> L<<656.0,626.0>--<655.0,626.0>>

	* sparks (U+E011): L<<691.0,623.0>--<690.0,623.0>> -> L<<690.0,623.0>--<656.0,626.0>>

	* sparks (U+E011): L<<750.0,397.0>--<579.0,101.0>> -> L<<579.0,101.0>--<550.0,51.0>>

	* sparks (U+E011): L<<780.0,759.0>--<807.0,768.0>> -> L<<807.0,768.0>--<886.0,797.0>>

	* sparks (U+E011): L<<897.0,652.0>--<750.0,397.0>> -> L<<750.0,397.0>--<579.0,101.0>>

	* sparks (U+E011): L<<942.0,730.0>--<897.0,652.0>> -> L<<897.0,652.0>--<750.0,397.0>> 

	* sparks (U+E011): L<<943.0,732.0>--<942.0,730.0>> -> L<<942.0,730.0>--<897.0,652.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* petapp (U+E006): B<<289.0,471.0>-<290.0,469.0>-<291.0,468.0>>/L<<291.0,468.0>--<289.0,471.0>> = 11.309932474020227

	* petapp (U+E006): B<<295.0,293.0>-<289.0,300.0>-<282.0,304.0>>/L<<282.0,304.0>--<312.0,286.0>> = 1.2188752351307344

	* petapp (U+E006): B<<328.0,429.0>-<329.0,428.0>-<331.0,427.0>>/L<<331.0,427.0>--<328.0,429.0>> = 7.125016348901757

	* petapp (U+E006): B<<415.0,76.0>-<416.0,76.0>-<418.0,75.0>>/L<<418.0,75.0>--<415.0,76.0>> = 8.130102354155916

	* petapp (U+E006): B<<424.0,71.0>-<425.0,71.0>-<427.0,70.0>>/L<<427.0,70.0>--<424.0,71.0>> = 8.130102354155916

	* petapp (U+E006): B<<439.0,65.0>-<440.0,65.0>-<442.0,64.0>>/L<<442.0,64.0>--<439.0,65.0>> = 8.130102354155916

	* petapp (U+E006): B<<483.0,64.0>-<484.0,64.0>-<486.0,65.0>>/L<<486.0,65.0>--<483.0,64.0>> = 8.130102354155916

	* petapp (U+E006): B<<513.0,65.0>-<515.0,65.0>-<517.0,66.0>>/L<<517.0,66.0>--<513.0,65.0>> = 12.528807709151463

	* petapp (U+E006): B<<519.0,66.0>-<521.0,66.0>-<523.0,67.0>>/L<<523.0,67.0>--<519.0,66.0>> = 12.528807709151463

	* petapp (U+E006): B<<529.0,68.0>-<528.0,68.0>-<526.0,67.0>>/L<<526.0,67.0>--<529.0,68.0>> = 8.13010235415587

	* petapp (U+E006): B<<536.0,192.0>-<535.0,194.0>-<534.0,195.0>>/L<<534.0,195.0>--<536.0,192.0>> = 11.309932474020195

	* petapp (U+E006): B<<536.0,69.0>-<534.0,69.0>-<532.0,68.0>>/L<<532.0,68.0>--<536.0,69.0>> = 12.528807709151492

	* petapp (U+E006): B<<537.0,308.0>-<536.0,309.0>-<534.0,310.0>>/L<<534.0,310.0>--<537.0,308.0>> = 7.125016348901757

	* petapp (U+E006): B<<539.0,108.0>-<540.0,109.0>-<541.0,111.0>>/L<<541.0,111.0>--<539.0,108.0>> = 7.125016348901705

	* petapp (U+E006): B<<539.0,438.0>-<538.0,439.0>-<536.0,440.0>>/L<<536.0,440.0>--<539.0,438.0>> = 7.125016348901757

	* petapp (U+E006): B<<545.0,123.0>-<546.0,125.0>-<546.0,127.0>>/L<<546.0,127.0>--<545.0,123.0>> = 14.036243467926484

	* petapp (U+E006): B<<548.0,432.0>-<547.0,433.0>-<545.0,434.0>>/L<<545.0,434.0>--<548.0,432.0>> = 7.125016348901757

	* petapp (U+E006): B<<548.0,72.0>-<549.0,72.0>-<551.0,73.0>>/L<<551.0,73.0>--<548.0,72.0>> = 8.130102354155916

	* petapp (U+E006): B<<575.0,404.0>-<576.0,403.0>-<577.0,401.0>>/L<<577.0,401.0>--<575.0,404.0>> = 7.125016348901705

	* petapp (U+E006): B<<587.0,380.0>-<587.0,382.0>-<586.0,384.0>>/L<<586.0,384.0>--<587.0,380.0>> = 12.528807709151492

	* petapp (U+E006): B<<610.0,384.0>-<611.0,381.0>-<612.0,379.0>>/L<<612.0,379.0>--<610.0,384.0>> = 4.763641690726066

	* petapp (U+E006): B<<614.0,384.0>-<615.0,382.0>-<616.0,379.0>>/L<<616.0,379.0>--<614.0,384.0>> = 3.366460663429615

	* petapp (U+E006): B<<627.0,343.0>-<628.0,342.0>-<629.0,340.0>>/L<<629.0,340.0>--<627.0,343.0>> = 7.125016348901705

	* petapp (U+E006): B<<633.0,334.0>-<633.0,333.0>-<634.0,331.0>>/L<<634.0,331.0>--<633.0,334.0>> = 8.130102354155916

	* petapp (U+E006): B<<638.0,346.0>-<639.0,345.0>-<640.0,343.0>>/L<<640.0,343.0>--<638.0,346.0>> = 7.125016348901705

	* petapp (U+E006): B<<641.0,321.0>-<642.0,320.0>-<643.0,318.0>>/L<<643.0,318.0>--<641.0,321.0>> = 7.125016348901705

	* petapp (U+E006): B<<669.0,316.0>-<670.0,315.0>-<672.0,314.0>>/L<<672.0,314.0>--<669.0,316.0>> = 7.125016348901757

	* petapp (U+E006): B<<669.0,456.0>-<667.0,454.0>-<666.0,452.0>>/L<<666.0,452.0>--<669.0,456.0>> = 10.304846468766044

	* petapp (U+E006): B<<670.0,137.0>-<671.0,138.0>-<672.0,140.0>>/L<<672.0,140.0>--<670.0,137.0>> = 7.125016348901705

	* petapp (U+E006): B<<679.0,141.0>-<681.0,142.0>-<682.0,143.0>>/L<<682.0,143.0>--<679.0,141.0>> = 11.309932474020195

	* petapp (U+E006): B<<687.0,164.0>-<688.0,166.0>-<689.0,167.0>>/L<<689.0,167.0>--<687.0,164.0>> = 11.309932474020227

	* petapp (U+E006): B<<713.0,484.0>-<712.0,484.0>-<710.0,483.0>>/L<<710.0,483.0>--<713.0,484.0>> = 8.13010235415587

	* petapp (U+E006): B<<763.0,5.0>-<762.0,7.0>-<761.0,8.0>>/L<<761.0,8.0>--<763.0,5.0>> = 11.309932474020195

	* petapp (U+E006): L<<274.0,517.0>--<273.0,520.0>>/B<<273.0,520.0>-<274.0,518.0>-<274.0,517.0>> = 8.130102354155916

	* petapp (U+E006): L<<280.0,491.0>--<279.0,494.0>>/B<<279.0,494.0>-<280.0,492.0>-<280.0,491.0>> = 8.130102354155916

	* petapp (U+E006): L<<291.0,468.0>--<289.0,471.0>>/B<<289.0,471.0>-<290.0,469.0>-<291.0,468.0>> = 7.125016348901705

	* petapp (U+E006): L<<296.0,459.0>--<295.0,462.0>>/B<<295.0,462.0>-<296.0,460.0>-<296.0,459.0>> = 8.130102354155916

	* petapp (U+E006): L<<312.0,442.0>--<308.0,445.0>>/B<<308.0,445.0>-<310.0,444.0>-<312.0,442.0>> = 10.304846468766009

	* petapp (U+E006): L<<331.0,427.0>--<328.0,429.0>>/B<<328.0,429.0>-<329.0,428.0>-<331.0,427.0>> = 11.309932474020195

	* petapp (U+E006): L<<380.0,128.0>--<379.0,131.0>>/B<<379.0,131.0>-<380.0,129.0>-<380.0,128.0>> = 8.130102354155916

	* petapp (U+E006): L<<387.0,108.0>--<386.0,111.0>>/B<<386.0,111.0>-<387.0,109.0>-<387.0,108.0>> = 8.130102354155916

	* petapp (U+E006): L<<499.0,225.0>--<505.0,222.0>>/L<<505.0,222.0>--<498.0,226.0>> = 3.1798301198640497

	* petapp (U+E006): L<<504.0,71.0>--<499.0,69.0>>/B<<499.0,69.0>-<502.0,71.0>-<504.0,71.0>> = 11.888658039627936

	* petapp (U+E006): L<<517.0,66.0>--<513.0,65.0>>/B<<513.0,65.0>-<515.0,65.0>-<517.0,66.0>> = 14.036243467926484

	* petapp (U+E006): L<<523.0,67.0>--<519.0,66.0>>/B<<519.0,66.0>-<521.0,66.0>-<523.0,67.0>> = 14.036243467926484

	* petapp (U+E006): L<<532.0,68.0>--<536.0,69.0>>/B<<536.0,69.0>-<534.0,69.0>-<532.0,68.0>> = 14.036243467926484

	* petapp (U+E006): L<<534.0,195.0>--<536.0,192.0>>/B<<536.0,192.0>-<535.0,194.0>-<534.0,195.0>> = 7.125016348901757

	* petapp (U+E006): L<<534.0,310.0>--<537.0,308.0>>/B<<537.0,308.0>-<536.0,309.0>-<534.0,310.0>> = 11.309932474020227

	* petapp (U+E006): L<<536.0,440.0>--<539.0,438.0>>/B<<539.0,438.0>-<538.0,439.0>-<536.0,440.0>> = 11.309932474020227

	* petapp (U+E006): L<<541.0,111.0>--<539.0,108.0>>/B<<539.0,108.0>-<540.0,109.0>-<541.0,111.0>> = 11.309932474020227

	* petapp (U+E006): L<<541.0,70.0>--<545.0,71.0>>/B<<545.0,71.0>-<540.0,70.0>-<541.0,70.0>> = 2.726310993906212

	* petapp (U+E006): L<<542.0,181.0>--<543.0,178.0>>/B<<543.0,178.0>-<542.0,180.0>-<542.0,181.0>> = 8.13010235415587

	* petapp (U+E006): L<<545.0,434.0>--<548.0,432.0>>/B<<548.0,432.0>-<547.0,433.0>-<545.0,434.0>> = 11.309932474020227

	* petapp (U+E006): L<<546.0,127.0>--<545.0,123.0>>/B<<545.0,123.0>-<546.0,125.0>-<546.0,127.0>> = 12.528807709151492

	* petapp (U+E006): L<<556.0,74.0>--<553.0,73.0>>/B<<553.0,73.0>-<555.0,74.0>-<556.0,74.0>> = 8.130102354155916

	* petapp (U+E006): L<<577.0,401.0>--<575.0,404.0>>/B<<575.0,404.0>-<576.0,403.0>-<577.0,401.0>> = 11.309932474020227

	* petapp (U+E006): L<<583.0,256.0>--<584.0,252.0>>/B<<584.0,252.0>-<584.0,254.0>-<583.0,256.0>> = 14.036243467926484

	* petapp (U+E006): L<<586.0,384.0>--<587.0,380.0>>/B<<587.0,380.0>-<587.0,382.0>-<586.0,384.0>> = 14.036243467926484

	* petapp (U+E006): L<<598.0,432.0>--<599.0,429.0>>/B<<599.0,429.0>-<598.0,431.0>-<598.0,432.0>> = 8.13010235415587

	* petapp (U+E006): L<<602.0,122.0>--<601.0,125.0>>/B<<601.0,125.0>-<602.0,123.0>-<602.0,122.0>> = 8.130102354155916

	* petapp (U+E006): L<<611.0,96.0>--<611.0,96.0>>/B<<611.0,96.0>-<607.0,95.0>-<603.5,92.5>> = 14.036243467926484

	* petapp (U+E006): L<<612.0,379.0>--<610.0,384.0>>/B<<610.0,384.0>-<611.0,381.0>-<612.0,379.0>> = 3.366460663429615

	* petapp (U+E006): L<<613.0,374.0>--<612.0,377.0>>/B<<612.0,377.0>-<613.0,375.0>-<613.0,374.0>> = 8.130102354155916

	* petapp (U+E006): L<<615.0,369.0>--<614.0,372.0>>/B<<614.0,372.0>-<615.0,370.0>-<615.0,369.0>> = 8.130102354155916

	* petapp (U+E006): L<<616.0,379.0>--<614.0,384.0>>/B<<614.0,384.0>-<615.0,382.0>-<616.0,379.0>> = 4.763641690726066

	* petapp (U+E006): L<<629.0,340.0>--<627.0,343.0>>/B<<627.0,343.0>-<628.0,342.0>-<629.0,340.0>> = 11.309932474020227

	* petapp (U+E006): L<<640.0,343.0>--<638.0,346.0>>/B<<638.0,346.0>-<639.0,345.0>-<640.0,343.0>> = 11.309932474020227

	* petapp (U+E006): L<<643.0,318.0>--<641.0,321.0>>/B<<641.0,321.0>-<642.0,320.0>-<643.0,318.0>> = 11.309932474020227

	* petapp (U+E006): L<<657.0,433.0>--<658.0,436.0>>/B<<658.0,436.0>-<657.0,434.0>-<657.0,432.5>> = 8.13010235415587

	* petapp (U+E006): L<<661.0,383.0>--<660.0,386.0>>/B<<660.0,386.0>-<661.0,384.0>-<661.0,383.0>> = 8.130102354155916

	* petapp (U+E006): L<<666.0,452.0>--<669.0,456.0>>/B<<669.0,456.0>-<667.0,454.0>-<666.0,452.0>> = 8.13010235415596

	* petapp (U+E006): L<<672.0,140.0>--<670.0,137.0>>/B<<670.0,137.0>-<671.0,138.0>-<672.0,140.0>> = 11.309932474020227

	* petapp (U+E006): L<<682.0,143.0>--<679.0,141.0>>/B<<679.0,141.0>-<681.0,142.0>-<682.0,143.0>> = 7.125016348901757

	* petapp (U+E006): L<<686.0,162.0>--<685.0,159.0>>/B<<685.0,159.0>-<686.0,161.0>-<686.0,162.0>> = 8.130102354155916

	* petapp (U+E006): L<<689.0,167.0>--<687.0,164.0>>/B<<687.0,164.0>-<688.0,166.0>-<689.0,167.0>> = 7.125016348901705

	* petapp (U+E006): L<<689.0,256.0>--<690.0,253.0>>/B<<690.0,253.0>-<689.0,255.0>-<689.0,256.0>> = 8.13010235415587

	* petapp (U+E006): L<<691.0,251.0>--<692.0,248.0>>/B<<692.0,248.0>-<691.0,250.0>-<691.0,251.0>> = 8.13010235415587

	* petapp (U+E006): L<<700.0,480.0>--<703.0,481.0>>/B<<703.0,481.0>-<701.0,480.0>-<700.0,479.5>> = 8.13010235415587

	* petapp (U+E006): L<<705.0,482.0>--<708.0,483.0>>/B<<708.0,483.0>-<706.0,482.0>-<705.0,482.0>> = 8.13010235415587

	* petapp (U+E006): L<<708.0,293.0>--<705.0,294.0>>/B<<705.0,294.0>-<707.0,293.0>-<708.0,293.0>> = 8.130102354155916

	* petapp (U+E006): L<<728.0,285.0>--<725.0,286.0>>/B<<725.0,286.0>-<727.0,285.0>-<728.0,285.0>> = 8.130102354155916

	* petapp (U+E006): L<<761.0,8.0>--<763.0,5.0>>/B<<763.0,5.0>-<762.0,7.0>-<761.0,8.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<581.0,372.0>-<585.0,368.0>-<588.0,366.0>>/L<<588.0,366.0>--<581.0,372.0>> = 6.911227119024609

	* petapp.minimal (U+E007): B<<631.0,435.0>-<631.0,433.0>-<632.0,430.0>>/L<<632.0,430.0>--<631.0,435.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<632.0,481.0>-<632.0,480.0>-<631.0,478.0>>/L<<631.0,478.0>--<632.0,481.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<645.0,399.0>-<646.0,397.0>-<647.0,396.0>>/L<<647.0,396.0>--<645.0,399.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<646.0,510.0>-<645.0,508.0>-<644.0,507.0>>/L<<644.0,507.0>--<646.0,510.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<676.0,538.0>-<674.0,537.0>-<673.0,536.0>>/L<<673.0,536.0>--<676.0,538.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<700.0,247.0>-<699.0,248.0>-<698.0,250.0>>/L<<698.0,250.0>--<700.0,247.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<714.0,147.0>-<714.0,148.0>-<713.0,150.0>>/L<<713.0,150.0>--<714.0,147.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<720.0,137.0>-<719.0,139.0>-<718.0,140.0>>/L<<718.0,140.0>--<720.0,137.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<732.0,185.0>-<731.0,187.0>-<731.0,189.0>>/L<<731.0,189.0>--<732.0,185.0>> = 14.036243467926484

	* petapp.minimal (U+E007): B<<743.0,53.0>-<743.0,54.0>-<742.0,56.0>>/L<<742.0,56.0>--<743.0,53.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<212.0,538.0>--<212.0,800.0>>/B<<212.0,800.0>-<214.0,769.0>-<226.5,742.0>> = 3.6913859864512575

	* petapp.minimal (U+E007): L<<628.0,462.0>--<629.0,465.0>>/B<<629.0,465.0>-<628.0,463.0>-<628.0,462.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<630.0,473.0>--<631.0,476.0>>/B<<631.0,476.0>-<630.0,474.0>-<630.0,473.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<632.0,430.0>--<631.0,435.0>>/B<<631.0,435.0>-<631.0,433.0>-<632.0,430.0>> = 11.309932474020227

	* petapp.minimal (U+E007): L<<637.0,222.0>--<640.0,221.0>>/B<<640.0,221.0>-<638.0,222.0>-<637.0,222.5>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<639.0,498.0>--<640.0,501.0>>/B<<640.0,501.0>-<639.0,499.0>-<639.0,498.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<644.0,507.0>--<646.0,510.0>>/B<<646.0,510.0>-<645.0,508.0>-<644.0,507.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<647.0,396.0>--<645.0,399.0>>/B<<645.0,399.0>-<646.0,397.0>-<647.0,396.0>> = 7.125016348901705

	* petapp.minimal (U+E007): L<<673.0,536.0>--<676.0,538.0>>/B<<676.0,538.0>-<674.0,537.0>-<673.0,536.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<682.0,542.0>--<685.0,543.0>>/B<<685.0,543.0>-<683.0,542.0>-<682.0,542.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<687.0,544.0>--<690.0,545.0>>/B<<690.0,545.0>-<688.0,544.0>-<687.0,544.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<698.0,250.0>--<700.0,247.0>>/B<<700.0,247.0>-<699.0,248.0>-<698.0,250.0>> = 11.309932474020195

	* petapp.minimal (U+E007): L<<718.0,218.0>--<719.0,215.0>>/B<<719.0,215.0>-<718.0,217.0>-<718.0,218.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<731.0,113.0>--<732.0,110.0>>/B<<732.0,110.0>-<731.0,112.0>-<731.0,113.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<740.0,156.0>--<739.0,160.0>>/B<<739.0,160.0>-<740.0,153.0>-<740.0,156.0>> = 5.906141113770497

	* petapp.minimal (U+E007): L<<744.0,137.0>--<743.0,140.0>>/B<<743.0,140.0>-<744.0,138.0>-<744.0,137.0>> = 8.130102354155916

	* petapp.minimal (U+E007): L<<746.0,123.0>--<747.0,120.0>>/B<<747.0,120.0>-<746.0,122.0>-<746.0,123.0>> = 8.13010235415587

	* petapp.wpda (U+E008): B<<485.0,2.0>-<482.0,5.0>-<482.0,6.0>>/L<<482.0,6.0>--<481.0,1.0>> = 11.309932474020227

	* petapp.wpda (U+E008): L<<185.0,222.0>--<180.0,218.0>>/B<<180.0,218.0>-<182.0,219.0>-<183.0,218.0>> = 12.094757077012058

	* pisafe (U+E010): B<<175.0,538.0>-<175.0,536.0>-<174.0,534.0>>/L<<174.0,534.0>--<175.0,538.0>> = 12.528807709151492

	* pisafe (U+E010): B<<190.0,573.0>-<189.0,572.0>-<188.0,570.0>>/L<<188.0,570.0>--<190.0,573.0>> = 7.125016348901757

	* pisafe (U+E010): B<<211.0,602.0>-<210.0,600.0>-<208.0,598.0>>/L<<208.0,598.0>--<211.0,602.0>> = 8.13010235415596

	* pisafe (U+E010): B<<784.0,594.0>-<783.0,596.0>-<782.0,597.0>>/L<<782.0,597.0>--<784.0,594.0>> = 11.309932474020195

	* pisafe (U+E010): B<<797.0,577.0>-<796.0,579.0>-<795.0,580.0>>/L<<795.0,580.0>--<797.0,577.0>> = 11.309932474020195

	* pisafe (U+E010): B<<816.0,530.0>-<816.0,532.0>-<815.0,534.0>>/L<<815.0,534.0>--<816.0,530.0>> = 12.528807709151492

	* pisafe (U+E010): B<<820.0,515.0>-<820.0,516.0>-<819.0,518.0>>/L<<819.0,518.0>--<820.0,515.0>> = 8.13010235415587

	* pisafe (U+E010): L<<174.0,534.0>--<175.0,538.0>>/B<<175.0,538.0>-<175.0,536.0>-<174.0,534.0>> = 14.036243467926484

	* pisafe (U+E010): L<<188.0,570.0>--<190.0,573.0>>/B<<190.0,573.0>-<189.0,572.0>-<188.0,570.0>> = 11.309932474020195

	* pisafe (U+E010): L<<208.0,598.0>--<211.0,602.0>>/B<<211.0,602.0>-<210.0,600.0>-<208.0,598.0>> = 10.304846468766044

	* pisafe (U+E010): L<<750.0,626.0>--<754.0,623.0>>/B<<754.0,623.0>-<752.0,624.0>-<750.0,626.0>> = 10.304846468766009

	* pisafe (U+E010): L<<782.0,597.0>--<784.0,594.0>>/B<<784.0,594.0>-<783.0,596.0>-<782.0,597.0>> = 7.125016348901757

	* pisafe (U+E010): L<<795.0,580.0>--<797.0,577.0>>/B<<797.0,577.0>-<796.0,579.0>-<795.0,580.0>> = 7.125016348901757

	* pisafe (U+E010): L<<815.0,534.0>--<816.0,530.0>>/B<<816.0,530.0>-<816.0,532.0>-<815.0,534.0>> = 14.036243467926484

	* pisafe (U+E010): L<<817.0,528.0>--<818.0,525.0>>/B<<818.0,525.0>-<817.0,527.0>-<817.0,528.0>> = 8.13010235415587

	* uni0200 (U+0200): L<<433.0,865.0>--<413.0,907.0>>/L<<413.0,907.0>--<421.0,875.0>> = 11.42710159394516

	* uni0201 (U+0201): L<<340.0,663.0>--<320.0,705.0>>/L<<320.0,705.0>--<328.0,673.0>> = 11.42710159394516

	* uni0204 (U+0204): L<<397.0,865.0>--<377.0,907.0>>/L<<377.0,907.0>--<385.0,875.0>> = 11.42710159394516

	* uni0205 (U+0205): L<<356.0,663.0>--<336.0,705.0>>/L<<336.0,705.0>--<344.0,673.0>> = 11.42710159394516

	* uni0208 (U+0208): L<<217.0,865.0>--<197.0,907.0>>/L<<197.0,907.0>--<205.0,875.0>> = 11.42710159394516

	* uni0209 (U+0209): L<<164.0,663.0>--<144.0,705.0>>/L<<144.0,705.0>--<152.0,673.0>> = 11.42710159394516

	* uni020C (U+020C): L<<518.0,865.0>--<498.0,907.0>>/L<<498.0,907.0>--<506.0,875.0>> = 11.42710159394516

	* uni020D (U+020D): L<<377.0,663.0>--<357.0,705.0>>/L<<357.0,705.0>--<365.0,673.0>> = 11.42710159394516

	* uni0210 (U+0210): L<<407.0,865.0>--<387.0,907.0>>/L<<387.0,907.0>--<395.0,875.0>> = 11.42710159394516

	* uni0211 (U+0211): L<<261.0,663.0>--<241.0,705.0>>/L<<241.0,705.0>--<249.0,673.0>> = 11.42710159394516

	* uni0214 (U+0214): L<<436.0,865.0>--<416.0,907.0>>/L<<416.0,907.0>--<424.0,875.0>> = 11.42710159394516

	* uni0215 (U+0215): L<<346.0,663.0>--<326.0,705.0>>/L<<326.0,705.0>--<334.0,673.0>> = 11.42710159394516 

	* uni030F (U+030F): L<<452.0,663.0>--<432.0,705.0>>/L<<432.0,705.0>--<440.0,673.0>> = 11.42710159394516 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[20] PitagonSansText-Light.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check OFL body text is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text">com.google.fonts/check/license/OFL_body_text</a>)</summary><div>


* 🔥 **FAIL** The OFL.txt body text is incorrect. Please use https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt as a template. You should only modify the first line. [code: incorrect-ofl-body-text]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ
at: https://scripts.sil.org/OFL." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks">com.google.fonts/check/name/line_breaks</a>)</summary><div>


* 🔥 **FAIL** Name entry DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1294, but got 1214 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.11, while a newer 0.8.13 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'Pita' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
</div></details><details><summary>⚠ <b>WARN:</b> Description strings in the name table must not exceed 200 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/description_max_length">com.google.fonts/check/name/description_max_length</a>)</summary><div>


* ⚠ **WARN** A few name table entries with ID=10 (NameID.DESCRIPTION) are longer than 200 characters. Please check whether those entries are copyright notices mistakenly stored in the description string entries by a bug in an old FontLab version. If that's the case, then such copyright notices must be removed from these entries. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Pitagon Sans Text Light' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- dotlessi.wide 

	- registered.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* petapp (U+E006): L<<282.0,304.0>--<312.0,286.0>> -> L<<312.0,286.0>--<339.0,271.0>>

	* petapp (U+E006): L<<312.0,333.0>--<273.0,356.0>> -> L<<273.0,356.0>--<257.0,365.0>>

	* petapp (U+E006): L<<355.0,309.0>--<312.0,333.0>> -> L<<312.0,333.0>--<273.0,356.0>>

	* petapp (U+E006): L<<371.0,299.0>--<355.0,309.0>> -> L<<355.0,309.0>--<312.0,333.0>>

	* petapp (U+E006): L<<371.0,640.0>--<467.0,585.0>> -> L<<467.0,585.0>--<515.0,556.0>>

	* petapp (U+E006): L<<373.0,298.0>--<371.0,299.0>> -> L<<371.0,299.0>--<355.0,309.0>>

	* petapp (U+E006): L<<426.0,268.0>--<373.0,298.0>> -> L<<373.0,298.0>--<371.0,299.0>>

	* petapp (U+E006): L<<467.0,585.0>--<515.0,556.0>> -> L<<515.0,556.0>--<534.0,545.0>>

	* petapp (U+E006): L<<468.0,243.0>--<426.0,268.0>> -> L<<426.0,268.0>--<373.0,298.0>>

	* petapp (U+E006): L<<474.0,240.0>--<468.0,243.0>> -> L<<468.0,243.0>--<426.0,268.0>>

	* petapp (U+E006): L<<498.0,226.0>--<474.0,240.0>> -> L<<474.0,240.0>--<468.0,243.0>>

	* petapp (U+E006): L<<505.0,222.0>--<498.0,226.0>> -> L<<498.0,226.0>--<474.0,240.0>>

	* petapp (U+E006): L<<691.0,61.0>--<692.0,60.0>> -> L<<692.0,60.0>--<696.0,56.0>>

	* petapp (U+E006): L<<721.0,485.0>--<725.0,485.0>> -> L<<725.0,485.0>--<764.0,485.0>>

	* petapp.minimal (U+E007): L<<264.0,373.0>--<351.0,339.0>> -> L<<351.0,339.0>--<432.0,305.0>>

	* petapp.minimal (U+E007): L<<351.0,339.0>--<432.0,305.0>> -> L<<432.0,305.0>--<448.0,299.0>>

	* petapp.minimal (U+E007): L<<381.0,352.0>--<331.0,376.0>> -> L<<331.0,376.0>--<305.0,390.0>>

	* petapp.minimal (U+E007): L<<432.0,305.0>--<448.0,299.0>> -> L<<448.0,299.0>--<504.0,276.0>>

	* petapp.minimal (U+E007): L<<432.0,326.0>--<381.0,352.0>> -> L<<381.0,352.0>--<331.0,376.0>>

	* petapp.minimal (U+E007): L<<435.0,187.0>--<405.0,192.0>> -> L<<405.0,192.0>--<304.0,211.0>>

	* petapp.minimal (U+E007): L<<448.0,299.0>--<504.0,276.0>> -> L<<504.0,276.0>--<612.0,232.0>>

	* petapp.minimal (U+E007): L<<455.0,314.0>--<432.0,326.0>> -> L<<432.0,326.0>--<381.0,352.0>>

	* petapp.minimal (U+E007): L<<504.0,175.0>--<435.0,187.0>> -> L<<435.0,187.0>--<405.0,192.0>>

	* petapp.minimal (U+E007): L<<504.0,276.0>--<612.0,232.0>> -> L<<612.0,232.0>--<621.0,229.0>>

	* petapp.minimal (U+E007): L<<504.0,289.0>--<455.0,314.0>> -> L<<455.0,314.0>--<432.0,326.0>>

	* petapp.minimal (U+E007): L<<588.0,160.0>--<504.0,175.0>> -> L<<504.0,175.0>--<435.0,187.0>>

	* petapp.minimal (U+E007): L<<621.0,229.0>--<504.0,289.0>> -> L<<504.0,289.0>--<455.0,314.0>>

	* petapp.minimal (U+E007): L<<742.0,30.0>--<742.0,31.0>> -> L<<742.0,31.0>--<742.0,32.0>>

	* petapp.minimal (U+E007): L<<743.0,33.0>--<743.0,34.0>> -> L<<743.0,34.0>--<743.0,36.0>>

	* petapp.minimal (U+E007): L<<743.0,34.0>--<743.0,36.0>> -> L<<743.0,36.0>--<743.0,37.0>>

	* petapp.minimal (U+E007): L<<747.0,73.0>--<746.0,63.0>> -> L<<746.0,63.0>--<743.0,38.0>>

	* petapp.minimal (U+E007): L<<747.0,74.0>--<747.0,73.0>> -> L<<747.0,73.0>--<746.0,63.0>>

	* petapp.minimal (U+E007): L<<752.0,131.0>--<747.0,74.0>> -> L<<747.0,74.0>--<747.0,73.0>>

	* petapp.minimal (U+E007): L<<754.0,162.0>--<752.0,131.0>> -> L<<752.0,131.0>--<747.0,74.0>>

	* petapp.minimal (U+E007): L<<755.0,175.0>--<754.0,162.0>> -> L<<754.0,162.0>--<752.0,131.0>>

	* petapp.minimal (U+E007): L<<757.0,196.0>--<755.0,175.0>> -> L<<755.0,175.0>--<754.0,162.0>>

	* petapp.minimal (U+E007): L<<758.0,210.0>--<757.0,196.0>> -> L<<757.0,196.0>--<755.0,175.0>>

	* petapp.minimal (U+E007): L<<758.0,213.0>--<758.0,210.0>> -> L<<758.0,210.0>--<757.0,196.0>>

	* petapp.wpda (U+E008): L<<640.0,140.0>--<627.0,132.0>> -> L<<627.0,132.0>--<618.0,127.0>>

	* piads (U+E001): L<<112.0,541.0>--<116.0,544.0>> -> L<<116.0,544.0>--<445.0,782.0>>

	* piads (U+E001): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<878.0,541.0>>

	* picall (U+E009): L<<112.0,541.0>--<116.0,544.0>> -> L<<116.0,544.0>--<445.0,782.0>>

	* picall (U+E009): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<878.0,541.0>>

	* pioffice (U+E002): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<877.0,542.0>>

	* pisafe (U+E010): L<<167.0,362.0>--<167.0,491.0>> -> L<<167.0,491.0>--<167.0,494.0>>

	* pisafe (U+E010): L<<203.0,695.0>--<239.0,708.0>> -> L<<239.0,708.0>--<389.0,762.0>>

	* pisafe (U+E010): L<<239.0,708.0>--<389.0,762.0>> -> L<<389.0,762.0>--<494.0,800.0>>

	* pisafe (U+E010): L<<495.0,800.0>--<600.0,762.0>> -> L<<600.0,762.0>--<750.0,708.0>>

	* pisafe (U+E010): L<<600.0,762.0>--<750.0,708.0>> -> L<<750.0,708.0>--<786.0,695.0>>

	* pisign (U+E005): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<877.0,542.0>>

	* pitagon (U+E000): L<<112.0,543.0>--<116.0,546.0>> -> L<<116.0,546.0>--<445.0,784.0>>

	* pitagon (U+E000): L<<209.0,62.0>--<84.0,446.0>> -> L<<84.0,446.0>--<82.0,452.0>>

	* pitagon (U+E000): L<<547.0,784.0>--<874.0,546.0>> -> L<<874.0,546.0>--<878.0,543.0>>

	* pitagram (U+E003): L<<813.0,512.0>--<810.0,514.0>> -> L<<810.0,514.0>--<537.0,711.0>>

	* piweb (U+E004): L<<813.0,512.0>--<810.0,514.0>> -> L<<810.0,514.0>--<537.0,711.0>>

	* sparks (U+E011): L<<100.0,798.0>--<103.0,797.0>> -> L<<103.0,797.0>--<198.0,762.0>>

	* sparks (U+E011): L<<103.0,797.0>--<198.0,762.0>> -> L<<198.0,762.0>--<209.0,759.0>>

	* sparks (U+E011): L<<198.0,762.0>--<209.0,759.0>> -> L<<209.0,759.0>--<400.0,690.0>>

	* sparks (U+E011): L<<209.0,759.0>--<400.0,690.0>> -> L<<400.0,690.0>--<431.0,680.0>>

	* sparks (U+E011): L<<291.0,596.0>--<363.0,534.0>> -> L<<363.0,534.0>--<382.0,516.0>>

	* sparks (U+E011): L<<381.0,366.0>--<383.0,367.0>> -> L<<383.0,367.0>--<486.0,429.0>>

	* sparks (U+E011): L<<383.0,367.0>--<486.0,429.0>> -> L<<486.0,429.0>--<488.0,430.0>>

	* sparks (U+E011): L<<409.0,102.0>--<98.0,641.0>> -> L<<98.0,641.0>--<47.0,731.0>>

	* sparks (U+E011): L<<440.0,659.0>--<436.0,649.0>> -> L<<436.0,649.0>--<434.0,643.0>>

	* sparks (U+E011): L<<454.0,24.0>--<409.0,102.0>> -> L<<409.0,102.0>--<98.0,641.0>>

	* sparks (U+E011): L<<504.0,429.0>--<606.0,367.0>> -> L<<606.0,367.0>--<608.0,366.0>>

	* sparks (U+E011): L<<558.0,680.0>--<596.0,694.0>> -> L<<596.0,694.0>--<780.0,759.0>>

	* sparks (U+E011): L<<579.0,101.0>--<550.0,51.0>> -> L<<550.0,51.0>--<535.0,24.0>>

	* sparks (U+E011): L<<596.0,694.0>--<780.0,759.0>> -> L<<780.0,759.0>--<807.0,768.0>>

	* sparks (U+E011): L<<607.0,516.0>--<627.0,534.0>> -> L<<627.0,534.0>--<699.0,596.0>>

	* sparks (U+E011): L<<614.0,629.0>--<577.0,632.0>> -> L<<577.0,632.0>--<568.0,633.0>>

	* sparks (U+E011): L<<655.0,626.0>--<614.0,629.0>> -> L<<614.0,629.0>--<577.0,632.0>>

	* sparks (U+E011): L<<656.0,626.0>--<655.0,626.0>> -> L<<655.0,626.0>--<614.0,629.0>>

	* sparks (U+E011): L<<690.0,623.0>--<656.0,626.0>> -> L<<656.0,626.0>--<655.0,626.0>>

	* sparks (U+E011): L<<691.0,623.0>--<690.0,623.0>> -> L<<690.0,623.0>--<656.0,626.0>>

	* sparks (U+E011): L<<750.0,397.0>--<579.0,101.0>> -> L<<579.0,101.0>--<550.0,51.0>>

	* sparks (U+E011): L<<780.0,759.0>--<807.0,768.0>> -> L<<807.0,768.0>--<886.0,797.0>>

	* sparks (U+E011): L<<897.0,652.0>--<750.0,397.0>> -> L<<750.0,397.0>--<579.0,101.0>>

	* sparks (U+E011): L<<942.0,730.0>--<897.0,652.0>> -> L<<897.0,652.0>--<750.0,397.0>> 

	* sparks (U+E011): L<<943.0,732.0>--<942.0,730.0>> -> L<<942.0,730.0>--<897.0,652.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* petapp (U+E006): B<<289.0,471.0>-<290.0,469.0>-<291.0,468.0>>/L<<291.0,468.0>--<289.0,471.0>> = 11.309932474020227

	* petapp (U+E006): B<<295.0,293.0>-<289.0,300.0>-<282.0,304.0>>/L<<282.0,304.0>--<312.0,286.0>> = 1.2188752351307344

	* petapp (U+E006): B<<328.0,429.0>-<329.0,428.0>-<331.0,427.0>>/L<<331.0,427.0>--<328.0,429.0>> = 7.125016348901757

	* petapp (U+E006): B<<415.0,76.0>-<416.0,76.0>-<418.0,75.0>>/L<<418.0,75.0>--<415.0,76.0>> = 8.130102354155916

	* petapp (U+E006): B<<424.0,71.0>-<425.0,71.0>-<427.0,70.0>>/L<<427.0,70.0>--<424.0,71.0>> = 8.130102354155916

	* petapp (U+E006): B<<439.0,65.0>-<440.0,65.0>-<442.0,64.0>>/L<<442.0,64.0>--<439.0,65.0>> = 8.130102354155916

	* petapp (U+E006): B<<483.0,64.0>-<484.0,64.0>-<486.0,65.0>>/L<<486.0,65.0>--<483.0,64.0>> = 8.130102354155916

	* petapp (U+E006): B<<513.0,65.0>-<515.0,65.0>-<517.0,66.0>>/L<<517.0,66.0>--<513.0,65.0>> = 12.528807709151463

	* petapp (U+E006): B<<519.0,66.0>-<521.0,66.0>-<523.0,67.0>>/L<<523.0,67.0>--<519.0,66.0>> = 12.528807709151463

	* petapp (U+E006): B<<529.0,68.0>-<528.0,68.0>-<526.0,67.0>>/L<<526.0,67.0>--<529.0,68.0>> = 8.13010235415587

	* petapp (U+E006): B<<536.0,192.0>-<535.0,194.0>-<534.0,195.0>>/L<<534.0,195.0>--<536.0,192.0>> = 11.309932474020195

	* petapp (U+E006): B<<536.0,69.0>-<534.0,69.0>-<532.0,68.0>>/L<<532.0,68.0>--<536.0,69.0>> = 12.528807709151492

	* petapp (U+E006): B<<537.0,308.0>-<536.0,309.0>-<534.0,310.0>>/L<<534.0,310.0>--<537.0,308.0>> = 7.125016348901757

	* petapp (U+E006): B<<539.0,108.0>-<540.0,109.0>-<541.0,111.0>>/L<<541.0,111.0>--<539.0,108.0>> = 7.125016348901705

	* petapp (U+E006): B<<539.0,438.0>-<538.0,439.0>-<536.0,440.0>>/L<<536.0,440.0>--<539.0,438.0>> = 7.125016348901757

	* petapp (U+E006): B<<545.0,123.0>-<546.0,125.0>-<546.0,127.0>>/L<<546.0,127.0>--<545.0,123.0>> = 14.036243467926484

	* petapp (U+E006): B<<548.0,432.0>-<547.0,433.0>-<545.0,434.0>>/L<<545.0,434.0>--<548.0,432.0>> = 7.125016348901757

	* petapp (U+E006): B<<548.0,72.0>-<549.0,72.0>-<551.0,73.0>>/L<<551.0,73.0>--<548.0,72.0>> = 8.130102354155916

	* petapp (U+E006): B<<575.0,404.0>-<576.0,403.0>-<577.0,401.0>>/L<<577.0,401.0>--<575.0,404.0>> = 7.125016348901705

	* petapp (U+E006): B<<587.0,380.0>-<587.0,382.0>-<586.0,384.0>>/L<<586.0,384.0>--<587.0,380.0>> = 12.528807709151492

	* petapp (U+E006): B<<610.0,384.0>-<611.0,381.0>-<612.0,379.0>>/L<<612.0,379.0>--<610.0,384.0>> = 4.763641690726066

	* petapp (U+E006): B<<614.0,384.0>-<615.0,382.0>-<616.0,379.0>>/L<<616.0,379.0>--<614.0,384.0>> = 3.366460663429615

	* petapp (U+E006): B<<627.0,343.0>-<628.0,342.0>-<629.0,340.0>>/L<<629.0,340.0>--<627.0,343.0>> = 7.125016348901705

	* petapp (U+E006): B<<633.0,334.0>-<633.0,333.0>-<634.0,331.0>>/L<<634.0,331.0>--<633.0,334.0>> = 8.130102354155916

	* petapp (U+E006): B<<638.0,346.0>-<639.0,345.0>-<640.0,343.0>>/L<<640.0,343.0>--<638.0,346.0>> = 7.125016348901705

	* petapp (U+E006): B<<641.0,321.0>-<642.0,320.0>-<643.0,318.0>>/L<<643.0,318.0>--<641.0,321.0>> = 7.125016348901705

	* petapp (U+E006): B<<669.0,316.0>-<670.0,315.0>-<672.0,314.0>>/L<<672.0,314.0>--<669.0,316.0>> = 7.125016348901757

	* petapp (U+E006): B<<669.0,456.0>-<667.0,454.0>-<666.0,452.0>>/L<<666.0,452.0>--<669.0,456.0>> = 10.304846468766044

	* petapp (U+E006): B<<670.0,137.0>-<671.0,138.0>-<672.0,140.0>>/L<<672.0,140.0>--<670.0,137.0>> = 7.125016348901705

	* petapp (U+E006): B<<679.0,141.0>-<681.0,142.0>-<682.0,143.0>>/L<<682.0,143.0>--<679.0,141.0>> = 11.309932474020195

	* petapp (U+E006): B<<687.0,164.0>-<688.0,166.0>-<689.0,167.0>>/L<<689.0,167.0>--<687.0,164.0>> = 11.309932474020227

	* petapp (U+E006): B<<713.0,484.0>-<712.0,484.0>-<710.0,483.0>>/L<<710.0,483.0>--<713.0,484.0>> = 8.13010235415587

	* petapp (U+E006): B<<763.0,5.0>-<762.0,7.0>-<761.0,8.0>>/L<<761.0,8.0>--<763.0,5.0>> = 11.309932474020195

	* petapp (U+E006): L<<274.0,517.0>--<273.0,520.0>>/B<<273.0,520.0>-<274.0,518.0>-<274.0,517.0>> = 8.130102354155916

	* petapp (U+E006): L<<280.0,491.0>--<279.0,494.0>>/B<<279.0,494.0>-<280.0,492.0>-<280.0,491.0>> = 8.130102354155916

	* petapp (U+E006): L<<291.0,468.0>--<289.0,471.0>>/B<<289.0,471.0>-<290.0,469.0>-<291.0,468.0>> = 7.125016348901705

	* petapp (U+E006): L<<296.0,459.0>--<295.0,462.0>>/B<<295.0,462.0>-<296.0,460.0>-<296.0,459.0>> = 8.130102354155916

	* petapp (U+E006): L<<312.0,442.0>--<308.0,445.0>>/B<<308.0,445.0>-<310.0,444.0>-<312.0,442.0>> = 10.304846468766009

	* petapp (U+E006): L<<331.0,427.0>--<328.0,429.0>>/B<<328.0,429.0>-<329.0,428.0>-<331.0,427.0>> = 11.309932474020195

	* petapp (U+E006): L<<380.0,128.0>--<379.0,131.0>>/B<<379.0,131.0>-<380.0,129.0>-<380.0,128.0>> = 8.130102354155916

	* petapp (U+E006): L<<387.0,108.0>--<386.0,111.0>>/B<<386.0,111.0>-<387.0,109.0>-<387.0,108.0>> = 8.130102354155916

	* petapp (U+E006): L<<499.0,225.0>--<505.0,222.0>>/L<<505.0,222.0>--<498.0,226.0>> = 3.1798301198640497

	* petapp (U+E006): L<<504.0,71.0>--<499.0,69.0>>/B<<499.0,69.0>-<502.0,71.0>-<504.0,71.0>> = 11.888658039627936

	* petapp (U+E006): L<<517.0,66.0>--<513.0,65.0>>/B<<513.0,65.0>-<515.0,65.0>-<517.0,66.0>> = 14.036243467926484

	* petapp (U+E006): L<<523.0,67.0>--<519.0,66.0>>/B<<519.0,66.0>-<521.0,66.0>-<523.0,67.0>> = 14.036243467926484

	* petapp (U+E006): L<<532.0,68.0>--<536.0,69.0>>/B<<536.0,69.0>-<534.0,69.0>-<532.0,68.0>> = 14.036243467926484

	* petapp (U+E006): L<<534.0,195.0>--<536.0,192.0>>/B<<536.0,192.0>-<535.0,194.0>-<534.0,195.0>> = 7.125016348901757

	* petapp (U+E006): L<<534.0,310.0>--<537.0,308.0>>/B<<537.0,308.0>-<536.0,309.0>-<534.0,310.0>> = 11.309932474020227

	* petapp (U+E006): L<<536.0,440.0>--<539.0,438.0>>/B<<539.0,438.0>-<538.0,439.0>-<536.0,440.0>> = 11.309932474020227

	* petapp (U+E006): L<<541.0,111.0>--<539.0,108.0>>/B<<539.0,108.0>-<540.0,109.0>-<541.0,111.0>> = 11.309932474020227

	* petapp (U+E006): L<<541.0,70.0>--<545.0,71.0>>/B<<545.0,71.0>-<540.0,70.0>-<541.0,70.0>> = 2.726310993906212

	* petapp (U+E006): L<<542.0,181.0>--<543.0,178.0>>/B<<543.0,178.0>-<542.0,180.0>-<542.0,181.0>> = 8.13010235415587

	* petapp (U+E006): L<<545.0,434.0>--<548.0,432.0>>/B<<548.0,432.0>-<547.0,433.0>-<545.0,434.0>> = 11.309932474020227

	* petapp (U+E006): L<<546.0,127.0>--<545.0,123.0>>/B<<545.0,123.0>-<546.0,125.0>-<546.0,127.0>> = 12.528807709151492

	* petapp (U+E006): L<<556.0,74.0>--<553.0,73.0>>/B<<553.0,73.0>-<555.0,74.0>-<556.0,74.0>> = 8.130102354155916

	* petapp (U+E006): L<<577.0,401.0>--<575.0,404.0>>/B<<575.0,404.0>-<576.0,403.0>-<577.0,401.0>> = 11.309932474020227

	* petapp (U+E006): L<<583.0,256.0>--<584.0,252.0>>/B<<584.0,252.0>-<584.0,254.0>-<583.0,256.0>> = 14.036243467926484

	* petapp (U+E006): L<<586.0,384.0>--<587.0,380.0>>/B<<587.0,380.0>-<587.0,382.0>-<586.0,384.0>> = 14.036243467926484

	* petapp (U+E006): L<<598.0,432.0>--<599.0,429.0>>/B<<599.0,429.0>-<598.0,431.0>-<598.0,432.0>> = 8.13010235415587

	* petapp (U+E006): L<<602.0,122.0>--<601.0,125.0>>/B<<601.0,125.0>-<602.0,123.0>-<602.0,122.0>> = 8.130102354155916

	* petapp (U+E006): L<<611.0,96.0>--<611.0,96.0>>/B<<611.0,96.0>-<607.0,95.0>-<603.5,92.5>> = 14.036243467926484

	* petapp (U+E006): L<<612.0,379.0>--<610.0,384.0>>/B<<610.0,384.0>-<611.0,381.0>-<612.0,379.0>> = 3.366460663429615

	* petapp (U+E006): L<<613.0,374.0>--<612.0,377.0>>/B<<612.0,377.0>-<613.0,375.0>-<613.0,374.0>> = 8.130102354155916

	* petapp (U+E006): L<<615.0,369.0>--<614.0,372.0>>/B<<614.0,372.0>-<615.0,370.0>-<615.0,369.0>> = 8.130102354155916

	* petapp (U+E006): L<<616.0,379.0>--<614.0,384.0>>/B<<614.0,384.0>-<615.0,382.0>-<616.0,379.0>> = 4.763641690726066

	* petapp (U+E006): L<<629.0,340.0>--<627.0,343.0>>/B<<627.0,343.0>-<628.0,342.0>-<629.0,340.0>> = 11.309932474020227

	* petapp (U+E006): L<<640.0,343.0>--<638.0,346.0>>/B<<638.0,346.0>-<639.0,345.0>-<640.0,343.0>> = 11.309932474020227

	* petapp (U+E006): L<<643.0,318.0>--<641.0,321.0>>/B<<641.0,321.0>-<642.0,320.0>-<643.0,318.0>> = 11.309932474020227

	* petapp (U+E006): L<<657.0,433.0>--<658.0,436.0>>/B<<658.0,436.0>-<657.0,434.0>-<657.0,432.5>> = 8.13010235415587

	* petapp (U+E006): L<<661.0,383.0>--<660.0,386.0>>/B<<660.0,386.0>-<661.0,384.0>-<661.0,383.0>> = 8.130102354155916

	* petapp (U+E006): L<<666.0,452.0>--<669.0,456.0>>/B<<669.0,456.0>-<667.0,454.0>-<666.0,452.0>> = 8.13010235415596

	* petapp (U+E006): L<<672.0,140.0>--<670.0,137.0>>/B<<670.0,137.0>-<671.0,138.0>-<672.0,140.0>> = 11.309932474020227

	* petapp (U+E006): L<<682.0,143.0>--<679.0,141.0>>/B<<679.0,141.0>-<681.0,142.0>-<682.0,143.0>> = 7.125016348901757

	* petapp (U+E006): L<<686.0,162.0>--<685.0,159.0>>/B<<685.0,159.0>-<686.0,161.0>-<686.0,162.0>> = 8.130102354155916

	* petapp (U+E006): L<<689.0,167.0>--<687.0,164.0>>/B<<687.0,164.0>-<688.0,166.0>-<689.0,167.0>> = 7.125016348901705

	* petapp (U+E006): L<<689.0,256.0>--<690.0,253.0>>/B<<690.0,253.0>-<689.0,255.0>-<689.0,256.0>> = 8.13010235415587

	* petapp (U+E006): L<<691.0,251.0>--<692.0,248.0>>/B<<692.0,248.0>-<691.0,250.0>-<691.0,251.0>> = 8.13010235415587

	* petapp (U+E006): L<<700.0,480.0>--<703.0,481.0>>/B<<703.0,481.0>-<701.0,480.0>-<700.0,479.5>> = 8.13010235415587

	* petapp (U+E006): L<<705.0,482.0>--<708.0,483.0>>/B<<708.0,483.0>-<706.0,482.0>-<705.0,482.0>> = 8.13010235415587

	* petapp (U+E006): L<<708.0,293.0>--<705.0,294.0>>/B<<705.0,294.0>-<707.0,293.0>-<708.0,293.0>> = 8.130102354155916

	* petapp (U+E006): L<<728.0,285.0>--<725.0,286.0>>/B<<725.0,286.0>-<727.0,285.0>-<728.0,285.0>> = 8.130102354155916

	* petapp (U+E006): L<<761.0,8.0>--<763.0,5.0>>/B<<763.0,5.0>-<762.0,7.0>-<761.0,8.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<581.0,372.0>-<585.0,368.0>-<588.0,366.0>>/L<<588.0,366.0>--<581.0,372.0>> = 6.911227119024609

	* petapp.minimal (U+E007): B<<631.0,435.0>-<631.0,433.0>-<632.0,430.0>>/L<<632.0,430.0>--<631.0,435.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<632.0,481.0>-<632.0,480.0>-<631.0,478.0>>/L<<631.0,478.0>--<632.0,481.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<645.0,399.0>-<646.0,397.0>-<647.0,396.0>>/L<<647.0,396.0>--<645.0,399.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<646.0,510.0>-<645.0,508.0>-<644.0,507.0>>/L<<644.0,507.0>--<646.0,510.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<676.0,538.0>-<674.0,537.0>-<673.0,536.0>>/L<<673.0,536.0>--<676.0,538.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<700.0,247.0>-<699.0,248.0>-<698.0,250.0>>/L<<698.0,250.0>--<700.0,247.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<714.0,147.0>-<714.0,148.0>-<713.0,150.0>>/L<<713.0,150.0>--<714.0,147.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<720.0,137.0>-<719.0,139.0>-<718.0,140.0>>/L<<718.0,140.0>--<720.0,137.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<732.0,185.0>-<731.0,187.0>-<731.0,189.0>>/L<<731.0,189.0>--<732.0,185.0>> = 14.036243467926484

	* petapp.minimal (U+E007): B<<743.0,53.0>-<743.0,54.0>-<742.0,56.0>>/L<<742.0,56.0>--<743.0,53.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<212.0,538.0>--<212.0,800.0>>/B<<212.0,800.0>-<214.0,769.0>-<226.5,742.0>> = 3.6913859864512575

	* petapp.minimal (U+E007): L<<628.0,462.0>--<629.0,465.0>>/B<<629.0,465.0>-<628.0,463.0>-<628.0,462.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<630.0,473.0>--<631.0,476.0>>/B<<631.0,476.0>-<630.0,474.0>-<630.0,473.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<632.0,430.0>--<631.0,435.0>>/B<<631.0,435.0>-<631.0,433.0>-<632.0,430.0>> = 11.309932474020227

	* petapp.minimal (U+E007): L<<637.0,222.0>--<640.0,221.0>>/B<<640.0,221.0>-<638.0,222.0>-<637.0,222.5>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<639.0,498.0>--<640.0,501.0>>/B<<640.0,501.0>-<639.0,499.0>-<639.0,498.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<644.0,507.0>--<646.0,510.0>>/B<<646.0,510.0>-<645.0,508.0>-<644.0,507.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<647.0,396.0>--<645.0,399.0>>/B<<645.0,399.0>-<646.0,397.0>-<647.0,396.0>> = 7.125016348901705

	* petapp.minimal (U+E007): L<<673.0,536.0>--<676.0,538.0>>/B<<676.0,538.0>-<674.0,537.0>-<673.0,536.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<682.0,542.0>--<685.0,543.0>>/B<<685.0,543.0>-<683.0,542.0>-<682.0,542.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<687.0,544.0>--<690.0,545.0>>/B<<690.0,545.0>-<688.0,544.0>-<687.0,544.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<698.0,250.0>--<700.0,247.0>>/B<<700.0,247.0>-<699.0,248.0>-<698.0,250.0>> = 11.309932474020195

	* petapp.minimal (U+E007): L<<718.0,218.0>--<719.0,215.0>>/B<<719.0,215.0>-<718.0,217.0>-<718.0,218.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<731.0,113.0>--<732.0,110.0>>/B<<732.0,110.0>-<731.0,112.0>-<731.0,113.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<740.0,156.0>--<739.0,160.0>>/B<<739.0,160.0>-<740.0,153.0>-<740.0,156.0>> = 5.906141113770497

	* petapp.minimal (U+E007): L<<744.0,137.0>--<743.0,140.0>>/B<<743.0,140.0>-<744.0,138.0>-<744.0,137.0>> = 8.130102354155916

	* petapp.minimal (U+E007): L<<746.0,123.0>--<747.0,120.0>>/B<<747.0,120.0>-<746.0,122.0>-<746.0,123.0>> = 8.13010235415587

	* petapp.wpda (U+E008): B<<485.0,2.0>-<482.0,5.0>-<482.0,6.0>>/L<<482.0,6.0>--<481.0,1.0>> = 11.309932474020227

	* petapp.wpda (U+E008): L<<185.0,222.0>--<180.0,218.0>>/B<<180.0,218.0>-<182.0,219.0>-<183.0,218.0>> = 12.094757077012058

	* pisafe (U+E010): B<<175.0,538.0>-<175.0,536.0>-<174.0,534.0>>/L<<174.0,534.0>--<175.0,538.0>> = 12.528807709151492

	* pisafe (U+E010): B<<190.0,573.0>-<189.0,572.0>-<188.0,570.0>>/L<<188.0,570.0>--<190.0,573.0>> = 7.125016348901757

	* pisafe (U+E010): B<<211.0,602.0>-<210.0,600.0>-<208.0,598.0>>/L<<208.0,598.0>--<211.0,602.0>> = 8.13010235415596

	* pisafe (U+E010): B<<784.0,594.0>-<783.0,596.0>-<782.0,597.0>>/L<<782.0,597.0>--<784.0,594.0>> = 11.309932474020195

	* pisafe (U+E010): B<<797.0,577.0>-<796.0,579.0>-<795.0,580.0>>/L<<795.0,580.0>--<797.0,577.0>> = 11.309932474020195

	* pisafe (U+E010): B<<816.0,530.0>-<816.0,532.0>-<815.0,534.0>>/L<<815.0,534.0>--<816.0,530.0>> = 12.528807709151492

	* pisafe (U+E010): B<<820.0,515.0>-<820.0,516.0>-<819.0,518.0>>/L<<819.0,518.0>--<820.0,515.0>> = 8.13010235415587

	* pisafe (U+E010): L<<174.0,534.0>--<175.0,538.0>>/B<<175.0,538.0>-<175.0,536.0>-<174.0,534.0>> = 14.036243467926484

	* pisafe (U+E010): L<<188.0,570.0>--<190.0,573.0>>/B<<190.0,573.0>-<189.0,572.0>-<188.0,570.0>> = 11.309932474020195

	* pisafe (U+E010): L<<208.0,598.0>--<211.0,602.0>>/B<<211.0,602.0>-<210.0,600.0>-<208.0,598.0>> = 10.304846468766044

	* pisafe (U+E010): L<<750.0,626.0>--<754.0,623.0>>/B<<754.0,623.0>-<752.0,624.0>-<750.0,626.0>> = 10.304846468766009

	* pisafe (U+E010): L<<782.0,597.0>--<784.0,594.0>>/B<<784.0,594.0>-<783.0,596.0>-<782.0,597.0>> = 7.125016348901757

	* pisafe (U+E010): L<<795.0,580.0>--<797.0,577.0>>/B<<797.0,577.0>-<796.0,579.0>-<795.0,580.0>> = 7.125016348901757

	* pisafe (U+E010): L<<815.0,534.0>--<816.0,530.0>>/B<<816.0,530.0>-<816.0,532.0>-<815.0,534.0>> = 14.036243467926484 

	* pisafe (U+E010): L<<817.0,528.0>--<818.0,525.0>>/B<<818.0,525.0>-<817.0,527.0>-<817.0,528.0>> = 8.13010235415587 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* exclam (U+0021): L<<106.0,231.0>--<102.0,725.0>>

	* exclam (U+0021): L<<167.0,725.0>--<163.0,231.0>>

	* exclamdown (U+00A1): L<<102.0,-194.0>--<106.0,300.0>> 

	* exclamdown (U+00A1): L<<163.0,300.0>--<167.0,-194.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[19] PitagonSansText-ExtraBold.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check OFL body text is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text">com.google.fonts/check/license/OFL_body_text</a>)</summary><div>


* 🔥 **FAIL** The OFL.txt body text is incorrect. Please use https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt as a template. You should only modify the first line. [code: incorrect-ofl-body-text]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ
at: https://scripts.sil.org/OFL." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks">com.google.fonts/check/name/line_breaks</a>)</summary><div>


* 🔥 **FAIL** Name entry DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1294, but got 1214 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.11, while a newer 0.8.13 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'Pita' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
</div></details><details><summary>⚠ <b>WARN:</b> Description strings in the name table must not exceed 200 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/description_max_length">com.google.fonts/check/name/description_max_length</a>)</summary><div>


* ⚠ **WARN** A few name table entries with ID=10 (NameID.DESCRIPTION) are longer than 200 characters. Please check whether those entries are copyright notices mistakenly stored in the description string entries by a bug in an old FontLab version. If that's the case, then such copyright notices must be removed from these entries. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Pitagon Sans Text ExtraBold' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- dotlessi.wide 

	- registered.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* petapp (U+E006): L<<285.0,304.0>--<315.0,286.0>> -> L<<315.0,286.0>--<342.0,271.0>>

	* petapp (U+E006): L<<315.0,333.0>--<276.0,356.0>> -> L<<276.0,356.0>--<260.0,365.0>>

	* petapp (U+E006): L<<358.0,309.0>--<315.0,333.0>> -> L<<315.0,333.0>--<276.0,356.0>>

	* petapp (U+E006): L<<374.0,299.0>--<358.0,309.0>> -> L<<358.0,309.0>--<315.0,333.0>>

	* petapp (U+E006): L<<374.0,640.0>--<470.0,585.0>> -> L<<470.0,585.0>--<518.0,556.0>>

	* petapp (U+E006): L<<376.0,298.0>--<374.0,299.0>> -> L<<374.0,299.0>--<358.0,309.0>>

	* petapp (U+E006): L<<429.0,268.0>--<376.0,298.0>> -> L<<376.0,298.0>--<374.0,299.0>>

	* petapp (U+E006): L<<470.0,585.0>--<518.0,556.0>> -> L<<518.0,556.0>--<537.0,545.0>>

	* petapp (U+E006): L<<471.0,243.0>--<429.0,268.0>> -> L<<429.0,268.0>--<376.0,298.0>>

	* petapp (U+E006): L<<477.0,240.0>--<471.0,243.0>> -> L<<471.0,243.0>--<429.0,268.0>>

	* petapp (U+E006): L<<501.0,226.0>--<477.0,240.0>> -> L<<477.0,240.0>--<471.0,243.0>>

	* petapp (U+E006): L<<508.0,222.0>--<501.0,226.0>> -> L<<501.0,226.0>--<477.0,240.0>>

	* petapp (U+E006): L<<694.0,61.0>--<695.0,60.0>> -> L<<695.0,60.0>--<699.0,56.0>>

	* petapp (U+E006): L<<724.0,485.0>--<728.0,485.0>> -> L<<728.0,485.0>--<767.0,485.0>>

	* petapp.minimal (U+E007): L<<267.0,373.0>--<354.0,339.0>> -> L<<354.0,339.0>--<435.0,305.0>>

	* petapp.minimal (U+E007): L<<354.0,339.0>--<435.0,305.0>> -> L<<435.0,305.0>--<451.0,299.0>>

	* petapp.minimal (U+E007): L<<384.0,352.0>--<334.0,376.0>> -> L<<334.0,376.0>--<308.0,390.0>>

	* petapp.minimal (U+E007): L<<435.0,305.0>--<451.0,299.0>> -> L<<451.0,299.0>--<507.0,276.0>>

	* petapp.minimal (U+E007): L<<435.0,326.0>--<384.0,352.0>> -> L<<384.0,352.0>--<334.0,376.0>>

	* petapp.minimal (U+E007): L<<438.0,187.0>--<408.0,192.0>> -> L<<408.0,192.0>--<307.0,211.0>>

	* petapp.minimal (U+E007): L<<451.0,299.0>--<507.0,276.0>> -> L<<507.0,276.0>--<615.0,232.0>>

	* petapp.minimal (U+E007): L<<458.0,314.0>--<435.0,326.0>> -> L<<435.0,326.0>--<384.0,352.0>>

	* petapp.minimal (U+E007): L<<507.0,175.0>--<438.0,187.0>> -> L<<438.0,187.0>--<408.0,192.0>>

	* petapp.minimal (U+E007): L<<507.0,276.0>--<615.0,232.0>> -> L<<615.0,232.0>--<624.0,229.0>>

	* petapp.minimal (U+E007): L<<507.0,289.0>--<458.0,314.0>> -> L<<458.0,314.0>--<435.0,326.0>>

	* petapp.minimal (U+E007): L<<591.0,160.0>--<507.0,175.0>> -> L<<507.0,175.0>--<438.0,187.0>>

	* petapp.minimal (U+E007): L<<624.0,229.0>--<507.0,289.0>> -> L<<507.0,289.0>--<458.0,314.0>>

	* petapp.minimal (U+E007): L<<745.0,30.0>--<745.0,31.0>> -> L<<745.0,31.0>--<745.0,32.0>>

	* petapp.minimal (U+E007): L<<746.0,33.0>--<746.0,34.0>> -> L<<746.0,34.0>--<746.0,36.0>>

	* petapp.minimal (U+E007): L<<746.0,34.0>--<746.0,36.0>> -> L<<746.0,36.0>--<746.0,37.0>>

	* petapp.minimal (U+E007): L<<750.0,73.0>--<749.0,63.0>> -> L<<749.0,63.0>--<746.0,38.0>>

	* petapp.minimal (U+E007): L<<750.0,74.0>--<750.0,73.0>> -> L<<750.0,73.0>--<749.0,63.0>>

	* petapp.minimal (U+E007): L<<755.0,131.0>--<750.0,74.0>> -> L<<750.0,74.0>--<750.0,73.0>>

	* petapp.minimal (U+E007): L<<757.0,162.0>--<755.0,131.0>> -> L<<755.0,131.0>--<750.0,74.0>>

	* petapp.minimal (U+E007): L<<758.0,175.0>--<757.0,162.0>> -> L<<757.0,162.0>--<755.0,131.0>>

	* petapp.minimal (U+E007): L<<760.0,196.0>--<758.0,175.0>> -> L<<758.0,175.0>--<757.0,162.0>>

	* petapp.minimal (U+E007): L<<761.0,210.0>--<760.0,196.0>> -> L<<760.0,196.0>--<758.0,175.0>>

	* petapp.minimal (U+E007): L<<761.0,213.0>--<761.0,210.0>> -> L<<761.0,210.0>--<760.0,196.0>>

	* petapp.wpda (U+E008): L<<642.0,140.0>--<629.0,132.0>> -> L<<629.0,132.0>--<620.0,127.0>>

	* piads (U+E001): L<<115.0,541.0>--<119.0,544.0>> -> L<<119.0,544.0>--<448.0,782.0>>

	* piads (U+E001): L<<549.0,782.0>--<877.0,544.0>> -> L<<877.0,544.0>--<881.0,541.0>>

	* picall (U+E009): L<<115.0,541.0>--<119.0,544.0>> -> L<<119.0,544.0>--<448.0,782.0>>

	* picall (U+E009): L<<549.0,782.0>--<877.0,544.0>> -> L<<877.0,544.0>--<881.0,541.0>>

	* pioffice (U+E002): L<<549.0,782.0>--<877.0,544.0>> -> L<<877.0,544.0>--<880.0,542.0>>

	* pisafe (U+E010): L<<170.0,362.0>--<170.0,491.0>> -> L<<170.0,491.0>--<170.0,494.0>>

	* pisafe (U+E010): L<<206.0,695.0>--<242.0,708.0>> -> L<<242.0,708.0>--<392.0,762.0>>

	* pisafe (U+E010): L<<242.0,708.0>--<392.0,762.0>> -> L<<392.0,762.0>--<497.0,800.0>>

	* pisafe (U+E010): L<<498.0,800.0>--<603.0,762.0>> -> L<<603.0,762.0>--<753.0,708.0>>

	* pisafe (U+E010): L<<603.0,762.0>--<753.0,708.0>> -> L<<753.0,708.0>--<789.0,695.0>>

	* pisign (U+E005): L<<549.0,782.0>--<877.0,544.0>> -> L<<877.0,544.0>--<880.0,542.0>>

	* pitagon (U+E000): L<<115.0,543.0>--<119.0,546.0>> -> L<<119.0,546.0>--<448.0,784.0>>

	* pitagon (U+E000): L<<212.0,62.0>--<87.0,446.0>> -> L<<87.0,446.0>--<85.0,452.0>>

	* pitagon (U+E000): L<<550.0,784.0>--<877.0,546.0>> -> L<<877.0,546.0>--<881.0,543.0>>

	* pitagram (U+E003): L<<816.0,512.0>--<813.0,514.0>> -> L<<813.0,514.0>--<540.0,711.0>>

	* piweb (U+E004): L<<816.0,512.0>--<813.0,514.0>> -> L<<813.0,514.0>--<540.0,711.0>>

	* sparks (U+E011): L<<103.0,798.0>--<106.0,797.0>> -> L<<106.0,797.0>--<201.0,762.0>>

	* sparks (U+E011): L<<106.0,797.0>--<201.0,762.0>> -> L<<201.0,762.0>--<212.0,759.0>>

	* sparks (U+E011): L<<201.0,762.0>--<212.0,759.0>> -> L<<212.0,759.0>--<403.0,690.0>>

	* sparks (U+E011): L<<212.0,759.0>--<403.0,690.0>> -> L<<403.0,690.0>--<434.0,680.0>>

	* sparks (U+E011): L<<294.0,596.0>--<366.0,534.0>> -> L<<366.0,534.0>--<385.0,516.0>>

	* sparks (U+E011): L<<384.0,366.0>--<386.0,367.0>> -> L<<386.0,367.0>--<489.0,429.0>>

	* sparks (U+E011): L<<386.0,367.0>--<489.0,429.0>> -> L<<489.0,429.0>--<491.0,430.0>>

	* sparks (U+E011): L<<412.0,102.0>--<101.0,641.0>> -> L<<101.0,641.0>--<50.0,731.0>>

	* sparks (U+E011): L<<443.0,659.0>--<439.0,649.0>> -> L<<439.0,649.0>--<437.0,643.0>>

	* sparks (U+E011): L<<457.0,24.0>--<412.0,102.0>> -> L<<412.0,102.0>--<101.0,641.0>>

	* sparks (U+E011): L<<507.0,429.0>--<609.0,367.0>> -> L<<609.0,367.0>--<611.0,366.0>>

	* sparks (U+E011): L<<561.0,680.0>--<599.0,694.0>> -> L<<599.0,694.0>--<783.0,759.0>>

	* sparks (U+E011): L<<582.0,101.0>--<553.0,51.0>> -> L<<553.0,51.0>--<538.0,24.0>>

	* sparks (U+E011): L<<599.0,694.0>--<783.0,759.0>> -> L<<783.0,759.0>--<810.0,768.0>>

	* sparks (U+E011): L<<610.0,516.0>--<630.0,534.0>> -> L<<630.0,534.0>--<702.0,596.0>>

	* sparks (U+E011): L<<617.0,629.0>--<580.0,632.0>> -> L<<580.0,632.0>--<571.0,633.0>>

	* sparks (U+E011): L<<658.0,626.0>--<617.0,629.0>> -> L<<617.0,629.0>--<580.0,632.0>>

	* sparks (U+E011): L<<659.0,626.0>--<658.0,626.0>> -> L<<658.0,626.0>--<617.0,629.0>>

	* sparks (U+E011): L<<693.0,623.0>--<659.0,626.0>> -> L<<659.0,626.0>--<658.0,626.0>>

	* sparks (U+E011): L<<694.0,623.0>--<693.0,623.0>> -> L<<693.0,623.0>--<659.0,626.0>>

	* sparks (U+E011): L<<753.0,397.0>--<582.0,101.0>> -> L<<582.0,101.0>--<553.0,51.0>>

	* sparks (U+E011): L<<783.0,759.0>--<810.0,768.0>> -> L<<810.0,768.0>--<889.0,797.0>>

	* sparks (U+E011): L<<900.0,652.0>--<753.0,397.0>> -> L<<753.0,397.0>--<582.0,101.0>>

	* sparks (U+E011): L<<945.0,730.0>--<900.0,652.0>> -> L<<900.0,652.0>--<753.0,397.0>> 

	* sparks (U+E011): L<<946.0,732.0>--<945.0,730.0>> -> L<<945.0,730.0>--<900.0,652.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* petapp (U+E006): B<<292.0,471.0>-<293.0,469.0>-<294.0,468.0>>/L<<294.0,468.0>--<292.0,471.0>> = 11.309932474020227

	* petapp (U+E006): B<<298.0,293.0>-<292.0,300.0>-<285.0,304.0>>/L<<285.0,304.0>--<315.0,286.0>> = 1.2188752351307344

	* petapp (U+E006): B<<331.0,429.0>-<332.0,428.0>-<334.0,427.0>>/L<<334.0,427.0>--<331.0,429.0>> = 7.125016348901757

	* petapp (U+E006): B<<418.0,76.0>-<419.0,76.0>-<421.0,75.0>>/L<<421.0,75.0>--<418.0,76.0>> = 8.130102354155916

	* petapp (U+E006): B<<427.0,71.0>-<428.0,71.0>-<430.0,70.0>>/L<<430.0,70.0>--<427.0,71.0>> = 8.130102354155916

	* petapp (U+E006): B<<442.0,65.0>-<443.0,65.0>-<445.0,64.0>>/L<<445.0,64.0>--<442.0,65.0>> = 8.130102354155916

	* petapp (U+E006): B<<486.0,64.0>-<487.0,64.0>-<489.0,65.0>>/L<<489.0,65.0>--<486.0,64.0>> = 8.130102354155916

	* petapp (U+E006): B<<516.0,65.0>-<518.0,65.0>-<520.0,66.0>>/L<<520.0,66.0>--<516.0,65.0>> = 12.528807709151463

	* petapp (U+E006): B<<522.0,66.0>-<524.0,66.0>-<526.0,67.0>>/L<<526.0,67.0>--<522.0,66.0>> = 12.528807709151463

	* petapp (U+E006): B<<532.0,68.0>-<531.0,68.0>-<529.0,67.0>>/L<<529.0,67.0>--<532.0,68.0>> = 8.13010235415587

	* petapp (U+E006): B<<539.0,192.0>-<538.0,194.0>-<537.0,195.0>>/L<<537.0,195.0>--<539.0,192.0>> = 11.309932474020195

	* petapp (U+E006): B<<539.0,69.0>-<537.0,69.0>-<535.0,68.0>>/L<<535.0,68.0>--<539.0,69.0>> = 12.528807709151492

	* petapp (U+E006): B<<540.0,308.0>-<539.0,309.0>-<537.0,310.0>>/L<<537.0,310.0>--<540.0,308.0>> = 7.125016348901757

	* petapp (U+E006): B<<542.0,108.0>-<543.0,109.0>-<544.0,111.0>>/L<<544.0,111.0>--<542.0,108.0>> = 7.125016348901705

	* petapp (U+E006): B<<542.0,438.0>-<541.0,439.0>-<539.0,440.0>>/L<<539.0,440.0>--<542.0,438.0>> = 7.125016348901757

	* petapp (U+E006): B<<548.0,123.0>-<549.0,125.0>-<549.0,127.0>>/L<<549.0,127.0>--<548.0,123.0>> = 14.036243467926484

	* petapp (U+E006): B<<551.0,432.0>-<550.0,433.0>-<548.0,434.0>>/L<<548.0,434.0>--<551.0,432.0>> = 7.125016348901757

	* petapp (U+E006): B<<551.0,72.0>-<552.0,72.0>-<554.0,73.0>>/L<<554.0,73.0>--<551.0,72.0>> = 8.130102354155916

	* petapp (U+E006): B<<578.0,404.0>-<579.0,403.0>-<580.0,401.0>>/L<<580.0,401.0>--<578.0,404.0>> = 7.125016348901705

	* petapp (U+E006): B<<590.0,380.0>-<590.0,382.0>-<589.0,384.0>>/L<<589.0,384.0>--<590.0,380.0>> = 12.528807709151492

	* petapp (U+E006): B<<613.0,384.0>-<614.0,381.0>-<615.0,379.0>>/L<<615.0,379.0>--<613.0,384.0>> = 4.763641690726066

	* petapp (U+E006): B<<617.0,384.0>-<618.0,382.0>-<619.0,379.0>>/L<<619.0,379.0>--<617.0,384.0>> = 3.366460663429615

	* petapp (U+E006): B<<630.0,343.0>-<631.0,342.0>-<632.0,340.0>>/L<<632.0,340.0>--<630.0,343.0>> = 7.125016348901705

	* petapp (U+E006): B<<636.0,334.0>-<636.0,333.0>-<637.0,331.0>>/L<<637.0,331.0>--<636.0,334.0>> = 8.130102354155916

	* petapp (U+E006): B<<641.0,346.0>-<642.0,345.0>-<643.0,343.0>>/L<<643.0,343.0>--<641.0,346.0>> = 7.125016348901705

	* petapp (U+E006): B<<644.0,321.0>-<645.0,320.0>-<646.0,318.0>>/L<<646.0,318.0>--<644.0,321.0>> = 7.125016348901705

	* petapp (U+E006): B<<672.0,316.0>-<673.0,315.0>-<675.0,314.0>>/L<<675.0,314.0>--<672.0,316.0>> = 7.125016348901757

	* petapp (U+E006): B<<672.0,456.0>-<670.0,454.0>-<669.0,452.0>>/L<<669.0,452.0>--<672.0,456.0>> = 10.304846468766044

	* petapp (U+E006): B<<673.0,137.0>-<674.0,138.0>-<675.0,140.0>>/L<<675.0,140.0>--<673.0,137.0>> = 7.125016348901705

	* petapp (U+E006): B<<682.0,141.0>-<684.0,142.0>-<685.0,143.0>>/L<<685.0,143.0>--<682.0,141.0>> = 11.309932474020195

	* petapp (U+E006): B<<690.0,164.0>-<691.0,166.0>-<692.0,167.0>>/L<<692.0,167.0>--<690.0,164.0>> = 11.309932474020227

	* petapp (U+E006): B<<716.0,484.0>-<715.0,484.0>-<713.0,483.0>>/L<<713.0,483.0>--<716.0,484.0>> = 8.13010235415587

	* petapp (U+E006): B<<766.0,5.0>-<765.0,7.0>-<764.0,8.0>>/L<<764.0,8.0>--<766.0,5.0>> = 11.309932474020195

	* petapp (U+E006): L<<277.0,517.0>--<276.0,520.0>>/B<<276.0,520.0>-<277.0,518.0>-<277.0,517.0>> = 8.130102354155916

	* petapp (U+E006): L<<283.0,491.0>--<282.0,494.0>>/B<<282.0,494.0>-<283.0,492.0>-<283.0,491.0>> = 8.130102354155916

	* petapp (U+E006): L<<294.0,468.0>--<292.0,471.0>>/B<<292.0,471.0>-<293.0,469.0>-<294.0,468.0>> = 7.125016348901705

	* petapp (U+E006): L<<299.0,459.0>--<298.0,462.0>>/B<<298.0,462.0>-<299.0,460.0>-<299.0,459.0>> = 8.130102354155916

	* petapp (U+E006): L<<315.0,442.0>--<311.0,445.0>>/B<<311.0,445.0>-<313.0,444.0>-<315.0,442.0>> = 10.304846468766009

	* petapp (U+E006): L<<334.0,427.0>--<331.0,429.0>>/B<<331.0,429.0>-<332.0,428.0>-<334.0,427.0>> = 11.309932474020195

	* petapp (U+E006): L<<383.0,128.0>--<382.0,131.0>>/B<<382.0,131.0>-<383.0,129.0>-<383.0,128.0>> = 8.130102354155916

	* petapp (U+E006): L<<390.0,108.0>--<389.0,111.0>>/B<<389.0,111.0>-<390.0,109.0>-<390.0,108.0>> = 8.130102354155916

	* petapp (U+E006): L<<502.0,225.0>--<508.0,222.0>>/L<<508.0,222.0>--<501.0,226.0>> = 3.1798301198640497

	* petapp (U+E006): L<<507.0,71.0>--<502.0,69.0>>/B<<502.0,69.0>-<505.0,71.0>-<507.0,71.0>> = 11.888658039627936

	* petapp (U+E006): L<<520.0,66.0>--<516.0,65.0>>/B<<516.0,65.0>-<518.0,65.0>-<520.0,66.0>> = 14.036243467926484

	* petapp (U+E006): L<<526.0,67.0>--<522.0,66.0>>/B<<522.0,66.0>-<524.0,66.0>-<526.0,67.0>> = 14.036243467926484

	* petapp (U+E006): L<<535.0,68.0>--<539.0,69.0>>/B<<539.0,69.0>-<537.0,69.0>-<535.0,68.0>> = 14.036243467926484

	* petapp (U+E006): L<<537.0,195.0>--<539.0,192.0>>/B<<539.0,192.0>-<538.0,194.0>-<537.0,195.0>> = 7.125016348901757

	* petapp (U+E006): L<<537.0,310.0>--<540.0,308.0>>/B<<540.0,308.0>-<539.0,309.0>-<537.0,310.0>> = 11.309932474020227

	* petapp (U+E006): L<<539.0,440.0>--<542.0,438.0>>/B<<542.0,438.0>-<541.0,439.0>-<539.0,440.0>> = 11.309932474020227

	* petapp (U+E006): L<<544.0,111.0>--<542.0,108.0>>/B<<542.0,108.0>-<543.0,109.0>-<544.0,111.0>> = 11.309932474020227

	* petapp (U+E006): L<<544.0,70.0>--<548.0,71.0>>/B<<548.0,71.0>-<543.0,70.0>-<544.0,70.0>> = 2.726310993906212

	* petapp (U+E006): L<<545.0,181.0>--<546.0,178.0>>/B<<546.0,178.0>-<545.0,180.0>-<545.0,181.0>> = 8.13010235415587

	* petapp (U+E006): L<<548.0,434.0>--<551.0,432.0>>/B<<551.0,432.0>-<550.0,433.0>-<548.0,434.0>> = 11.309932474020227

	* petapp (U+E006): L<<549.0,127.0>--<548.0,123.0>>/B<<548.0,123.0>-<549.0,125.0>-<549.0,127.0>> = 12.528807709151492

	* petapp (U+E006): L<<559.0,74.0>--<556.0,73.0>>/B<<556.0,73.0>-<558.0,74.0>-<559.0,74.0>> = 8.130102354155916

	* petapp (U+E006): L<<580.0,401.0>--<578.0,404.0>>/B<<578.0,404.0>-<579.0,403.0>-<580.0,401.0>> = 11.309932474020227

	* petapp (U+E006): L<<586.0,256.0>--<587.0,252.0>>/B<<587.0,252.0>-<587.0,254.0>-<586.0,256.0>> = 14.036243467926484

	* petapp (U+E006): L<<589.0,384.0>--<590.0,380.0>>/B<<590.0,380.0>-<590.0,382.0>-<589.0,384.0>> = 14.036243467926484

	* petapp (U+E006): L<<601.0,432.0>--<602.0,429.0>>/B<<602.0,429.0>-<601.0,431.0>-<601.0,432.0>> = 8.13010235415587

	* petapp (U+E006): L<<605.0,122.0>--<604.0,125.0>>/B<<604.0,125.0>-<605.0,123.0>-<605.0,122.0>> = 8.130102354155916

	* petapp (U+E006): L<<614.0,96.0>--<614.0,96.0>>/B<<614.0,96.0>-<610.0,95.0>-<606.5,92.5>> = 14.036243467926484

	* petapp (U+E006): L<<615.0,379.0>--<613.0,384.0>>/B<<613.0,384.0>-<614.0,381.0>-<615.0,379.0>> = 3.366460663429615

	* petapp (U+E006): L<<616.0,374.0>--<615.0,377.0>>/B<<615.0,377.0>-<616.0,375.0>-<616.0,374.0>> = 8.130102354155916

	* petapp (U+E006): L<<618.0,369.0>--<617.0,372.0>>/B<<617.0,372.0>-<618.0,370.0>-<618.0,369.0>> = 8.130102354155916

	* petapp (U+E006): L<<619.0,379.0>--<617.0,384.0>>/B<<617.0,384.0>-<618.0,382.0>-<619.0,379.0>> = 4.763641690726066

	* petapp (U+E006): L<<632.0,340.0>--<630.0,343.0>>/B<<630.0,343.0>-<631.0,342.0>-<632.0,340.0>> = 11.309932474020227

	* petapp (U+E006): L<<643.0,343.0>--<641.0,346.0>>/B<<641.0,346.0>-<642.0,345.0>-<643.0,343.0>> = 11.309932474020227

	* petapp (U+E006): L<<646.0,318.0>--<644.0,321.0>>/B<<644.0,321.0>-<645.0,320.0>-<646.0,318.0>> = 11.309932474020227

	* petapp (U+E006): L<<660.0,433.0>--<661.0,436.0>>/B<<661.0,436.0>-<660.0,434.0>-<660.0,432.5>> = 8.13010235415587

	* petapp (U+E006): L<<664.0,383.0>--<663.0,386.0>>/B<<663.0,386.0>-<664.0,384.0>-<664.0,383.0>> = 8.130102354155916

	* petapp (U+E006): L<<669.0,452.0>--<672.0,456.0>>/B<<672.0,456.0>-<670.0,454.0>-<669.0,452.0>> = 8.13010235415596

	* petapp (U+E006): L<<675.0,140.0>--<673.0,137.0>>/B<<673.0,137.0>-<674.0,138.0>-<675.0,140.0>> = 11.309932474020227

	* petapp (U+E006): L<<685.0,143.0>--<682.0,141.0>>/B<<682.0,141.0>-<684.0,142.0>-<685.0,143.0>> = 7.125016348901757

	* petapp (U+E006): L<<689.0,162.0>--<688.0,159.0>>/B<<688.0,159.0>-<689.0,161.0>-<689.0,162.0>> = 8.130102354155916

	* petapp (U+E006): L<<692.0,167.0>--<690.0,164.0>>/B<<690.0,164.0>-<691.0,166.0>-<692.0,167.0>> = 7.125016348901705

	* petapp (U+E006): L<<692.0,256.0>--<693.0,253.0>>/B<<693.0,253.0>-<692.0,255.0>-<692.0,256.0>> = 8.13010235415587

	* petapp (U+E006): L<<694.0,251.0>--<695.0,248.0>>/B<<695.0,248.0>-<694.0,250.0>-<694.0,251.0>> = 8.13010235415587

	* petapp (U+E006): L<<703.0,480.0>--<706.0,481.0>>/B<<706.0,481.0>-<704.0,480.0>-<703.0,479.5>> = 8.13010235415587

	* petapp (U+E006): L<<708.0,482.0>--<711.0,483.0>>/B<<711.0,483.0>-<709.0,482.0>-<708.0,482.0>> = 8.13010235415587

	* petapp (U+E006): L<<711.0,293.0>--<708.0,294.0>>/B<<708.0,294.0>-<710.0,293.0>-<711.0,293.0>> = 8.130102354155916

	* petapp (U+E006): L<<731.0,285.0>--<728.0,286.0>>/B<<728.0,286.0>-<730.0,285.0>-<731.0,285.0>> = 8.130102354155916

	* petapp (U+E006): L<<764.0,8.0>--<766.0,5.0>>/B<<766.0,5.0>-<765.0,7.0>-<764.0,8.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<584.0,372.0>-<588.0,368.0>-<591.0,366.0>>/L<<591.0,366.0>--<584.0,372.0>> = 6.911227119024609

	* petapp.minimal (U+E007): B<<634.0,435.0>-<634.0,433.0>-<635.0,430.0>>/L<<635.0,430.0>--<634.0,435.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<635.0,481.0>-<635.0,480.0>-<634.0,478.0>>/L<<634.0,478.0>--<635.0,481.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<648.0,399.0>-<649.0,397.0>-<650.0,396.0>>/L<<650.0,396.0>--<648.0,399.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<649.0,510.0>-<648.0,508.0>-<647.0,507.0>>/L<<647.0,507.0>--<649.0,510.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<679.0,538.0>-<677.0,537.0>-<676.0,536.0>>/L<<676.0,536.0>--<679.0,538.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<703.0,247.0>-<702.0,248.0>-<701.0,250.0>>/L<<701.0,250.0>--<703.0,247.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<717.0,147.0>-<717.0,148.0>-<716.0,150.0>>/L<<716.0,150.0>--<717.0,147.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<723.0,137.0>-<722.0,139.0>-<721.0,140.0>>/L<<721.0,140.0>--<723.0,137.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<735.0,185.0>-<734.0,187.0>-<734.0,189.0>>/L<<734.0,189.0>--<735.0,185.0>> = 14.036243467926484

	* petapp.minimal (U+E007): B<<746.0,53.0>-<746.0,54.0>-<745.0,56.0>>/L<<745.0,56.0>--<746.0,53.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<215.0,538.0>--<215.0,800.0>>/B<<215.0,800.0>-<217.0,769.0>-<229.5,742.0>> = 3.6913859864512575

	* petapp.minimal (U+E007): L<<631.0,462.0>--<632.0,465.0>>/B<<632.0,465.0>-<631.0,463.0>-<631.0,462.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<633.0,473.0>--<634.0,476.0>>/B<<634.0,476.0>-<633.0,474.0>-<633.0,473.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<635.0,430.0>--<634.0,435.0>>/B<<634.0,435.0>-<634.0,433.0>-<635.0,430.0>> = 11.309932474020227

	* petapp.minimal (U+E007): L<<640.0,222.0>--<643.0,221.0>>/B<<643.0,221.0>-<641.0,222.0>-<640.0,222.5>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<642.0,498.0>--<643.0,501.0>>/B<<643.0,501.0>-<642.0,499.0>-<642.0,498.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<647.0,507.0>--<649.0,510.0>>/B<<649.0,510.0>-<648.0,508.0>-<647.0,507.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<650.0,396.0>--<648.0,399.0>>/B<<648.0,399.0>-<649.0,397.0>-<650.0,396.0>> = 7.125016348901705

	* petapp.minimal (U+E007): L<<676.0,536.0>--<679.0,538.0>>/B<<679.0,538.0>-<677.0,537.0>-<676.0,536.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<685.0,542.0>--<688.0,543.0>>/B<<688.0,543.0>-<686.0,542.0>-<685.0,542.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<690.0,544.0>--<693.0,545.0>>/B<<693.0,545.0>-<691.0,544.0>-<690.0,544.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<701.0,250.0>--<703.0,247.0>>/B<<703.0,247.0>-<702.0,248.0>-<701.0,250.0>> = 11.309932474020195

	* petapp.minimal (U+E007): L<<721.0,218.0>--<722.0,215.0>>/B<<722.0,215.0>-<721.0,217.0>-<721.0,218.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<734.0,113.0>--<735.0,110.0>>/B<<735.0,110.0>-<734.0,112.0>-<734.0,113.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<743.0,156.0>--<742.0,160.0>>/B<<742.0,160.0>-<743.0,153.0>-<743.0,156.0>> = 5.906141113770497

	* petapp.minimal (U+E007): L<<747.0,137.0>--<746.0,140.0>>/B<<746.0,140.0>-<747.0,138.0>-<747.0,137.0>> = 8.130102354155916

	* petapp.minimal (U+E007): L<<749.0,123.0>--<750.0,120.0>>/B<<750.0,120.0>-<749.0,122.0>-<749.0,123.0>> = 8.13010235415587

	* petapp.wpda (U+E008): B<<487.0,2.0>-<484.0,5.0>-<484.0,6.0>>/L<<484.0,6.0>--<483.0,1.0>> = 11.309932474020227

	* petapp.wpda (U+E008): L<<187.0,222.0>--<182.0,218.0>>/B<<182.0,218.0>-<184.0,219.0>-<185.0,218.0>> = 12.094757077012058

	* pisafe (U+E010): B<<178.0,538.0>-<178.0,536.0>-<177.0,534.0>>/L<<177.0,534.0>--<178.0,538.0>> = 12.528807709151492

	* pisafe (U+E010): B<<193.0,573.0>-<192.0,572.0>-<191.0,570.0>>/L<<191.0,570.0>--<193.0,573.0>> = 7.125016348901757

	* pisafe (U+E010): B<<214.0,602.0>-<213.0,600.0>-<211.0,598.0>>/L<<211.0,598.0>--<214.0,602.0>> = 8.13010235415596

	* pisafe (U+E010): B<<787.0,594.0>-<786.0,596.0>-<785.0,597.0>>/L<<785.0,597.0>--<787.0,594.0>> = 11.309932474020195

	* pisafe (U+E010): B<<800.0,577.0>-<799.0,579.0>-<798.0,580.0>>/L<<798.0,580.0>--<800.0,577.0>> = 11.309932474020195

	* pisafe (U+E010): B<<819.0,530.0>-<819.0,532.0>-<818.0,534.0>>/L<<818.0,534.0>--<819.0,530.0>> = 12.528807709151492

	* pisafe (U+E010): B<<823.0,515.0>-<823.0,516.0>-<822.0,518.0>>/L<<822.0,518.0>--<823.0,515.0>> = 8.13010235415587

	* pisafe (U+E010): L<<177.0,534.0>--<178.0,538.0>>/B<<178.0,538.0>-<178.0,536.0>-<177.0,534.0>> = 14.036243467926484

	* pisafe (U+E010): L<<191.0,570.0>--<193.0,573.0>>/B<<193.0,573.0>-<192.0,572.0>-<191.0,570.0>> = 11.309932474020195

	* pisafe (U+E010): L<<211.0,598.0>--<214.0,602.0>>/B<<214.0,602.0>-<213.0,600.0>-<211.0,598.0>> = 10.304846468766044

	* pisafe (U+E010): L<<753.0,626.0>--<757.0,623.0>>/B<<757.0,623.0>-<755.0,624.0>-<753.0,626.0>> = 10.304846468766009

	* pisafe (U+E010): L<<785.0,597.0>--<787.0,594.0>>/B<<787.0,594.0>-<786.0,596.0>-<785.0,597.0>> = 7.125016348901757

	* pisafe (U+E010): L<<798.0,580.0>--<800.0,577.0>>/B<<800.0,577.0>-<799.0,579.0>-<798.0,580.0>> = 7.125016348901757

	* pisafe (U+E010): L<<818.0,534.0>--<819.0,530.0>>/B<<819.0,530.0>-<819.0,532.0>-<818.0,534.0>> = 14.036243467926484 

	* pisafe (U+E010): L<<820.0,528.0>--<821.0,525.0>>/B<<821.0,525.0>-<820.0,527.0>-<820.0,528.0>> = 8.13010235415587 [code: found-jaggy-segments]
</div></details><br></div></details><details><summary><b>[20] PitagonSansText-ExtraLight.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check OFL body text is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text">com.google.fonts/check/license/OFL_body_text</a>)</summary><div>


* 🔥 **FAIL** The OFL.txt body text is incorrect. Please use https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt as a template. You should only modify the first line. [code: incorrect-ofl-body-text]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ
at: https://scripts.sil.org/OFL." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks">com.google.fonts/check/name/line_breaks</a>)</summary><div>


* 🔥 **FAIL** Name entry DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1294, but got 1214 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.11, while a newer 0.8.13 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'Pita' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
</div></details><details><summary>⚠ <b>WARN:</b> Description strings in the name table must not exceed 200 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/description_max_length">com.google.fonts/check/name/description_max_length</a>)</summary><div>


* ⚠ **WARN** A few name table entries with ID=10 (NameID.DESCRIPTION) are longer than 200 characters. Please check whether those entries are copyright notices mistakenly stored in the description string entries by a bug in an old FontLab version. If that's the case, then such copyright notices must be removed from these entries. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Pitagon Sans Text ExtraLight' / SUBFAMILY_NAME = 'Regular'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- dotlessi.wide 

	- registered.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* petapp (U+E006): L<<282.0,304.0>--<312.0,286.0>> -> L<<312.0,286.0>--<339.0,271.0>>

	* petapp (U+E006): L<<312.0,333.0>--<273.0,356.0>> -> L<<273.0,356.0>--<257.0,365.0>>

	* petapp (U+E006): L<<355.0,309.0>--<312.0,333.0>> -> L<<312.0,333.0>--<273.0,356.0>>

	* petapp (U+E006): L<<371.0,299.0>--<355.0,309.0>> -> L<<355.0,309.0>--<312.0,333.0>>

	* petapp (U+E006): L<<371.0,640.0>--<467.0,585.0>> -> L<<467.0,585.0>--<515.0,556.0>>

	* petapp (U+E006): L<<373.0,298.0>--<371.0,299.0>> -> L<<371.0,299.0>--<355.0,309.0>>

	* petapp (U+E006): L<<426.0,268.0>--<373.0,298.0>> -> L<<373.0,298.0>--<371.0,299.0>>

	* petapp (U+E006): L<<467.0,585.0>--<515.0,556.0>> -> L<<515.0,556.0>--<534.0,545.0>>

	* petapp (U+E006): L<<468.0,243.0>--<426.0,268.0>> -> L<<426.0,268.0>--<373.0,298.0>>

	* petapp (U+E006): L<<474.0,240.0>--<468.0,243.0>> -> L<<468.0,243.0>--<426.0,268.0>>

	* petapp (U+E006): L<<498.0,226.0>--<474.0,240.0>> -> L<<474.0,240.0>--<468.0,243.0>>

	* petapp (U+E006): L<<505.0,222.0>--<498.0,226.0>> -> L<<498.0,226.0>--<474.0,240.0>>

	* petapp (U+E006): L<<691.0,61.0>--<692.0,60.0>> -> L<<692.0,60.0>--<696.0,56.0>>

	* petapp (U+E006): L<<721.0,485.0>--<725.0,485.0>> -> L<<725.0,485.0>--<764.0,485.0>>

	* petapp.minimal (U+E007): L<<264.0,373.0>--<351.0,339.0>> -> L<<351.0,339.0>--<432.0,305.0>>

	* petapp.minimal (U+E007): L<<351.0,339.0>--<432.0,305.0>> -> L<<432.0,305.0>--<448.0,299.0>>

	* petapp.minimal (U+E007): L<<381.0,352.0>--<331.0,376.0>> -> L<<331.0,376.0>--<305.0,390.0>>

	* petapp.minimal (U+E007): L<<432.0,305.0>--<448.0,299.0>> -> L<<448.0,299.0>--<504.0,276.0>>

	* petapp.minimal (U+E007): L<<432.0,326.0>--<381.0,352.0>> -> L<<381.0,352.0>--<331.0,376.0>>

	* petapp.minimal (U+E007): L<<435.0,187.0>--<405.0,192.0>> -> L<<405.0,192.0>--<304.0,211.0>>

	* petapp.minimal (U+E007): L<<448.0,299.0>--<504.0,276.0>> -> L<<504.0,276.0>--<612.0,232.0>>

	* petapp.minimal (U+E007): L<<455.0,314.0>--<432.0,326.0>> -> L<<432.0,326.0>--<381.0,352.0>>

	* petapp.minimal (U+E007): L<<504.0,175.0>--<435.0,187.0>> -> L<<435.0,187.0>--<405.0,192.0>>

	* petapp.minimal (U+E007): L<<504.0,276.0>--<612.0,232.0>> -> L<<612.0,232.0>--<621.0,229.0>>

	* petapp.minimal (U+E007): L<<504.0,289.0>--<455.0,314.0>> -> L<<455.0,314.0>--<432.0,326.0>>

	* petapp.minimal (U+E007): L<<588.0,160.0>--<504.0,175.0>> -> L<<504.0,175.0>--<435.0,187.0>>

	* petapp.minimal (U+E007): L<<621.0,229.0>--<504.0,289.0>> -> L<<504.0,289.0>--<455.0,314.0>>

	* petapp.minimal (U+E007): L<<742.0,30.0>--<742.0,31.0>> -> L<<742.0,31.0>--<742.0,32.0>>

	* petapp.minimal (U+E007): L<<743.0,33.0>--<743.0,34.0>> -> L<<743.0,34.0>--<743.0,36.0>>

	* petapp.minimal (U+E007): L<<743.0,34.0>--<743.0,36.0>> -> L<<743.0,36.0>--<743.0,37.0>>

	* petapp.minimal (U+E007): L<<747.0,73.0>--<746.0,63.0>> -> L<<746.0,63.0>--<743.0,38.0>>

	* petapp.minimal (U+E007): L<<747.0,74.0>--<747.0,73.0>> -> L<<747.0,73.0>--<746.0,63.0>>

	* petapp.minimal (U+E007): L<<752.0,131.0>--<747.0,74.0>> -> L<<747.0,74.0>--<747.0,73.0>>

	* petapp.minimal (U+E007): L<<754.0,162.0>--<752.0,131.0>> -> L<<752.0,131.0>--<747.0,74.0>>

	* petapp.minimal (U+E007): L<<755.0,175.0>--<754.0,162.0>> -> L<<754.0,162.0>--<752.0,131.0>>

	* petapp.minimal (U+E007): L<<757.0,196.0>--<755.0,175.0>> -> L<<755.0,175.0>--<754.0,162.0>>

	* petapp.minimal (U+E007): L<<758.0,210.0>--<757.0,196.0>> -> L<<757.0,196.0>--<755.0,175.0>>

	* petapp.minimal (U+E007): L<<758.0,213.0>--<758.0,210.0>> -> L<<758.0,210.0>--<757.0,196.0>>

	* petapp.wpda (U+E008): L<<640.0,140.0>--<627.0,132.0>> -> L<<627.0,132.0>--<618.0,127.0>>

	* piads (U+E001): L<<112.0,541.0>--<116.0,544.0>> -> L<<116.0,544.0>--<445.0,782.0>>

	* piads (U+E001): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<878.0,541.0>>

	* picall (U+E009): L<<112.0,541.0>--<116.0,544.0>> -> L<<116.0,544.0>--<445.0,782.0>>

	* picall (U+E009): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<878.0,541.0>>

	* pioffice (U+E002): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<877.0,542.0>>

	* pisafe (U+E010): L<<167.0,362.0>--<167.0,491.0>> -> L<<167.0,491.0>--<167.0,494.0>>

	* pisafe (U+E010): L<<203.0,695.0>--<239.0,708.0>> -> L<<239.0,708.0>--<389.0,762.0>>

	* pisafe (U+E010): L<<239.0,708.0>--<389.0,762.0>> -> L<<389.0,762.0>--<494.0,800.0>>

	* pisafe (U+E010): L<<495.0,800.0>--<600.0,762.0>> -> L<<600.0,762.0>--<750.0,708.0>>

	* pisafe (U+E010): L<<600.0,762.0>--<750.0,708.0>> -> L<<750.0,708.0>--<786.0,695.0>>

	* pisign (U+E005): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<877.0,542.0>>

	* pitagon (U+E000): L<<112.0,543.0>--<116.0,546.0>> -> L<<116.0,546.0>--<445.0,784.0>>

	* pitagon (U+E000): L<<209.0,62.0>--<84.0,446.0>> -> L<<84.0,446.0>--<82.0,452.0>>

	* pitagon (U+E000): L<<547.0,784.0>--<874.0,546.0>> -> L<<874.0,546.0>--<878.0,543.0>>

	* pitagram (U+E003): L<<813.0,512.0>--<810.0,514.0>> -> L<<810.0,514.0>--<537.0,711.0>>

	* piweb (U+E004): L<<813.0,512.0>--<810.0,514.0>> -> L<<810.0,514.0>--<537.0,711.0>>

	* sparks (U+E011): L<<100.0,798.0>--<103.0,797.0>> -> L<<103.0,797.0>--<198.0,762.0>>

	* sparks (U+E011): L<<103.0,797.0>--<198.0,762.0>> -> L<<198.0,762.0>--<209.0,759.0>>

	* sparks (U+E011): L<<198.0,762.0>--<209.0,759.0>> -> L<<209.0,759.0>--<400.0,690.0>>

	* sparks (U+E011): L<<209.0,759.0>--<400.0,690.0>> -> L<<400.0,690.0>--<431.0,680.0>>

	* sparks (U+E011): L<<291.0,596.0>--<363.0,534.0>> -> L<<363.0,534.0>--<382.0,516.0>>

	* sparks (U+E011): L<<381.0,366.0>--<383.0,367.0>> -> L<<383.0,367.0>--<486.0,429.0>>

	* sparks (U+E011): L<<383.0,367.0>--<486.0,429.0>> -> L<<486.0,429.0>--<488.0,430.0>>

	* sparks (U+E011): L<<409.0,102.0>--<98.0,641.0>> -> L<<98.0,641.0>--<47.0,731.0>>

	* sparks (U+E011): L<<440.0,659.0>--<436.0,649.0>> -> L<<436.0,649.0>--<434.0,643.0>>

	* sparks (U+E011): L<<454.0,24.0>--<409.0,102.0>> -> L<<409.0,102.0>--<98.0,641.0>>

	* sparks (U+E011): L<<504.0,429.0>--<606.0,367.0>> -> L<<606.0,367.0>--<608.0,366.0>>

	* sparks (U+E011): L<<558.0,680.0>--<596.0,694.0>> -> L<<596.0,694.0>--<780.0,759.0>>

	* sparks (U+E011): L<<579.0,101.0>--<550.0,51.0>> -> L<<550.0,51.0>--<535.0,24.0>>

	* sparks (U+E011): L<<596.0,694.0>--<780.0,759.0>> -> L<<780.0,759.0>--<807.0,768.0>>

	* sparks (U+E011): L<<607.0,516.0>--<627.0,534.0>> -> L<<627.0,534.0>--<699.0,596.0>>

	* sparks (U+E011): L<<614.0,629.0>--<577.0,632.0>> -> L<<577.0,632.0>--<568.0,633.0>>

	* sparks (U+E011): L<<655.0,626.0>--<614.0,629.0>> -> L<<614.0,629.0>--<577.0,632.0>>

	* sparks (U+E011): L<<656.0,626.0>--<655.0,626.0>> -> L<<655.0,626.0>--<614.0,629.0>>

	* sparks (U+E011): L<<690.0,623.0>--<656.0,626.0>> -> L<<656.0,626.0>--<655.0,626.0>>

	* sparks (U+E011): L<<691.0,623.0>--<690.0,623.0>> -> L<<690.0,623.0>--<656.0,626.0>>

	* sparks (U+E011): L<<750.0,397.0>--<579.0,101.0>> -> L<<579.0,101.0>--<550.0,51.0>>

	* sparks (U+E011): L<<780.0,759.0>--<807.0,768.0>> -> L<<807.0,768.0>--<886.0,797.0>>

	* sparks (U+E011): L<<897.0,652.0>--<750.0,397.0>> -> L<<750.0,397.0>--<579.0,101.0>>

	* sparks (U+E011): L<<942.0,730.0>--<897.0,652.0>> -> L<<897.0,652.0>--<750.0,397.0>>

	* sparks (U+E011): L<<943.0,732.0>--<942.0,730.0>> -> L<<942.0,730.0>--<897.0,652.0>> 

	* uni20BF (U+20BF): L<<406.0,0.0>--<400.0,0.0>> -> L<<400.0,0.0>--<281.0,0.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* petapp (U+E006): B<<289.0,471.0>-<290.0,469.0>-<291.0,468.0>>/L<<291.0,468.0>--<289.0,471.0>> = 11.309932474020227

	* petapp (U+E006): B<<295.0,293.0>-<289.0,300.0>-<282.0,304.0>>/L<<282.0,304.0>--<312.0,286.0>> = 1.2188752351307344

	* petapp (U+E006): B<<328.0,429.0>-<329.0,428.0>-<331.0,427.0>>/L<<331.0,427.0>--<328.0,429.0>> = 7.125016348901757

	* petapp (U+E006): B<<415.0,76.0>-<416.0,76.0>-<418.0,75.0>>/L<<418.0,75.0>--<415.0,76.0>> = 8.130102354155916

	* petapp (U+E006): B<<424.0,71.0>-<425.0,71.0>-<427.0,70.0>>/L<<427.0,70.0>--<424.0,71.0>> = 8.130102354155916

	* petapp (U+E006): B<<439.0,65.0>-<440.0,65.0>-<442.0,64.0>>/L<<442.0,64.0>--<439.0,65.0>> = 8.130102354155916

	* petapp (U+E006): B<<483.0,64.0>-<484.0,64.0>-<486.0,65.0>>/L<<486.0,65.0>--<483.0,64.0>> = 8.130102354155916

	* petapp (U+E006): B<<513.0,65.0>-<515.0,65.0>-<517.0,66.0>>/L<<517.0,66.0>--<513.0,65.0>> = 12.528807709151463

	* petapp (U+E006): B<<519.0,66.0>-<521.0,66.0>-<523.0,67.0>>/L<<523.0,67.0>--<519.0,66.0>> = 12.528807709151463

	* petapp (U+E006): B<<529.0,68.0>-<528.0,68.0>-<526.0,67.0>>/L<<526.0,67.0>--<529.0,68.0>> = 8.13010235415587

	* petapp (U+E006): B<<536.0,192.0>-<535.0,194.0>-<534.0,195.0>>/L<<534.0,195.0>--<536.0,192.0>> = 11.309932474020195

	* petapp (U+E006): B<<536.0,69.0>-<534.0,69.0>-<532.0,68.0>>/L<<532.0,68.0>--<536.0,69.0>> = 12.528807709151492

	* petapp (U+E006): B<<537.0,308.0>-<536.0,309.0>-<534.0,310.0>>/L<<534.0,310.0>--<537.0,308.0>> = 7.125016348901757

	* petapp (U+E006): B<<539.0,108.0>-<540.0,109.0>-<541.0,111.0>>/L<<541.0,111.0>--<539.0,108.0>> = 7.125016348901705

	* petapp (U+E006): B<<539.0,438.0>-<538.0,439.0>-<536.0,440.0>>/L<<536.0,440.0>--<539.0,438.0>> = 7.125016348901757

	* petapp (U+E006): B<<545.0,123.0>-<546.0,125.0>-<546.0,127.0>>/L<<546.0,127.0>--<545.0,123.0>> = 14.036243467926484

	* petapp (U+E006): B<<548.0,432.0>-<547.0,433.0>-<545.0,434.0>>/L<<545.0,434.0>--<548.0,432.0>> = 7.125016348901757

	* petapp (U+E006): B<<548.0,72.0>-<549.0,72.0>-<551.0,73.0>>/L<<551.0,73.0>--<548.0,72.0>> = 8.130102354155916

	* petapp (U+E006): B<<575.0,404.0>-<576.0,403.0>-<577.0,401.0>>/L<<577.0,401.0>--<575.0,404.0>> = 7.125016348901705

	* petapp (U+E006): B<<587.0,380.0>-<587.0,382.0>-<586.0,384.0>>/L<<586.0,384.0>--<587.0,380.0>> = 12.528807709151492

	* petapp (U+E006): B<<610.0,384.0>-<611.0,381.0>-<612.0,379.0>>/L<<612.0,379.0>--<610.0,384.0>> = 4.763641690726066

	* petapp (U+E006): B<<614.0,384.0>-<615.0,382.0>-<616.0,379.0>>/L<<616.0,379.0>--<614.0,384.0>> = 3.366460663429615

	* petapp (U+E006): B<<627.0,343.0>-<628.0,342.0>-<629.0,340.0>>/L<<629.0,340.0>--<627.0,343.0>> = 7.125016348901705

	* petapp (U+E006): B<<633.0,334.0>-<633.0,333.0>-<634.0,331.0>>/L<<634.0,331.0>--<633.0,334.0>> = 8.130102354155916

	* petapp (U+E006): B<<638.0,346.0>-<639.0,345.0>-<640.0,343.0>>/L<<640.0,343.0>--<638.0,346.0>> = 7.125016348901705

	* petapp (U+E006): B<<641.0,321.0>-<642.0,320.0>-<643.0,318.0>>/L<<643.0,318.0>--<641.0,321.0>> = 7.125016348901705

	* petapp (U+E006): B<<669.0,316.0>-<670.0,315.0>-<672.0,314.0>>/L<<672.0,314.0>--<669.0,316.0>> = 7.125016348901757

	* petapp (U+E006): B<<669.0,456.0>-<667.0,454.0>-<666.0,452.0>>/L<<666.0,452.0>--<669.0,456.0>> = 10.304846468766044

	* petapp (U+E006): B<<670.0,137.0>-<671.0,138.0>-<672.0,140.0>>/L<<672.0,140.0>--<670.0,137.0>> = 7.125016348901705

	* petapp (U+E006): B<<679.0,141.0>-<681.0,142.0>-<682.0,143.0>>/L<<682.0,143.0>--<679.0,141.0>> = 11.309932474020195

	* petapp (U+E006): B<<687.0,164.0>-<688.0,166.0>-<689.0,167.0>>/L<<689.0,167.0>--<687.0,164.0>> = 11.309932474020227

	* petapp (U+E006): B<<713.0,484.0>-<712.0,484.0>-<710.0,483.0>>/L<<710.0,483.0>--<713.0,484.0>> = 8.13010235415587

	* petapp (U+E006): B<<763.0,5.0>-<762.0,7.0>-<761.0,8.0>>/L<<761.0,8.0>--<763.0,5.0>> = 11.309932474020195

	* petapp (U+E006): L<<274.0,517.0>--<273.0,520.0>>/B<<273.0,520.0>-<274.0,518.0>-<274.0,517.0>> = 8.130102354155916

	* petapp (U+E006): L<<280.0,491.0>--<279.0,494.0>>/B<<279.0,494.0>-<280.0,492.0>-<280.0,491.0>> = 8.130102354155916

	* petapp (U+E006): L<<291.0,468.0>--<289.0,471.0>>/B<<289.0,471.0>-<290.0,469.0>-<291.0,468.0>> = 7.125016348901705

	* petapp (U+E006): L<<296.0,459.0>--<295.0,462.0>>/B<<295.0,462.0>-<296.0,460.0>-<296.0,459.0>> = 8.130102354155916

	* petapp (U+E006): L<<312.0,442.0>--<308.0,445.0>>/B<<308.0,445.0>-<310.0,444.0>-<312.0,442.0>> = 10.304846468766009

	* petapp (U+E006): L<<331.0,427.0>--<328.0,429.0>>/B<<328.0,429.0>-<329.0,428.0>-<331.0,427.0>> = 11.309932474020195

	* petapp (U+E006): L<<380.0,128.0>--<379.0,131.0>>/B<<379.0,131.0>-<380.0,129.0>-<380.0,128.0>> = 8.130102354155916

	* petapp (U+E006): L<<387.0,108.0>--<386.0,111.0>>/B<<386.0,111.0>-<387.0,109.0>-<387.0,108.0>> = 8.130102354155916

	* petapp (U+E006): L<<499.0,225.0>--<505.0,222.0>>/L<<505.0,222.0>--<498.0,226.0>> = 3.1798301198640497

	* petapp (U+E006): L<<504.0,71.0>--<499.0,69.0>>/B<<499.0,69.0>-<502.0,71.0>-<504.0,71.0>> = 11.888658039627936

	* petapp (U+E006): L<<517.0,66.0>--<513.0,65.0>>/B<<513.0,65.0>-<515.0,65.0>-<517.0,66.0>> = 14.036243467926484

	* petapp (U+E006): L<<523.0,67.0>--<519.0,66.0>>/B<<519.0,66.0>-<521.0,66.0>-<523.0,67.0>> = 14.036243467926484

	* petapp (U+E006): L<<532.0,68.0>--<536.0,69.0>>/B<<536.0,69.0>-<534.0,69.0>-<532.0,68.0>> = 14.036243467926484

	* petapp (U+E006): L<<534.0,195.0>--<536.0,192.0>>/B<<536.0,192.0>-<535.0,194.0>-<534.0,195.0>> = 7.125016348901757

	* petapp (U+E006): L<<534.0,310.0>--<537.0,308.0>>/B<<537.0,308.0>-<536.0,309.0>-<534.0,310.0>> = 11.309932474020227

	* petapp (U+E006): L<<536.0,440.0>--<539.0,438.0>>/B<<539.0,438.0>-<538.0,439.0>-<536.0,440.0>> = 11.309932474020227

	* petapp (U+E006): L<<541.0,111.0>--<539.0,108.0>>/B<<539.0,108.0>-<540.0,109.0>-<541.0,111.0>> = 11.309932474020227

	* petapp (U+E006): L<<541.0,70.0>--<545.0,71.0>>/B<<545.0,71.0>-<540.0,70.0>-<541.0,70.0>> = 2.726310993906212

	* petapp (U+E006): L<<542.0,181.0>--<543.0,178.0>>/B<<543.0,178.0>-<542.0,180.0>-<542.0,181.0>> = 8.13010235415587

	* petapp (U+E006): L<<545.0,434.0>--<548.0,432.0>>/B<<548.0,432.0>-<547.0,433.0>-<545.0,434.0>> = 11.309932474020227

	* petapp (U+E006): L<<546.0,127.0>--<545.0,123.0>>/B<<545.0,123.0>-<546.0,125.0>-<546.0,127.0>> = 12.528807709151492

	* petapp (U+E006): L<<556.0,74.0>--<553.0,73.0>>/B<<553.0,73.0>-<555.0,74.0>-<556.0,74.0>> = 8.130102354155916

	* petapp (U+E006): L<<577.0,401.0>--<575.0,404.0>>/B<<575.0,404.0>-<576.0,403.0>-<577.0,401.0>> = 11.309932474020227

	* petapp (U+E006): L<<583.0,256.0>--<584.0,252.0>>/B<<584.0,252.0>-<584.0,254.0>-<583.0,256.0>> = 14.036243467926484

	* petapp (U+E006): L<<586.0,384.0>--<587.0,380.0>>/B<<587.0,380.0>-<587.0,382.0>-<586.0,384.0>> = 14.036243467926484

	* petapp (U+E006): L<<598.0,432.0>--<599.0,429.0>>/B<<599.0,429.0>-<598.0,431.0>-<598.0,432.0>> = 8.13010235415587

	* petapp (U+E006): L<<602.0,122.0>--<601.0,125.0>>/B<<601.0,125.0>-<602.0,123.0>-<602.0,122.0>> = 8.130102354155916

	* petapp (U+E006): L<<611.0,96.0>--<611.0,96.0>>/B<<611.0,96.0>-<607.0,95.0>-<603.5,92.5>> = 14.036243467926484

	* petapp (U+E006): L<<612.0,379.0>--<610.0,384.0>>/B<<610.0,384.0>-<611.0,381.0>-<612.0,379.0>> = 3.366460663429615

	* petapp (U+E006): L<<613.0,374.0>--<612.0,377.0>>/B<<612.0,377.0>-<613.0,375.0>-<613.0,374.0>> = 8.130102354155916

	* petapp (U+E006): L<<615.0,369.0>--<614.0,372.0>>/B<<614.0,372.0>-<615.0,370.0>-<615.0,369.0>> = 8.130102354155916

	* petapp (U+E006): L<<616.0,379.0>--<614.0,384.0>>/B<<614.0,384.0>-<615.0,382.0>-<616.0,379.0>> = 4.763641690726066

	* petapp (U+E006): L<<629.0,340.0>--<627.0,343.0>>/B<<627.0,343.0>-<628.0,342.0>-<629.0,340.0>> = 11.309932474020227

	* petapp (U+E006): L<<640.0,343.0>--<638.0,346.0>>/B<<638.0,346.0>-<639.0,345.0>-<640.0,343.0>> = 11.309932474020227

	* petapp (U+E006): L<<643.0,318.0>--<641.0,321.0>>/B<<641.0,321.0>-<642.0,320.0>-<643.0,318.0>> = 11.309932474020227

	* petapp (U+E006): L<<657.0,433.0>--<658.0,436.0>>/B<<658.0,436.0>-<657.0,434.0>-<657.0,432.5>> = 8.13010235415587

	* petapp (U+E006): L<<661.0,383.0>--<660.0,386.0>>/B<<660.0,386.0>-<661.0,384.0>-<661.0,383.0>> = 8.130102354155916

	* petapp (U+E006): L<<666.0,452.0>--<669.0,456.0>>/B<<669.0,456.0>-<667.0,454.0>-<666.0,452.0>> = 8.13010235415596

	* petapp (U+E006): L<<672.0,140.0>--<670.0,137.0>>/B<<670.0,137.0>-<671.0,138.0>-<672.0,140.0>> = 11.309932474020227

	* petapp (U+E006): L<<682.0,143.0>--<679.0,141.0>>/B<<679.0,141.0>-<681.0,142.0>-<682.0,143.0>> = 7.125016348901757

	* petapp (U+E006): L<<686.0,162.0>--<685.0,159.0>>/B<<685.0,159.0>-<686.0,161.0>-<686.0,162.0>> = 8.130102354155916

	* petapp (U+E006): L<<689.0,167.0>--<687.0,164.0>>/B<<687.0,164.0>-<688.0,166.0>-<689.0,167.0>> = 7.125016348901705

	* petapp (U+E006): L<<689.0,256.0>--<690.0,253.0>>/B<<690.0,253.0>-<689.0,255.0>-<689.0,256.0>> = 8.13010235415587

	* petapp (U+E006): L<<691.0,251.0>--<692.0,248.0>>/B<<692.0,248.0>-<691.0,250.0>-<691.0,251.0>> = 8.13010235415587

	* petapp (U+E006): L<<700.0,480.0>--<703.0,481.0>>/B<<703.0,481.0>-<701.0,480.0>-<700.0,479.5>> = 8.13010235415587

	* petapp (U+E006): L<<705.0,482.0>--<708.0,483.0>>/B<<708.0,483.0>-<706.0,482.0>-<705.0,482.0>> = 8.13010235415587

	* petapp (U+E006): L<<708.0,293.0>--<705.0,294.0>>/B<<705.0,294.0>-<707.0,293.0>-<708.0,293.0>> = 8.130102354155916

	* petapp (U+E006): L<<728.0,285.0>--<725.0,286.0>>/B<<725.0,286.0>-<727.0,285.0>-<728.0,285.0>> = 8.130102354155916

	* petapp (U+E006): L<<761.0,8.0>--<763.0,5.0>>/B<<763.0,5.0>-<762.0,7.0>-<761.0,8.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<581.0,372.0>-<585.0,368.0>-<588.0,366.0>>/L<<588.0,366.0>--<581.0,372.0>> = 6.911227119024609

	* petapp.minimal (U+E007): B<<631.0,435.0>-<631.0,433.0>-<632.0,430.0>>/L<<632.0,430.0>--<631.0,435.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<632.0,481.0>-<632.0,480.0>-<631.0,478.0>>/L<<631.0,478.0>--<632.0,481.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<645.0,399.0>-<646.0,397.0>-<647.0,396.0>>/L<<647.0,396.0>--<645.0,399.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<646.0,510.0>-<645.0,508.0>-<644.0,507.0>>/L<<644.0,507.0>--<646.0,510.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<676.0,538.0>-<674.0,537.0>-<673.0,536.0>>/L<<673.0,536.0>--<676.0,538.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<700.0,247.0>-<699.0,248.0>-<698.0,250.0>>/L<<698.0,250.0>--<700.0,247.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<714.0,147.0>-<714.0,148.0>-<713.0,150.0>>/L<<713.0,150.0>--<714.0,147.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<720.0,137.0>-<719.0,139.0>-<718.0,140.0>>/L<<718.0,140.0>--<720.0,137.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<732.0,185.0>-<731.0,187.0>-<731.0,189.0>>/L<<731.0,189.0>--<732.0,185.0>> = 14.036243467926484

	* petapp.minimal (U+E007): B<<743.0,53.0>-<743.0,54.0>-<742.0,56.0>>/L<<742.0,56.0>--<743.0,53.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<212.0,538.0>--<212.0,800.0>>/B<<212.0,800.0>-<214.0,769.0>-<226.5,742.0>> = 3.6913859864512575

	* petapp.minimal (U+E007): L<<628.0,462.0>--<629.0,465.0>>/B<<629.0,465.0>-<628.0,463.0>-<628.0,462.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<630.0,473.0>--<631.0,476.0>>/B<<631.0,476.0>-<630.0,474.0>-<630.0,473.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<632.0,430.0>--<631.0,435.0>>/B<<631.0,435.0>-<631.0,433.0>-<632.0,430.0>> = 11.309932474020227

	* petapp.minimal (U+E007): L<<637.0,222.0>--<640.0,221.0>>/B<<640.0,221.0>-<638.0,222.0>-<637.0,222.5>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<639.0,498.0>--<640.0,501.0>>/B<<640.0,501.0>-<639.0,499.0>-<639.0,498.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<644.0,507.0>--<646.0,510.0>>/B<<646.0,510.0>-<645.0,508.0>-<644.0,507.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<647.0,396.0>--<645.0,399.0>>/B<<645.0,399.0>-<646.0,397.0>-<647.0,396.0>> = 7.125016348901705

	* petapp.minimal (U+E007): L<<673.0,536.0>--<676.0,538.0>>/B<<676.0,538.0>-<674.0,537.0>-<673.0,536.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<682.0,542.0>--<685.0,543.0>>/B<<685.0,543.0>-<683.0,542.0>-<682.0,542.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<687.0,544.0>--<690.0,545.0>>/B<<690.0,545.0>-<688.0,544.0>-<687.0,544.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<698.0,250.0>--<700.0,247.0>>/B<<700.0,247.0>-<699.0,248.0>-<698.0,250.0>> = 11.309932474020195

	* petapp.minimal (U+E007): L<<718.0,218.0>--<719.0,215.0>>/B<<719.0,215.0>-<718.0,217.0>-<718.0,218.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<731.0,113.0>--<732.0,110.0>>/B<<732.0,110.0>-<731.0,112.0>-<731.0,113.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<740.0,156.0>--<739.0,160.0>>/B<<739.0,160.0>-<740.0,153.0>-<740.0,156.0>> = 5.906141113770497

	* petapp.minimal (U+E007): L<<744.0,137.0>--<743.0,140.0>>/B<<743.0,140.0>-<744.0,138.0>-<744.0,137.0>> = 8.130102354155916

	* petapp.minimal (U+E007): L<<746.0,123.0>--<747.0,120.0>>/B<<747.0,120.0>-<746.0,122.0>-<746.0,123.0>> = 8.13010235415587

	* petapp.wpda (U+E008): B<<485.0,2.0>-<482.0,5.0>-<482.0,6.0>>/L<<482.0,6.0>--<481.0,1.0>> = 11.309932474020227

	* petapp.wpda (U+E008): L<<185.0,222.0>--<180.0,218.0>>/B<<180.0,218.0>-<182.0,219.0>-<183.0,218.0>> = 12.094757077012058

	* pisafe (U+E010): B<<175.0,538.0>-<175.0,536.0>-<174.0,534.0>>/L<<174.0,534.0>--<175.0,538.0>> = 12.528807709151492

	* pisafe (U+E010): B<<190.0,573.0>-<189.0,572.0>-<188.0,570.0>>/L<<188.0,570.0>--<190.0,573.0>> = 7.125016348901757

	* pisafe (U+E010): B<<211.0,602.0>-<210.0,600.0>-<208.0,598.0>>/L<<208.0,598.0>--<211.0,602.0>> = 8.13010235415596

	* pisafe (U+E010): B<<784.0,594.0>-<783.0,596.0>-<782.0,597.0>>/L<<782.0,597.0>--<784.0,594.0>> = 11.309932474020195

	* pisafe (U+E010): B<<797.0,577.0>-<796.0,579.0>-<795.0,580.0>>/L<<795.0,580.0>--<797.0,577.0>> = 11.309932474020195

	* pisafe (U+E010): B<<816.0,530.0>-<816.0,532.0>-<815.0,534.0>>/L<<815.0,534.0>--<816.0,530.0>> = 12.528807709151492

	* pisafe (U+E010): B<<820.0,515.0>-<820.0,516.0>-<819.0,518.0>>/L<<819.0,518.0>--<820.0,515.0>> = 8.13010235415587

	* pisafe (U+E010): L<<174.0,534.0>--<175.0,538.0>>/B<<175.0,538.0>-<175.0,536.0>-<174.0,534.0>> = 14.036243467926484

	* pisafe (U+E010): L<<188.0,570.0>--<190.0,573.0>>/B<<190.0,573.0>-<189.0,572.0>-<188.0,570.0>> = 11.309932474020195

	* pisafe (U+E010): L<<208.0,598.0>--<211.0,602.0>>/B<<211.0,602.0>-<210.0,600.0>-<208.0,598.0>> = 10.304846468766044

	* pisafe (U+E010): L<<750.0,626.0>--<754.0,623.0>>/B<<754.0,623.0>-<752.0,624.0>-<750.0,626.0>> = 10.304846468766009

	* pisafe (U+E010): L<<782.0,597.0>--<784.0,594.0>>/B<<784.0,594.0>-<783.0,596.0>-<782.0,597.0>> = 7.125016348901757

	* pisafe (U+E010): L<<795.0,580.0>--<797.0,577.0>>/B<<797.0,577.0>-<796.0,579.0>-<795.0,580.0>> = 7.125016348901757

	* pisafe (U+E010): L<<815.0,534.0>--<816.0,530.0>>/B<<816.0,530.0>-<816.0,532.0>-<815.0,534.0>> = 14.036243467926484 

	* pisafe (U+E010): L<<817.0,528.0>--<818.0,525.0>>/B<<818.0,525.0>-<817.0,527.0>-<817.0,528.0>> = 8.13010235415587 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* exclam (U+0021): L<<105.0,224.0>--<103.0,729.0>>

	* exclam (U+0021): L<<153.0,729.0>--<150.0,224.0>>

	* exclamdown (U+00A1): L<<103.0,-203.0>--<105.0,302.0>> 

	* exclamdown (U+00A1): L<<150.0,302.0>--<153.0,-203.0>> [code: found-semi-vertical]
</div></details><br></div></details><details><summary><b>[19] PitagonSansText-ExtraLightItalic.ttf</b></summary><div><details><summary>🔥 <b>FAIL:</b> Check Google Fonts glyph coverage. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/glyph_coverage">com.google.fonts/check/glyph_coverage</a>)</summary><div>


* 🔥 **FAIL** Missing required codepoints:

	- 0x0132 (LATIN CAPITAL LIGATURE IJ)
 

	- 0x0133 (LATIN SMALL LIGATURE IJ)
 [code: missing-codepoints]
</div></details><details><summary>🔥 <b>FAIL:</b> Check OFL body text is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text">com.google.fonts/check/license/OFL_body_text</a>)</summary><div>


* 🔥 **FAIL** The OFL.txt body text is incorrect. Please use https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt as a template. You should only modify the first line. [code: incorrect-ofl-body-text]
</div></details><details><summary>🔥 <b>FAIL:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* 🔥 **FAIL** License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ
at: https://scripts.sil.org/OFL." Must be changed to "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL" [code: wrong]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>🔥 <b>FAIL:</b> Name table entries should not contain line-breaks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/line_breaks">com.google.fonts/check/name/line_breaks</a>)</summary><div>


* 🔥 **FAIL** Name entry DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
* 🔥 **FAIL** Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break. [code: line-break]
</div></details><details><summary>🔥 <b>FAIL:</b> Checking OS/2 usWinAscent & usWinDescent. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/family/win_ascent_and_descent">com.google.fonts/check/family/win_ascent_and_descent</a>)</summary><div>


* 🔥 **FAIL** OS/2.usWinAscent value should be equal or greater than 1294, but got 1214 instead [code: ascent]
</div></details><details><summary>🔥 <b>FAIL:</b> Do we have the latest version of FontBakery installed? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/fontbakery_version">com.google.fonts/check/fontbakery_version</a>)</summary><div>


* 🔥 **FAIL** Current Font Bakery version is 0.8.11, while a newer 0.8.13 is already available. Please upgrade it with 'pip install -U fontbakery' [code: outdated-fontbakery]
</div></details><details><summary>🔥 <b>FAIL:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 🔥 **FAIL** The dot of soft dotted characters used in orthographies must disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ ị̀ ị́ ị̂ ị̃ ị̄

The dot of soft dotted characters should disappear in other cases, for example: i̦̇ i̦̊ i̦̋ ǐ̦ i̦̒ j̦̀ j̦́ j̦̃ j̦̄ j̦̆ j̦̇ j̦̈ j̦̉ j̦̊ j̦̋ ǰ̦ j̦̏ j̦̑ j̦̒ į̆ [code: soft-dotted]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'Pita' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
</div></details><details><summary>⚠ <b>WARN:</b> Description strings in the name table must not exceed 200 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/description_max_length">com.google.fonts/check/name/description_max_length</a>)</summary><div>


* ⚠ **WARN** A few name table entries with ID=10 (NameID.DESCRIPTION) are longer than 200 characters. Please check whether those entries are copyright notices mistakenly stored in the description string entries by a bug in an old FontLab version. If that's the case, then such copyright notices must be removed from these entries. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Is there kerning info for non-ligated sequences? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/kerning_for_non_ligated_sequences">com.google.fonts/check/kerning_for_non_ligated_sequences</a>)</summary><div>


* ⚠ **WARN** GPOS table lacks kerning info for the following non-ligated sequences:

	- f + f

	- f + i

	- i + f

	- f + l

	- l + f 

	- i + l [code: lacks-kern-info]
</div></details><details><summary>⚠ <b>WARN:</b> Combined length of family and style must not exceed 27 characters. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/family_and_style_max_length">com.google.fonts/check/name/family_and_style_max_length</a>)</summary><div>


* ⚠ **WARN** The combined length of family and style exceeds 27 chars in the following 'WINDOWS' entries:
 FONT_FAMILY_NAME = 'Pitagon Sans Text ExtraLight' / SUBFAMILY_NAME = 'Italic'

Please take a look at the conversation at https://github.com/googlefonts/fontbakery/issues/2179 in order to understand the reasoning behind these name table records max-length criteria. [code: too-long]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- periodcentered.001 

	- registered.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni01EA	Contours detected: 3	Expected: 2

	- Glyph name: uni01EB	Contours detected: 3	Expected: 2

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: fi	Contours detected: 1	Expected: 3

	- Glyph name: fl	Contours detected: 1	Expected: 2

	- Glyph name: tbar	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni1E08	Contours detected: 3	Expected: 2

	- Glyph name: uni1E09	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1C	Contours detected: 3	Expected: 2

	- Glyph name: uni1E1D	Contours detected: 4	Expected: 3

	- Glyph name: uni1E9E	Contours detected: 2	Expected: 1 

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* petapp (U+E006): L<<282.0,304.0>--<312.0,286.0>> -> L<<312.0,286.0>--<339.0,271.0>>

	* petapp (U+E006): L<<312.0,333.0>--<273.0,356.0>> -> L<<273.0,356.0>--<257.0,365.0>>

	* petapp (U+E006): L<<355.0,309.0>--<312.0,333.0>> -> L<<312.0,333.0>--<273.0,356.0>>

	* petapp (U+E006): L<<371.0,299.0>--<355.0,309.0>> -> L<<355.0,309.0>--<312.0,333.0>>

	* petapp (U+E006): L<<371.0,640.0>--<467.0,585.0>> -> L<<467.0,585.0>--<515.0,556.0>>

	* petapp (U+E006): L<<373.0,298.0>--<371.0,299.0>> -> L<<371.0,299.0>--<355.0,309.0>>

	* petapp (U+E006): L<<426.0,268.0>--<373.0,298.0>> -> L<<373.0,298.0>--<371.0,299.0>>

	* petapp (U+E006): L<<467.0,585.0>--<515.0,556.0>> -> L<<515.0,556.0>--<534.0,545.0>>

	* petapp (U+E006): L<<468.0,243.0>--<426.0,268.0>> -> L<<426.0,268.0>--<373.0,298.0>>

	* petapp (U+E006): L<<474.0,240.0>--<468.0,243.0>> -> L<<468.0,243.0>--<426.0,268.0>>

	* petapp (U+E006): L<<498.0,226.0>--<474.0,240.0>> -> L<<474.0,240.0>--<468.0,243.0>>

	* petapp (U+E006): L<<505.0,222.0>--<498.0,226.0>> -> L<<498.0,226.0>--<474.0,240.0>>

	* petapp (U+E006): L<<691.0,61.0>--<692.0,60.0>> -> L<<692.0,60.0>--<696.0,56.0>>

	* petapp (U+E006): L<<721.0,485.0>--<725.0,485.0>> -> L<<725.0,485.0>--<764.0,485.0>>

	* petapp.minimal (U+E007): L<<264.0,373.0>--<351.0,339.0>> -> L<<351.0,339.0>--<432.0,305.0>>

	* petapp.minimal (U+E007): L<<351.0,339.0>--<432.0,305.0>> -> L<<432.0,305.0>--<448.0,299.0>>

	* petapp.minimal (U+E007): L<<381.0,352.0>--<331.0,376.0>> -> L<<331.0,376.0>--<305.0,390.0>>

	* petapp.minimal (U+E007): L<<432.0,305.0>--<448.0,299.0>> -> L<<448.0,299.0>--<504.0,276.0>>

	* petapp.minimal (U+E007): L<<432.0,326.0>--<381.0,352.0>> -> L<<381.0,352.0>--<331.0,376.0>>

	* petapp.minimal (U+E007): L<<435.0,187.0>--<405.0,192.0>> -> L<<405.0,192.0>--<304.0,211.0>>

	* petapp.minimal (U+E007): L<<448.0,299.0>--<504.0,276.0>> -> L<<504.0,276.0>--<612.0,232.0>>

	* petapp.minimal (U+E007): L<<455.0,314.0>--<432.0,326.0>> -> L<<432.0,326.0>--<381.0,352.0>>

	* petapp.minimal (U+E007): L<<504.0,175.0>--<435.0,187.0>> -> L<<435.0,187.0>--<405.0,192.0>>

	* petapp.minimal (U+E007): L<<504.0,276.0>--<612.0,232.0>> -> L<<612.0,232.0>--<621.0,229.0>>

	* petapp.minimal (U+E007): L<<504.0,289.0>--<455.0,314.0>> -> L<<455.0,314.0>--<432.0,326.0>>

	* petapp.minimal (U+E007): L<<588.0,160.0>--<504.0,175.0>> -> L<<504.0,175.0>--<435.0,187.0>>

	* petapp.minimal (U+E007): L<<621.0,229.0>--<504.0,289.0>> -> L<<504.0,289.0>--<455.0,314.0>>

	* petapp.minimal (U+E007): L<<742.0,30.0>--<742.0,31.0>> -> L<<742.0,31.0>--<742.0,32.0>>

	* petapp.minimal (U+E007): L<<743.0,33.0>--<743.0,34.0>> -> L<<743.0,34.0>--<743.0,36.0>>

	* petapp.minimal (U+E007): L<<743.0,34.0>--<743.0,36.0>> -> L<<743.0,36.0>--<743.0,37.0>>

	* petapp.minimal (U+E007): L<<747.0,73.0>--<746.0,63.0>> -> L<<746.0,63.0>--<743.0,38.0>>

	* petapp.minimal (U+E007): L<<747.0,74.0>--<747.0,73.0>> -> L<<747.0,73.0>--<746.0,63.0>>

	* petapp.minimal (U+E007): L<<752.0,131.0>--<747.0,74.0>> -> L<<747.0,74.0>--<747.0,73.0>>

	* petapp.minimal (U+E007): L<<754.0,162.0>--<752.0,131.0>> -> L<<752.0,131.0>--<747.0,74.0>>

	* petapp.minimal (U+E007): L<<755.0,175.0>--<754.0,162.0>> -> L<<754.0,162.0>--<752.0,131.0>>

	* petapp.minimal (U+E007): L<<757.0,196.0>--<755.0,175.0>> -> L<<755.0,175.0>--<754.0,162.0>>

	* petapp.minimal (U+E007): L<<758.0,210.0>--<757.0,196.0>> -> L<<757.0,196.0>--<755.0,175.0>>

	* petapp.minimal (U+E007): L<<758.0,213.0>--<758.0,210.0>> -> L<<758.0,210.0>--<757.0,196.0>>

	* petapp.wpda (U+E008): L<<640.0,140.0>--<627.0,132.0>> -> L<<627.0,132.0>--<618.0,127.0>>

	* piads (U+E001): L<<112.0,541.0>--<116.0,544.0>> -> L<<116.0,544.0>--<445.0,782.0>>

	* piads (U+E001): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<878.0,541.0>>

	* picall (U+E009): L<<112.0,541.0>--<116.0,544.0>> -> L<<116.0,544.0>--<445.0,782.0>>

	* picall (U+E009): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<878.0,541.0>>

	* pioffice (U+E002): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<877.0,542.0>>

	* pisafe (U+E010): L<<167.0,362.0>--<167.0,491.0>> -> L<<167.0,491.0>--<167.0,494.0>>

	* pisafe (U+E010): L<<203.0,695.0>--<239.0,708.0>> -> L<<239.0,708.0>--<389.0,762.0>>

	* pisafe (U+E010): L<<239.0,708.0>--<389.0,762.0>> -> L<<389.0,762.0>--<494.0,800.0>>

	* pisafe (U+E010): L<<495.0,800.0>--<600.0,762.0>> -> L<<600.0,762.0>--<750.0,708.0>>

	* pisafe (U+E010): L<<600.0,762.0>--<750.0,708.0>> -> L<<750.0,708.0>--<786.0,695.0>>

	* pisign (U+E005): L<<546.0,782.0>--<874.0,544.0>> -> L<<874.0,544.0>--<877.0,542.0>>

	* pitagon (U+E000): L<<112.0,543.0>--<116.0,546.0>> -> L<<116.0,546.0>--<445.0,784.0>>

	* pitagon (U+E000): L<<209.0,62.0>--<84.0,446.0>> -> L<<84.0,446.0>--<82.0,452.0>>

	* pitagon (U+E000): L<<547.0,784.0>--<874.0,546.0>> -> L<<874.0,546.0>--<878.0,543.0>>

	* pitagram (U+E003): L<<813.0,512.0>--<810.0,514.0>> -> L<<810.0,514.0>--<537.0,711.0>>

	* piweb (U+E004): L<<813.0,512.0>--<810.0,514.0>> -> L<<810.0,514.0>--<537.0,711.0>>

	* sparks (U+E011): L<<100.0,798.0>--<103.0,797.0>> -> L<<103.0,797.0>--<198.0,762.0>>

	* sparks (U+E011): L<<103.0,797.0>--<198.0,762.0>> -> L<<198.0,762.0>--<209.0,759.0>>

	* sparks (U+E011): L<<198.0,762.0>--<209.0,759.0>> -> L<<209.0,759.0>--<400.0,690.0>>

	* sparks (U+E011): L<<209.0,759.0>--<400.0,690.0>> -> L<<400.0,690.0>--<431.0,680.0>>

	* sparks (U+E011): L<<291.0,596.0>--<363.0,534.0>> -> L<<363.0,534.0>--<382.0,516.0>>

	* sparks (U+E011): L<<381.0,366.0>--<383.0,367.0>> -> L<<383.0,367.0>--<486.0,429.0>>

	* sparks (U+E011): L<<383.0,367.0>--<486.0,429.0>> -> L<<486.0,429.0>--<488.0,430.0>>

	* sparks (U+E011): L<<409.0,102.0>--<98.0,641.0>> -> L<<98.0,641.0>--<47.0,731.0>>

	* sparks (U+E011): L<<440.0,659.0>--<436.0,649.0>> -> L<<436.0,649.0>--<434.0,643.0>>

	* sparks (U+E011): L<<454.0,24.0>--<409.0,102.0>> -> L<<409.0,102.0>--<98.0,641.0>>

	* sparks (U+E011): L<<504.0,429.0>--<606.0,367.0>> -> L<<606.0,367.0>--<608.0,366.0>>

	* sparks (U+E011): L<<558.0,680.0>--<596.0,694.0>> -> L<<596.0,694.0>--<780.0,759.0>>

	* sparks (U+E011): L<<579.0,101.0>--<550.0,51.0>> -> L<<550.0,51.0>--<535.0,24.0>>

	* sparks (U+E011): L<<596.0,694.0>--<780.0,759.0>> -> L<<780.0,759.0>--<807.0,768.0>>

	* sparks (U+E011): L<<607.0,516.0>--<627.0,534.0>> -> L<<627.0,534.0>--<699.0,596.0>>

	* sparks (U+E011): L<<614.0,629.0>--<577.0,632.0>> -> L<<577.0,632.0>--<568.0,633.0>>

	* sparks (U+E011): L<<655.0,626.0>--<614.0,629.0>> -> L<<614.0,629.0>--<577.0,632.0>>

	* sparks (U+E011): L<<656.0,626.0>--<655.0,626.0>> -> L<<655.0,626.0>--<614.0,629.0>>

	* sparks (U+E011): L<<690.0,623.0>--<656.0,626.0>> -> L<<656.0,626.0>--<655.0,626.0>>

	* sparks (U+E011): L<<691.0,623.0>--<690.0,623.0>> -> L<<690.0,623.0>--<656.0,626.0>>

	* sparks (U+E011): L<<750.0,397.0>--<579.0,101.0>> -> L<<579.0,101.0>--<550.0,51.0>>

	* sparks (U+E011): L<<780.0,759.0>--<807.0,768.0>> -> L<<807.0,768.0>--<886.0,797.0>>

	* sparks (U+E011): L<<897.0,652.0>--<750.0,397.0>> -> L<<750.0,397.0>--<579.0,101.0>>

	* sparks (U+E011): L<<942.0,730.0>--<897.0,652.0>> -> L<<897.0,652.0>--<750.0,397.0>> 

	* sparks (U+E011): L<<943.0,732.0>--<942.0,730.0>> -> L<<942.0,730.0>--<897.0,652.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* petapp (U+E006): B<<289.0,471.0>-<290.0,469.0>-<291.0,468.0>>/L<<291.0,468.0>--<289.0,471.0>> = 11.309932474020227

	* petapp (U+E006): B<<295.0,293.0>-<289.0,300.0>-<282.0,304.0>>/L<<282.0,304.0>--<312.0,286.0>> = 1.2188752351307344

	* petapp (U+E006): B<<328.0,429.0>-<329.0,428.0>-<331.0,427.0>>/L<<331.0,427.0>--<328.0,429.0>> = 7.125016348901757

	* petapp (U+E006): B<<415.0,76.0>-<416.0,76.0>-<418.0,75.0>>/L<<418.0,75.0>--<415.0,76.0>> = 8.130102354155916

	* petapp (U+E006): B<<424.0,71.0>-<425.0,71.0>-<427.0,70.0>>/L<<427.0,70.0>--<424.0,71.0>> = 8.130102354155916

	* petapp (U+E006): B<<439.0,65.0>-<440.0,65.0>-<442.0,64.0>>/L<<442.0,64.0>--<439.0,65.0>> = 8.130102354155916

	* petapp (U+E006): B<<483.0,64.0>-<484.0,64.0>-<486.0,65.0>>/L<<486.0,65.0>--<483.0,64.0>> = 8.130102354155916

	* petapp (U+E006): B<<513.0,65.0>-<515.0,65.0>-<517.0,66.0>>/L<<517.0,66.0>--<513.0,65.0>> = 12.528807709151463

	* petapp (U+E006): B<<519.0,66.0>-<521.0,66.0>-<523.0,67.0>>/L<<523.0,67.0>--<519.0,66.0>> = 12.528807709151463

	* petapp (U+E006): B<<529.0,68.0>-<528.0,68.0>-<526.0,67.0>>/L<<526.0,67.0>--<529.0,68.0>> = 8.13010235415587

	* petapp (U+E006): B<<536.0,192.0>-<535.0,194.0>-<534.0,195.0>>/L<<534.0,195.0>--<536.0,192.0>> = 11.309932474020195

	* petapp (U+E006): B<<536.0,69.0>-<534.0,69.0>-<532.0,68.0>>/L<<532.0,68.0>--<536.0,69.0>> = 12.528807709151492

	* petapp (U+E006): B<<537.0,308.0>-<536.0,309.0>-<534.0,310.0>>/L<<534.0,310.0>--<537.0,308.0>> = 7.125016348901757

	* petapp (U+E006): B<<539.0,108.0>-<540.0,109.0>-<541.0,111.0>>/L<<541.0,111.0>--<539.0,108.0>> = 7.125016348901705

	* petapp (U+E006): B<<539.0,438.0>-<538.0,439.0>-<536.0,440.0>>/L<<536.0,440.0>--<539.0,438.0>> = 7.125016348901757

	* petapp (U+E006): B<<545.0,123.0>-<546.0,125.0>-<546.0,127.0>>/L<<546.0,127.0>--<545.0,123.0>> = 14.036243467926484

	* petapp (U+E006): B<<548.0,432.0>-<547.0,433.0>-<545.0,434.0>>/L<<545.0,434.0>--<548.0,432.0>> = 7.125016348901757

	* petapp (U+E006): B<<548.0,72.0>-<549.0,72.0>-<551.0,73.0>>/L<<551.0,73.0>--<548.0,72.0>> = 8.130102354155916

	* petapp (U+E006): B<<575.0,404.0>-<576.0,403.0>-<577.0,401.0>>/L<<577.0,401.0>--<575.0,404.0>> = 7.125016348901705

	* petapp (U+E006): B<<587.0,380.0>-<587.0,382.0>-<586.0,384.0>>/L<<586.0,384.0>--<587.0,380.0>> = 12.528807709151492

	* petapp (U+E006): B<<610.0,384.0>-<611.0,381.0>-<612.0,379.0>>/L<<612.0,379.0>--<610.0,384.0>> = 4.763641690726066

	* petapp (U+E006): B<<614.0,384.0>-<615.0,382.0>-<616.0,379.0>>/L<<616.0,379.0>--<614.0,384.0>> = 3.366460663429615

	* petapp (U+E006): B<<627.0,343.0>-<628.0,342.0>-<629.0,340.0>>/L<<629.0,340.0>--<627.0,343.0>> = 7.125016348901705

	* petapp (U+E006): B<<633.0,334.0>-<633.0,333.0>-<634.0,331.0>>/L<<634.0,331.0>--<633.0,334.0>> = 8.130102354155916

	* petapp (U+E006): B<<638.0,346.0>-<639.0,345.0>-<640.0,343.0>>/L<<640.0,343.0>--<638.0,346.0>> = 7.125016348901705

	* petapp (U+E006): B<<641.0,321.0>-<642.0,320.0>-<643.0,318.0>>/L<<643.0,318.0>--<641.0,321.0>> = 7.125016348901705

	* petapp (U+E006): B<<669.0,316.0>-<670.0,315.0>-<672.0,314.0>>/L<<672.0,314.0>--<669.0,316.0>> = 7.125016348901757

	* petapp (U+E006): B<<669.0,456.0>-<667.0,454.0>-<666.0,452.0>>/L<<666.0,452.0>--<669.0,456.0>> = 10.304846468766044

	* petapp (U+E006): B<<670.0,137.0>-<671.0,138.0>-<672.0,140.0>>/L<<672.0,140.0>--<670.0,137.0>> = 7.125016348901705

	* petapp (U+E006): B<<679.0,141.0>-<681.0,142.0>-<682.0,143.0>>/L<<682.0,143.0>--<679.0,141.0>> = 11.309932474020195

	* petapp (U+E006): B<<687.0,164.0>-<688.0,166.0>-<689.0,167.0>>/L<<689.0,167.0>--<687.0,164.0>> = 11.309932474020227

	* petapp (U+E006): B<<713.0,484.0>-<712.0,484.0>-<710.0,483.0>>/L<<710.0,483.0>--<713.0,484.0>> = 8.13010235415587

	* petapp (U+E006): B<<763.0,5.0>-<762.0,7.0>-<761.0,8.0>>/L<<761.0,8.0>--<763.0,5.0>> = 11.309932474020195

	* petapp (U+E006): L<<274.0,517.0>--<273.0,520.0>>/B<<273.0,520.0>-<274.0,518.0>-<274.0,517.0>> = 8.130102354155916

	* petapp (U+E006): L<<280.0,491.0>--<279.0,494.0>>/B<<279.0,494.0>-<280.0,492.0>-<280.0,491.0>> = 8.130102354155916

	* petapp (U+E006): L<<291.0,468.0>--<289.0,471.0>>/B<<289.0,471.0>-<290.0,469.0>-<291.0,468.0>> = 7.125016348901705

	* petapp (U+E006): L<<296.0,459.0>--<295.0,462.0>>/B<<295.0,462.0>-<296.0,460.0>-<296.0,459.0>> = 8.130102354155916

	* petapp (U+E006): L<<312.0,442.0>--<308.0,445.0>>/B<<308.0,445.0>-<310.0,444.0>-<312.0,442.0>> = 10.304846468766009

	* petapp (U+E006): L<<331.0,427.0>--<328.0,429.0>>/B<<328.0,429.0>-<329.0,428.0>-<331.0,427.0>> = 11.309932474020195

	* petapp (U+E006): L<<380.0,128.0>--<379.0,131.0>>/B<<379.0,131.0>-<380.0,129.0>-<380.0,128.0>> = 8.130102354155916

	* petapp (U+E006): L<<387.0,108.0>--<386.0,111.0>>/B<<386.0,111.0>-<387.0,109.0>-<387.0,108.0>> = 8.130102354155916

	* petapp (U+E006): L<<499.0,225.0>--<505.0,222.0>>/L<<505.0,222.0>--<498.0,226.0>> = 3.1798301198640497

	* petapp (U+E006): L<<504.0,71.0>--<499.0,69.0>>/B<<499.0,69.0>-<502.0,71.0>-<504.0,71.0>> = 11.888658039627936

	* petapp (U+E006): L<<517.0,66.0>--<513.0,65.0>>/B<<513.0,65.0>-<515.0,65.0>-<517.0,66.0>> = 14.036243467926484

	* petapp (U+E006): L<<523.0,67.0>--<519.0,66.0>>/B<<519.0,66.0>-<521.0,66.0>-<523.0,67.0>> = 14.036243467926484

	* petapp (U+E006): L<<532.0,68.0>--<536.0,69.0>>/B<<536.0,69.0>-<534.0,69.0>-<532.0,68.0>> = 14.036243467926484

	* petapp (U+E006): L<<534.0,195.0>--<536.0,192.0>>/B<<536.0,192.0>-<535.0,194.0>-<534.0,195.0>> = 7.125016348901757

	* petapp (U+E006): L<<534.0,310.0>--<537.0,308.0>>/B<<537.0,308.0>-<536.0,309.0>-<534.0,310.0>> = 11.309932474020227

	* petapp (U+E006): L<<536.0,440.0>--<539.0,438.0>>/B<<539.0,438.0>-<538.0,439.0>-<536.0,440.0>> = 11.309932474020227

	* petapp (U+E006): L<<541.0,111.0>--<539.0,108.0>>/B<<539.0,108.0>-<540.0,109.0>-<541.0,111.0>> = 11.309932474020227

	* petapp (U+E006): L<<541.0,70.0>--<545.0,71.0>>/B<<545.0,71.0>-<540.0,70.0>-<541.0,70.0>> = 2.726310993906212

	* petapp (U+E006): L<<542.0,181.0>--<543.0,178.0>>/B<<543.0,178.0>-<542.0,180.0>-<542.0,181.0>> = 8.13010235415587

	* petapp (U+E006): L<<545.0,434.0>--<548.0,432.0>>/B<<548.0,432.0>-<547.0,433.0>-<545.0,434.0>> = 11.309932474020227

	* petapp (U+E006): L<<546.0,127.0>--<545.0,123.0>>/B<<545.0,123.0>-<546.0,125.0>-<546.0,127.0>> = 12.528807709151492

	* petapp (U+E006): L<<556.0,74.0>--<553.0,73.0>>/B<<553.0,73.0>-<555.0,74.0>-<556.0,74.0>> = 8.130102354155916

	* petapp (U+E006): L<<577.0,401.0>--<575.0,404.0>>/B<<575.0,404.0>-<576.0,403.0>-<577.0,401.0>> = 11.309932474020227

	* petapp (U+E006): L<<583.0,256.0>--<584.0,252.0>>/B<<584.0,252.0>-<584.0,254.0>-<583.0,256.0>> = 14.036243467926484

	* petapp (U+E006): L<<586.0,384.0>--<587.0,380.0>>/B<<587.0,380.0>-<587.0,382.0>-<586.0,384.0>> = 14.036243467926484

	* petapp (U+E006): L<<598.0,432.0>--<599.0,429.0>>/B<<599.0,429.0>-<598.0,431.0>-<598.0,432.0>> = 8.13010235415587

	* petapp (U+E006): L<<602.0,122.0>--<601.0,125.0>>/B<<601.0,125.0>-<602.0,123.0>-<602.0,122.0>> = 8.130102354155916

	* petapp (U+E006): L<<611.0,96.0>--<611.0,96.0>>/B<<611.0,96.0>-<607.0,95.0>-<603.5,92.5>> = 14.036243467926484

	* petapp (U+E006): L<<612.0,379.0>--<610.0,384.0>>/B<<610.0,384.0>-<611.0,381.0>-<612.0,379.0>> = 3.366460663429615

	* petapp (U+E006): L<<613.0,374.0>--<612.0,377.0>>/B<<612.0,377.0>-<613.0,375.0>-<613.0,374.0>> = 8.130102354155916

	* petapp (U+E006): L<<615.0,369.0>--<614.0,372.0>>/B<<614.0,372.0>-<615.0,370.0>-<615.0,369.0>> = 8.130102354155916

	* petapp (U+E006): L<<616.0,379.0>--<614.0,384.0>>/B<<614.0,384.0>-<615.0,382.0>-<616.0,379.0>> = 4.763641690726066

	* petapp (U+E006): L<<629.0,340.0>--<627.0,343.0>>/B<<627.0,343.0>-<628.0,342.0>-<629.0,340.0>> = 11.309932474020227

	* petapp (U+E006): L<<640.0,343.0>--<638.0,346.0>>/B<<638.0,346.0>-<639.0,345.0>-<640.0,343.0>> = 11.309932474020227

	* petapp (U+E006): L<<643.0,318.0>--<641.0,321.0>>/B<<641.0,321.0>-<642.0,320.0>-<643.0,318.0>> = 11.309932474020227

	* petapp (U+E006): L<<657.0,433.0>--<658.0,436.0>>/B<<658.0,436.0>-<657.0,434.0>-<657.0,432.5>> = 8.13010235415587

	* petapp (U+E006): L<<661.0,383.0>--<660.0,386.0>>/B<<660.0,386.0>-<661.0,384.0>-<661.0,383.0>> = 8.130102354155916

	* petapp (U+E006): L<<666.0,452.0>--<669.0,456.0>>/B<<669.0,456.0>-<667.0,454.0>-<666.0,452.0>> = 8.13010235415596

	* petapp (U+E006): L<<672.0,140.0>--<670.0,137.0>>/B<<670.0,137.0>-<671.0,138.0>-<672.0,140.0>> = 11.309932474020227

	* petapp (U+E006): L<<682.0,143.0>--<679.0,141.0>>/B<<679.0,141.0>-<681.0,142.0>-<682.0,143.0>> = 7.125016348901757

	* petapp (U+E006): L<<686.0,162.0>--<685.0,159.0>>/B<<685.0,159.0>-<686.0,161.0>-<686.0,162.0>> = 8.130102354155916

	* petapp (U+E006): L<<689.0,167.0>--<687.0,164.0>>/B<<687.0,164.0>-<688.0,166.0>-<689.0,167.0>> = 7.125016348901705

	* petapp (U+E006): L<<689.0,256.0>--<690.0,253.0>>/B<<690.0,253.0>-<689.0,255.0>-<689.0,256.0>> = 8.13010235415587

	* petapp (U+E006): L<<691.0,251.0>--<692.0,248.0>>/B<<692.0,248.0>-<691.0,250.0>-<691.0,251.0>> = 8.13010235415587

	* petapp (U+E006): L<<700.0,480.0>--<703.0,481.0>>/B<<703.0,481.0>-<701.0,480.0>-<700.0,479.5>> = 8.13010235415587

	* petapp (U+E006): L<<705.0,482.0>--<708.0,483.0>>/B<<708.0,483.0>-<706.0,482.0>-<705.0,482.0>> = 8.13010235415587

	* petapp (U+E006): L<<708.0,293.0>--<705.0,294.0>>/B<<705.0,294.0>-<707.0,293.0>-<708.0,293.0>> = 8.130102354155916

	* petapp (U+E006): L<<728.0,285.0>--<725.0,286.0>>/B<<725.0,286.0>-<727.0,285.0>-<728.0,285.0>> = 8.130102354155916

	* petapp (U+E006): L<<761.0,8.0>--<763.0,5.0>>/B<<763.0,5.0>-<762.0,7.0>-<761.0,8.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<581.0,372.0>-<585.0,368.0>-<588.0,366.0>>/L<<588.0,366.0>--<581.0,372.0>> = 6.911227119024609

	* petapp.minimal (U+E007): B<<631.0,435.0>-<631.0,433.0>-<632.0,430.0>>/L<<632.0,430.0>--<631.0,435.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<632.0,481.0>-<632.0,480.0>-<631.0,478.0>>/L<<631.0,478.0>--<632.0,481.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<645.0,399.0>-<646.0,397.0>-<647.0,396.0>>/L<<647.0,396.0>--<645.0,399.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<646.0,510.0>-<645.0,508.0>-<644.0,507.0>>/L<<644.0,507.0>--<646.0,510.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<676.0,538.0>-<674.0,537.0>-<673.0,536.0>>/L<<673.0,536.0>--<676.0,538.0>> = 11.309932474020227

	* petapp.minimal (U+E007): B<<700.0,247.0>-<699.0,248.0>-<698.0,250.0>>/L<<698.0,250.0>--<700.0,247.0>> = 7.125016348901757

	* petapp.minimal (U+E007): B<<714.0,147.0>-<714.0,148.0>-<713.0,150.0>>/L<<713.0,150.0>--<714.0,147.0>> = 8.13010235415587

	* petapp.minimal (U+E007): B<<720.0,137.0>-<719.0,139.0>-<718.0,140.0>>/L<<718.0,140.0>--<720.0,137.0>> = 11.309932474020195

	* petapp.minimal (U+E007): B<<732.0,185.0>-<731.0,187.0>-<731.0,189.0>>/L<<731.0,189.0>--<732.0,185.0>> = 14.036243467926484

	* petapp.minimal (U+E007): B<<743.0,53.0>-<743.0,54.0>-<742.0,56.0>>/L<<742.0,56.0>--<743.0,53.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<212.0,538.0>--<212.0,800.0>>/B<<212.0,800.0>-<214.0,769.0>-<226.5,742.0>> = 3.6913859864512575

	* petapp.minimal (U+E007): L<<628.0,462.0>--<629.0,465.0>>/B<<629.0,465.0>-<628.0,463.0>-<628.0,462.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<630.0,473.0>--<631.0,476.0>>/B<<631.0,476.0>-<630.0,474.0>-<630.0,473.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<632.0,430.0>--<631.0,435.0>>/B<<631.0,435.0>-<631.0,433.0>-<632.0,430.0>> = 11.309932474020227

	* petapp.minimal (U+E007): L<<637.0,222.0>--<640.0,221.0>>/B<<640.0,221.0>-<638.0,222.0>-<637.0,222.5>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<639.0,498.0>--<640.0,501.0>>/B<<640.0,501.0>-<639.0,499.0>-<639.0,498.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<644.0,507.0>--<646.0,510.0>>/B<<646.0,510.0>-<645.0,508.0>-<644.0,507.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<647.0,396.0>--<645.0,399.0>>/B<<645.0,399.0>-<646.0,397.0>-<647.0,396.0>> = 7.125016348901705

	* petapp.minimal (U+E007): L<<673.0,536.0>--<676.0,538.0>>/B<<676.0,538.0>-<674.0,537.0>-<673.0,536.0>> = 7.125016348901757

	* petapp.minimal (U+E007): L<<682.0,542.0>--<685.0,543.0>>/B<<685.0,543.0>-<683.0,542.0>-<682.0,542.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<687.0,544.0>--<690.0,545.0>>/B<<690.0,545.0>-<688.0,544.0>-<687.0,544.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<698.0,250.0>--<700.0,247.0>>/B<<700.0,247.0>-<699.0,248.0>-<698.0,250.0>> = 11.309932474020195

	* petapp.minimal (U+E007): L<<718.0,218.0>--<719.0,215.0>>/B<<719.0,215.0>-<718.0,217.0>-<718.0,218.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<731.0,113.0>--<732.0,110.0>>/B<<732.0,110.0>-<731.0,112.0>-<731.0,113.0>> = 8.13010235415587

	* petapp.minimal (U+E007): L<<740.0,156.0>--<739.0,160.0>>/B<<739.0,160.0>-<740.0,153.0>-<740.0,156.0>> = 5.906141113770497

	* petapp.minimal (U+E007): L<<744.0,137.0>--<743.0,140.0>>/B<<743.0,140.0>-<744.0,138.0>-<744.0,137.0>> = 8.130102354155916

	* petapp.minimal (U+E007): L<<746.0,123.0>--<747.0,120.0>>/B<<747.0,120.0>-<746.0,122.0>-<746.0,123.0>> = 8.13010235415587

	* petapp.wpda (U+E008): B<<485.0,2.0>-<482.0,5.0>-<482.0,6.0>>/L<<482.0,6.0>--<481.0,1.0>> = 11.309932474020227

	* petapp.wpda (U+E008): L<<185.0,222.0>--<180.0,218.0>>/B<<180.0,218.0>-<182.0,219.0>-<183.0,218.0>> = 12.094757077012058

	* pisafe (U+E010): B<<175.0,538.0>-<175.0,536.0>-<174.0,534.0>>/L<<174.0,534.0>--<175.0,538.0>> = 12.528807709151492

	* pisafe (U+E010): B<<190.0,573.0>-<189.0,572.0>-<188.0,570.0>>/L<<188.0,570.0>--<190.0,573.0>> = 7.125016348901757

	* pisafe (U+E010): B<<211.0,602.0>-<210.0,600.0>-<208.0,598.0>>/L<<208.0,598.0>--<211.0,602.0>> = 8.13010235415596

	* pisafe (U+E010): B<<784.0,594.0>-<783.0,596.0>-<782.0,597.0>>/L<<782.0,597.0>--<784.0,594.0>> = 11.309932474020195

	* pisafe (U+E010): B<<797.0,577.0>-<796.0,579.0>-<795.0,580.0>>/L<<795.0,580.0>--<797.0,577.0>> = 11.309932474020195

	* pisafe (U+E010): B<<816.0,530.0>-<816.0,532.0>-<815.0,534.0>>/L<<815.0,534.0>--<816.0,530.0>> = 12.528807709151492

	* pisafe (U+E010): B<<820.0,515.0>-<820.0,516.0>-<819.0,518.0>>/L<<819.0,518.0>--<820.0,515.0>> = 8.13010235415587

	* pisafe (U+E010): L<<174.0,534.0>--<175.0,538.0>>/B<<175.0,538.0>-<175.0,536.0>-<174.0,534.0>> = 14.036243467926484

	* pisafe (U+E010): L<<188.0,570.0>--<190.0,573.0>>/B<<190.0,573.0>-<189.0,572.0>-<188.0,570.0>> = 11.309932474020195

	* pisafe (U+E010): L<<208.0,598.0>--<211.0,602.0>>/B<<211.0,602.0>-<210.0,600.0>-<208.0,598.0>> = 10.304846468766044

	* pisafe (U+E010): L<<750.0,626.0>--<754.0,623.0>>/B<<754.0,623.0>-<752.0,624.0>-<750.0,626.0>> = 10.304846468766009

	* pisafe (U+E010): L<<782.0,597.0>--<784.0,594.0>>/B<<784.0,594.0>-<783.0,596.0>-<782.0,597.0>> = 7.125016348901757

	* pisafe (U+E010): L<<795.0,580.0>--<797.0,577.0>>/B<<797.0,577.0>-<796.0,579.0>-<795.0,580.0>> = 7.125016348901757

	* pisafe (U+E010): L<<815.0,534.0>--<816.0,530.0>>/B<<816.0,530.0>-<816.0,532.0>-<815.0,534.0>> = 14.036243467926484 

	* pisafe (U+E010): L<<817.0,528.0>--<818.0,525.0>>/B<<818.0,525.0>-<817.0,527.0>-<817.0,528.0>> = 8.13010235415587 [code: found-jaggy-segments]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 101 | 168 | 1619 | 85 | 1207 | 0 |
| 0% | 3% | 5% | 51% | 3% | 38% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
