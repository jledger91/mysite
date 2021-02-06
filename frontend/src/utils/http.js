import { getCookie } from './cookies';

/**
 * Generates a GET URL from the base URL and the search parameters.
 * @param url The base URL to search.
 * @param params The search parameters.
 * @returns {string}
 */
export function encodeURL(url, params) {
  let params_url = Object.keys(params)
    .filter(key => params[key] !== undefined)
    .map(key => key + '=' + encodeURIComponent(params[key]))
    .join('&');

  return url + "?" + params_url
}

/**
 * Handles a GET request.
 * @param uri The URI to send the request to.
 * @param params Optional GET parameters.
 * @returns {Promise<{json, status, statusMessage}>}
 */
export const get = async (uri, params = {}) => {
  const url = encodeURL(uri, params);
  const result = await fetch(url, {
    method: 'GET',
    headers: {
      'X-CSRFToken': getCookie('csrftoken'),
    }
  })
  return await handleResponse(result);
}

/**
 * Handles a PATCH request.
 * @param uri The URI to send the request to.
 * @param data The PATCH data.
 * @param headers Any optional headers to add to the request.
 * @returns {Promise<{json, status, statusText}>}
 */
export const patch = async (uri, data, headers={}) => {
  const result = await fetch(uri, {
    method: 'PATCH',
    body: JSON.stringify(data),
    headers: {
      ...headers,
      'X-CSRFToken': getCookie('csrftoken'),
      'Content-Type': 'application/json',
    }
  })
  return await handleResponse(result);
}

/**
 * Handles a POST request.
 * @param uri The URI to send the request to.
 * @param data The PATCH data.
 * @param headers Any optional headers to add to the request.
 * @returns {Promise<{json, status, statusText}>}
 */
export const post = async (uri, data, headers={}) => {
  const result = await fetch(uri, {
    method: 'POST',
    body: JSON.stringify(data),
    headers: {
      ...headers,
      'X-CSRFToken': getCookie('csrftoken'),
      'Content-Type': 'application/json',
    }
  })
  return await handleResponse(result);
}

/**
 * Handles a response from a fetch request.
 * @param res The response object.
 * @returns {Promise<{json, status, statusText}>}
 */
async function handleResponse(res) {
  const ret = { status: res.status, statusText: res.statusText }
  try {
    const json = await res.json()
    return { ...ret, json }
  } catch(err) {
    return { ...ret, json: {} }
  }
}
