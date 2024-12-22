// Disable the option-command-S shortcut for search, since it
// conflicts annoyingly with Arc Browser's sidebar toggle.
// shift-command-S still works!
document.addEventListener("DOMContentLoaded", function () {
    document.addEventListener("keydown", function (event) {
        // Check if the key combination is Option (Alt) + Command (Meta) + S
        if (event.altKey && event.metaKey && event.key.toLowerCase() === "s") {
            event.preventDefault(); // Prevent the default action
            event.stopPropagation(); // Stop the event from propagating
        }
    });
});
