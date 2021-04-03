/**
 * Retrieves a browser cookie's value.
 * @param name The name of the cookie to be retrieved.
 * @returns {string}
 */
export function getCookie(name) {
  const decodedCookie = decodeURIComponent(document.cookie);
  const cookieArr = decodedCookie.split('; ');
  const value = cookieArr.find(cookie => cookie.startsWith(name))
  
  return value ? value.substring(name.length + 1) : '';
}
