import React, { PropTypes }  from 'react';

const Stats = ({len, start, numFound, qtime}) => {
  if (len > 0) {
    const first = start + 1;
    const last = start + len;
    return <div className="col-sm-8">
      {`${first}-${last} of ${numFound} found (search time ${qtime}ms)`}
      </div>;
    } else {
      return <div className="col-sm-8">No results found</div>;
    }
};

Stats.propTypes = {
  qtime: PropTypes.number.isRequired,
  numFound: PropTypes.number.isRequired,
  start: PropTypes.number.isRequired,
  len: PropTypes.number.isRequired
};

export default Stats;
