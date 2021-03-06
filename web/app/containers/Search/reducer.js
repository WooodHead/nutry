/*
 *
 * SearchB reducer
 *
 */

import { fromJS } from 'immutable';
import {
  CHANGE_SEARCH,
  REFRESH_SEARCH,
  SEARCH_COMPLETE,
  PROFILE_SELECTED,
  SEARCH_TYPE_CHANGED,
} from './constants';

const initialState = fromJS({
  searchString: '',
  loading: false,
  results: [],
  searchType: 'all',
  profileSelected: null,
});

function searchReducer(state = initialState, action) {
  switch (action.type) {
    case CHANGE_SEARCH:
      return state
        .set('searchString', action.searchString)
        .set('loading', true);
    case REFRESH_SEARCH:
      return state;
    case SEARCH_COMPLETE:
      return state
        .set('results', action.results)
        .set('loading', false);
    case SEARCH_TYPE_CHANGED:
      return state
        .set('searchType', action.searchType);
    case PROFILE_SELECTED:
      return state
        .set('profileSelected', action.profileInfo);
    default:
      return state;
  }
}

export default searchReducer;
