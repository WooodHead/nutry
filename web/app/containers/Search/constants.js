/*
 *
 * SearchB constants
 *
 */
const prefix = (name) => `app/Search/${name}`;
export const DEFAULT_ACTION = prefix('DEFAULT_ACTION');

export const SEARCH_TYPE_CHANGED = prefix('SEARCH_TYPE_CHANGED');
export const CHANGE_SEARCH = prefix('CHANGE_SEARCH');

export const SEARCH_COMPLETE = prefix('SEARCH_COMPLETE');
export const SEARCH_LOADING = prefix('SEARCH_LOADING');
export const SEARCH_FAILURE = prefix('SEARCH_FAILURE');
