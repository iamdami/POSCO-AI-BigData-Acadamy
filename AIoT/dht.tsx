import React from 'react';
import PageWrapper from 'components/internal/PageWrapper';
import NumberDisplay from 'components/NumberDisplay';

const Page: React.FC = function () {
  return (
    <PageWrapper title="DHT Status">
      <NumberDisplay label="Temperature" dataID="temperature" unit="c" />
      <NumberDisplay label="Humidity" dataID="humidity" unit="%" />
      <NumberDisplay label="Temperature After 1m" dataID="temperature" dataDispID="temperature-inf" action="inference" unit="C" />
      <NumberDisplay label="Humidity After 1m" dataID="Humidity" dataDispID="Humidity-inf" action="inference" unit="%" />
    </PageWrapper>
  );
};
export default Page;
