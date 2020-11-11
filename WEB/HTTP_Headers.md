
# Example HTTP Headers Recommendations

## X-Content-Type-Options

`X-Content-Type-Options: nosniff`

## Referrer-Policy

`Referrer-Policy: strict-origin-when-cross-origin`

## X-XSS-Protection

`X-XSS-Protection: 1; mode=block`

## X-Frame-Options

`X-Frame-Options: Deny`

## Content-Security-Policy

`Content-Security-Policy: default-src 'none'; script-src 'self'; connect-src 'self'; img-src 'self'; style-src 'self'; frame-ancestors 'self';`

## Feature-Policy

`Feature-Policy: accelerometer 'none';autoplay 'none';camera 'none';fullscreen 'self';geolocation 'self';gyroscope 'none';magnetometer 'none';microphone 'none';payment 'none';speaker 'none';sync-xhr 'none';usb 'none';`
