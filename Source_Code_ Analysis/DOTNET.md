
# XXE

## Vulnerability

`xmlReaderSettings.DtdProcessing = DtdProcessing.Parse;`

## Fix

`xmlReaderSettings.DtdProcessing = DtdProcessing.Prohibit;`

Or using "XDocument"

# XML Bomb (Billion Laughs Attack)

## Vulnerability

```
var xmlReaderSettings = new XmlReaderSettings();
xmlReaderSettings.MaxCharactersFromEntities = 0;
```

## Fix

```
var xmlReaderSettings = new XmlReaderSettings();
xmlReaderSettings.MaxCharactersFromEntities = 500;
```

