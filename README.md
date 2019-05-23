# Ethiopia Data Entry Forms
DHIS2 Custom HTML Forms.

The HTML forms will replace the custom DHIS2 entry forms.

# Notes
File sdgOld.html and aspsOld.html are all available in English.

The forms can be served using your preferred server i.e apache, nginx

All the forms have unique ids that must not be changed. They are a basis of mapping the entry forms to the dataelements.

The forms are in English for Ethiopia since it is an English speaking nation.

# Installation
1. Remove all the cdn links from the sdgs.html form. Only leave the custom Javascript functions and custom styles enclosed in the ```<style> </style>``` and ```<script></script>``` tags.

2. Copy the entire file after the above (1) exercise and paste the code in the custom window for the data set.

3. Save the changes and reload DHIS2 Data Entry Module.

To use the files in development, you will have to maintain the links in (1) above.