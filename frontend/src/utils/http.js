import { getCookie } from './cookies';

const csrfToken = getCookie('csrftoken');

// Requests ===================================================================

/**
 * Handles a GET request.
 * @param uri The URI to send the request to.
 * @param params Optional GET parameters.
 * @returns {Promise<{json, status, statusMessage}>}
 */
export const get = async (uri, params ={}) => {
  const urlParams = new URLSearchParams(params).toString()
  const url =`${uri}?${urlParams}`;
  const result = await fetch(url, {
    method: 'GET',
    headers: {
      'X-CSRFToken': csrfToken,
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
    ...getSendingDataParams(data, headers),
  })
  return await handleResponse(result);
}

/**
 * Handles a POST request.
 * @param uri The URI to send the request to.
 * @param data The POST data.
 * @param headers Any optional headers to add to the request.
 * @returns {Promise<{json, status, statusText}>}
 */
export const post = async (uri, data, headers={}) => {
  const result = await fetch(uri, {
    method: 'POST',
    ...getSendingDataParams(data, headers),
  })
  return await handleResponse(result);
}

// Requests Tools -------------------------------------------------------------

/**
 * Returns request parameters for POST/PUT/PATCH requests.
 * @param data The data to be sent.
 * @param headers Any optional headers to add to the request.
 * @returns {{headers: (*&{"X-CSRFToken": string, "Content-Type": string}), body: string}}
 */
const getSendingDataParams = (data, headers) => {
  return {
    body: JSON.stringify(data),
    headers: {
      'X-CSRFToken': csrfToken,
      'Content-Type': 'application/json',
      ...headers,
    }
  }
}

/**
 * Handles a response from a fetch request.
 * @param res The response object.
 * @returns {Promise<{json, status, statusText}>}
 */
const handleResponse = async (res) => {
  const ret = { status: res.status, statusText: res.statusText }
  try {
    const json = await res.json()
    return { ...ret, json }
  } catch(err) {
    return { ...ret, json: {} }
  }
}
