with company as (
             select cast(json_extract_scalar(_message, '$.Id') as BIGINT) Id
                    , json_extract_scalar(_message, '$.name') name
                    , json_extract_scalar(_message, '$.internal') internal
               from kafka.jpb.company
             ), q as (
             select b.isbn, i.name internalCompany, e.name externalCompany
             from company i, company e, booksale s, book b
            where s.bookid = b.id
              and i.id = s.intcompanyid
              and e.id = s.extcompanyid)
           select count(*) from (select distinct internalCompany, externalCompany
         from q
         group by internalCompany, externalCompany);

