/*
 * Copyright 2012, Vladimir Zapolskiy <vz@mleia.com> and other contributors
 * Released under the BSD 3-Clause license
 * http://opensource.org/licenses/BSD-3-Clause
 *
 */

var validated;

function sight()
{
    $(':file').change(function() {
        var file = this.files[0];
        name = file.name;
        size = file.size;
        type = file.type;

        if (size > 1000 * 1024) {
            alert("Too big file size: " +
                  Math.floor(size / 1024) +
                  "Kb, max is 1000Kb");
            // this.parent().html(jQuery(this).parent().html());
            validated = false;
        } else {
            validated = true;
        }
    });

    /*
     * To upload files asynchronously the form should have button and implemented
     * POST method in jQuery, for details see
     * http://stackoverflow.com/questions/166221/how-can-i-upload-files-asynchronously-with-jquery
     * Also see http://api.jquery.com/jQuery.post/
     */

    $(':button').click(function() {
        if (!validated) {
            alert("Valid file is not selected");
            return false;
        }

        return true;
    });
}

$(document).ready(sight);
