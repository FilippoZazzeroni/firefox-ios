
echo "\n\n[*] Building tools/Localizations"
(cd LocalizationTools && swift build)

python3 "firefoxios-l10n/.github/scripts/rewrite_original_attribute.py" --path "firefoxios-l10n"
echo "\n\n[*] Importing Strings - takes a minute. (output in import-strings.log)"
(cd LocalizationTools && swift run LocalizationTools \
  --import \
  --project-path "$PWD/../firefox-ios/Client.xcodeproj" \
  --l10n-project-path "$PWD/../firefoxios-l10n") > import-strings.log 2>&1

echo "\n\n[!] Strings have been imported. You can now create a PR."
