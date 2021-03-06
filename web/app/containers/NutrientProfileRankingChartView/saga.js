import { delay } from 'redux-saga';
import { takeLatest, call, put, select } from 'redux-saga/effects';
import { getRankingResults } from 'lib/nutrientAnalytics';
import { makeSelectSearchResults } from 'containers/App/selectors';
import { GET_NUTRIENT_RANKING } from './constants';
import { loadRankingsSuccess, loadRankingsFailure } from './actions';


export function* getRankings() { /* eslint no-underscore-dangle: ["error", { "allow": ["_source"] }]*/
  const searchResults = yield select(makeSelectSearchResults());
  let error = null;
  for (let i = 1; i <= 3; i += 1) {
    try {
      const rankingResults = yield call(getRankingResults, searchResults);
      yield put(loadRankingsSuccess(rankingResults));
      break;
    } catch (err) {
      error = err;
      yield call(delay, 1000); // retry after 2s
    }
  }
  if (error) {
    yield put(loadRankingsFailure(error));
  }
}


/**
 * Root saga manages watcher lifecycle
 */
export default function* fetchRankings() {
  // Watches for LOAD_REPOS actions and calls getRepos when one comes in.
  // By using `takeLatest` only the result of the latest API call is applied.
  // It returns task descriptor (just like fork) so we can continue execution
  // It will be cancelled automatically on component unmount
  yield takeLatest(GET_NUTRIENT_RANKING, getRankings);
  // yield take([LOCATION_CHANGE, GET_NUTRIENT_RANKING_SUCCESS]);
  // yield cancel(watcher);
}
