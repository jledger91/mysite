import QueryString from 'query-string';

/**
 * Returns the URL search parameters as a JSON object.
 */
export const useSearchParams = () => QueryString.parse(window.location.search);
