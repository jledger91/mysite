import { all } from 'redux-saga/effects';

import { getReviewSaga } from './_sagas/getReview';
import { getReviewsSaga } from './_sagas/getReviews';

export default function* combinedSagas() {
  yield all([
    getReviewSaga(),
    getReviewsSaga(),
  ]);
}
