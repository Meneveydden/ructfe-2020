let uploadFilename = null;


$(document).ready(function() {
    main();
});


function listFiles() {
    let files = null;
    $.get({
        url: "/files/" + path.join("/"),
        success: function (e) {
            files = e;
        },
        async:false
    });
    return files;
}


function buildFileUrl(filename) {
    return "/files/" + (path.concat([filename])).join("/");
}

function catFile(filename) {
    let result = null;
    $.get({
        url: buildFileUrl(filename),
        success: function (e) {
            result = e;
        },
        error: function (e) {
            console.log(e);
        },
        async:false
    });
    if (typeof result !== "string") {
        return null;
    }
    return result;
}


function isFile(filename) {
    return catFile(filename) !== null;
}


function buildPrompt() {
    return `${username}@keeper:${(['~'].concat(path)).join('/')} `;
}


// function getCommandArgs(parts, cmd) {
//     if (parts.length === 0) {
//         return null
//     }
//     if (parts[0] === cmd) {
//         return parts
//     }
// }


function processLS(args, term) {
    listFiles().forEach(function (name) {
        term.echo(name);
    });
}


function processCD(args, term) {
    let newPathParts = args[0].split("/");
    let oldPath = [...path];

    newPathParts.forEach(function (pathPart) {
        if (pathPart === "..") {
            if (path.length !== 0) {
                path.pop();
            }
        } else {
            path.push(pathPart);
            let res = listFiles();
            if (res === null || typeof res !== "object") {
                term.echo(`Incorrect path '${args[0]}'`);
                path = oldPath;
            }
        }
    });
    term.set_prompt(buildPrompt());
}


function processCAT(args, term) {
    let catPath = args[0];
    let fileContent = catFile(catPath);
    if (fileContent === null) {
        term.echo(`No such file '${catPath}'`);
    } else {
        term.echo(fileContent);
    }
}


function processPWD(args, term) {
    term.echo((["~"].concat(path)).join("/"));
}


function processDownload(args, term) {
    if (args.length === 0 || args[0].length === 0) {
        term.echo("Pass one argument as filename to download");
        return;
    }
    let filename = args[0];
    if (!isFile(filename)) {
        term.echo(`No such file '${filename}'`);
    } else {
        let url = `/files/${(path.concat([filename])).join("/")}`;
        window.open(url, '_blank');
    }
}


function processUpload(args, term) {
    if (args.length === 0 || args[0].length === 0) {
        term.echo("Pass one argument as filename to upload");
        return;
    }
    uploadFilename = args[0];
    $("#ufile").click();
}


const processors = {
    'ls': processLS,
    'cd': processCD,
    'cat': processCAT,
    'pwd': processPWD,
    'download': processDownload,
    'upload': processUpload,
};


function main() {
    jQuery(function ($, undefined) {
        $('#term_demo').terminal(function (line, term) {
            if (line === '') {
                return;
            }
            let parts = line.split(' ');
            if (parts.length === 0) {
                return;
            }
            let cmd = parts[0];
            let args = parts.slice(1);
            if (!Object.keys(processors).includes(cmd)) {
                term.echo(`No such command '${cmd}'`);
            } else {
                processors[cmd](args, term);
            }
        }, {
            greetings: 'Javascript Interpreter',
            name: 'js_demo',
            // height: '100%',
            // width: 450,
            prompt: cmd_prompt
            // prompt: 'user@keeper: ~/path '
        });
    });

    $("#ufile").on("change", function (e) {
        let file = $("#ufile")[0].files[0];
        file.name = uploadFilename;
        let formData = new FormData();

        formData.append("file", file);
        fetch(buildFileUrl(uploadFilename), {method: "POST", body: formData});
    });
}