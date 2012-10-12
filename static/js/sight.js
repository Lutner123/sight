// Copyright 2012, Vladimir Zapolskiy <vz@mleia.com> and other contributors
// Released under the BSD 3-Clause license
// http://opensource.org/licenses/BSD-3-Clause

function sight()
{
    alert("Hello");

    $(':file').change(function(){
        var file = this.files[0];
        name = file.name;
        size = file.size;
        type = file.type;

        if (size > 1000 * 1024) {
            alert("Too big file size: " +
                  Math.floor(size / 1024) +
                  "Kb, max is 1000Kb");
        }
    });

    $(':button').click(function() {
        // empty
    });
}

$(document).ready(sight);
